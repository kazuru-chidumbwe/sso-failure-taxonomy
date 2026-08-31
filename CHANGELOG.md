# Changelog

## 1.0.9 — 2026-08-31

Manuscript title alignment and release-metadata hygiene. No taxonomy, category, severity, reliability, or case-catalog changes.

- **Title.** `codebook/taxonomy.json` and README aligned to current IEEE Access manuscript title.
- **Scope.** `docs/SCOPE.md`: "classification instrument" wording (not "failure taxonomy").
- **Release procedure.** `docs/TAGS.md`: DOI wiring checklist after Zenodo mint.

## 1.0.8 — 2026-08-31

Fig. 3 filename alignment only. No taxonomy, category, severity, reliability, or case-catalog changes.

- **Naming.** `figures/fig3-nonce-consume.png` → `figures/fig3-callback-consume.png` (companion copy; captions remain in manuscript).
- **Metadata.** README cite pin updated to v1.0.8. Version DOI wired on `main` after tag (see v1.0.9 release procedure).

## 1.0.7 — 2026-08-31

Pre-submission consistency and anonymization pass. No taxonomy, category, severity, or reliability values changed; the N=11 catalog and all coding are unchanged.

- **Anonymization.** Removed product, directory-topology, and monitoring-tool names from `docs/EVIDENCE-INDEX.md` I1; no bogus §VI-E cross-reference.
- **Table III parity.** `codebook/incidents.json` summaries byte-identical to manuscript Table III publishable-summary column; I3 mechanism corrected.
- **Evidence classes.** Added E0–E3 alongside DESIGN/RETRO `form` key (primary key unchanged for reliability packet).
- **Checklist parity.** Items 3 and 8 aligned with manuscript Table IV (no buffer default; linearizable single-winner consume wording).
- **Naming.** `harness/nonce_consume.py` → `callback_consume.py`; `test_nonce_consume.py` → `test_callback_consume.py`.
- **Metadata.** `CITATION.cff` and `docs/TAGS.md` prepared for v1.0.7; README cite pin updated.

## 1.0.1 – 1.0.6 — 2026-08-13 to 2026-08-15

Packaging and manuscript-alignment iterations between the first Access freeze (`v1.0.0`) and the `v1.0.6` Zenodo pin (`10.5281/zenodo.21950902`). No taxonomy relabels after `v1.0.0`.

## 1.0.0 — 2026-08-13

- Manuscript-aligned freeze for IEEE Access companion artifact.
- Broaden `mfa_delivery` inclusion to MFA completion on an out-of-band path (SMS unreliability or OTP verification/lifecycle), keeping the ten-category id set.
- Clarify `codebook/stress-cases.json` as illustrative decision-test vignettes only (not empirical validation).
- Sync checklist item 9, packet Table I row, I5 publishable summary, and `docs/EVIDENCE-INDEX.md`.

## 0.1.7 — 2026-08-13

- Add `codebook/stress-cases.json` (five outside-taxonomy / multi-causal instrument stress vignettes; not N=11).
- Add synthetic I4 request-size fixtures and checker under `harness/fixtures/i4/`; extend `make smoke`.
- Update I4/I5 publishable summaries and `docs/EVIDENCE-INDEX.md` provenance (ticket-reviewed privately; artifacts not released).

## 0.1.6 — 2026-08-12

Document explicit F3/F5 harness schedules (`harness/SCHEDULES.md`): Schedule A `jwt_only` (second acceptance), Schedule B `naive` (false reject), Schedule C `atomic`. Narrow threat model and atomic single-winner wording for manuscript IV lock.

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
