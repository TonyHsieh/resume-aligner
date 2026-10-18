"""Ingest Job Descriptions from web URLs, Google Docs, or local files.

Saves normalized text to work/<job_id>/jd_raw.txt and extracts metadata.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests


USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

_GDOC_ID = re.compile(r"/document/d/([A-Za-z0-9_-]+)")


@dataclass
class JobDescription:
    id: str
    source: str
    title: str
    company: str
    raw_text: str


def fetch_url_content(url: str, timeout: int = 25) -> str:
    url = url.strip()
    match = _GDOC_ID.search(url)
    if match and "docs.google.com" in url:
        export_url = f"https://docs.google.com/document/d/{match.group(1)}/export?format=txt"
        resp = requests.get(export_url, timeout=timeout)
        resp.raise_for_status()
        return resp.content.decode("utf-8-sig")

    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(cleaned_lines)


def parse_jd(job_id: str, source: str, work_dir: Path | str = "work") -> JobDescription:
    dest_dir = Path(work_dir) / job_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    raw_file = dest_dir / "jd_raw.txt"

    if raw_file.exists():
        raw_text = raw_file.read_text(encoding="utf-8")
    else:
        if source.startswith(("http://", "https://")):
            raw_text = fetch_url_content(source)
        else:
            raw_text = Path(source).expanduser().read_text(encoding="utf-8")
        raw_file.write_text(raw_text, encoding="utf-8")

    # Basic heuristic extraction of title and company from source and text
    title = ""
    company = ""
    lines = [line for line in raw_text.splitlines() if line.strip()]
    header_sample = " ".join(lines[:15])

    parsed = urlparse(source)
    domain = parsed.netloc.lower()

    if "apple.com" in domain:
        company = "Apple"
        if "ase-compute" in source or "apple-services-engineering" in source:
            title = "Apple Services Engineering (ASE) Compute - Software Engineering Manager"
        elif "apple-arcade" in source:
            title = "Senior Creative Gameplay Engineer - Apple Arcade"
        elif "developer-publications" in source:
            title = "Engineering Project Manager - Developer Publications"
        elif "middleware" in source:
            title = "Sr Software Engineer - Java Middleware, eBusiness Services"
    elif "thatch.com" in domain:
        company = "Thatch"
        if "backend" in source:
            title = "Software Engineer, Backend"
        elif "full-stack" in source:
            title = "Software Engineer, Full Stack"
    elif "togetherai" in source or "together.ai" in source:
        company = "Together AI"
        title = "AI / Systems Engineer"
    elif "sutterhealth" in source:
        company = "Sutter Health"
        title = "Manager - Artificial Intelligence Governance"
    elif "activisionblizzard" in domain or "xbox" in source.lower():
        company = "Activision Blizzard / Microsoft Gaming"
        title = "Principal Software Engineer - Xbox Media"

    # Fallback heuristics if not matched
    if not title and lines:
        title = lines[0][:80]
    if not company:
        company = domain.replace("www.", "").split(".")[0].capitalize()

    return JobDescription(
        id=job_id,
        source=source,
        title=title,
        company=company,
        raw_text=raw_text,
    )
