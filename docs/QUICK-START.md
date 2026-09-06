# Quick start — SSO failure taxonomy artifact

**Audience:** IAM/SSO operators classifying authentication failures in constrained multi-site federated deployments.

## 1. Read the instrument

1. Open `codebook/taxonomy.json` — ten mechanism categories + tie-breakers (manuscript **Table IV**).
2. Skim `docs/MANUSCRIPT-TABLES.md` — maps manuscript tables I–X to artifact files.
3. Optional: `figures/fig2-tie-breaker.png` — decision walk (not a prevalence chart).

## 2. Classify a case

1. Gather symptom, mechanism, and negative evidence (why neighboring labels do not apply).
2. Walk Table IV inclusion rules in order; apply tie-breakers.
3. If no cell fits or two remain equally plausible → `outside_taxonomy / candidate new label`.
4. Assign operational priority class separately (Table V / `incidents.json` mapping).

## 3. Reproduce harness demos (F3/F5)

```bash
cd harness
python3 callback_consume.py both --mode both --workers 8 --json
make smoke   # from repo root
```

Modes: `presence_only` (F5 second acceptance), `naive` (F3 false reject), `atomic` (single winner).

## 4. Submit an external incident (falsifiability)

Use GitHub issue template **External incident (Table IV)** or `docs/EXTERNAL-INCIDENTS.md`. Submissions are scored `fits` / `fits_with_clarification` / `forces_new_label` — **not** added to N=11.

## 5. Public-narrative pilot

See `codebook/external-eval/` for the §IV-K feasibility corpus (65 narratives, multi-coder sheets).

## Cite

Tag `v1.0.13` · wire Zenodo version DOI in manuscript ref [38]. N=11 catalog byte-frozen at `v1.0.12`.
