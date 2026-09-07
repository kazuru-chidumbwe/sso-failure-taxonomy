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
    if data.get("corpus_layer") != "decision_test_battery":
        raise SystemExit("stress-cases: corpus_layer must be decision_test_battery")
    if data.get("manuscript_table") != "VIII":
        raise SystemExit("stress-cases: manuscript_table must be VIII")
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


def verify_corpus_manifest() -> None:
    corpus = json.loads((ROOT / "corpus.json").read_text(encoding="utf-8"))
    incidents = json.loads((ROOT / "incidents.json").read_text(encoding="utf-8"))
    stress = json.loads((ROOT / "stress-cases.json").read_text(encoding="utf-8"))

    if incidents.get("evaluation_corpus") != "codebook/corpus.json":
        raise SystemExit("incidents.json: evaluation_corpus must point to codebook/corpus.json")

    tables = corpus.get("manuscript_tables", {})
    if incidents.get("manuscript_tables") != tables:
        raise SystemExit("incidents.json manuscript_tables != corpus.json manuscript_tables")
    if "decision_test_battery" not in tables or tables["decision_test_battery"] != "VIII":
        raise SystemExit("corpus.json: decision_test_battery must map to VIII")
    if "overlap_routing_contingency" in tables:
        raise SystemExit("corpus.json: legacy overlap_routing_contingency key must be removed")

    layers = {layer["id"]: layer for layer in corpus.get("layers", [])}
    if set(layers) != {"estate_catalog_n11", "decision_test_battery"}:
        raise SystemExit(f"corpus.json: unexpected layer ids {set(layers)}")

    n11 = layers["estate_catalog_n11"]
    if n11.get("n") != 11 or n11.get("file") != "codebook/incidents.json":
        raise SystemExit("corpus.json: estate_catalog_n11 layer mismatch")
    if len(incidents.get("incidents", [])) != 11:
        raise SystemExit("corpus.json: estate layer n=11 but incidents.json row count differs")

    battery = layers["decision_test_battery"]
    if battery.get("n") != 8 or battery.get("file") != "codebook/stress-cases.json":
        raise SystemExit("corpus.json: decision_test_battery layer mismatch")
    if stress.get("corpus_layer") != "decision_test_battery":
        raise SystemExit("stress-cases.json corpus_layer does not match corpus manifest")

    oracle = corpus.get("oracle")
    if oracle != "codebook/validate_catalog_assignments.py":
        raise SystemExit("corpus.json oracle path mismatch")
    if not (ROOT / "validate_catalog_assignments.py").is_file():
        raise SystemExit("corpus oracle file missing")


def main() -> int:
    verify_catalog()
    verify_decision_tests()
    verify_corpus_manifest()
    print("catalog assignments, decision-test battery, and corpus manifest: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
