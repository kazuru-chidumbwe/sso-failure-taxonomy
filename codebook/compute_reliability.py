#!/usr/bin/env python3
"""Regenerate or verify reliability statistics for N=11 and external-eval overlap."""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTERNAL = ROOT / "external-eval"
N11_SEED = 20260812
EXT_SEED = 20260906
BOOTSTRAP = 10000
OVERLAP_IDS = [
    "EN027", "EN028", "EN029", "EN030",
    "GH001", "GH002", "GH003", "GH004", "GH005",
    "GH009", "GH010", "GH015", "GH016",
]


def cohen_kappa_pairs(a: list, b: list) -> float:
    n = len(a)
    cats = sorted(set(a) | set(b))
    agree = sum(1 for x, y in zip(a, b) if x == y)
    po = agree / n
    pe = sum(sum(1 for x in a if x == c) / n * sum(1 for x in b if x == c) / n for c in cats)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def gwet_ac1_pairs(a: list, b: list) -> float:
    n = len(a)
    cats = sorted(set(a) | set(b))
    q = len(cats)
    agree = sum(1 for x, y in zip(a, b) if x == y)
    po = agree / n
    pe = sum(((sum(1 for x in a if x == c) / n) + (sum(1 for x in b if x == c) / n)) / 2 *
             (1 - ((sum(1 for x in a if x == c) / n) + (sum(1 for x in b if x == c) / n)) / 2)
             for c in cats) / (q - 1 if q > 1 else 1)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def bootstrap_ci(a: list, b: list, metric: str, seed: int) -> list[float]:
    n = len(a)
    rng = random.Random(seed)
    fn = cohen_kappa_pairs if metric == "kappa" else gwet_ac1_pairs
    vals = []
    for _ in range(BOOTSTRAP):
        idx = [rng.randrange(n) for _ in range(n)]
        la = [a[i] for i in idx]
        lb = [b[i] for i in idx]
        vals.append(fn(la, lb))
    vals.sort()
    return [vals[int(0.025 * BOOTSTRAP)], vals[int(0.975 * BOOTSTRAP)]]


def load_external_labels(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {a["narrative_id"]: a["primary_label"] for a in data["assignments"]}


def compute_n11() -> dict:
    incidents = json.loads((ROOT / "incidents.json").read_text(encoding="utf-8"))
    responses = json.loads((ROOT / "second-coder" / "responses.json").read_text(encoding="utf-8"))
    gold = {r["id"]: r for r in incidents["incidents"]}
    coder = {r["id"]: r for r in responses["responses"]}
    ids = sorted(gold.keys())
    gold_cat = [gold[i]["category"] for i in ids]
    coder_cat = [coder[i]["category"] for i in ids]
    gold_sev = [gold[i]["sev"] for i in ids]
    coder_sev = [coder[i]["sev"] for i in ids]
    cat_agree = sum(1 for a, b in zip(gold_cat, coder_cat) if a == b)
    sev_agree = sum(1 for a, b in zip(gold_sev, coder_sev) if a == b)
    return {
        "category": {
            "n_agree": cat_agree,
            "raw_agreement": cat_agree / len(ids),
            "gwet_ac1": gwet_ac1_pairs(gold_cat, coder_cat),
            "gwet_ac1_bootstrap_ci95": bootstrap_ci(gold_cat, coder_cat, "ac1", N11_SEED),
            "cohen_kappa": cohen_kappa_pairs(gold_cat, coder_cat),
            "cohen_kappa_bootstrap_ci95": bootstrap_ci(gold_cat, coder_cat, "kappa", N11_SEED),
        },
        "severity": {
            "n_agree": sev_agree,
            "raw_agreement": sev_agree / len(ids),
            "gwet_ac1": gwet_ac1_pairs(gold_sev, coder_sev),
            "gwet_ac1_bootstrap_ci95": bootstrap_ci(gold_sev, coder_sev, "ac1", N11_SEED),
            "cohen_kappa": cohen_kappa_pairs(gold_sev, coder_sev),
            "cohen_kappa_bootstrap_ci95": bootstrap_ci(gold_sev, coder_sev, "kappa", N11_SEED),
        },
    }


def compute_overlap() -> dict:
    a = load_external_labels(EXTERNAL / "coder-a.json")
    b = load_external_labels(EXTERNAL / "coder-b.json")
    la = [a[i] for i in OVERLAP_IDS]
    lb = [b[i] for i in OVERLAP_IDS]
    agree = sum(1 for x, y in zip(la, lb) if x == y)
    return {
        "n": len(OVERLAP_IDS),
        "raw_agreement": agree,
        "raw_agreement_pct": round(100 * agree / len(OVERLAP_IDS), 1),
        "gwet_ac1": gwet_ac1_pairs(la, lb),
        "gwet_ac1_bootstrap_ci95": bootstrap_ci(la, lb, "ac1", EXT_SEED),
        "cohen_kappa": cohen_kappa_pairs(la, lb),
        "cohen_kappa_bootstrap_ci95": bootstrap_ci(la, lb, "kappa", EXT_SEED),
    }


def approx_equal(a: float, b: float, tol: float = 1e-3) -> bool:
    return abs(a - b) <= tol


def verify_n11(computed: dict) -> None:
    rel = json.loads((ROOT / "reliability.json").read_text(encoding="utf-8"))
    for axis in ("category", "severity"):
        for key in ("n_agree", "raw_agreement", "gwet_ac1", "cohen_kappa"):
            if not approx_equal(computed[axis][key], rel[axis][key]):
                raise SystemExit(f"n11 {axis}.{key}: computed={computed[axis][key]} file={rel[axis][key]}")


def verify_overlap(computed: dict) -> None:
    rel = json.loads((EXTERNAL / "reliability-external-v1.json").read_text(encoding="utf-8"))
    oa = rel["overlap_agreement"]
    checks = [
        ("raw_agreement", oa["raw_agreement"]),
        ("gwet_ac1", oa["gwet_ac1"]),
        ("cohen_kappa", oa["cohen_kappa"]),
    ]
    for key, expected in checks:
        if not approx_equal(computed[key], expected, 1e-2):
            raise SystemExit(f"overlap {key}: computed={computed[key]} file={expected}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true", help="Verify against on-disk JSON (default)")
    parser.add_argument("--write", action="store_true", help="Rewrite reliability JSON stats sections")
    args = parser.parse_args()
    n11 = compute_n11()
    overlap = compute_overlap()
    if args.write:
        rel_path = ROOT / "reliability.json"
        rel = json.loads(rel_path.read_text(encoding="utf-8"))
        rel["category"].update({k: n11["category"][k] for k in n11["category"]})
        rel["severity"].update({k: n11["severity"][k] for k in n11["severity"]})
        rel_path.write_text(json.dumps(rel, indent=2) + "\n", encoding="utf-8")
        ext_path = EXTERNAL / "reliability-external-v1.json"
        ext = json.loads(ext_path.read_text(encoding="utf-8"))
        ext["overlap_agreement"].update({
            k: overlap[k] for k in overlap if k in ext["overlap_agreement"] or k in (
                "n", "raw_agreement", "raw_agreement_pct", "gwet_ac1",
                "gwet_ac1_bootstrap_ci95", "cohen_kappa", "cohen_kappa_bootstrap_ci95",
            )
        })
        ext_path.write_text(json.dumps(ext, indent=2) + "\n", encoding="utf-8")
        print("Wrote reliability stats")
    else:
        verify_n11(n11)
        verify_overlap(overlap)
        print("reliability.json and overlap_agreement: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
