---
name: snapshot-artifacts
description: >-
  Creates an integrity-verified, timestamped snapshot archive (.tar.gz) of all personalized and generated artifacts (inputs, output, work, context, alignment configs, .env) that are not tracked in git.
  Use when the user asks to "snapshot artifacts", "archive artifacts", "backup personalized data", "backup resume data", or "create artifact snapshot".
---

# Snapshot Artifacts Skill

This skill creates a standalone, integrity-checked snapshot archive of all personalized, sensitive, and generated artifacts in the `resume-aligner` repository. Because these directories and files are personal and excluded from version control (`.gitignore`), snapshots ensure your master resumes, facts, targeted output, work tracking, and session contexts can be archived, preserved across machines, or backed up offsite.

---

## What is Included in the Snapshot

The snapshot captures all files in the following target directories and paths:
- `inputs/`: Master resume, personal facts, directives, job source URLs, webhooks.
- `output/`: Generated tailored resumes (HTML, DOCX), alignment analyses, trackers, indices.
- `work/`: Intermediate extraction drafts, parsed job descriptions, candidate alignment notes.
- `context/`: Historical session context reports (`*-context.html`) and context metadata.
- `src/resume_factory/alignments*.py`: Custom alignment rules and configurations (if present).
- `src/resume_factory/builder_data.py`: Custom builder data modules (if present).
- `.env`: Environment variables and secrets (if present).

### What is Excluded
To keep archives clean, compact, and deterministic, the tool strictly excludes:
- `__pycache__` and `*.pyc`
- `.pytest_cache`
- `.git`
- `.devenv` and `.direnv`
- `.venv` and virtual environments
- `snapshots/` and `archives/` (prevents recursive nesting)
- System temporary and hidden files (`.DS_Store`)

---

## Quick Reference / Commands

### 1. Create a Timestamped Snapshot
To create a snapshot archive in the `snapshots/` directory:

```bash
# Using Python directly
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py

# Or using the helper script
.agents/skills/snapshot-artifacts/scripts/snapshot.sh
```

**Output:**
- Archive: `snapshots/resume-aligner-snapshot-<YYYY-MM-DD-HHMMSS>.tar.gz`
- Sidecar Manifest: `snapshots/resume-aligner-snapshot-<YYYY-MM-DD-HHMMSS>.manifest.json`
- Prints: File counts per category, uncompressed and compressed sizes, and SHA-256 hash.

### 2. Custom Output Location (e.g. External Backup Drive or Directory)
```bash
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --outdir /path/to/backup/folder
# Or explicit filename:
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --output /path/to/my-backup.tar.gz
```

### 3. Verify Archive Integrity & Manifest
```bash
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --verify snapshots/<archive-name>.tar.gz
```

### 4. Inspect Archive Contents
```bash
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --list snapshots/<archive-name>.tar.gz
```

### 5. Restore Artifacts from Archive
```bash
# Restore without overwriting existing files:
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --restore snapshots/<archive-name>.tar.gz

# Force overwrite existing files:
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --restore snapshots/<archive-name>.tar.gz --force

# Restore to an alternate directory:
python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py --restore snapshots/<archive-name>.tar.gz --target-dir /path/to/extracted/
```

---

## Helper Scripts

- Python CLI Tool: [snapshot.py](./scripts/snapshot.py)
- Shell Wrapper: [snapshot.sh](./scripts/snapshot.sh)

---

## Agent Execution Checklist
When invoked by the user:
1. Identify if a custom destination directory or filename was requested.
2. Run `python3 .agents/skills/snapshot-artifacts/scripts/snapshot.py` (with any requested arguments).
3. Verify the generated `.tar.gz` file and inspect its SHA-256 and size summary.
4. Provide the user with:
   - Clickable link to the generated archive file.
   - Summary of archived files by category (`inputs`, `output`, `work`, `context`).
   - SHA-256 checksum for verification.

