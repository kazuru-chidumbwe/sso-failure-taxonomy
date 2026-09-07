#!/usr/bin/env python3
"""Verify N=11 catalog assignments and S1-S10 decision-test battery (make smoke)."""
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
    "S9": "mfa_delivery",
    "S10": "outside_taxonomy",
}

NEGATIVE_DECOYS_GOLDEN: dict[str, tuple[str, str, str]] = {
    "D1": ("S1", "protocol_gateway", "outside_taxonomy"),
    "D2": ("S5", "edge_side_effect", "session_plane"),
    "D3": ("S7", "edge_side_effect", "edge_callback_consume"),
    "D4": ("S8", "protocol_gateway", "dual_idp_boundary"),
}

REJECTED_ESTATE_GOLDEN: dict[str, str] = {
    "R1": "outside_taxonomy",
    "R2": "outside_taxonomy",
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
    if len(vignettes) != 10:
        raise SystemExit(f"stress-cases: expected 10 vignettes, got {len(vignettes)}")
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
    if outside != 5:
        raise SystemExit(f"stress-cases: expected 5 outside_taxonomy, got {outside}")
    summary = data.get("summary", {})
    if summary.get("n") != 10 or summary.get("outside_taxonomy") != 5:
        raise SystemExit("stress-cases summary counts mismatch")
    if summary.get("negative_decoys") != 4:
        raise SystemExit("stress-cases summary negative_decoys must be 4")


def verify_negative_decoys() -> None:
    data = json.loads((ROOT / "stress-cases.json").read_text(encoding="utf-8"))
    valid = valid_category_ids() | {"outside_taxonomy"}
    decoys = data.get("negative_decoys", [])
    if len(decoys) != 4:
        raise SystemExit(f"negative_decoys: expected 4, got {len(decoys)}")
    for d in decoys:
        did = d["id"]
        expected = NEGATIVE_DECOYS_GOLDEN.get(did)
        if expected is None:
            raise SystemExit(f"decoy {did}: not in golden map")
        pairs_with, incorrect, correct = expected
        if d.get("pairs_with") != pairs_with:
            raise SystemExit(f"decoy {did}: pairs_with mismatch")
        if d.get("incorrect_label") != incorrect:
            raise SystemExit(f"decoy {did}: incorrect_label mismatch")
        if d.get("correct_label") != correct:
            raise SystemExit(f"decoy {did}: correct_label mismatch")
        if incorrect == correct:
            raise SystemExit(f"decoy {did}: incorrect_label must differ from correct_label")
        if incorrect not in valid or correct not in valid:
            raise SystemExit(f"decoy {did}: label not in valid set")
        if STRESS_GOLDEN.get(pairs_with) != correct:
            raise SystemExit(f"decoy {did}: correct_label must match paired vignette golden")


def verify_rejected_estate() -> None:
    data = json.loads((ROOT / "rejected-estate-vignettes.json").read_text(encoding="utf-8"))
    valid = valid_category_ids() | {"outside_taxonomy"}
    vignettes = data.get("vignettes", [])
    if len(vignettes) != 2:
        raise SystemExit(f"rejected-estate: expected 2 vignettes, got {len(vignettes)}")
    if data.get("not_in_n11") is not True:
        raise SystemExit("rejected-estate: not_in_n11 must be true")
    for v in vignettes:
        vid = v["id"]
        coding = v["coding"]
        if coding not in valid:
            raise SystemExit(f"rejected-estate {vid}: invalid coding {coding}")
        expected = REJECTED_ESTATE_GOLDEN.get(vid)
        if expected is None:
            raise SystemExit(f"rejected-estate {vid}: not in golden map")
        if coding != expected:
            raise SystemExit(f"rejected-estate {vid}: coding {coding} != golden {expected}")
    summary = data.get("summary", {})
    if summary.get("n") != 2 or summary.get("outside_taxonomy") != 2:
        raise SystemExit("rejected-estate summary counts mismatch")


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
    if set(layers) != {"estate_catalog_n11", "decision_test_battery", "rejected_estate_adjacent"}:
        raise SystemExit(f"corpus.json: unexpected layer ids {set(layers)}")

    n11 = layers["estate_catalog_n11"]
    if n11.get("n") != 11 or n11.get("file") != "codebook/incidents.json":
        raise SystemExit("corpus.json: estate_catalog_n11 layer mismatch")
    if len(incidents.get("incidents", [])) != 11:
        raise SystemExit("corpus.json: estate layer n=11 but incidents.json row count differs")

    battery = layers["decision_test_battery"]
    if battery.get("n") != 10 or battery.get("file") != "codebook/stress-cases.json":
        raise SystemExit("corpus.json: decision_test_battery layer mismatch")
    if battery.get("negative_decoys") != 4:
        raise SystemExit("corpus.json: decision_test_battery negative_decoys must be 4")
    if stress.get("corpus_layer") != "decision_test_battery":
        raise SystemExit("stress-cases.json corpus_layer does not match corpus manifest")

    rejected_layer = layers["rejected_estate_adjacent"]
    if rejected_layer.get("n") != 2:
        raise SystemExit("corpus.json: rejected_estate_adjacent n must be 2")
    if rejected_layer.get("file") != "codebook/rejected-estate-vignettes.json":
        raise SystemExit("corpus.json: rejected_estate_adjacent file mismatch")
    rejected = json.loads((ROOT / "rejected-estate-vignettes.json").read_text(encoding="utf-8"))
    if len(rejected.get("vignettes", [])) != 2:
        raise SystemExit("rejected-estate-vignettes.json row count mismatch")

    oracle = corpus.get("oracle")
    if oracle != "codebook/validate_catalog_assignments.py":
        raise SystemExit("corpus.json oracle path mismatch")
    if not (ROOT / "validate_catalog_assignments.py").is_file():
        raise SystemExit("corpus oracle file missing")


def main() -> int:
    verify_catalog()
    verify_decision_tests()
    verify_negative_decoys()
    verify_rejected_estate()
    verify_corpus_manifest()
    print("catalog, decision tests, decoys, rejected estate, corpus manifest: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
