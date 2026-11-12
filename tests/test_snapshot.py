"""Tests for the artifact snapshot and restore tool."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tarfile
import pytest

# Ensure snapshot module is importable
SKILL_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / ".agents" / "skills" / "snapshot-artifacts" / "scripts"
if str(SKILL_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SKILL_SCRIPTS_DIR))

import snapshot


@pytest.fixture
def mock_repo(tmp_path: Path) -> Path:
    """Create a mock repository structure with git and sample artifacts."""
    git_dir = tmp_path / ".git"
    git_dir.mkdir()

    # Create artifact directories
    inputs_dir = tmp_path / "inputs"
    inputs_dir.mkdir()
    (inputs_dir / "master_resume.html").write_text("<h1>Master Resume</h1>", encoding="utf-8")
    (inputs_dir / "facts.yaml").write_text("name: Test Candidate", encoding="utf-8")

    output_dir = tmp_path / "output"
    output_dir.mkdir()
    (output_dir / "INDEX.md").write_text("# Index", encoding="utf-8")
    job_out = output_dir / "job-123"
    job_out.mkdir()
    (job_out / "resume.html").write_text("Tailored resume", encoding="utf-8")

    work_dir = tmp_path / "work"
    work_dir.mkdir()
    (work_dir / "draft.txt").write_text("Draft notes", encoding="utf-8")

    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "2026-10-30-1200-context.html").write_text("<html>Context</html>", encoding="utf-8")

    # Create items that should be excluded
    pycache = output_dir / "__pycache__"
    pycache.mkdir()
    (pycache / "cached.pyc").write_bytes(b"\x00\x01\x02")

    pytest_cache = tmp_path / ".pytest_cache"
    pytest_cache.mkdir()
    (pytest_cache / "node").write_text("cache", encoding="utf-8")

    return tmp_path


# --- Boundary & Exclusion Unit Tests ---

def test_find_repo_root(mock_repo: Path) -> None:
    sub = mock_repo / "inputs" / "nested"
    sub.mkdir()
    assert snapshot.find_repo_root(sub) == mock_repo


def test_should_exclude_positive_matches() -> None:
    assert snapshot.should_exclude("work/__pycache__/file.pyc")
    assert snapshot.should_exclude(".git/HEAD")
    assert snapshot.should_exclude(".pytest_cache/v/cache")
    assert snapshot.should_exclude("output/job-1/temp.pyc")
    assert snapshot.should_exclude(".venv/bin/python")
    assert snapshot.should_exclude("snapshots/old-snapshot.tar.gz")


def test_should_exclude_negative_matches() -> None:
    assert not snapshot.should_exclude("inputs/master_resume.html")
    assert not snapshot.should_exclude("context/2026-10-30-1200-context.html")
    assert not snapshot.should_exclude("output/job-123/resume.html")
    assert not snapshot.should_exclude("work/draft.txt")


# --- Collection Unit Tests ---

def test_collect_artifact_files(mock_repo: Path) -> None:
    files = snapshot.collect_artifact_files(mock_repo)
    rel_paths = [rel for _, rel in files]

    assert "inputs/master_resume.html" in rel_paths
    assert "inputs/facts.yaml" in rel_paths
    assert "output/INDEX.md" in rel_paths
    assert "output/job-123/resume.html" in rel_paths
    assert "work/draft.txt" in rel_paths
    assert "context/2026-10-30-1200-context.html" in rel_paths

    # Verify exclusions
    for rel in rel_paths:
        assert "__pycache__" not in rel
        assert not rel.endswith(".pyc")
        assert ".pytest_cache" not in rel
        assert ".git" not in rel


# --- Creation & Manifest Tests ---

def test_create_snapshot_success(mock_repo: Path) -> None:
    archive_path, manifest = snapshot.create_snapshot(
        repo_root=mock_repo,
        verbose=False,
    )

    assert archive_path.exists()
    assert archive_path.stat().st_size > 0
    assert archive_path.name.startswith("resume-aligner-snapshot-")
    assert archive_path.name.endswith(".tar.gz")

    manifest_path = archive_path.with_suffix("").with_suffix(".manifest.json")
    assert manifest_path.exists()

    with manifest_path.open("r", encoding="utf-8") as f:
        loaded_manifest = json.load(f)

    assert loaded_manifest["file_count"] == 6
    assert loaded_manifest["sha256"] == snapshot.compute_sha256(archive_path)
    assert "inputs" in loaded_manifest["category_counts"]
    assert "context" in loaded_manifest["category_counts"]


def test_create_snapshot_empty_repo_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="No matching artifacts found"):
        snapshot.create_snapshot(repo_root=tmp_path, verbose=False)


# --- Inspection & Verification Tests ---

def test_list_and_verify_snapshot(mock_repo: Path) -> None:
    archive_path, _ = snapshot.create_snapshot(repo_root=mock_repo, verbose=False)

    members = snapshot.list_snapshot(archive_path)
    assert len(members) == 6
    assert "inputs/master_resume.html" in members

    ok, msg = snapshot.verify_snapshot(archive_path, verbose=False)
    assert ok
    assert "Archive OK" in msg
    assert "Manifest verified" in msg


def test_verify_snapshot_tampered_fails(mock_repo: Path) -> None:
    archive_path, _ = snapshot.create_snapshot(repo_root=mock_repo, verbose=False)
    manifest_path = archive_path.with_suffix("").with_suffix(".manifest.json")

    # Tamper with manifest sha
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump({"sha256": "bad_hash_value"}, f)

    ok, msg = snapshot.verify_snapshot(archive_path, verbose=False)
    assert not ok
    assert "SHA-256 mismatch" in msg


def test_verify_snapshot_missing_archive(tmp_path: Path) -> None:
    ok, msg = snapshot.verify_snapshot(tmp_path / "non_existent.tar.gz", verbose=False)
    assert not ok
    assert "Archive not found" in msg


# --- Restore Tests & Security Boundaries ---

def test_restore_snapshot_success(mock_repo: Path, tmp_path: Path) -> None:
    archive_path, _ = snapshot.create_snapshot(repo_root=mock_repo, verbose=False)

    restore_target = tmp_path / "restored_dir"
    count = snapshot.restore_snapshot(archive_path, restore_target, verbose=False)

    assert count == 6
    assert (restore_target / "inputs" / "master_resume.html").read_text(encoding="utf-8") == "<h1>Master Resume</h1>"
    assert (restore_target / "context" / "2026-10-30-1200-context.html").exists()


def test_restore_snapshot_preserves_existing_without_force(mock_repo: Path, tmp_path: Path) -> None:
    archive_path, _ = snapshot.create_snapshot(repo_root=mock_repo, verbose=False)

    restore_target = tmp_path / "restored_dir"
    restore_target.mkdir()
    inputs_target = restore_target / "inputs"
    inputs_target.mkdir()
    (inputs_target / "master_resume.html").write_text("Original Content", encoding="utf-8")

    # Restore without force
    snapshot.restore_snapshot(archive_path, restore_target, force=False, verbose=False)
    assert (inputs_target / "master_resume.html").read_text(encoding="utf-8") == "Original Content"

    # Restore with force
    snapshot.restore_snapshot(archive_path, restore_target, force=True, verbose=False)
    assert (inputs_target / "master_resume.html").read_text(encoding="utf-8") == "<h1>Master Resume</h1>"


def test_restore_snapshot_path_traversal_detection(tmp_path: Path) -> None:
    malicious_archive = tmp_path / "malicious.tar.gz"

    with tarfile.open(malicious_archive, "w:gz") as tar:
        # Create a member trying to escape target dir
        info = tarfile.TarInfo(name="../../outside_file.txt")
        info.size = 5
        import io
        tar.addfile(info, io.BytesIO(b"hello"))

    target_dir = tmp_path / "safe_extract"
    with pytest.raises(ValueError, match="Path traversal detected"):
        snapshot.restore_snapshot(malicious_archive, target_dir, verbose=False)

