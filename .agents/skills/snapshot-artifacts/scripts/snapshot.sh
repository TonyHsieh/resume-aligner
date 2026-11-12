#!/usr/bin/env bash
# Snapshot and restore helper script for resume-aligner artifacts

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/snapshot.py"

# Prefer devenv python if available, fallback to python3
if [ -x "$SCRIPT_DIR/../../../../.devenv/state/venv/bin/python" ]; then
    PYTHON_BIN="$SCRIPT_DIR/../../../../.devenv/state/venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
else
    echo "Error: Python 3 not found." >&2
    exit 1
fi

exec "$PYTHON_BIN" "$PYTHON_SCRIPT" "$@"

