# Callback-consume harness (F3 / F5)

Manuscript `edge_callback_consume`: F3 (Severity-2 false reject) and F5 (Severity-3 second acceptance / replay of the **same edge callback capability**).  
Not a Keycloak or WSO2 deployment. Not a production config. Synthetic callback values only.

**Modeled schedules (required reading):** [`SCHEDULES.md`](SCHEDULES.md) — Schedule A (`jwt_only` / F5), Schedule B (`naive` / F3), Schedule C (`atomic`).

```text
python3 callback_consume.py both --mode both --workers 8
python3 callback_consume.py both --json
python3 -m unittest discover -s . -v
```

From the repository root: `make smoke`.

| Mode | Schedule | Expected |
| --- | --- | --- |
| `jwt_only` | A | second presentation accepted (F5) |
| `naive` | B | TOCTOU → F3 false-reject risk under concurrency |
| `atomic` | C | one concurrent winner; replay rejected |

Resolution class: checklist item 3 — atomic single-winner get-and-delete at the callback-consistency scope (GETDEL / one lock), TTL ≥ round-trip, do not trust JWT `exp` alone.
