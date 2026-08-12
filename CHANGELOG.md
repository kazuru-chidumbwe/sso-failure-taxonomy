# Changelog

## 0.1.5 — 2026-08-12

Rename category `edge_nonce` → `edge_callback_consume` for protocol precision (callback-correlation consume ≠ OIDC ID-Token nonce / AS–RS token replay). Sync Table I, incidents, checklist, packet, evidence index, and harness docs. Second-coder agreement remains on the same mechanism cell; earlier tags used the prior label name.

## 0.1.4 — 2026-08-12

Add `docs/EVIDENCE-INDEX.md` and `docs/EXTERNAL-INCIDENTS.md` (plus GitHub issue template) so manuscript Availability references resolve. Align README / `taxonomy.json` title with the current manuscript. Retire checklist “citation-removal” label in favor of bidirectional case traceability; sync Table IV item wording (incl. item 8 buffer/fixture language).

## 0.1.3 — 2026-08-12

Reliability computation: add Gwet’s AC1 (primary under severity skew) alongside Cohen’s κ, same bootstrap treatment. Document the `cluster_state` Sev-2/Sev-3 split as severity-boundary judgment.

## 0.1.2 — 2026-08-12

Data release for Access Availability: `codebook/reliability.json` (+ `reliability.md`) with second-coder raw agreement, Cohen’s κ, and bootstrap CIs. Scrub programme placeholder from `CITATION.cff` DOI comment. README authorship left to `CITATION.cff` only (plain harness style).

## 0.1.1 — 2026-08-12

Packet and docs state the second-coder round as **unblinded** relative to the published catalog (`incidents.json` / Table III). “Packet only until submit” remains the working protocol (not a blinding claim).

## 0.1.0 — 2026-08-12

Independent-coding packet: paraphrased cases (no Table I inclusion vocabulary), additional-observations fields for excludes, Sev-1/2/3 on the response sheet. Gold labels are disclosed as `codebook/incidents.json` (published catalog); working protocol is “do not browse the repo until submit.” Dropped empty `patterns/` placeholder. CI actions SHA-pinned.

## 0.0.0 — 2026-08-11

Initial public scaffold. Hartl-shaped README. License MIT. Public name `sso-failure-taxonomy`.
