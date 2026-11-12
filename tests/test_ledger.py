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
    assert ledger.phone  # Populated dynamically from local facts.yaml (not hardcoded in git)

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
    assert ledger.phone  # Parsed from local master_resume.html / facts_addendum.md

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


def test_validate_resume_rejects_mismatched_phone_number() -> None:
    from resume_factory.model import Resume
    from resume_factory.validate import validate_resume

    ledger = FactLedger(
        name="Test Candidate",
        phone="(555) 010-1234",
        email="candidate@example.com",
        education=[],
        skills={},
        roles=[],
    )
    bad_resume = Resume(
        name="Test Candidate",
        headline="Principal Technologist",
        contact="mobile: (555) 010-9999  •  e-mail: candidate@example.com",
        summary="Experienced cloud platform leader.",
        expertise=[],
        roles=[],
        additional_roles=[],
        education=[],
        skills=[],
    )
    ok, errs = validate_resume(bad_resume, ledger, [])
    assert ok is False
    assert any("phone" in e.lower() for e in errs)


def test_load_fact_ledger_uses_facts_yaml_as_single_source_of_truth(tmp_path: Path) -> None:
    facts_file = tmp_path / "facts.yaml"
    facts_file.write_text(
        "name: Test Candidate\nphone: (555) 010-1234\nemail: canonical@example.com\neducation: []\nskills: {}\nroles: []\n",
        encoding="utf-8",
    )
    (tmp_path / "facts_addendum.md").write_text(
        "- Phone: (555) 010-9999\n- Email: stale@example.com\n",
        encoding="utf-8",
    )
    ledger = load_fact_ledger(facts_file)
    assert ledger.phone == "(555) 010-1234"
    assert ledger.email == "canonical@example.com"


def test_ingest_master_resume_writes_facts_yaml_and_cli(tmp_path: Path) -> None:
    from resume_factory.cli import main as cli_main
    from resume_factory.ledger import ingest_master_resume

    html_file = tmp_path / "master_resume.html"
    html_file.write_text(
        "<html><head><title>Test Candidate</title></head><body>"
        "<pre>mobile: (555) 010-1234\ne-mail: candidate@example.com</pre>"
        "</body></html>",
        encoding="utf-8",
    )
    out_file = tmp_path / "facts.yaml"
    rc = cli_main(["facts", "ingest", str(html_file), "--out", str(out_file)])
    assert rc == 0
    assert out_file.exists()

    loaded = load_fact_ledger(out_file)
    assert loaded.name == "Test Candidate"
    assert loaded.phone == "(555) 010-1234"
    assert loaded.email == "candidate@example.com"
    assert len(loaded.roles) > 0

    # Preserve-contact keeps existing contact info when re-ingesting updated HTML
    html_file.write_text(
        "<html><head><title>Other Name</title></head><body>"
        "<pre>mobile: (555) 010-9999\ne-mail: stale@example.com</pre>"
        "</body></html>",
        encoding="utf-8",
    )
    ingest_master_resume(html_file, out_path=out_file, preserve_contact=True)
    preserved = load_fact_ledger(out_file)
    assert preserved.name == "Test Candidate"
    assert preserved.phone == "(555) 010-1234"
    assert preserved.email == "candidate@example.com"


def test_ingest_master_resume_missing_source_fails(tmp_path: Path) -> None:
    from resume_factory.cli import main as cli_main

    with pytest.raises(SystemExit):
        cli_main(["facts", "ingest", str(tmp_path / "missing.html"), "--out", str(tmp_path / "facts.yaml")])

