#!/usr/bin/env bash
# One-time setup: creates a virtual environment in .venv and installs the libraries.
set -e
cd "$(dirname "$0")"
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
echo
echo "All set! Activate the environment with:"
echo "    source .venv/bin/activate"
