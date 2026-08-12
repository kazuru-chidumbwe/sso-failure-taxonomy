# SSO Failure Taxonomy

Codebook and nonce-consume demonstration for the manuscript *Production Failure Modes in Federated SSO: Lessons from Operating OSS IAM in a Low-Bandwidth, Multi-Site Environment*.

It is **not** a production identity provider.

License: MIT · [`LICENSE`](LICENSE) · [`CITATION.cff`](CITATION.cff)

https://github.com/kazuru-chidumbwe/sso-failure-taxonomy — cite tag `v0.1.3` (or its Zenodo DOI), not floating `main`.

## What is in the archive

| Path | Role |
| --- | --- |
| [`codebook/`](codebook/) | Ten-category taxonomy, N=11 publishable summaries, checklist |
| [`codebook/second-coder/`](codebook/second-coder/) | Unblinded independent-coding packet (send standalone; public catalog is not hidden) |
| [`codebook/reliability.json`](codebook/reliability.json) | Second-coder agreement (AC1 primary + κ + bootstrap CI) |
| [`harness/`](harness/) | Stdlib demo of Fig. 3: naive check-then-delete vs atomic consume |
| [`figures/`](figures/) | Fig. 1–3 (captions in the manuscript). Fig. 2 is the tie-breaker walk, not a count chart |
| [`docs/`](docs/) | Scope, tag policy |

No hostnames, secrets, ticket IDs, or geography.

## How to run

Python 3.10+. Standard library only.

```bash
git clone https://github.com/kazuru-chidumbwe/sso-failure-taxonomy.git
cd sso-failure-taxonomy
make smoke
```

`make smoke` runs six unittests. Atomic consume: one concurrent winner, replay rejected. Naive check-then-delete: false-reject window. JWT-expiry-only: replay accepted.

```bash
python3 harness/nonce_consume.py both --mode both --workers 8
```
