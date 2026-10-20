"""Data model for a resume that can be rendered in the SAMPLE_FORMAT style.

Text fields may contain ``**changed wording**`` markers. The clean resume
strips the markers; the REVIEW resume renders the marked spans in bold so
modified wording is easy to audit against the source.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

CHANGE_MARK = "**"


@dataclass
class Labeled:
    """A ``Bold Label:`` followed by plain text (bullets, education, skills)."""

    label: str
    text: str


@dataclass
class Role:
    company: str
    dates: str
    title: str
    bullets: list[Labeled] = field(default_factory=list)


@dataclass
class Resume:
    name: str
    headline: str
    contact: str
    summary: str
    expertise: list[str] = field(default_factory=list)
    roles: list[Role] = field(default_factory=list)
    education: list[Labeled] = field(default_factory=list)
    skills: list[Labeled] = field(default_factory=list)


def split_marked(text: str) -> list[tuple[str, bool]]:
    """Split ``text`` into ``(segment, changed)`` pairs on ``**`` markers."""
    parts = text.split(CHANGE_MARK)
    segments = [(part, i % 2 == 1) for i, part in enumerate(parts) if part]
    return segments or [("", False)]


def strip_marks(text: str) -> str:
    return text.replace(CHANGE_MARK, "")


_WS = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Collapse whitespace so fragmented runs compare equal."""
    return _WS.sub(" ", text).strip()
