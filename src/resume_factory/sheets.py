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


def push_to_sheets(
    webhook_url: str | None = None,
    tracker_path: str = "output/tracker.json",
    intros_path: str | Path = DEFAULT_INTROS_FILE,
) -> dict:
    url = get_webhook_url(webhook_url)
    tracker = Tracker(tracker_path)
    intros_text = Path(intros_path).read_text(encoding="utf-8") if Path(intros_path).exists() else ""

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

    for jid, job in tracker.jobs.items():
        if job.status == "blocked":
            continue
        resume_path = job.outputs.get("resume", "")

        # Extract intro note for this job
        intro_note = ""
        for chunk in intros_text.split("## "):
            job_key = job.title.split("-")[0].strip().lower() if job.title else ""
            if (job_key and job_key in chunk.lower()) or (job.company and job.company.lower() in chunk.lower()):
                if "> *\"" in chunk:
                    intro_note = chunk.split("> *\"")[1].split("\"*")[0].strip()
                    break

        search_query = f"https://www.linkedin.com/search/results/people/?keywords={job.company or 'Tech'}%20Recruiter"
        item_dict = {
            "Status": job.status.capitalize(),
            "Company": job.company or "",
            "Role Title": job.title or "",
            "Job Posting URL": job.source,
            "Tailored Resume File": resume_path,
            "Recruiter Search Query / Link": search_query,
            "Recruiter Intro Message": intro_note or "I noticed you're hiring for this role. I'd love to connect and be considered.",
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
