# Second-coder reliability (summary)

Machine-readable: [`reliability.json`](reliability.json).

**Primary chance-corrected metric:** Gwet’s AC1 (severity is skewed; kappa paradox). Cohen’s κ reported alongside.

| Axis | Raw | Gwet AC1 (95% CI) | Cohen’s κ (95% CI) |
| --- | ---: | --- | --- |
| Category | 11/11 | **1.00** [1.00, 1.00] | 1.00 [1.00, 1.00] |
| Severity | 10/11 | **0.89** [0.64, 1.00] | 0.76 [0.00, 1.00] |

Protocol: **unblinded** independent coding (packet-only; public gold in `incidents.json`).

**Sole disagreement (severity only):** `cluster_state` — author Sev-2 (cohort/site ops intervention), coder Sev-3 (conflicting replica state as trust/security-boundary risk). Category agreed. That split is where the Sev-2/Sev-3 boundary does real judgment work (stale state → wrong trust), not noise in the mechanism label.

Frame: agreement given Table I; n=11 → wide CIs; not multi-estate reliability. The Case→incident shuffle map stays out of this tree (author-only).
