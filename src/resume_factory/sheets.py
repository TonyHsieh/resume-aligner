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



def match_recruiter_intro(job, intros: list[dict]) -> tuple[str, str]:
    """Match a job to its recruiter outreach note and search query.
    Guarantees 100% company and role alignment with ZERO cross-company contamination.
    """
    job_canon = canonical_source(job.source)
    c_lower = (job.company or "").lower().strip()
    t_lower = (job.title or "").lower().strip()

    c_tokens = [tok for tok in re.split(r"[\s/–-]+", c_lower) if len(tok) > 2 and tok not in ["inc", "llc", "corp", "group", "the", "and"]]
    if "amazon" in c_tokens or "aws" in c_tokens:
        c_tokens = list(set(c_tokens + ["amazon", "aws"]))

    intro = None

    # 1. Match by Canonical URL (Exact URL correlation)
    for e in intros:
        if e["canonical_url"] and e["canonical_url"] == job_canon:
            intro = e
            break

    # 2. Match by BOTH Company AND Title (never match across different companies!)
    if not intro and c_tokens and t_lower:
        for e in intros:
            header_lower = e["header"].lower()
            if any(tok in header_lower for tok in c_tokens):
                clean_t = re.sub(r"[\(\)\[\],–-]", " ", t_lower).strip()
                title_words = [w for w in clean_t.split() if len(w) > 3]
                if title_words and sum(1 for w in title_words if w in header_lower) >= max(2, len(title_words) // 2):
                    intro = e
                    break

    # 3. Sanity check: Ensure company consistency
    if intro and c_tokens:
        header_lower = intro["header"].lower()
        note_lower = intro["note"].lower()
        query_lower = intro["query"].lower()
        if not any(tok in header_lower or tok in note_lower or tok in query_lower for tok in c_tokens):
            intro = None

    if intro and intro.get("note"):
        note = intro["note"]
        query = intro["query"] if intro.get("query") else f'site:linkedin.com/in ("{job.company or "Tech"}") ("Technical Recruiter" OR "Talent Acquisition")'
        return note, query

    # 4. Dynamic fallback guaranteed to be company-specific
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

    note = f"Hi [Name], I noticed {comp} is hiring for a {title}. {hook}. I'd love to connect and be considered."
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
    ]

    items = []
    rows = [headers]

    active_jobs = [j for j in tracker.jobs.values() if j.status != "blocked"]

    for idx, job in enumerate(active_jobs):
        resume_path = job.outputs.get("resume", "")

        # Precise, company-isolated matching for recruiter intro note & search query
        intro_note, search_query = match_recruiter_intro(job, intros)

        item_dict = {
            "Status": job.status.capitalize(),
            "Company": job.company or "",
            "Role Title": job.title or "",
            "Job Posting URL": job.source,
            "Tailored Resume File": resume_path,
            "Recruiter Search Query / Link": search_query,
            "Recruiter Intro Message": intro_note,
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
