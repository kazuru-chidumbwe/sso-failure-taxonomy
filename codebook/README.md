# Codebook (fingerprint-safe)

Machine-readable copy of the frozen coding scheme. No hostnames, geography, tickets, or mail-stack names.

| File | Contents |
| --- | --- |
| [`taxonomy.json`](taxonomy.json) | Ten a priori labels + inclusion/exclusion |
| [`incidents.json`](incidents.json) | N=11 publishable catalog (category, severity, form, summary) |
| [`checklist.json`](checklist.json) | Table XI items with bidirectional case traceability |
| [`compute_reliability.py`](compute_reliability.py) | Regenerate / verify agreement statistics |
| [`reliability.json`](reliability.json) | Second-coder raw agreement + Gwet AC1 (primary) + Cohen's κ + bootstrap CI |
| [`reliability.md`](reliability.md) | Human-readable reliability summary |
| [`second-coder/PACKET.md`](second-coder/PACKET.md) | Unblinded independent-coding packet. Send standalone. `incidents.json` is the published catalog, not a hidden key. |
| [`second-coder/responses.json`](second-coder/responses.json) | Independent coder responses for the N=11 structured-packet pilot |

Canonical definitions are Tables I–XII in the manuscript. This directory is the machine-readable copy.
