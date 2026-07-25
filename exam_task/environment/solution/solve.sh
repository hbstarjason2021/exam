#!/bin/bash
# Oracle solution that drives the analyzer end to end.
set -euo pipefail
/app/analyze.py /app/access.log /app/output.json
