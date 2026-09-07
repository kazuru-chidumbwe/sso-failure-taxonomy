# Evidence index (case → released material)

Honest map for the manuscript **Table IX** case catalog. **No estate tickets, live logs, hostnames, product names, topology descriptors, or configuration fragments are released.**

## Evidence classes

| Class | Meaning |
| --- | --- |
| **E0** | Design-derived scenario. Author-constructed from estate architecture; no retained production record. |
| **E1** | Retrospective architect note. Post hoc operational recollection; no ticket, log, or configuration retained for review. |
| **E2** | Privately ticket-reviewed reconstruction. Reviewed by the author; public release limited to an anonymized paraphrase. |
| **E3** | Artifact-reproduced mechanism. A synthetic runnable artifact reproduces the stated mechanism under explicitly bounded assumptions. E3 attaches to the **mechanism**, never to the original operational event. |

`form` (DESIGN / RETRO) remains the primary key used by `codebook/incidents.json`.
Evidence class is an additional, finer-grained label; it does not renumber or recode any row.

## Per-case map

| Case | Category | Form | Class | Released technical material | Notes |
| --- | --- | --- | --- | --- | --- |
| F1 | edge_side_effect | DESIGN | E0 | Architect note / Table IX summary only | No state-machine fixture released |
| F2 | edge_identifier | DESIGN | E0 | Architect note / Table IX summary only | Mechanism literature is cited in the paper, not as proof of a local event |
| F3 | edge_callback_consume | DESIGN | E0 + E3 | Architect note + [`harness/`](../harness/) callback-consume demo | Harness models the race class under single-store assumptions; not estate logs |
| F4 | session_plane | DESIGN | E0 | Architect note / Table IX summary only | |
| F5 | edge_callback_consume | DESIGN | E0 + E3 | Architect note + [`harness/`](../harness/) callback-consume demo | Same harness as F3; see [`harness/SCHEDULES.md`](../harness/SCHEDULES.md) for the threat model |
| I1 | directory_federation | RETRO | E1 | Architect note / Table IX summary only | No corroborating ticket, log, or configuration retained |
| I2 | multi_site_affinity | RETRO | E1 | Architect note / Table IX summary only | |
| I3 | cluster_state | RETRO | E1 | Architect note / Table IX summary only | |
| I4 | protocol_gateway | RETRO | E2 | Publishable summary + [`harness/fixtures/i4/`](../harness/fixtures/i4/) synthetic size-class fixtures | **Ticket-reviewed privately; publishable summary + synthetic fixtures** (not released). Fixtures are **not** estate SAML captures |
| I5 | mfa_delivery | RETRO | E2 | Publishable summary only | **Ticket-reviewed privately** (not released) |
| I6 | dual_idp_boundary | RETRO | E1 | Architect note / Table IX summary only | No claim matrix released |

## How to run the executable evidence objects

```bash
make smoke
python3 harness/callback_consume.py both --mode both --workers 8
```

Expected class of result: atomic consume admits one concurrent winner and rejects a second
presentation; naive check-then-delete admits a false-reject window; presence-only (`presence_only`)
admits a second presentation. Exact modeled schedules: [`harness/SCHEDULES.md`](../harness/SCHEDULES.md).

## I4 synthetic size-class fixtures

```bash
python3 harness/fixtures/i4/check_sizes.py --limit 16384
python3 -m unittest harness.fixtures.i4.test_i4_fixtures -v
```

See [`harness/fixtures/i4/README.md`](../harness/fixtures/i4/README.md).
Illustrative decision-test vignettes (not N=11; not validation evidence):
[`codebook/stress-cases.json`](../codebook/stress-cases.json).
