#!/usr/bin/env python3
"""Verify N=11 catalog assignments and S1-S8 decision-test battery (make smoke)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Byte-frozen catalog labels @ v1.0.12 (category only; summaries checked separately).
CATALOG_GOLDEN: dict[str, str] = {
    "F1": "edge_side_effect",
    "F2": "edge_identifier",
    "F3": "edge_callback_consume",
    "F4": "session_plane",
    "F5": "edge_callback_consume",
    "I1": "directory_federation",
    "I2": "multi_site_affinity",
    "I3": "cluster_state",
    "I4": "protocol_gateway",
    "I5": "mfa_delivery",
    "I6": "dual_idp_boundary",
}

SEV_COUNTS_GOLDEN = {1: 1, 2: 9, 3: 1}
FORM_COUNTS_GOLDEN = {"DESIGN": 5, "RETRO": 6}

STRESS_GOLDEN: dict[str, str] = {
    "S1": "outside_taxonomy",
    "S2": "outside_taxonomy",
    "S3": "outside_taxonomy",
    "S4": "outside_taxonomy",
    "S5": "session_plane",
    "S6": "multi_site_affinity",
    "S7": "edge_callback_consume",
    "S8": "dual_idp_boundary",
}


def valid_category_ids() -> set[str]:
    tax = json.loads((ROOT / "taxonomy.json").read_text(encoding="utf-8"))
    return {c["id"] for c in tax["categories"]}


def verify_catalog() -> None:
    data = json.loads((ROOT / "incidents.json").read_text(encoding="utf-8"))
    valid = valid_category_ids()
    rows = data["incidents"]
    if len(rows) != 11:
        raise SystemExit(f"catalog: expected 11 rows, got {len(rows)}")
    sev_counts: dict[int, int] = {1: 0, 2: 0, 3: 0}
    form_counts: dict[str, int] = {"DESIGN": 0, "RETRO": 0}
    for row in rows:
        iid = row["id"]
        cat = row["category"]
        if cat not in valid:
            raise SystemExit(f"catalog {iid}: invalid category {cat}")
        expected = CATALOG_GOLDEN.get(iid)
        if expected is None:
            raise SystemExit(f"catalog {iid}: not in golden map")
        if cat != expected:
            raise SystemExit(f"catalog {iid}: category {cat} != golden {expected}")
        sev_counts[row["sev"]] += 1
        form_counts[row["form"]] += 1
    if sev_counts != SEV_COUNTS_GOLDEN:
        raise SystemExit(f"catalog sev counts: {sev_counts} != {SEV_COUNTS_GOLDEN}")
    if form_counts != FORM_COUNTS_GOLDEN:
        raise SystemExit(f"catalog form counts: {form_counts} != {FORM_COUNTS_GOLDEN}")


def verify_decision_tests() -> None:
    data = json.loads((ROOT / "stress-cases.json").read_text(encoding="utf-8"))
    valid = valid_category_ids() | {"outside_taxonomy"}
    vignettes = data["vignettes"]
    if len(vignettes) != 8:
        raise SystemExit(f"stress-cases: expected 8 vignettes, got {len(vignettes)}")
    outside = 0
    for v in vignettes:
        vid = v["id"]
        coding = v["coding"]
        if coding not in valid:
            raise SystemExit(f"stress {vid}: invalid coding {coding}")
        expected = STRESS_GOLDEN.get(vid)
        if expected is None:
            raise SystemExit(f"stress {vid}: not in golden map")
        if coding != expected:
            raise SystemExit(f"stress {vid}: coding {coding} != golden {expected}")
        if coding == "outside_taxonomy":
            outside += 1
    if outside != 4:
        raise SystemExit(f"stress-cases: expected 4 outside_taxonomy, got {outside}")
    summary = data.get("summary", {})
    if summary.get("n") != 8 or summary.get("outside_taxonomy") != 4:
        raise SystemExit("stress-cases summary counts mismatch")


def main() -> int:
    verify_catalog()
    verify_decision_tests()
    print("catalog assignments and decision-test battery: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
