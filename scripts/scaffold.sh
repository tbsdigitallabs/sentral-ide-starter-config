#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: scaffold.sh <brief.yaml> <target-directory>"
  exit 1
fi
STARTER_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python -m scaffold --brief "$1" --target "$2"
