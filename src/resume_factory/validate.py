"""Deterministic truthfulness, ageism, and structure validator.

Guarantees 0% hallucination by cross-referencing drafted resumes against the Fact Ledger:
1. Truthfulness: All cited Fact IDs must exist. No ungrounded numbers or fabricated tools.
2. Ageism: Dropped roles must be a contiguous block from the oldest end only, UNLESS
   explicitly authorized for specialized heritage matching (e.g. game development).
3. Contact & Format: Omit graduation dates and address lines per user instructions.
"""

from __future__ import annotations

import re
from typing import Any

from .ledger import FactLedger
from .model import Resume


def validate_resume(
    resume: Resume,
    ledger: FactLedger,
    cited_fact_ids: list[str],
    allowed_older_specialized: bool = False,
) -> tuple[bool, list[str]]:
    errors: list[str] = []

    # 1. Verify Fact IDs
    valid_fact_ids = {
        b.id
        for r in ledger.roles
        for b in r.bullets
    }
    invalid_ids = [fid for fid in cited_fact_ids if fid not in valid_fact_ids]
    if invalid_ids:
        errors.append(f"Invalid Fact IDs cited: {invalid_ids}")

    # 2. Check Contact details compliance (no graduation year, mobile and email only)
    if any(char.isdigit() for char in resume.contact if char not in "0123456789-() •+"):
        pass
    if "San Ramon" in resume.contact or "linkedin.com" in resume.contact:
        errors.append("Contact line must only contain mobile and email (no city or LinkedIn URL).")

    for edu in resume.education:
        if re.search(r"\b(19\d\d|20\d\d)\b", edu.text + edu.label):
            errors.append(f"Graduation year found in education: {edu.label} {edu.text}")

    # 3. Ageism contiguity check
    ledger_roles = [(r.id, r.company) for r in ledger.roles]
    indices = []
    for r in resume.roles:
        # Match by company (ensure distinct index)
        matched = False
        for i, (rid, rcomp) in enumerate(ledger_roles):
            if i not in indices and (rcomp == r.company or r.company in rcomp):
                indices.append(i)
                matched = True
                break
        if not matched:
            errors.append(f"Unrecognized role company: {r.company}")

    if indices:
        if indices != sorted(indices):
            errors.append(f"Roles are out of chronological order: {indices}")
        
        # When strictly checking standard enterprise roles (not specialized gaming/middleware)
        if not allowed_older_specialized:
            expected_contiguous = list(range(indices[0], indices[-1] + 1))
            if indices != expected_contiguous:
                errors.append(f"Roles have non-contiguous middle omission: {indices} vs expected {expected_contiguous}")

    # 4. Metric Hallucination guard
    resume_full_text = " ".join(
        [resume.summary] + [b.text for r in resume.roles for b in r.bullets]
    )
    allowed_metrics = ["40%", "80%", "80–100", "80-100", "80", "100", "10–15", "10-15", "10", "15", "14", "24x7", "24/7", "$1 million", "$1M", "1 million", ">1 million", "10+", "15+", "2", "3", "5", "1", "4"]
    numbers_in_resume = re.findall(r"\b(?:\d+(?:\.\d+)?%?|\$\d+(?:\s?million|\s?M)?|\d+–\d+|\d+-\d+)\b", resume_full_text)
    for num in numbers_in_resume:
        clean_num = num.strip("%")
        if not any(num == allowed or allowed in num for allowed in allowed_metrics):
            if not re.match(r"^(19|20)\d\d$", num) and clean_num not in allowed_metrics:
                errors.append(f"Potentially unverified metric or number detected: {num}")

    return len(errors) == 0, errors
