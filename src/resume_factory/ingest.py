"""Ingest Job Descriptions from web URLs, Google Docs, or local files.

Saves normalized text to work/<job_id>/jd_raw.txt and extracts metadata.
Supports Greenhouse, Ashby, Workable, Workday CXS, Roblox, Amazon, AngelList, etc.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
import requests

from .tracker import Tracker

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
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
    closed: bool = False


def fetch_url_content(url: str, timeout: int = 25) -> tuple[str, str, str, bool]:
    """Fetch URL and return (cleaned_text, extracted_title, extracted_company, is_closed)."""
    url = url.strip()

    # Google Doc
    match = _GDOC_ID.search(url)
    if match and "docs.google.com" in url:
        export_url = f"https://docs.google.com/document/d/{match.group(1)}/export?format=txt"
        resp = requests.get(export_url, timeout=timeout)
        resp.raise_for_status()
        return resp.content.decode("utf-8-sig"), "", "", False

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # 1. Workday CXS API
    if "myworkdayjobs.com" in domain:
        # Example: https://devoted.wd1.myworkdayjobs.com/en-US/Devoted/job/Remote-USA/Principal-Software-Engineer--Growth_R3746?q=Software
        parts = parsed.path.strip("/").split("/")
        # Path format: <locale>/<site>/job/<location>/<slug>
        if len(parts) >= 5 and parts[2] == "job":
            site = parts[1]
            slug = "/".join(parts[3:])
            tenant = domain.split(".")[0]
            api_url = f"https://{domain}/wday/cxs/{tenant}/{site}/job/{slug}"
            try:
                r = requests.get(api_url, headers={"Accept": "application/json", "User-Agent": USER_AGENT}, timeout=timeout)
                if r.status_code == 200:
                    data = r.json().get("jobPostingInfo", {})
                    title = data.get("title", "")
                    company = tenant.capitalize()
                    html_desc = data.get("jobDescription", "")
                    soup = BeautifulSoup(html_desc, "html.parser")
                    text = soup.get_text(separator="\n")
                    lines = [line.strip() for line in text.splitlines() if line.strip()]
                    return "\n".join(lines), title, company, False
            except Exception:
                pass

    # 2. Greenhouse Embedded Query Param (e.g. Zwift ?gh_jid=8881996002)
    qs = parse_qs(parsed.query)
    if "gh_jid" in qs:
        gh_jid = qs["gh_jid"][0]
        board = domain.replace("www.", "").split(".")[0]
        api_url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{gh_jid}"
        try:
            r = requests.get(api_url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
            if r.status_code == 200:
                data = r.json()
                title = data.get("title", "")
                company = board.capitalize()
                soup = BeautifulSoup(data.get("content", ""), "html.parser")
                text = soup.get_text(separator="\n")
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                return "\n".join(lines), title, company, False
        except Exception:
            pass

    # 2.5 Ashby API
    if "ashbyhq.com" in domain:
        parts = parsed.path.strip("/").split("/")
        if len(parts) >= 2:
            board = parts[0]
            posting_id = parts[1]
            api_url = f"https://api.ashbyhq.com/posting-api/job-board/{board}"
            try:
                r = requests.get(api_url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
                if r.status_code == 200:
                    data = r.json()
                    for j in data.get("jobs", []):
                        if j.get("id") == posting_id:
                            title = j.get("title", "")
                            company = board.replace("-", " ").title()
                            desc = j.get("descriptionPlain")
                            if not desc and j.get("descriptionHtml"):
                                soup = BeautifulSoup(j.get("descriptionHtml"), "html.parser")
                                desc = soup.get_text(separator="\n")
                            lines = [line.strip() for line in (desc or "").splitlines() if line.strip()]
                            return "\n".join(lines), title, company, False
            except Exception:
                pass

    # 2.6 Google Careers
    if "google.com" in domain and "/careers/" in url:
        m = re.search(r'/results/(\d+)', url)
        target_id = m.group(1) if m else ''
        try:
            r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
            if r.status_code == 200:
                matches = re.findall(r'AF_initDataCallback\(\{.*?data:\s*(\[.*?\])\s*,\s*sideChannel', r.text, re.DOTALL)
                for data_str in matches:
                    if target_id and target_id in data_str:
                        data = json.loads(data_str)
                        for entry in data:
                            if isinstance(entry, list) and len(entry) > 1 and str(entry[0]) == target_id:
                                title = entry[1]
                                company = "Google"
                                parts = []
                                for item in entry:
                                    if isinstance(item, list) and len(item) > 1 and isinstance(item[1], str) and ('<' in item[1] or '\n' in item[1]):
                                        soup = BeautifulSoup(item[1], 'html.parser')
                                        clean = soup.get_text(separator='\n').strip()
                                        if clean:
                                            parts.append(clean)
                                text = "\n\n".join(parts)
                                lines = [line.strip() for line in text.splitlines() if line.strip()]
                                return "\n".join(lines), title, company, False
        except Exception:
            pass

    # 2.7 Eightfold / Netflix
    if "jobs.netflix.net" in domain or "eightfold.ai" in domain:
        qs = parse_qs(parsed.query)
        pid = qs.get("pid", [None])[0]
        if not pid:
            m = re.search(r'/job/(\d+)', parsed.path)
            if m:
                pid = m.group(1)
        if pid:
            api_url = f"https://{parsed.netloc}/api/apply/v2/jobs/{pid}?domain=netflix.com"
            try:
                r = requests.get(api_url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
                if r.status_code == 200:
                    d = r.json()
                    title = d.get("name", "")
                    company = "Netflix"
                    jd_html = d.get("job_description", "")
                    soup = BeautifulSoup(jd_html, "html.parser")
                    text = soup.get_text(separator="\n")
                    lines = [line.strip() for line in text.splitlines() if line.strip()]
                    return "\n".join(lines), title, company, False
            except Exception:
                pass

    # 2.8 Oracle Cloud HCM Candidate Experience
    if "oraclecloud.com" in domain and ("/jobs/preview/" in parsed.path or "/job/" in parsed.path):
        m = re.search(r'/(?:jobs/preview|job)/(\d+)', parsed.path)
        if m:
            req_id = m.group(1)
            api_url = f"https://{parsed.netloc}/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails/{req_id}"
            try:
                r = requests.get(api_url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}, timeout=timeout)
                if r.status_code == 200:
                    d = r.json()
                    title = d.get("Title", "")
                    if "jpmc" in domain:
                        company = "JPMorganChase"
                    else:
                        company = d.get("Organization") or "Oracle Cloud"
                    desc_html = d.get("ExternalDescriptionStr") or d.get("ShortDescriptionStr") or ""
                    soup = BeautifulSoup(desc_html, "html.parser")
                    text = soup.get_text(separator="\n")
                    lines = [line.strip() for line in text.splitlines() if line.strip()]
                    return "\n".join(lines), title, company, False
            except Exception:
                pass

    # 2.85 Apple Jobs API
    if "jobs.apple.com" in domain and "/details/" in parsed.path:
        m = re.search(r"/details/([^/?#]+)", parsed.path)
        if m:
            job_number = m.group(1)
            api_url = f"https://jobs.apple.com/api/v1/jobDetails/{job_number}"
            try:
                r = requests.get(
                    api_url,
                    headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
                    timeout=timeout,
                )
                if r.status_code == 200:
                    res = (r.json() or {}).get("res") or {}
                    title = (res.get("postingTitle") or "").strip()
                    req_id = (res.get("reqId") or job_number).strip()
                    sections = []
                    if title:
                        sections.append(f"Title: {title}")
                    sections.append("Company: Apple")
                    sections.append(f"Req ID: {req_id}")
                    for label, key in (
                        ("SUMMARY:", "jobSummary"),
                        ("DESCRIPTION:", "description"),
                        ("MINIMUM QUALIFICATIONS:", "minimumQualifications"),
                        ("PREFERRED QUALIFICATIONS:", "preferredQualifications"),
                    ):
                        val = res.get(key)
                        if val and isinstance(val, str) and val.strip():
                            clean = BeautifulSoup(val, "html.parser").get_text(separator="\n").strip()
                            sections.append(f"\n{label}\n{clean}")
                    full_jd = "\n".join(sections).strip()
                    if title and len(full_jd) > 100:
                        return full_jd, title, "Apple", False
            except Exception:
                pass

    # 3. Direct HTML fetch with BeautifulSoup cleanup
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")
    raw_page_title = soup.title.string.strip() if soup.title and soup.title.string else ""

    # 2.9 Schema.org JSON-LD (e.g. Phenom People / Stanford / Sutter / Eightfold Microsoft)
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            d = json.loads(s.string)
            if d.get("@type") == "JobPosting":
                jp_title = d.get("title", "")
                org = d.get("hiringOrganization", {})
                jp_company = org.get("name", "") if isinstance(org, dict) else (org if isinstance(org, str) else "")
                if not jp_company and "microsoft.com" in domain:
                    jp_company = "Microsoft"
                desc_html = d.get("description", "")
                if desc_html:
                    from html import unescape
                    desc_soup = BeautifulSoup(unescape(desc_html), "html.parser")
                    for tag in desc_soup(["script", "style", "noscript"]):
                        tag.decompose()
                    desc_text = desc_soup.get_text(separator="\n")
                    lines = [line.strip() for line in desc_text.splitlines() if line.strip()]
                    cleaned_desc = "\n".join(lines) if lines else desc_text.strip()
                    if len(cleaned_desc) > 100:
                        return cleaned_desc, jp_title, jp_company, False
        except Exception:
            pass

    for tag in soup(["script", "style", "noscript", "svg", "nav", "footer", "template"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    full_text = "\n".join(cleaned_lines)

    # Detect closed/expired postings on visible page text
    page_text_lower = full_text.lower()
    is_closed = any(
        phrase in page_text_lower
        for phrase in [
            "not currently accepting applications",
            "job is no longer available",
            "this job has closed",
            "this position has been closed",
            "posting is no longer active",
        ]
    )

    title = ""
    company = ""

    # Extract metadata based on domain patterns
    if "roblox.com" in domain:
        company = "Roblox"
        # Title in page title: "<Title> | Roblox"
        if "|" in raw_page_title:
            title = raw_page_title.split("|")[0].strip()
        else:
            title = raw_page_title.replace("Roblox", "").strip()
    elif "greenhouse.io" in domain:
        # e.g. "Job Application for Senior Software Engineer, Backend (Card Loan Platform) at Affirm"
        if " at " in raw_page_title:
            pre, post = raw_page_title.rsplit(" at ", 1)
            company = post.strip()
            title = pre.replace("Job Application for", "").strip()
        elif " - " in raw_page_title:
            company, title = [p.strip() for p in raw_page_title.split(" - ", 1)]
    elif "angellist.com" in domain:
        company = "AngelList"
        if "|" in raw_page_title:
            title = raw_page_title.split("|")[0].strip()
    elif "amazon.jobs" in domain:
        company = "Amazon"
        # e.g. "WW Tech Leader, Games TFC, AWS for Games - Job ID: 10578627 | Amazon.jobs"
        t = raw_page_title.split("|")[0].strip()
        if " - Job ID:" in t:
            t = t.split(" - Job ID:")[0].strip()
        title = t
        if "AWS" in title or "AWS" in full_text[:500]:
            company = "Amazon AWS"
    elif "kaiserpermanentejobs.org" in domain:
        company = "Kaiser Permanente"
        if " at Kaiser Permanente" in raw_page_title:
            title = raw_page_title.split(" at Kaiser Permanente")[0].strip()
    elif "lilly.com" in domain:
        company = "Eli Lilly"
        if " in " in raw_page_title:
            title = raw_page_title.split(" in ")[0].strip()
        elif "|" in raw_page_title:
            title = raw_page_title.split("|")[0].strip()
    elif "biospace.com" in domain:
        company = "TuneLab / Eli Lilly"
        if "|" in raw_page_title:
            title = raw_page_title.split("|")[0].strip()

    return full_text, title, company, is_closed


def parse_jd(job_id: str, source: str, work_dir: Path | str = "work") -> JobDescription:
    dest_dir = Path(work_dir) / job_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    raw_file = dest_dir / "jd_raw.txt"

    if raw_file.exists():
        raw_text = raw_file.read_text(encoding="utf-8")
        title = ""
        company = ""
        is_closed = False
    else:
        if source.startswith(("http://", "https://")):
            raw_text, title, company, is_closed = fetch_url_content(source)
        else:
            raw_text = Path(source).expanduser().read_text(encoding="utf-8")
            title = ""
            company = ""
            is_closed = False
        raw_file.write_text(raw_text, encoding="utf-8")

    # Fallback heuristic extraction if not already matched
    parsed = urlparse(source)
    domain = parsed.netloc.lower()

    if not company:
        if "apple.com" in domain:
            company = "Apple"
        elif "thatch.com" in domain:
            company = "Thatch"
        elif "togetherai" in source or "together.ai" in source:
            company = "Together AI"
        elif "sutterhealth" in source:
            company = "Sutter Health"
        elif "activisionblizzard" in domain or "xbox" in source.lower():
            company = "Activision Blizzard / Microsoft Gaming"
        else:
            company = domain.replace("www.", "").split(".")[0].capitalize()

    if not title:
        lines = [line for line in raw_text.splitlines() if line.strip()]
        if lines:
            title = lines[0][:80]

    return JobDescription(
        id=job_id,
        source=source,
        title=title,
        company=company,
        raw_text=raw_text,
        closed=is_closed,
    )


def ingest_all_pending(tracker_path: str = "output/tracker.json", work_dir: str = "work") -> list[JobDescription]:
    """Ingest raw JDs for all jobs in tracker that are 'new' or missing jd_raw.txt."""
    tracker = Tracker(tracker_path)
    work_path = Path(work_dir)
    results = []

    for jid, job in tracker.jobs.items():
        raw_file = work_path / jid / "jd_raw.txt"
        needs_ingest = job.status == "new" or not raw_file.exists()
        if not needs_ingest:
            continue

        print(f"Ingesting {jid} ({job.source})...")
        try:
            jd = parse_jd(jid, job.source, work_dir=work_path)
            if jd.company:
                job.company = jd.company
            if jd.title:
                job.title = jd.title
            if jd.closed:
                job.status = "blocked"
                job.note = "Posting is closed / expired on company portal"
                print(f"  [CLOSED] Marked {jid} as blocked ({job.company} - {job.title})")
            else:
                if job.status == "new":
                    job.status = "fetched"
                print(f"  [OK] Ingested: {job.company} – {job.title} ({len(jd.raw_text)} chars)")
            results.append(jd)
        except Exception as e:
            print(f"  [ERROR] Failed to ingest {jid}: {e}")
            job.status = "blocked"
            job.note = f"Ingestion error: {e}"

    tracker.save()
    tracker.write_index()
    print(f"\nIngestion complete: {len(results)} jobs processed.")
    return results


if __name__ == "__main__":
    ingest_all_pending()
