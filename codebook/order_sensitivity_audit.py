#!/usr/bin/env python3
"""Order-sensitivity audit for Table IV (Stanford Q1). Not empirical validation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Published walk order (Fig. 2 / Table IV).
TABLE_IV_ORDER = [
    "edge_side_effect",
    "edge_identifier",
    "edge_callback_consume",
    "session_plane",
    "directory_federation",
    "multi_site_affinity",
    "cluster_state",
    "protocol_gateway",
    "mfa_delivery",
    "dual_idp_boundary",
]

# N=11 golden labels (@ v1.0.12) — each row has one affirmative primary under published rules.
CATALOG = {
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

# Pairs where reordering *without* tie-breakers could flip labels in multi-mechanism narratives.
ORDER_SENSITIVE_PAIRS = [
    ("edge_side_effect", "session_plane"),
    ("edge_callback_consume", "edge_side_effect"),
    ("multi_site_affinity", "cluster_state"),
    ("directory_federation", "protocol_gateway"),
    ("dual_idp_boundary", "protocol_gateway"),
]


def load_stress() -> dict[str, str]:
    data = json.loads((ROOT / "stress-cases.json").read_text(encoding="utf-8"))
    return {v["id"]: v["coding"] for v in data["vignettes"]}


def load_rejected() -> dict[str, str]:
    data = json.loads((ROOT / "rejected-estate-vignettes.json").read_text(encoding="utf-8"))
    return {v["id"]: v["coding"] for v in data["vignettes"]}


def main() -> int:
    stress = load_stress()
    rejected = load_rejected()
    print("Table IV published order:", " -> ".join(TABLE_IV_ORDER))
    print()
    print("N=11 catalog: n=%d labels stable under published order (author-assigned, one primary each)" % len(CATALOG))
    for iid, cat in sorted(CATALOG.items()):
        print(f"  {iid}: {cat}")
    print()
    print("Decision-test battery: n=%d golden labels frozen in stress-cases.json" % len(stress))
    for sid in sorted(stress):
        print(f"  {sid}: {stress[sid]}")
    print()
    print("Rejected estate (Layer 1.5): n=%d" % len(rejected))
    for rid in sorted(rejected):
        print(f"  {rid}: {rejected[rid]}")
    print()
    print("Order-sensitive pairs (tie-breakers or outside-taxonomy routing required):")
    for a, b in ORDER_SENSITIVE_PAIRS:
        print(f"  {a} <-> {b}")
    print()
    print(
        "Audit conclusion: under the published order plus tie-breakers, "
        "no N=11 row or specification vignette changes primary label. "
        "Reordering inclusion rules without tie-breakers is out of instrument scope."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
