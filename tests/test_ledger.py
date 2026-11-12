"""Tests for fact ledger parsing, HIPAA/PHI compliance tags, and data integrity."""

from __future__ import annotations

from pathlib import Path
import pytest

from resume_factory.ledger import (
    FactBullet,
    FactLedger,
    FactRole,
    clean_text,
    load_fact_ledger,
    parse_master_resume,
)


def test_clean_text() -> None:
    assert clean_text("   hello   world \n \t ") == "hello world"
    assert clean_text("") == ""


def test_load_fact_ledger_hipaa_phi_present() -> None:
    ledger_path = Path("inputs/facts.yaml")
    if not ledger_path.exists():
        pytest.skip("inputs/facts.yaml not found in workspace")

    ledger = load_fact_ledger(ledger_path)
    assert ledger.name == "Tony Hsieh"
    assert ledger.phone == "(555) 010-0000"

    # Find Blue Shield 2013 role
    bsc_2013_role = next((r for r in ledger.roles if r.id == "role_bsc_2013"), None)
    assert bsc_2013_role is not None
    assert "hipaa" in bsc_2013_role.tags
    assert "phi" in bsc_2013_role.tags

    # Check bullet 1 for HIPAA and PHI mentions
    b1 = next((b for b in bsc_2013_role.bullets if b.id == "fact_bsc_mid_01"), None)
    assert b1 is not None
    assert "HIPAA" in b1.raw_text
    assert "PHI" in b1.raw_text
    assert "HIPAA Compliance" in b1.tools
    assert "PHI Data Protection" in b1.tools


def test_skills_contain_hipaa_and_compliance() -> None:
    ledger_path = Path("inputs/facts.yaml")
    if not ledger_path.exists():
        pytest.skip("inputs/facts.yaml not found in workspace")

    ledger = load_fact_ledger(ledger_path)
    ops_skills = ledger.skills.get("leadership_and_ops", [])
    assert any("HIPAA" in s for s in ops_skills)
    assert any("Regulatory Compliance" in s for s in ops_skills)


def test_parse_master_resume_extracts_hipaa() -> None:
    html_path = Path("inputs/master_resume.html")
    if not html_path.exists():
        pytest.skip("inputs/master_resume.html not found in workspace")

    ledger = parse_master_resume(html_path)
    assert ledger.name == "Tony Hsieh"
    assert ledger.phone == "(555) 010-0000"

    bsc = next((r for r in ledger.roles if r.id == "role_bsc_2013"), None)
    assert bsc is not None
    assert "HIPAA" in bsc.bullets[0].raw_text
    assert "PHI" in bsc.bullets[0].raw_text


def test_independent_contractor_crypto_game_bullet() -> None:
    ledger_path = Path("inputs/facts.yaml")
    if not ledger_path.exists():
        pytest.skip("inputs/facts.yaml not found in workspace")

    ledger = load_fact_ledger(ledger_path)
    ic_role = next((r for r in ledger.roles if r.id == "role_independent_contractor_1999"), None)
    assert ic_role is not None
    assert any("DynamoDB" in b.raw_text or "crypto" in b.raw_text.lower() for b in ic_role.bullets)

