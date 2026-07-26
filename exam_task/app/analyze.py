#!/usr/bin/env python3
"""Reference analyzer for top-10 5xx-emitting IPs in the last 24 hours.

DO NOT MODIFY. The exam framework checks for byte-equality of this file.
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta

LINE_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]+" '
    r'(?P<status>\d{3}) \d+'
)


def parse_ts(s: str) -> datetime:
    return datetime.strptime(s.split()[0], "%d/%b/%Y:%H:%M:%S")


def main(log_path: str, out_path: str) -> None:
    rows = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            m = LINE_RE.match(line)
            if not m:
                continue
            rows.append((parse_ts(m["ts"]), m["ip"], int(m["status"])))

    if not rows:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return

    latest = max(t for t, _, _ in rows)
    cutoff = latest - timedelta(hours=24)
    counts: Counter = Counter()
    for ts, ip, status in rows:
        if ts >= cutoff and 500 <= status < 600:
            counts[ip] += 1

    top = [{"ip": ip, "errors": n} for ip, n in counts.most_common(10)]
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(top, f)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: analyze.py <access.log> <output.json>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
