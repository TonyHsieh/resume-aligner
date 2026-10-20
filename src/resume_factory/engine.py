"""Alignment and tailoring engine for target job descriptions.

Strictly adheres to:
1. Absolute Truthfulness: Only facts, metrics, and tools from Fact Ledger.
2. Tailoring & Reframing: Emphasizes genuine accomplishments relevant to the target role.
3. Review Highlighting: Changes marked with **bold** in resume_REVIEW.docx.
4. SAMPLE_FORMAT.docx fidelity: Header (mobile/email only, no grad year), 9pt Times New Roman, bold headings.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from .ledger import FactLedger, load_fact_ledger
from .model import Labeled, Resume, Role
from .render_docx import render_resume
from .tracker import Tracker, sha
from .validate import validate_resume


def load_all_alignments(
    alignments_dir: Path | str = "output/alignments",
) -> dict[str, dict[str, Any]]:
    """Load all alignment configurations from output/alignments/*.py (with fallback to src/resume_factory/alignments_*.py)."""
    alignments: dict[str, dict[str, Any]] = {}

    # 1. Primary: output/alignments/*.py
    p = Path(alignments_dir)
    if p.exists():
        for f in sorted(p.glob("*.py")):
            if f.name.startswith("__"):
                continue
            mod_name = f"output_alignments_{f.stem}"
            try:
                spec = importlib.util.spec_from_file_location(mod_name, f)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    sys.modules[mod_name] = mod
                    spec.loader.exec_module(mod)
                    for var_name in dir(mod):
                        if var_name.endswith("_ALIGNMENTS") and isinstance(getattr(mod, var_name), dict):
                            alignments.update(getattr(mod, var_name))
            except Exception as e:
                print(f"Warning: could not load alignments from {f}: {e}")

    # 2. Fallback / backward compatibility: src/resume_factory/alignments_*.py
    src_dir = Path(__file__).parent
    for f in sorted(src_dir.glob("alignments_*.py")):
        mod_name = f"resume_factory.{f.stem}"
        if mod_name not in sys.modules:
            try:
                spec = importlib.util.spec_from_file_location(mod_name, f)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    sys.modules[mod_name] = mod
                    spec.loader.exec_module(mod)
                    for var_name in dir(mod):
                        if var_name.endswith("_ALIGNMENTS") and isinstance(getattr(mod, var_name), dict):
                            alignments.update(getattr(mod, var_name))
            except Exception as e:
                print(f"Warning: could not load alignments from {f}: {e}")

    return alignments


def generate_all_alignments(
    ledger_path: str = "inputs/facts.yaml",
    tracker_path: str = "output/tracker.json",
    output_base: str = "output",
    alignments_dir: str = "output/alignments",
):
    ledger = load_fact_ledger(ledger_path)
    tracker = Tracker(tracker_path)

    # Master facts hash for freshness tracking
    master_facts_hash = sha(Path(ledger_path).read_text(encoding="utf-8"))

    # Load alignment strategies from output/alignments (gitignored)
    alignments = load_all_alignments(alignments_dir)

    # Ensure search category listings are blocked
    if "job-2061ebf1" in tracker.jobs:
        tracker.jobs["job-2061ebf1"].status = "blocked"
        tracker.jobs["job-2061ebf1"].company = "Amazon"
        tracker.jobs["job-2061ebf1"].title = "Category Search Index"
        tracker.jobs["job-2061ebf1"].note = "Search category index (moved to List of List of Jobs tab)"

    results = []


    for jid, cfg in alignments.items():
        job = tracker.jobs.get(jid)
        if not job:
            continue

        if "company" in cfg and not job.company:
            job.company = cfg["company"]
        if "title" in cfg and not job.title:
            job.title = cfg["title"]

        slug = cfg["slug"]
        # Load directives
        directives_path = Path("inputs/directives.yaml")
        cutoff_year = 2011
        key_leadership_skills = []
        if directives_path.exists():
            import yaml
            dirs = yaml.safe_load(directives_path.read_text(encoding="utf-8")) or {}
            cutoff_year = dirs.get("ageism", {}).get("cutoff_year", 2011)
            key_leadership_skills = dirs.get("skills_emphasis", {}).get("key_leadership_skills", [])

        # Apply 15-year ageism filter to chronological roles
        import re
        filtered_roles = []
        for r in cfg["roles"]:
            years = re.findall(r"\b(19\d\d|20\d\d)\b", r.dates)
            end_yr = 2026 if "Present" in r.dates else (int(years[-1]) if years else 2026)
            if end_yr >= cutoff_year:
                filtered_roles.append(r)

        # Enhance skills with directives key leadership skills emphasis
        enhanced_skills = list(cfg["skills"])
        if key_leadership_skills:
            lead_text = ", ".join(key_leadership_skills) + "."
            has_lead = False
            for idx, s in enumerate(enhanced_skills):
                if any(k in s.label.lower() for k in ["leadership", "management", "operations"]):
                    enhanced_skills[idx] = Labeled(s.label, lead_text)
                    has_lead = True
                    break
            if not has_lead:
                enhanced_skills.append(Labeled("Key Leadership & Governance:", lead_text))

        # 1. Build Resume Object
        resume = Resume(
            name=ledger.name,
            headline=cfg["headline"],
            contact=f"mobile: {ledger.phone}  •  e-mail: {ledger.email}",
            summary=cfg["summary"],
            expertise=cfg["expertise"],
            roles=filtered_roles,
            education=[
                Labeled(f"{edu['institution']}:", edu["degree"])
                for edu in ledger.education
            ],
            skills=enhanced_skills,
        )


        # 2. Validate Resume
        is_valid, validation_errors = validate_resume(
            resume,
            ledger,
            cfg["cited_facts"],
            allowed_older_specialized=True,
        )
        if not is_valid:
            print(f"Validation warnings for {jid}: {validation_errors}")

        # 3. Render DOCX files
        job_dir = Path(output_base) / f"{jid}_{slug}"
        job_dir.mkdir(parents=True, exist_ok=True)
        clean_path = job_dir / "resume.docx"
        review_path = job_dir / "resume_REVIEW.docx"
        render_resume(resume, clean_path, review=False)
        render_resume(resume, review_path, review=True)

        # 4. Generate Comparative Alignment Report
        report_path = job_dir / "alignment_report.md"
        report_lines = [
            f"# Comparative Gap & Alignment Analysis: {job.company} – {job.title}",
            "",
            f"**Target Role:** {job.title}  ",
            f"**Company:** {job.company}  ",
            f"**Source Link:** [{job.source}]({job.source})  ",
            "",
            "## 1. Requirement vs. Evidence Matrix",
            "",
            "| Core Job Requirement / Competency | Direct Evidence in Source Resume | Alignment Status | Recommended Action / Reframing |",
            "|---|---|---|---|",
        ]
        for req, ev, status, rec in cfg["comparisons"]:
            report_lines.append(f"| **{req}** | {ev} | `{status}` | {rec} |")

        report_lines.extend([
            "",
            "## 2. Factual Integrity & Validation Audit",
            "",
            f"- **Validation Status:** `{'PASSED (0% Hallucination)' if is_valid else 'WARNINGS DETECTED'}`",
            f"- **Cited Fact IDs:** {', '.join(cfg['cited_facts'])}",
            f"- **Age-Trimming Strategy:** Contiguous oldest-experience truncation applied while retaining authentic specialized gaming/systems heritage for media/gaming targets.",
            f"- **Contact Hygiene:** Mobile and email only; graduation year omitted to combat ageism.",
            "",
            "## 3. Generated Artifacts",
            "",
            f"- [Tailored Resume (Clean DOCX)](file://{clean_path.resolve()})",
            f"- [Tailored Resume with Changes in Bold (Review DOCX)](file://{review_path.resolve()})",
            f"- [Clarifying Questions](file://{job_dir.resolve()}/questions.md)",
        ])
        report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

        # 5. Generate Clarifying Questions file
        q_path = job_dir / "questions.md"
        q_lines = [
            f"# Clarifying Questions for Disambiguation Gate: {job.company} – {job.title}",
            "",
            "The following targeted questions address nuances and specific team context where additional detail can further sharpen your interview positioning:",
            "",
        ]
        for i, q in enumerate(cfg["questions"], 1):
            q_lines.append(f"{i}. **{q}**")
        q_lines.append("")
        q_path.write_text("\n".join(q_lines) + "\n", encoding="utf-8")

        # 6. Update Tracker
        jd_file = Path("work") / jid / "jd_raw.txt"
        jd_hash = sha(jd_file.read_text(encoding="utf-8")) if jd_file.exists() else sha(job.source)
        tracker.mark_aligned(
            jid,
            jd_hash=jd_hash,
            master_hash=master_facts_hash,
            outputs={
                "resume": f"output/{jid}_{slug}/resume.docx",
                "review": f"output/{jid}_{slug}/resume_REVIEW.docx",
                "report": f"output/{jid}_{slug}/alignment_report.md",
                "questions": f"output/{jid}_{slug}/questions.md",
            },
            open_questions=len(cfg["questions"]),
        )
        results.append((jid, job.company, job.title, str(clean_path)))

    tracker.save()
    tracker.write_index()
    print(f"Successfully generated alignments for {len(results)} jobs.")
    return results


if __name__ == "__main__":
    generate_all_alignments()
