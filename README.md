# SSO Failure Taxonomy

Companion codebook and callback-consume harness for the manuscript *An Artifact-Supported Instrument for Classifying Federated SSO Failure Mechanisms*.

It is **not** a production identity provider.

License: MIT · [`LICENSE`](LICENSE) · [`CITATION.cff`](CITATION.cff)

https://github.com/kazuru-chidumbwe/sso-failure-taxonomy — cite tag **`v1.0.26`** (or its Zenodo version DOI), not floating `main`.

**Quick start:** [`docs/QUICK-START.md`](docs/QUICK-START.md) · **Manuscript cite map:** [`docs/MANUSCRIPT-CITE.md`](docs/MANUSCRIPT-CITE.md)

## What is in the archive

| Path | Role |
| --- | --- |
| [`docs/CASE-SELECTION.md`](docs/CASE-SELECTION.md) | N=11 selection criteria |
| [`docs/OBSERVABILITY-MAP.md`](docs/OBSERVABILITY-MAP.md) | Category → signal map |
| [`codebook/corpus.json`](codebook/corpus.json) | Two-layer evaluation corpus manifest |
| [`codebook/`](codebook/) | Ten-category taxonomy, N=11 publishable summaries, checklist |
| [`codebook/stress-cases.json`](codebook/stress-cases.json) | S1–S8 decision tests + D1–D4 negative decoys (§IV-E) |
| [`codebook/validate_catalog_assignments.py`](codebook/validate_catalog_assignments.py) | Catalog + decision-test + corpus manifest oracle (`make smoke`) |
| [`harness/`](harness/) | Stdlib demo of Fig. 3: naive check-then-delete vs atomic consume |
| [`figures/`](figures/) | Fig. 1–3 (captions in the manuscript). Fig. 2 is the tie-breaker walk, not a count chart |
| [`docs/EXTERNAL-INCIDENTS.md`](docs/EXTERNAL-INCIDENTS.md) | Open community falsifiability template |

## Reproducibility notes

- **CI:** GitHub Actions runs `make smoke` on `ubuntu-latest` with Python **3.10** and **3.12** (`.github/workflows/ci.yml`).
- **Release integrity:** publish SHA256 of the source archive in each GitHub Release notes.
- **Non-determinism:** harness concurrency outcomes can vary with scheduler timing; see `harness/SCHEDULES.md`.

No hostnames, secrets, ticket IDs, or geography.

## External incidents (falsifiability)

Operators of similar constrained multi-site open-source IAM deployments may submit fingerprint-safe incident summaries against the published Table IV. Use the **External incident (Table IV)** GitHub issue template or follow [`docs/EXTERNAL-INCIDENTS.md`](docs/EXTERNAL-INCIDENTS.md). Submissions are scored `fits` / `fits_with_clarification` / `forces_new_label`. They are **not** part of the manuscript's N=11 catalog.

## Evidence index

Per-case map of what is released (honest when "architect note only"): [`docs/EVIDENCE-INDEX.md`](docs/EVIDENCE-INDEX.md).

## How to run

Python 3.10+. Standard library only.

```bash
git clone https://github.com/kazuru-chidumbwe/sso-failure-taxonomy.git
cd sso-failure-taxonomy
make smoke
```

`make smoke` runs unittests, the I4 fixture size check, and `validate_catalog_assignments.py`. Atomic consume: one concurrent winner, replay rejected. Naive check-then-delete: false-reject window. Presence-only (`presence_only`): second presentation accepted.

```bash
python3 harness/callback_consume.py both --mode both --workers 8
```
