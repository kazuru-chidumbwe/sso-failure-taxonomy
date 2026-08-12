# Evidence index (case → released material)

Honest map for the manuscript Table III. **No estate tickets, live logs, hostnames, or configuration fragments are released.**

| Case | Category | Form | Released technical material | Notes |
| --- | --- | --- | --- | --- |
| F1 | edge_side_effect | DESIGN | Architect note / Table III summary only | No state-machine fixture released |
| F2 | edge_identifier | DESIGN | Architect note / Table III summary only | Mechanism literature is cited in the paper, not as proof of the local event |
| F3 | edge_nonce | DESIGN | Architect note + [`harness/`](../harness/) nonce-consume demo | Harness models the race class; not original estate logs |
| F4 | session_plane | DESIGN | Architect note / Table III summary only | |
| F5 | edge_nonce | DESIGN | Architect note + [`harness/`](../harness/) nonce-consume demo | Same harness as F3 |
| I1 | directory_federation | RETRO | Architect note / Table III summary only | |
| I2 | multi_site_affinity | RETRO | Architect note / Table III summary only | |
| I3 | cluster_state | RETRO | Architect note / Table III summary only | |
| I4 | protocol_gateway | RETRO | Architect note / Table III summary only | No proxy config or SAML fixture released |
| I5 | mfa_delivery | RETRO | Architect note / Table III summary only | |
| I6 | dual_idp_boundary | RETRO | Architect note / Table III summary only | No claim matrix released |

## How to run the only executable evidence object

```bash
make smoke
python3 harness/nonce_consume.py both --mode both --workers 8
```

Expected class of result: atomic consume admits one concurrent winner and rejects replay; naive check-then-delete admits a false-reject window. See harness README / unittest output.
