# Nonce consume harness (F3 / F5)

Manuscript `edge_nonce`: F3 (Severity-2 false reject) and F5 (Severity-3 replay).  
Not a Keycloak or WSO2 deployment. Not a production config. Synthetic nonces only.

```text
python3 nonce_consume.py both --mode both --workers 8
python3 nonce_consume.py both --json
python3 -m unittest discover -s . -v
```

From the repository root: `make smoke`.

| Mode | Expected |
| --- | --- |
| `atomic` | one concurrent winner; replay rejected |
| `naive` | TOCTOU window → F3 false-reject risk |
| `jwt_only` | presence/expiry without consume → F5 replay |

Resolution class: checklist item 3 — atomic single-use consume (GETDEL / one lock), TTL ≥ round-trip, do not trust JWT `exp` alone.
