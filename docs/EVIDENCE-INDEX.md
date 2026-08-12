# Evidence index (case → released material)

Honest map for the manuscript Table III. **No estate tickets, live logs, hostnames, or configuration fragments are released.**

| Case | Category | Form | Released technical material | Notes |
| --- | --- | --- | --- | --- |
| F1 | edge_side_effect | DESIGN | Architect note / Table III summary only | No state-machine fixture released |
| F2 | edge_identifier | DESIGN | Architect note / Table III summary only | Mechanism literature is cited in the paper, not as proof of the local event |
| F3 | edge_callback_consume | DESIGN | Architect note + [`harness/`](../harness/) callback-consume demo | Harness models the race class; not original estate logs |
| F4 | session_plane | DESIGN | Architect note / Table III summary only | |
| F5 | edge_callback_consume | DESIGN | Architect note + [`harness/`](../harness/) callback-consume demo | Same harness as F3 |
| I1 | directory_federation | RETRO | Architect note / Table III summary only | |
| I2 | multi_site_affinity | RETRO | Architect note / Table III summary only | |
| I3 | cluster_state | RETRO | Architect note / Table III summary only | |
| I4 | protocol_gateway | RETRO | Architect note + [`harness/fixtures/i4/`](../harness/fixtures/i4/) synthetic size-class fixtures | Fixtures are **not** estate SAML captures; size-class helper only |

| I5 | mfa_delivery | RETRO | Architect note / Table III summary only | |
| I6 | dual_idp_boundary | RETRO | Architect note / Table III summary only | No claim matrix released |

## How to run the only executable evidence object

```bash
make smoke
python3 harness/nonce_consume.py both --mode both --workers 8
```

Expected class of result: atomic consume admits one concurrent winner and rejects replay; naive check-then-delete admits a false-reject window. See harness README / unittest output.

## I4 synthetic size-class fixtures

```bash
python3 harness/fixtures/i4/check_sizes.py --limit 16384
python3 -m unittest harness.fixtures.i4.test_i4_fixtures -v
```

See [`harness/fixtures/i4/README.md`](../harness/fixtures/i4/README.md). Instrument stress vignettes (outside taxonomy exercise; not N=11): [`codebook/stress-cases.json`](../codebook/stress-cases.json).
