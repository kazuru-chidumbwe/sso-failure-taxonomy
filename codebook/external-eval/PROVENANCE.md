# External-eval coder provenance

## Independent coders (authoritative)

Both external-narrative coders are **independent IAM/SSO practitioners**, not the manuscript author.

| Slot | File | `author_coded` | Completed |
| --- | --- | ---: | --- |
| Coder A | `coder-a.json` | `false` | 2026-09-06 (95 min) |
| Coder B | `coder-b.json` | `false` | 2026-09-06 (120 min) |

Machine-readable independence is recorded in each `coder-*.json` and mirrored under `reliability-external-v1.json` → `coders.*.author_coded`.

The N=11 structured-packet pilot (Section IV-E) used a **different** single practitioner; see `codebook/reliability.json` and `codebook/second-coder/README.md`.

## Erroneous commit message (e34f848)

Git commit `e34f848` (6 Sep 2026) carries the message **"external-eval: complete Coder B (author)"**. That label is **wrong**. Coder B is an independent practitioner.

Corrective commits:

- `9fd27f1` — `fix: Coder B is independent practitioner, not author.`
- `v1.0.17` — adds `author_coded: false` to coder JSON and this note.

**Do not cite `e34f848`'s subject line as provenance.** Use this file, `coder-b.json`, and `reliability-external-v1.json`.
