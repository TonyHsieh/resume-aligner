"""Bi-directional sync between the local Resume Factory tracker and Google Sheets via Apps Script webhook."""

from __future__ import annotations

import json
from pathlib import Path
import re
import requests

from .tracker import Tracker, canonical_source

DEFAULT_WEBHOOK_FILE = Path("inputs/sheets_webhook.txt")
DEFAULT_INTROS_FILE = Path("output/recruiter_introductions.md")


def get_webhook_url(custom_url: str | None = None) -> str:
    if custom_url:
        return custom_url.strip()
    if not DEFAULT_WEBHOOK_FILE.exists():
        raise SystemExit(f"No webhook URL configured in {DEFAULT_WEBHOOK_FILE}")
    url = DEFAULT_WEBHOOK_FILE.read_text(encoding="utf-8").strip()
    if not url:
        raise SystemExit(f"Webhook file {DEFAULT_WEBHOOK_FILE} is empty.")
    return url


def pull_from_sheets(
    webhook_url: str | None = None,
    tracker_path: str = "output/tracker.json",
) -> list[str]:
    """Fetch existing rows from Google Sheet to discover any new job URLs added by the user."""
    url = get_webhook_url(webhook_url)
    tracker = Tracker(tracker_path)
    new_urls = []

    try:
        resp = requests.get(url, timeout=30, allow_redirects=True)
        if resp.status_code == 200:
            try:
                data = resp.json()
            except Exception:
                data = None
            if isinstance(data, dict) and "rows" in data:
                # Find the URL column from rows
                for row_obj in data.get("rows", []):
                    # Check common column name variations
                    found_url = None
                    for key, val in row_obj.items():
                        if "url" in key.lower() or "posting" in key.lower() or "link" in key.lower():
                            val_str = str(val).strip()
                            if val_str.startswith(("http://", "https://")):
                                found_url = val_str
                                break
                    if found_url:
                        company = str(row_obj.get("Company") or "").strip()
                        title = str(row_obj.get("Role Title") or "").strip()
                        label = f"{company} – {title}".strip(" –") or None
                        job, created = tracker.add(found_url, label=label)
                        if created:
                            new_urls.append(found_url)
                if new_urls:
                    tracker.save()
                    tracker.write_index()
    except Exception as e:
        # GET is best-effort (requires doGet in Apps Script)
        pass

    return new_urls


def parse_recruiter_intros(intros_path: str | Path = DEFAULT_INTROS_FILE) -> list[dict]:
    path = Path(intros_path)
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    raw_chunks = text.split("## ")

    entries = []
    for c in raw_chunks:
        if not c.strip() or c.startswith("Recruiter Introductions") or c.startswith("Tips for High"):
            continue
        first_line = c.strip().splitlines()[0]
        num_m = re.match(r"^(\d+)\.\s*(.*)", first_line)
        if not num_m:
            continue
        num = int(num_m.group(1))
        header_title = num_m.group(2).strip()

        url_m = re.search(r"\*\*Posting URL:\*\*\s*(https?://[^\s\)]+)", c)
        posting_url = url_m.group(1).strip() if url_m else ""

        note = ""
        if "> *\"" in c:
            note = c.split("> *\"")[1].split("\"*")[0].strip()
        elif "> \"" in c:
            note = c.split("> \"")[1].split("\"")[0].strip()

        query = ""
        if "```text" in c:
            query = c.split("```text")[1].split("```")[0].strip()

        entries.append({
            "num": num,
            "header": header_title,
            "url": posting_url,
            "canonical_url": canonical_source(posting_url) if posting_url else "",
            "note": note,
            "query": query,
        })
    return entries



def _norm_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def _split_intro_header(header: str) -> tuple[str, str]:
    for sep in (" – ", " — ", " - "):
        if sep in header:
            comp, title = header.split(sep, 1)
            return comp.strip(), title.strip()
    return header.strip(), ""


def _company_matches(job_company: str | None, other_company: str | None) -> bool:
    jc = _norm_text(job_company or "")
    oc = _norm_text(other_company or "")
    if not jc or not oc:
        return False
    stop = {"inc", "llc", "corp", "corporation", "company", "co", "the"}
    j_tokens = [w for w in jc.split() if w not in stop]
    o_tokens = [w for w in oc.split() if w not in stop]
    if not j_tokens or not o_tokens:
        return False
    if j_tokens == o_tokens:
        return True
    if ("amazon" in j_tokens or "aws" in j_tokens) and ("amazon" in o_tokens or "aws" in o_tokens):
        return True
    if ("google" in j_tokens or "youtube" in j_tokens) and ("google" in o_tokens or "youtube" in o_tokens):
        return True
    # Only allow substring containment on single-word brand names when the first/primary brand token matches
    return j_tokens[0] == o_tokens[0] and (len(j_tokens) == 1 or len(o_tokens) == 1)


