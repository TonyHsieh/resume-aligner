"""Command line entry point: ``rf`` (or ``python -m resume_factory.cli``)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import requests

from .tracker import STATUSES, Tracker

DEFAULT_TRACKER = "output/tracker.json"
LIST_SOURCE_FILE = Path("inputs/job_list_source.txt")
_GDOC_ID = re.compile(r"/document/d/([A-Za-z0-9_-]+)")


def fetch_list_text(source: str) -> str:
    """Read a job list from a Google Doc (shared by link) or a local text file."""
    if source.lower().startswith(("http://", "https://")):
        match = _GDOC_ID.search(source)
        if not match:
            raise SystemExit("Only Google Doc links or local files are supported for job lists.")
        url = f"https://docs.google.com/document/d/{match.group(1)}/export?format=txt"
        resp = requests.get(url, timeout=30)
        if resp.status_code in (401, 403):
            raise SystemExit(
                f"HTTP {resp.status_code}: the Google Doc is not shared. Set sharing to "
                "'Anyone with the link can view'."
            )
        resp.raise_for_status()
        return resp.content.decode("utf-8-sig")
    return Path(source).expanduser().read_text(encoding="utf-8-sig")


def _save(tracker: Tracker) -> None:
    tracker.save()
    tracker.write_index()


def cmd_sync(args) -> int:
    source = args.source
    from .sheets import DEFAULT_WEBHOOK_FILE, pull_from_sheets, push_to_sheets
    if source == "sheets" or (not source and DEFAULT_WEBHOOK_FILE.exists()):
        pulled = pull_from_sheets(tracker_path=args.tracker)
        if pulled:
            print(f"Synced from Google Sheet: {len(pulled)} new jobs discovered:")
            for u in pulled:
                print(f"  + {u}")
        else:
            print("Synced from Google Sheet: no new jobs (all jobs up-to-date).")
        push_to_sheets(tracker_path=args.tracker)
        return 0

    if not source:
        if not LIST_SOURCE_FILE.exists():
            raise SystemExit("No list source given and none remembered. Pass a URL or file.")
        source = LIST_SOURCE_FILE.read_text(encoding="utf-8").strip()
    text = fetch_list_text(source)
    LIST_SOURCE_FILE.parent.mkdir(parents=True, exist_ok=True)
    LIST_SOURCE_FILE.write_text(source + "\n", encoding="utf-8")

    tracker = Tracker(args.tracker)
    new, known = tracker.add_list(text)
    _save(tracker)
    print(f"Synced from {source}")
    print(f"  {len(new)} new, {len(known)} already tracked, {len(tracker.jobs)} total")
    for job in new:
        print(f"  + {job.id}  {job.source}")
    return 0


def cmd_add(args) -> int:
    tracker = Tracker(args.tracker)
    job, created = tracker.add(args.source, args.label)
    _save(tracker)
    print(f"{'Added' if created else 'Already tracked'}: {job.id}  {job.source}")
    return 0


def cmd_list(args) -> int:
    tracker = Tracker(args.tracker)
    jobs = tracker.pending() if args.pending else list(tracker.jobs.values())
    counts = tracker.counts()
    print(
        f"{counts['aligned']}/{len(tracker.jobs)} aligned  |  "
        + "  ".join(f"{s}:{n}" for s, n in counts.items() if s != "aligned" and n)
    )
    for job in jobs:
        print(f"  {job.status:<9} {job.id}  {job.name}")
    return 0


def cmd_mark(args) -> int:
    tracker = Tracker(args.tracker)
    matches = [j for j in tracker.jobs.values() if j.id == args.job or j.id.endswith(args.job)]
    if len(matches) != 1:
        raise SystemExit(f"Job {args.job!r} matched {len(matches)} jobs; use the full id.")
    fields = {"note": args.note} if args.note is not None else {}
    tracker.set_status(matches[0].id, args.status, **fields)
    _save(tracker)
    print(f"{matches[0].id} -> {args.status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rf", description="Resume Factory")
    parser.add_argument("--tracker", default=DEFAULT_TRACKER, help="tracker JSON path")
    sub = parser.add_subparsers(dest="group", required=True)

    jobs = sub.add_parser("jobs", help="track which jobs have been aligned").add_subparsers(
        dest="action", required=True
    )
    p = jobs.add_parser("sync", help="import jobs from a Google Doc / text file list")
    p.add_argument("source", nargs="?", help="list URL or file (remembered after first use)")
    p.set_defaults(func=cmd_sync)

    p = jobs.add_parser("add", help="add a single job URL or JD file")
    p.add_argument("source")
    p.add_argument("--label")
    p.set_defaults(func=cmd_add)

    p = jobs.add_parser("align", help="generate tailored resumes and alignment artifacts for tracked jobs")
    def cmd_align(args):
        from .engine import generate_all_alignments
        generate_all_alignments(tracker_path=args.tracker)
        return 0
    p.set_defaults(func=cmd_align)

    # Sheets integration
    sheets = sub.add_parser("sheets", help="Google Sheets integration").add_subparsers(
        dest="action", required=True
    )
    p = sheets.add_parser("sync", help="push aligned jobs to your Google Sheet via webhook")
    p.add_argument("--webhook", help="custom webhook URL override")
    def cmd_sheets_sync(args):
        from .sheets import pull_from_sheets, push_to_sheets
        pulled = pull_from_sheets(webhook_url=args.webhook, tracker_path=args.tracker)
        if pulled:
            print(f"Discovered {len(pulled)} new job URLs from your Google Sheet and added to tracker:")
            for u in pulled:
                print(f"  + {u}")
        res = push_to_sheets(webhook_url=args.webhook, tracker_path=args.tracker)
        if res.get("new_urls"):
            for u in res["new_urls"]:
                if u not in pulled:
                    print(f"  + Discovered new job URL: {u}")
        if res["status_code"] in (200, 302):
            print(f"Successfully synced with Google Sheet ({res['rows_count']} jobs tracked)!")
        else:
            print(f"Error ({res['status_code']}): {res['response_text']}")
        return 0 if res["status_code"] in (200, 302) else 1
    p.set_defaults(func=cmd_sheets_sync)

    p = jobs.add_parser("list", help="show tracked jobs and their status")
    p.add_argument("--pending", action="store_true", help="only jobs that still need work")
    p.set_defaults(func=cmd_list)

    p = jobs.add_parser("mark", help="manually set a job's status")
    p.add_argument("job", help="job id (or unique suffix)")
    p.add_argument("status", choices=STATUSES)
    p.add_argument("--note")
    p.set_defaults(func=cmd_mark)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
