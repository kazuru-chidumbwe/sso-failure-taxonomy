# External-eval coder provenance

## Independent coders (authoritative)

Both external-narrative coders are **independent IAM/SSO practitioners**, not the manuscript author.

| Slot | File | `author_coded` | Completed |
| --- | --- | ---: | --- |
| Coder A | `coder-a.json` | `false` | 2026-09-06 (95 min) |
| Coder B | `coder-b.json` | `false` | 2026-09-06 (120 min) |

Machine-readable independence is recorded in each `coder-*.json` and mirrored under `reliability-external-v1.json` → `coders.*.author_coded`.

The N=11 structured-packet pilot (Section IV-E) used a **different** single practitioner; see `codebook/reliability.json` and `codebook/second-coder/README.md`.

## Coder B file history (e34f848 → 7df5a19)

`coder-b.json` was first committed (`e34f848`, 17:38 on 6 Sep 2026) carrying a
placeholder descriptor — "author (Coder B slot; disjoint block self-coded per
submitter)" — and a matching commit-message subject. That placeholder was a
fallback prepared during cold-outreach recruitment (five practitioners
contacted; one had already replied and become Coder A) in case a second reply
did not arrive before the recruitment deadline; it was never used as
published data. Coder B, an independent IAM/SSO practitioner reached through
that same cold-outreach round, replied shortly after with a completed
response sheet, and that content was transcribed into the same file — but the
placeholder descriptor and commit message were not updated at the time,
producing a misleading record even though the underlying 39 assignments were
always Coder B's own.

Corrective commits:

- `9fd27f1` — `fix: Coder B is independent practitioner, not author.` (descriptor)
- `b22ca48` — adds Coder B's self-reported `minutes_spent: 120`.
- `v1.0.17` (`7df5a19`) — adds `author_coded: false` to coder JSON.

This entry replaces an earlier, less specific note that called `e34f848`'s
subject line simply "erroneous" without explaining the underlying sequence.

Coder B's completed response sheet (~120 minutes reported; explicit
confirmation of no repository browse before submission) is retained privately
by the author, consistent with how ticket-reviewed evidence (E2) is handled
elsewhere in this study. Independently checkable against the public record:
EN027 was coded `edge_callback_consume` on callback-correlation-lifecycle
reasoning, and GH004 was coded `outside_taxonomy` on insufficient-stated-
mechanism reasoning — both match `codebook/external-eval/coder-b.json` and
`reliability-external-v1.json` byte-for-byte.

**Do not cite `e34f848`'s subject line alone as provenance.** Use this file,
`coder-b.json`, and `reliability-external-v1.json`.
