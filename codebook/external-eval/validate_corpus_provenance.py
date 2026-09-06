#!/usr/bin/env python3
"""Validate external-eval corpus provenance invariants."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = Path(__file__).resolve().parent / "narratives.json"
AUTHOR = {f"EN{i:03d}" for i in range(1, 31)}
FAKE_GH = re.compile(r"/issues/(1[5-9]|2[0-8])000$")
OVERLAP = {
    "EN027", "EN028", "EN029", "EN030",
    "GH001", "GH002", "GH003", "GH004", "GH005",
    "GH009", "GH010", "GH015", "GH016",
}


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    live = ac = 0
    for item in data["narratives"]:
        nid = item["id"]
        prov = item.get("provenance")
        url = item.get("url")
        if nid in AUTHOR:
            if prov != "author-constructed":
                errors.append(f"{nid}: expected author-constructed, got {prov}")
            if url is not None:
                errors.append(f"{nid}: author-constructed must have url null")
            ac += 1
        else:
            if prov != "live-harvested":
                errors.append(f"{nid}: expected live-harvested, got {prov}")
            if not url:
                errors.append(f"{nid}: live-harvested must have url")
            if "### " in item.get("text", ""):
                errors.append(f"{nid}: raw paste remains in text")
            live += 1
        if url and FAKE_GH.search(url):
            errors.append(f"{nid}: placeholder GitHub URL {url}")
        if url and "/tagged/" in url:
            errors.append(f"{nid}: tag-index URL {url}")
        if url in ("https://refeds.org/", "https://github.com/keycloak/keycloak/discussions"):
            errors.append(f"{nid}: directory/homepage URL {url}")

    if live != 35 or ac != 30:
        errors.append(f"counts live={live} ac={ac} (expected 35/30)")
    ob = data.get("overlap_block", {})
    if ob.get("n") != 13:
        errors.append("overlap_block.n != 13")
    if errors:
        print("FAIL", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print("OK: corpus provenance v2 valid (35 live + 30 author-constructed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
