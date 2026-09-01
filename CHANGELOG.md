# Changelog

## 1.0.12 — 2026-09-01

Submit-pass: figure render fix, Table VIII tracking, replicated-store production extension.

- **Figures.** Fix `build_figures.py` label spacing, callout badge placement, Fig. 3 three-panel single-row layout; regenerate PNGs.
- **Manuscript alignment.** Table VIII (protocol artifact contrast) tracked in `docs/MANUSCRIPT-TABLES.md` and `incidents.json` → `manuscript_tables`.
- **Harness.** `harness/SCHEDULES.md` adds "Production extension (not modelled)" for replicated-store consume primitives.
- **README** cite pin → `v1.0.12`.

## 1.0.11 — 2026-08-31

Manuscript Gates pass: sequential IEEE table numbering and operational-priority mapping. No taxonomy, category assignments, or reliability values changed.

- **Table numbering.** Manuscript tables renumbered I–VII sequentially; artifact docs and JSON updated (`docs/MANUSCRIPT-TABLES.md`).
- **Operational priority.** `codebook/incidents.json` adds `operational_priority_class` mapping (legacy `severity` / Sev-1/2/3 → Pri-1/2/3).
- **Checklist.** Items 3 and 5 synced with manuscript Table V (TTL and directory-federation timeout wording).
- **Figures.** Ideal-pass PNGs (swimlanes, diamond flowchart, three-panel Fig. 3).

## 1.0.10 — 2026-08-31

Stop version-DOI lag in `CITATION.cff`. No code or case-data changes.

- **CITATION.cff.** `url:` and `identifiers` now use concept DOI only (`10.5281/zenodo.21950901`). Version DOI for a release belongs in the manuscript Availability / ref [28], not inside the archived artifact metadata.
- **Release procedure.** `docs/TAGS.md` rewritten to match (no post-tag DOI commit into `CITATION.cff`).

## 1.0.9.1 — 2026-08-31

Wire Zenodo v1.0.9 version DOI into `CITATION.cff` (`10.5281/zenodo.22214839`). No code or case-data changes.

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
- **Table IV parity.** `codebook/incidents.json` summaries byte-identical to manuscript Table IV publishable-summary column; I3 mechanism corrected.
- **Evidence classes.** Added E0–E3 alongside DESIGN/RETRO `form` key (primary key unchanged for reliability packet).
- **Checklist parity.** Items 3 and 8 aligned with manuscript Table V (no buffer default; linearizable single-winner consume wording).
- **Naming.** `harness/nonce_consume.py` → `callback_consume.py`; `test_nonce_consume.py` → `test_callback_consume.py`.
- **Metadata.** `CITATION.cff` and `docs/TAGS.md` prepared for v1.0.7; README cite pin updated.

## 1.0.1 – 1.0.6 — 2026-08-13 to 2026-08-15

Packaging and manuscript-alignment iterations between the first Access freeze (`v1.0.0`) and the `v1.0.6` Zenodo pin (`10.5281/zenodo.21950902`). No taxonomy relabels after `v1.0.0`.

## 1.0.0 — 2026-08-13

- Manuscript-aligned freeze for IEEE Access companion artifact.
- Broaden `mfa_delivery` inclusion to MFA completion on an out-of-band path (SMS unreliability or OTP verification/lifecycle), keeping the ten-category id set.
- Clarify `codebook/stress-cases.json` as illustrative decision-test vignettes only (not empirical validation).
- Sync checklist item 9, packet Table II row, I5 publishable summary, and `docs/EVIDENCE-INDEX.md`.

## 0.1.7 — 2026-08-13

- Add `codebook/stress-cases.json` (five outside-taxonomy / multi-causal instrument stress vignettes; not N=11).
- Add synthetic I4 request-size fixtures and checker under `harness/fixtures/i4/`; extend `make smoke`.
- Update I4/I5 publishable summaries and `docs/EVIDENCE-INDEX.md` provenance (ticket-reviewed privately; artifacts not released).

## 0.1.6 — 2026-08-12

Document explicit F3/F5 harness schedules (`harness/SCHEDULES.md`): Schedule A `jwt_only` (second acceptance), Schedule B `naive` (false reject), Schedule C `atomic`. Narrow threat model and atomic single-winner wording for manuscript IV lock.

## 0.1.5 — 2026-08-12

Rename category `edge_nonce` → `edge_callback_consume` for protocol precision (callback-correlation consume ≠ OIDC ID-Token nonce / AS–RS token replay). Sync Table II, incidents, checklist, packet, evidence index, and harness docs. Second-coder agreement remains on the same mechanism cell; earlier tags used the prior label name.

## 0.1.4 — 2026-08-12

Add `docs/EVIDENCE-INDEX.md` and `docs/EXTERNAL-INCIDENTS.md` (plus GitHub issue template) so manuscript Availability references resolve. Align README / `taxonomy.json` title with the current manuscript. Retire checklist “citation-removal” label in favor of bidirectional case traceability; sync Table V item wording (incl. item 8 buffer/fixture language).

## 0.1.3 — 2026-08-12

Reliability computation: add Gwet’s AC1 (primary under severity skew) alongside Cohen’s κ, same bootstrap treatment. Document the `cluster_state` Sev-2/Sev-3 split as severity-boundary judgment.

## 0.1.2 — 2026-08-12

Data release for Access Availability: `codebook/reliability.json` (+ `reliability.md`) with second-coder raw agreement, Cohen’s κ, and bootstrap CIs. Scrub programme placeholder from `CITATION.cff` DOI comment. README authorship left to `CITATION.cff` only (plain harness style).

## 0.1.1 — 2026-08-12

Packet and docs state the second-coder round as **unblinded** relative to the published catalog (`incidents.json` / Table IV). “Packet only until submit” remains the working protocol (not a blinding claim).

## 0.1.0 — 2026-08-12

Independent-coding packet: paraphrased cases (no Table II inclusion vocabulary), additional-observations fields for excludes, Sev-1/2/3 on the response sheet. Gold labels are disclosed as `codebook/incidents.json` (published catalog); working protocol is “do not browse the repo until submit.” Dropped empty `patterns/` placeholder. CI actions SHA-pinned.

## 0.0.0 — 2026-08-11

Initial public scaffold. Hartl-shaped README. License MIT. Public name `sso-failure-taxonomy`.
