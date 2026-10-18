"""Parse a SAMPLE_FORMAT-style DOCX back into a :class:`Resume`.

Used for the renderer's round-trip golden test and, later, to validate
generated documents. Structure is recognised from formatting, not text:
section headings are bold 10 pt paragraphs with a bottom border.
"""

from __future__ import annotations

from pathlib import Path

import docx
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

from .model import Labeled, Resume, Role, normalize

HEADING_PT = 10.0


def _has_border(p: Paragraph) -> bool:
    ppr = p._p.pPr
    return ppr is not None and ppr.find(qn("w:pBdr")) is not None


def _is_bullet(p: Paragraph) -> bool:
    ppr = p._p.pPr
    return ppr is not None and ppr.find(qn("w:numPr")) is not None


def _runs(p: Paragraph) -> list[tuple[str, bool, bool, float | None]]:
    """Runs merged across fragments that share formatting."""
    merged: list[tuple[str, bool, bool, float | None]] = []
    for r in p.runs:
        size = r.font.size.pt if r.font.size else None
        key = (bool(r.bold), bool(r.italic), size)
        if merged and merged[-1][1:] == key:
            merged[-1] = (merged[-1][0] + r.text, *key)
        else:
            merged.append((r.text, *key))
    return merged


def _is_heading(p: Paragraph) -> bool:
    runs = _runs(p)
    return (
        _has_border(p)
        and len(runs) == 1
        and runs[0][1]
        and runs[0][3] == HEADING_PT
        and bool(runs[0][0].strip())
    )


def _labeled(p: Paragraph) -> Labeled:
    runs = _runs(p)
    label = runs[0][0] if runs and runs[0][1] else ""
    rest = "".join(t for t, *_ in runs[1:]) if label else "".join(t for t, *_ in runs)
    return Labeled(normalize(label), normalize(rest))


def _role(p: Paragraph) -> Role:
    runs = _runs(p)
    company = normalize(runs[0][0])
    middle = runs[1][0]  # " | dates | "
    dates = normalize(middle).strip("|").strip()
    title = normalize("".join(t for t, *_ in runs[2:]))
    return Role(company=company, dates=dates, title=title)


def parse_docx(path: str | Path) -> Resume:
    paras = docx.Document(str(path)).paragraphs
    name = normalize(paras[0].text)
    headline = normalize(paras[1].text)
    contact = normalize(paras[2].text)
    summary = normalize(paras[4].text)

    resume = Resume(name=name, headline=headline, contact=contact, summary=summary)
    section = None
    current: Role | None = None
    for p in paras[5:]:
        if _is_heading(p):
            section = normalize(p.text)
            current = None
            continue
        text = normalize(p.text)
        if section == "AREAS OF EXPERTISE":
            if text:
                resume.expertise = [normalize(x) for x in text.split("|")]
        elif section == "PROFESSIONAL EXPERIENCE":
            if _is_bullet(p):
                assert current is not None, "bullet before any role header"
                current.bullets.append(_labeled(p))
            elif text:
                current = _role(p)
                resume.roles.append(current)
        elif section == "EDUCATION":
            if text:
                resume.education.append(_labeled(p))
        elif section == "KEY SKILLS & TOOLS":
            if text:
                resume.skills.append(_labeled(p))
    return resume
