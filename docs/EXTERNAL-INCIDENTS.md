# External incidents against Table I

## Purpose

This is an **ongoing falsifiability check**, not part of the manuscript’s N=11 catalog.

Operators of constrained multi-site open-source IAM / federated SSO deployments may submit fingerprint-safe incident summaries and ask whether they fit the published ten-category scheme (`codebook/taxonomy.json` / manuscript Table I) without inventing a new label.

## How to submit

Open a GitHub issue with the **External incident (Table I)** template, or file a plain issue with the fields below.

Required fields:

1. **Symptom** — what users or operators saw (no hostnames, ticket IDs, geography, or org-identifying product names).
2. **Mechanism** — what failed on the path (identity vs edge vs directory vs cluster vs gateway vs MFA vs dual-IdP meaning).
3. **Resolution** — what closed or mitigated it (or “unknown”).
4. **Proposed Table I category** — one of the ten ids, or `none` if you believe no cell fits.
5. **Negative evidence** — why neighboring labels do not apply (one sentence each for the closest excludes).
6. **Severity (optional)** — Sev-1 / Sev-2 / Sev-3 using `codebook/taxonomy.json` / Table II meanings.

## Scoring (maintainer)

Each accepted submission is labeled one of:

| Outcome | Meaning |
| --- | --- |
| `fits` | Places in exactly one Table I cell under the published tie-breakers |
| `fits_with_clarification` | Fits after a wording clarification that does not add a category |
| `forces_new_label` | Cannot be placed without a new category or a layer merge that changes boundaries |

Outcomes and anonymized summaries may be recorded under `docs/external-submissions/` in a later tag. **None of those rows are claimed as evidence in the current manuscript corpus.**

## Fingerprint test

Same rule as the paper: procurement notices plus about ten minutes of search must not narrow the text to one organization.
