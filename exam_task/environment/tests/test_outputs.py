"""Hidden expected output for the verifier.

This file MUST NOT ship inside the built image. It contains the answer key.
"""
import json

EXPECTED_TOP = [
    {"ip": "203.0.113.10", "errors": 7},
    {"ip": "198.51.100.4", "errors": 4},
    {"ip": "192.0.2.55", "errors": 2},
    {"ip": "203.0.113.77", "errors": 2},
    {"ip": "192.0.2.7", "errors": 1},
]


def test_output_matches_expected():
    with open("/app/output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == EXPECTED_TOP
