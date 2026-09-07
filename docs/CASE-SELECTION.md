# Case selection (N=11 estate catalog)

**Manuscript table:** Table IX · **Corpus layer:** `estate_catalog_n11` in [`codebook/corpus.json`](../codebook/corpus.json)

This document records how the eleven Layer-1 cases were chosen. It is **not** an incident census and does not support prevalence claims.

## Selection goal

Illustrate each primary Table IV surface represented in the studied deployment model with at least one author-selected case that:

1. States symptom, attributed mechanism, and response under a disclosed evidence form (E0–E3).
2. Can receive a **single primary label** under the published ordered walk and tie-breakers.
3. Can be released as a fingerprint-safe publishable summary without unacceptable re-identification risk.
4. Where possible, pairs with runnable mechanism material (F3/F5 harness; I4 synthetic fixtures).

## What was excluded (not in N=11)

| Exclusion | Reason |
| --- | --- |
| Laboratory dual-IdP matrices | Out of corpus per Appendix A.6 — synthetic lab grids, not operational illustrations |
| Non-IAM outages | Unit of analysis is authentication-path mechanisms |
| Cases requiring ticket/log/config release | Re-identification or confidentiality risk |
| Cases with no stateable mechanism or response | Cannot support instrument illustration |
| Ambiguous or *outside taxonomy* estate rows | Layer 1 was limited to assignable illustrations; outside routing is tested in Layer 2 (S1–S4) |

## Outside taxonomy in Layer 1

**None** of the eleven estate rows are coded `outside_taxonomy`. That is a deliberate illustration choice for Table IX, not evidence that production estates rarely produce ambiguous cases. Outside-taxonomy routing on estate-adjacent material is illustrated in **Layer 1.5** (R1 in `codebook/rejected-estate-vignettes.json`) and in Layer 2 (S1–S4 specification vignettes).

## Coverage map (not prevalence)

| Category | Case(s) | Form | Notes |
| --- | --- | --- | --- |
| edge_side_effect | F1 | DESIGN (E0) | |
| edge_identifier | F2 | DESIGN (E0) | |
| edge_callback_consume | F3, F5 | DESIGN (E0+E3) | Two rows: availability vs security-boundary priority on same surface |
| session_plane | F4 | DESIGN (E0) | |
| directory_federation | I1 | RETRO (E1) | |
| multi_site_affinity | I2 | RETRO (E1) | |
| cluster_state | I3 | RETRO (E1) | |
| protocol_gateway | I4 | RETRO (E2) | Ticket-reviewed; synthetic fixtures only in public artifact |
| mfa_delivery | I5 | RETRO (E2) | Ticket-reviewed; summary only in public artifact |
| dual_idp_boundary | I6 | RETRO (E1) | |

Nine categories have one case; only `edge_callback_consume` has two (F3/F5).

## Byte freeze

Category, `sev`, `summary`, `form`, and `evidence_class` fields are byte-frozen at git tag **`v1.0.12`**. Selection prose and corpus metadata may evolve in later tags without changing frozen fields.
