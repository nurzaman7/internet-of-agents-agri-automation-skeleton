#!/usr/bin/env bash
set -euo pipefail
cp -n .env.example .env || true
python -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -e '.[dev,providers]'
echo "Bootstrap complete. Run: make dev"
