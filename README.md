# SSO Failure Taxonomy

Companion codebook and callback-consume harness for the manuscript *Federated SSO Failure Modes: A Rule-Bounded Classification Instrument for Constrained Multi-Site Open-Source IAM*.

It is **not** a production identity provider.

License: MIT · [`LICENSE`](LICENSE) · [`CITATION.cff`](CITATION.cff)

https://github.com/kazuru-chidumbwe/sso-failure-taxonomy — cite tag `v1.0.8` (or its Zenodo version DOI), not floating `main`.

## What is in the archive

| Path | Role |
| --- | --- |
| [`codebook/`](codebook/) | Ten-category taxonomy, N=11 publishable summaries, checklist |
| [`codebook/second-coder/`](codebook/second-coder/) | Unblinded independent-coding packet (send standalone; public catalog is not hidden) |
| [`codebook/reliability.json`](codebook/reliability.json) | Second-coder agreement (AC1 primary + κ + bootstrap CI) |
| [`harness/`](harness/) | Stdlib demo of Fig. 3: naive check-then-delete vs atomic consume |
| [`figures/`](figures/) | Fig. 1–3 (captions in the manuscript). Fig. 2 is the tie-breaker walk, not a count chart |
| [`docs/`](docs/) | Scope, tag policy, external-incident call, evidence index |

No hostnames, secrets, ticket IDs, or geography.

## External incidents (falsifiability)

Operators of similar constrained multi-site open-source IAM deployments may submit fingerprint-safe incident summaries against the published Table I. Use the **External incident (Table I)** GitHub issue template or follow [`docs/EXTERNAL-INCIDENTS.md`](docs/EXTERNAL-INCIDENTS.md). Submissions are scored `fits` / `fits_with_clarification` / `forces_new_label`. They are **not** part of the manuscript’s N=11 catalog.

## Evidence index

Per-case map of what is released (honest when “architect note only”): [`docs/EVIDENCE-INDEX.md`](docs/EVIDENCE-INDEX.md).

## How to run

Python 3.10+. Standard library only.

```bash
git clone https://github.com/kazuru-chidumbwe/sso-failure-taxonomy.git
cd sso-failure-taxonomy
make smoke
```

`make smoke` runs eight unittests plus the I4 fixture size check. Atomic consume: one concurrent winner, replay rejected. Naive check-then-delete: false-reject window. Presence-only (`jwt_only`): second presentation accepted.

```bash
python3 harness/callback_consume.py both --mode both --workers 8
```
