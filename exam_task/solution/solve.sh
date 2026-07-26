#!/bin/bash
set -euo pipefail

python3 /app/analyze.py \
    /app/access.log \
    /app/output.json
