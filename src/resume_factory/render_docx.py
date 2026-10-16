"""Render a :class:`Resume` into a DOCX that matches SAMPLE_FORMAT.docx.

The sample file itself is the template: its styles, numbering and page setup
are kept, and only the body paragraphs are replaced. Paragraph/run formatting
mirrors the sample exactly (PlainText style + Times New Roman run overrides).
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from .model import Labeled, Resume, Role, split_marked

FONT = "Times New Roman"
SZ_NAME = 28  # half-points (14 pt)
SZ_HEAD = 20  # 10 pt: headline and section headings
SZ_BODY = 18  # 9 pt
BULLET_NUM_ID = 1  # numbering definition used for bullets in the sample

DEFAULT_TEMPLATE = Path(__file__).resolve().parents[2] / "SAMPLE_FORMAT.docx"


def _rpr(bold: bool, italic: bool, size: int) -> str:
    return (
        "<w:rPr>"
        f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}"/>'
        + ("<w:b/><w:bCs/>" if bold else "")
        + ("<w:i/><w:iCs/>" if italic else "")
        + f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        "</w:rPr>"
    )


def _run(text: str, bold: bool = False, italic: bool = False, size: int = SZ_BODY) -> str:
    return (
        f"<w:r>{_rpr(bold, italic, size)}"
        f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    )


def _marked_runs(
    text: str, review: bool, bold: bool = False, italic: bool = False, size: int = SZ_BODY
) -> str:
    """Runs for ``text``; ``**changed**`` spans are bold only in review mode."""
    out = []
    for segment, changed in split_marked(text):
        out.append(_run(segment, bold=bold or (review and changed), italic=italic, size=size))
    return "".join(out)


def _para(
    runs: str = "",
    *,
    jc: str | None = None,
    border: bool = False,
    bullet: bool = False,
    mark_bold: bool = False,
    mark_italic: bool = False,
    mark_size: int | None = None,
):
    ppr = '<w:pStyle w:val="PlainText"/>'
    if bullet:
        ppr += f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{BULLET_NUM_ID}"/></w:numPr>'
    if border:
        ppr += '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="auto"/></w:pBdr>'
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    if mark_size is not None:
        ppr += _rpr(mark_bold, mark_italic, mark_size)
    xml = f"<w:p {nsdecls('w')}><w:pPr>{ppr}</w:pPr>{runs}</w:p>"
    return parse_xml(xml)


def _heading(text: str):
    return _para(
        _run(text, bold=True, size=SZ_HEAD), border=True, mark_bold=True, mark_size=SZ_HEAD
    )


def _labeled(item: Labeled, review: bool, bullet: bool = False):
    runs = _run(item.label, bold=True) + _marked_runs(" " + item.text, review)
    return _para(runs, bullet=bullet)


def _role_header(role: Role, review: bool):
    runs = (
        _run(role.company, bold=True)
        + _run(f" | {role.dates} | ")
        + _marked_runs(role.title, review, italic=True)
    )
    return _para(runs, mark_italic=True, mark_size=SZ_BODY)


def _blank():
    return _para()


def build_body(resume: Resume, review: bool = False) -> list:
    """Return the ordered list of body paragraph elements."""
    body = [
        _para(
            _run(resume.name, bold=True, size=SZ_NAME),
            jc="center",
            mark_bold=True,
            mark_size=SZ_NAME,
        ),
        _para(_marked_runs(resume.headline, review, size=SZ_HEAD), jc="center"),
        _para(
            _run(resume.contact),
            jc="center",
            border=True,
            mark_size=SZ_BODY,
        ),
        _para(jc="center", border=True, mark_size=SZ_BODY),
        _para(_marked_runs(resume.summary, review)),
        _heading("AREAS OF EXPERTISE"),
        _para(_marked_runs(" | ".join(resume.expertise), review)),
        _heading("PROFESSIONAL EXPERIENCE"),
    ]
    for role in resume.roles:
        body.append(_role_header(role, review))
        body.extend(_labeled(b, review, bullet=True) for b in role.bullets)
        body.append(_blank())
    body.append(_heading("EDUCATION"))
    body.extend(_labeled(e, review) for e in resume.education)
    body.append(_heading("KEY SKILLS & TOOLS"))
    body.extend(_labeled(s, review) for s in resume.skills)
    return body


def render_resume(
    resume: Resume,
    out_path: str | Path,
    *,
    review: bool = False,
    template: str | Path = DEFAULT_TEMPLATE,
) -> Path:
    """Write ``resume`` to ``out_path`` using ``template`` for styles/page setup."""
    document = docx.Document(str(template))
    body = document.element.body
    sect_pr = body.sectPr
    for child in list(body):
        if child is not sect_pr:
            body.remove(child)
    for element in build_body(resume, review=review):
        sect_pr.addprevious(element)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(out_path))
    return out_path