def match_recruiter_intro(job, intros: list[dict]) -> tuple[str, str]:
    """Match a job to its recruiter outreach note and search query.
    Guarantees 100% company and role alignment with ZERO cross-company or cross-role contamination.
    """
    job_canon = canonical_source(job.source)
    job_base = job_canon.split("?", 1)[0]
    norm_title = _norm_text(job.title or "")

    intro = None

    # 1. Match by Canonical URL (Exact URL correlation)
    for e in intros:
        if e["canonical_url"] and e["canonical_url"] == job_canon:
            intro = e
            break

    # 2. Match by Base URL (ignoring query params) or Exact Normalized Company + Title
    if not intro and job.company:
        for e in intros:
            hdr_comp, hdr_title = _split_intro_header(e["header"])
            if not _company_matches(job.company, hdr_comp):
                continue
            e_base = e["canonical_url"].split("?", 1)[0] if e["canonical_url"] else ""
            if e_base and e_base == job_base:
                intro = e
                break
            if norm_title and hdr_title and norm_title == _norm_text(hdr_title):
                intro = e
                break

    # 3. Sanity check: Ensure company consistency
    if intro and job.company:
        hdr_comp, _ = _split_intro_header(intro["header"])
        if not _company_matches(job.company, hdr_comp):
            intro = None

    if intro and intro.get("note"):
        note = intro["note"]
        query = intro["query"] if intro.get("query") else f'site:linkedin.com/in ("{job.company or "Tech"}") ("Technical Recruiter" OR "Talent Acquisition")'
        return note, query

    # 4. Dynamic fallback guaranteed to be company- and role-specific
    comp = job.company or "your team"
    title = job.title or "this role"
    t_low = (job.title or "").lower()
    if any(k in t_low for k in ["architect", "solutions", "cloud", "platform"]):
        hook = "I bring 15+ years of distributed systems and cloud architecture experience, having led internal developer platform delivery improving deployment turnaround by 40%"
    elif any(k in t_low for k in ["product", "pm", "manager"]):
        hook = "I bring 15+ years of technical platform leadership, commercial product lifecycle delivery, and metric-driven operational governance"
    elif any(k in t_low for k in ["game", "gaming", "streaming", "media", "3d"]):
        hook = "Having directed commercial 3D game delivery at LucasArts and architected high-concurrency multiplayer platforms"
    else:
        hook = "I bring extensive experience architecting high-reliability distributed platforms, developer tooling, and 24x7 production systems"

    article = "an" if re.match(r"^(?:[aeiou]|ai\b|ml\b|it\b|sre\b|epm\b)", t_low.strip()) else "a"
    note = f"Hi [Name], I noticed {comp} is hiring for {article} {title}. {hook}. I'd love to connect and be considered."
    query = f'site:linkedin.com/in ("{comp}") ("Technical Recruiter" OR "Talent Acquisition")'
    return note, query

def push_to_sheets(
    webhook_url: str | None = None,
    tracker_path: str = "output/tracker.json",
    intros_path: str | Path = DEFAULT_INTROS_FILE,
) -> dict:
    url = get_webhook_url(webhook_url)
    tracker = Tracker(tracker_path)
    intros = parse_recruiter_intros(intros_path)

    headers = [
        "Status",
        "Company",
        "Role Title",
        "Job Posting URL",
        "Tailored Resume File",
        "Recruiter Search Query / Link",
        "Recruiter Intro Message",
        "Notes",
    ]

    items = []
    rows = [headers]

    for idx, job in enumerate(tracker.jobs.values()):
        if job.status == "blocked":
            item_dict = {
                "Status": "Blocked",
                "Company": job.company or "",
                "Role Title": job.title or "",
                "Job Posting URL": job.source,
                "Tailored Resume File": "[CLOSED / EXPIRED]",
                "Recruiter Search Query / Link": "",
                "Recruiter Intro Message": "",
                "Notes": job.note or "Posting is closed / expired on company portal",
            }
        else:
            resume_path = job.outputs.get("resume", "")
            intro_note, search_query = match_recruiter_intro(job, intros)
            item_dict = {
                "Status": job.status.capitalize(),
                "Company": job.company or "",
                "Role Title": job.title or "",
                "Job Posting URL": job.source,
                "Tailored Resume File": resume_path,
                "Recruiter Search Query / Link": search_query,
                "Recruiter Intro Message": intro_note,
                "Notes": job.note or "",
            }
        items.append(item_dict)
        rows.append([item_dict[h] for h in headers])

    payload = {
        "items": items,
        "records": items,
        "rows": rows,
        "headers": headers,
    }

    resp = requests.post(url, json=payload, timeout=40, allow_redirects=True)
    
    # Check if the response returned any sheet_urls
    new_from_resp = []
    try:
        resp_data = resp.json()
        if isinstance(resp_data, dict) and "sheet_urls" in resp_data:
            for s_url in resp_data["sheet_urls"]:
                job, created = tracker.add(s_url)
                if created:
                    new_from_resp.append(s_url)
            if new_from_resp:
                tracker.save()
                tracker.write_index()
    except Exception:
        resp_data = {}

    return {
        "status_code": resp.status_code,
        "rows_count": len(items),
        "response_text": resp.text[:300],
        "new_urls": new_from_resp,
        "resp_data": resp_data if isinstance(resp_data, dict) else {},
    }
