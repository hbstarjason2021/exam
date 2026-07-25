"""Smoke verifier invoked by tests/test.sh during the Oracle run.

Reads /app/output.json (the path contract pinned by instruction.md) and
checks structural sanity plus the top-1 IP.
"""
import json
import os


OUTPUT_PATH = "/app/output.json"


def test_output_exists():
    assert os.path.exists(OUTPUT_PATH), f"missing {OUTPUT_PATH}"


def test_output_is_list():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) <= 10


def test_output_entries_well_formed():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    for row in data:
        assert set(row.keys()) == {"ip", "errors"}
        assert isinstance(row["ip"], str)
        assert isinstance(row["errors"], int)
        assert row["errors"] >= 1


def test_output_descending():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    counts = [row["errors"] for row in data]
    assert counts == sorted(counts, reverse=True)


def test_top_ip_is_correct():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data, "output should not be empty"
    assert data[0]["ip"] == "203.0.113.10"
    assert data[0]["errors"] == 7
