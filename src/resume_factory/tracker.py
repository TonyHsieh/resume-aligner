"""Track which job descriptions have been aligned.

State lives in one JSON file (default ``output/tracker.json``) and a
human-readable ``INDEX.md`` is generated from it. Jobs are identified by a
stable ID derived from the canonical source, so re-adding the same list is
idempotent. A job is *aligned* only after its resume was rendered; it becomes
*stale* if the JD text or the master facts change afterwards.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse

# Lifecycle, in order. ``blocked`` is a side state (e.g. JD not fetchable).
STATUSES = ("new", "fetched", "analyzed", "drafted", "aligned", "blocked")
_ORDER = {s: i for i, s in enumerate(STATUSES)}

_URL = re.compile(r"https?://[^\s<>\"')\]]+")
_LOCAL = re.compile(r"\.(txt|md|pdf|docx?|html?)$", re.IGNORECASE)
_TRACKING = re.compile(r"^(utm_|fbclid|gclid|trk|refid|trackingid)", re.IGNORECASE)
_GDOC = re.compile(r"/document/d/([A-Za-z0-9_-]+)")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def canonical_source(source: str) -> str:
    """Normalise a URL / path so equivalent links share one job ID."""
    source = source.strip()
    if not source.lower().startswith(("http://", "https://")):
        return str(Path(source).expanduser())
    parsed = urlparse(source)
    gdoc = _GDOC.search(parsed.path)
    if gdoc and parsed.netloc.endswith("docs.google.com"):
        tab = dict(parse_qsl(parsed.query)).get("tab", "")
        return f"gdoc:{gdoc.group(1)}" + (f"#{tab}" if tab else "")
    query = urlencode(
        sorted((k, v) for k, v in parse_qsl(parsed.query) if not _TRACKING.match(k))
    )
    path = parsed.path.rstrip("/") or "/"
    return f"{parsed.scheme.lower()}://{parsed.netloc.lower()}{path}" + (
        f"?{query}" if query else ""
    )


def job_id(source: str) -> str:
    return "job-" + sha(canonical_source(source))[:8]


def parse_job_list(text: str) -> list[tuple[str, str | None]]:
    """Extract ``(source, label)`` pairs from a plain-text job list.

    Accepts one entry per line: a URL or a local file path, optionally preceded
    by a label (``Apple - ASE Compute: https://...``). ``#`` lines are comments.
    """
    entries: list[tuple[str, str | None]] = []
    for raw in text.splitlines():
        line = raw.strip("\ufeff\u200b \t\r")
        if not line or line.startswith("#"):
            continue
        match = _URL.search(line)
        if match:
            label = line[: match.start()].strip(" -:|•*\t") or None
            entries.append((match.group(0).rstrip(".,;"), label))
        elif _LOCAL.search(line):
            entries.append((line, None))
    return entries


@dataclass
class Job:
    id: str
    source: str
    label: str | None = None
    company: str | None = None
    title: str | None = None
    status: str = "new"
    added: str = field(default_factory=_now)
    updated: str = field(default_factory=_now)
    aligned_at: str | None = None
    jd_hash: str | None = None
    master_hash: str | None = None
    outputs: dict[str, str] = field(default_factory=dict)
    open_questions: int = 0
    note: str | None = None

    @property
    def name(self) -> str:
        if self.company or self.title:
            return " – ".join(x for x in (self.company, self.title) if x)
        return self.label or self.source


class Tracker:
    def __init__(self, path: str | Path = "output/tracker.json"):
        self.path = Path(path)
        self.jobs: dict[str, Job] = {}
        if self.path.exists():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self.jobs = {k: Job(**v) for k, v in data.get("jobs", {}).items()}

    # -- persistence -------------------------------------------------------
    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"version": 1, "jobs": {k: asdict(v) for k, v in self.jobs.items()}}
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
        os.replace(tmp, self.path)  # atomic: never leaves a half-written tracker

    # -- mutation ----------------------------------------------------------
    def add(self, source: str, label: str | None = None) -> tuple[Job, bool]:
        """Register a job. Returns ``(job, created)``; existing jobs are kept."""
        jid = job_id(source)
        if jid in self.jobs:
            job = self.jobs[jid]
            if label and not job.label:
                job.label = label
            return job, False
        job = Job(id=jid, source=source.strip(), label=label)
        self.jobs[jid] = job
        return job, True

    def add_list(self, text: str) -> tuple[list[Job], list[Job]]:
        """Add every entry in ``text``. Returns ``(new_jobs, already_known)``."""
        new, known = [], []
        for source, label in parse_job_list(text):
            job, created = self.add(source, label)
            (new if created else known).append(job)
        return new, known

    def set_status(self, jid: str, status: str, **fields) -> Job:
        if status not in _ORDER:
            raise ValueError(f"unknown status {status!r}; expected one of {STATUSES}")
        job = self.jobs[jid]
        job.status = status
        job.updated = _now()
        for key, value in fields.items():
            if not hasattr(job, key):
                raise AttributeError(f"Job has no field {key!r}")
            setattr(job, key, value)
        return job

    def mark_aligned(
        self,
        jid: str,
        *,
        jd_hash: str,
        master_hash: str,
        outputs: dict[str, str],
        open_questions: int = 0,
    ) -> Job:
        return self.set_status(
            jid,
            "aligned",
            aligned_at=_now(),
            jd_hash=jd_hash,
            master_hash=master_hash,
            outputs=outputs,
            open_questions=open_questions,
            note=None,
        )

    # -- queries -----------------------------------------------------------
    @staticmethod
    def stale_reason(job: Job, jd_hash: str | None, master_hash: str | None) -> str | None:
        """Why an aligned job needs re-running, or ``None`` if it is current."""
        if job.status != "aligned":
            return None
        if jd_hash and job.jd_hash and jd_hash != job.jd_hash:
            return "job description changed"
        if master_hash and job.master_hash and master_hash != job.master_hash:
            return "master resume facts changed"
        return None

    def pending(self, jd_hashes: dict[str, str] | None = None, master_hash: str | None = None):
        """Jobs that still need work: not aligned, blocked excluded, or stale."""
        jd_hashes = jd_hashes or {}
        return [
            j
            for j in self.jobs.values()
            if j.status != "blocked"
            and (
                j.status != "aligned"
                or self.stale_reason(j, jd_hashes.get(j.id), master_hash)
            )
        ]

    def counts(self) -> dict[str, int]:
        out = {s: 0 for s in STATUSES}
        for job in self.jobs.values():
            out[job.status] += 1
        return out

    # -- reporting ---------------------------------------------------------
    def render_index(
        self, jd_hashes: dict[str, str] | None = None, master_hash: str | None = None
    ) -> str:
        jd_hashes = jd_hashes or {}
        counts = self.counts()
        total = len(self.jobs)
        lines = [
            "# Aligned Jobs Index",
            "",
            f"**{counts['aligned']} of {total} aligned** · "
            + " · ".join(f"{counts[s]} {s}" for s in STATUSES if s != "aligned" and counts[s]),
            "",
            "| | Job | Status | Aligned | Open Qs | Resume | Note |",
            "|---|---|---|---|---|---|---|",
        ]
        for job in sorted(self.jobs.values(), key=lambda j: (_ORDER[j.status], j.added)):
            stale = self.stale_reason(job, jd_hashes.get(job.id), master_hash)
            icon = "⚠️" if stale else {"aligned": "✅", "blocked": "⛔"}.get(job.status, "⬜")
            status = f"stale ({stale})" if stale else job.status
            resume = job.outputs.get("resume", "")
            lines.append(
                f"| {icon} | [{job.name}]({job.source}) | {status} | "
                f"{(job.aligned_at or '')[:10]} | {job.open_questions or ''} | "
                f"{resume} | {job.note or ''} |"
            )
        return "\n".join(lines) + "\n"

    def write_index(self, path: str | Path | None = None, **kwargs) -> Path:
        path = Path(path) if path else self.path.parent / "INDEX.md"
        path.write_text(self.render_index(**kwargs), encoding="utf-8")
        return path
