#!/usr/bin/env python3
"""Snapshot and restore tool for personalized and untracked resume-aligner artifacts.

Captures all personalized inputs, generated resumes, work artifacts, session contexts,
and custom alignment files into an integrity-verified, timestamped archive.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import sys
import tarfile
from typing import Sequence

# Default artifact targets relative to repository root
DEFAULT_ARTIFACT_TARGETS = [
    "inputs",
    "output",
    "work",
    "context",
    "src/resume_factory/alignments*.py",
    "src/resume_factory/builder_data.py",
    ".env",
]

# Patterns or directory names to strictly exclude from snapshots
DEFAULT_EXCLUDES = [
    "__pycache__",
    "*.pyc",
    "*.pyo",
    ".pytest_cache",
    ".git",
    ".devenv",
    ".direnv",
    ".venv",
    "venv",
    "snapshots",
    "archives",
    ".DS_Store",
]


def find_repo_root(start_path: Path | None = None) -> Path:
    """Walk up from start_path to discover the git repository root."""
    current = (start_path or Path.cwd()).resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".git").exists():
            return parent
    return current


def should_exclude(rel_path: str, excludes: Sequence[str] = DEFAULT_EXCLUDES) -> bool:
    """Check if relative path matches any exclusion rule."""
    parts = Path(rel_path).parts
    for exc in excludes:
        if exc in parts:
            return True
        for part in parts:
            if exc.startswith("*") and part.endswith(exc[1:]):
                return True
            if exc == part:
                return True
    return False


def collect_artifact_files(
    repo_root: Path,
    targets: Sequence[str] = DEFAULT_ARTIFACT_TARGETS,
    excludes: Sequence[str] = DEFAULT_EXCLUDES,
) -> list[tuple[Path, str]]:
    """Scan the repository for files matching target artifacts.

    Returns a sorted list of tuples (absolute_path, relative_archive_path).
    """
    matched: dict[str, Path] = {}

    for target in targets:
        if "*" in target or "?" in target:
            # Glob match
            for p in repo_root.glob(target):
                if p.is_file():
                    rel = p.relative_to(repo_root).as_posix()
                    if not should_exclude(rel, excludes):
                        matched[rel] = p
        else:
            target_path = repo_root / target
            if not target_path.exists():
                continue
            if target_path.is_file():
                rel = target_path.relative_to(repo_root).as_posix()
                if not should_exclude(rel, excludes):
                    matched[rel] = target_path
            elif target_path.is_dir():
                for p in target_path.rglob("*"):
                    if p.is_file():
                        rel = p.relative_to(repo_root).as_posix()
                        if not should_exclude(rel, excludes):
                            matched[rel] = p

    return [(matched[k], k) for k in sorted(matched.keys())]


def compute_sha256(file_path: Path) -> str:
    """Compute hex SHA-256 checksum of a file."""
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def format_bytes(num_bytes: int) -> str:
    """Format byte count into human-readable string."""
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024.0 or unit == "GB":
            return f"{num_bytes:.2f} {unit}" if unit != "B" else f"{num_bytes} B"
        num_bytes /= 1024.0
    return f"{num_bytes:.2f} GB"


def create_snapshot(
    repo_root: Path,
    output_path: Path | None = None,
    outdir: Path | None = None,
    extra_targets: Sequence[str] | None = None,
    excludes: Sequence[str] = DEFAULT_EXCLUDES,
    verbose: bool = True,
) -> tuple[Path, dict]:
    """Create a tar.gz snapshot of all artifacts."""
    targets = list(DEFAULT_ARTIFACT_TARGETS)
    if extra_targets:
        targets.extend(extra_targets)

    files_to_pack = collect_artifact_files(repo_root, targets, excludes)

    if not files_to_pack:
        raise ValueError("No matching artifacts found to snapshot.")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    if output_path is None:
        target_dir = outdir or (repo_root / "snapshots")
        target_dir.mkdir(parents=True, exist_ok=True)
        archive_name = f"resume-aligner-snapshot-{timestamp}.tar.gz"
        archive_path = target_dir / archive_name
    else:
        archive_path = output_path.resolve()
        archive_path.parent.mkdir(parents=True, exist_ok=True)

    total_uncompressed_bytes = 0
    categories: dict[str, int] = {}

    with tarfile.open(archive_path, "w:gz") as tar:
        for abs_p, rel_p in files_to_pack:
            tar.add(abs_p, arcname=rel_p)
            file_size = abs_p.stat().st_size
            total_uncompressed_bytes += file_size

            top_cat = Path(rel_p).parts[0]
            categories[top_cat] = categories.get(top_cat, 0) + 1

    compressed_bytes = archive_path.stat().st_size
    sha256_hash = compute_sha256(archive_path)

    # Save manifest sidecar JSON
    manifest = {
        "snapshot_timestamp": timestamp,
        "archive_file": archive_path.name,
        "sha256": sha256_hash,
        "file_count": len(files_to_pack),
        "uncompressed_bytes": total_uncompressed_bytes,
        "uncompressed_human": format_bytes(total_uncompressed_bytes),
        "compressed_bytes": compressed_bytes,
        "compressed_human": format_bytes(compressed_bytes),
        "category_counts": categories,
        "files": [rel_p for _, rel_p in files_to_pack],
    }

    manifest_path = archive_path.with_suffix("").with_suffix(".manifest.json")
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    if verbose:
        print("=" * 60)
        print("ARTIFACT SNAPSHOT CREATED SUCCESSFULLY")
        print("=" * 60)
        print(f"Archive:       {archive_path}")
        print(f"Manifest:      {manifest_path}")
        print(f"SHA-256:       {sha256_hash}")
        print(f"Total Files:   {len(files_to_pack)}")
        print(f"Uncompressed:  {format_bytes(total_uncompressed_bytes)}")
        print(f"Compressed:    {format_bytes(compressed_bytes)}")
        print("Categories Breakdown:")
        for cat, cnt in sorted(categories.items()):
            print(f"  - {cat:20s}: {cnt:4d} files")
        print("=" * 60)

    return archive_path, manifest


def list_snapshot(archive_path: Path) -> list[str]:
    """Inspect and list members of a snapshot archive."""
    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    with tarfile.open(archive_path, "r:gz") as tar:
        members = [m.name for m in tar.getmembers() if m.isfile()]
    return members


def verify_snapshot(archive_path: Path, verbose: bool = True) -> tuple[bool, str]:
    """Verify integrity of the archive and companion manifest if present."""
    if not archive_path.exists():
        return False, f"Archive not found: {archive_path}"

    try:
        with tarfile.open(archive_path, "r:gz") as tar:
            members = tar.getmembers()
            count = len([m for m in members if m.isfile()])
        current_sha256 = compute_sha256(archive_path)

        manifest_path = archive_path.with_suffix("").with_suffix(".manifest.json")
        manifest_status = "No manifest file"
        if manifest_path.exists():
            with manifest_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            expected_sha = data.get("sha256")
            if expected_sha and expected_sha != current_sha256:
                return False, f"SHA-256 mismatch! Expected {expected_sha}, got {current_sha256}"
            manifest_status = "Manifest verified (SHA-256 match)"

        msg = f"Archive OK ({count} files, SHA-256: {current_sha256}, {manifest_status})"
        if verbose:
            print(f"[VERIFY SUCCESS] {msg}")
        return True, msg
    except Exception as e:
        return False, f"Archive verification failed: {e}"


def restore_snapshot(archive_path: Path, target_dir: Path, force: bool = False, verbose: bool = True) -> int:
    """Safely restore files from snapshot to target directory."""
    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    target_dir = target_dir.resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    extracted_count = 0
    with tarfile.open(archive_path, "r:gz") as tar:
        members = tar.getmembers()
        # Security check: verify no path traversal
        for m in members:
            resolved_dest = (target_dir / m.name).resolve()
            if not str(resolved_dest).startswith(str(target_dir)):
                raise ValueError(f"Path traversal detected in archive member: {m.name}")

        # Safe extraction
        for m in members:
            if not m.isfile():
                continue
            dest_file = target_dir / m.name
            if dest_file.exists() and not force:
                continue
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            tar.extract(m, path=target_dir, filter="data" if hasattr(tarfile, "data_filter") else None)
            extracted_count += 1

    if verbose:
        print(f"Restored {extracted_count} files to {target_dir}")
    return extracted_count


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Snapshot and restore tool for personalized resume-aligner artifacts."
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--create",
        action="store_true",
        default=True,
        help="Create a new snapshot archive (default action).",
    )
    group.add_argument(
        "--list",
        metavar="ARCHIVE",
        type=Path,
        help="List file contents of a snapshot archive.",
    )
    group.add_argument(
        "--verify",
        metavar="ARCHIVE",
        type=Path,
        help="Verify the integrity and manifest of a snapshot archive.",
    )
    group.add_argument(
        "--restore",
        metavar="ARCHIVE",
        type=Path,
        help="Restore snapshot archive into repository or destination directory.",
    )

    parser.add_argument(
        "--outdir",
        type=Path,
        default=None,
        help="Directory where the snapshot archive will be created (default: <repo_root>/snapshots).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Explicit file path for the snapshot archive.",
    )
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=None,
        help="Destination directory for --restore (default: repository root).",
    )
    parser.add_argument(
        "--include",
        action="append",
        dest="extra_targets",
        help="Additional file, folder, or glob pattern to include.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing files during restore.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress detailed console output.",
    )
    return parser.parse_args(args)


def main(args: Sequence[str] | None = None) -> int:
    parsed = parse_args(args)
    repo_root = find_repo_root()

    try:
        if parsed.list:
            members = list_snapshot(parsed.list)
            print(f"Snapshot contents ({len(members)} files):")
            for m in members:
                print(f"  {m}")
            return 0

        if parsed.verify:
            ok, msg = verify_snapshot(parsed.verify, verbose=not parsed.quiet)
            return 0 if ok else 1

        if parsed.restore:
            dest = parsed.target_dir or repo_root
            restore_snapshot(
                parsed.restore,
                dest,
                force=parsed.force,
                verbose=not parsed.quiet,
            )
            return 0

        # Default: --create
        archive_path, manifest = create_snapshot(
            repo_root=repo_root,
            output_path=parsed.output,
            outdir=parsed.outdir,
            extra_targets=parsed.extra_targets,
            verbose=not parsed.quiet,
        )
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

