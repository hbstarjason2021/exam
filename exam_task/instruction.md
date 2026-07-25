# Task: Top-10 5xx Error IPs

You are given an nginx access log at `/app/access.log`. Read it, count how
many 5xx responses each client IP produced **within the most recent 24 hours
of log activity** (i.e. the 24 hours ending at the latest timestamp present
in the log), and write the top-10 IPs (sorted by error count, descending) to
`/app/output.json`.

## Output format

A JSON array, one object per IP, in descending order of `errors`:

```json
[
  {"ip": "203.0.113.10", "errors": 17},
  {"ip": "198.51.100.4", "errors": 9},
  ...
]
```

- At most 10 entries.
- Ties may be broken in any deterministic order.
- If no 5xx responses fall in the 24-hour window, write `[]`.

## What you can use

A reference Python script `/app/analyze.py` is already available; you may
invoke it directly. It expects two positional arguments: input log path,
output JSON path.

## Constraints

- Do not modify `/app/analyze.py` or `/app/access.log`.
- Do not write anything outside of `/app/output.json`.
