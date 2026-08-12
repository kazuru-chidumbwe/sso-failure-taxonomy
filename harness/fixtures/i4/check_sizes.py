#!/usr/bin/env python3
"""Size-class checker for synthetic I4 fixtures (not estate evidence)."""

from __future__ import annotations

import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = [
    "saml_post_body_8kib.txt",
    "saml_post_body_16kib.txt",
    "saml_post_body_32kib.txt",
    "saml_post_body_64kib.txt",
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--limit",
        type=int,
        default=16384,
        help="Synthetic request-body limit in bytes (default: 16384)",
    )
    args = ap.parse_args()
    print(f"limit_bytes={args.limit}")
    print(f"{'file':28} {'bytes':>8}  vs_limit")
    for name in FIXTURES:
        path = HERE / name
        n = path.stat().st_size
        status = "within" if n <= args.limit else "exceeds"
        print(f"{name:28} {n:8d}  {status}")
    print("note: synthetic fixtures only; not a claim about any production gateway")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
