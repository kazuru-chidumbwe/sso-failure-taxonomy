# What the IEEE Access manuscript cites (Path D)

**Manuscript cite pin:** tag **`v1.0.22`** (or latest Path D tag) · Zenodo version DOI in manuscript [38]  
**N=11 catalog freeze:** tag **`v1.0.12`** (category / priority / summary fields)

## Study evidence (cited in the paper)

| Path | Role |
| --- | --- |
| `codebook/taxonomy.json` | Table IV instrument |
| `codebook/incidents.json` | N=11 catalog (author-coded) |
| `codebook/stress-cases.json` | S1–S8 decision-test battery |
| `codebook/validate_catalog_assignments.py` | Catalog + decision-test oracle (`make smoke`) |
| `harness/` | F3/F5 mechanism demonstrations |
| `harness/fixtures/i4/` | Synthetic gateway size-class fixtures |
| `docs/EXTERNAL-INCIDENTS.md` | Open community falsifiability (ongoing; not N=11) |

## Exploratory archive (in repo; **not** manuscript study evidence)

Collected during earlier sponsor rounds. Retained for audit transparency only.

| Path | Note |
| --- | --- |
| `codebook/second-coder/` | Structured-packet pilot; not cited after Path D (Sep 2026) |
| `codebook/reliability.json`, `codebook/compute_reliability.py` | N=11 agreement stats for archival pilot |
| `codebook/external-eval/` | Public-narrative pilot (Coders A & B); banner in README |

Path D reframed evaluation as **executable specification tests** (S1–S8 + catalog oracle + harness), not inter-rater agreement on narratives. See `CHANGELOG.md` v1.0.21.

## Version history

Older tags (`v1.0.19`–`v1.0.21`) document sponsor alignment and reliability-script fixes on the **superseded** inter-rater claim path. They remain on Zenodo for reproducibility of prior drafts; the submitted manuscript cites the latest Path D tag (currently **`v1.0.22`**).
