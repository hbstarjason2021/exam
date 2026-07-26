#!/bin/bash
set -euo pipefail
./app/analyze.py app/access.log app/output.json
