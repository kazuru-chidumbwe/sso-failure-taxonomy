# Tag policy

Cite a tag, never floating `main`.

| Tag | Role |
| --- | --- |
| `v1.0.7` | **IEEE Access / Zenodo cite pin.** Manuscript-aligned: Table III summaries byte-matched, evidence classes E0–E3, checklist items 3 and 8 corrected, anonymization pass on `docs/EVIDENCE-INDEX.md`, `nonce_*` → `callback_*` rename |
| `v1.0.6` | Superseded — manuscript-alignment freeze with known Table III / checklist divergences |
| `v1.0.0` – `v1.0.5` | Superseded — packaging and metadata iterations |
| `v0.1.6` | Superseded — explicit F3/F5 harness schedules + threat model |
| `v0.1.5` | Superseded — `edge_nonce` → `edge_callback_consume` rename (data layer only) |
| `v0.1.0` – `v0.1.4` | Superseded — first public pins |

## Release procedure

1. Cut tag `vX.Y.Z` and publish a **GitHub Release** (Zenodo archives on releases, not on tags).
2. Copy the minted **version DOI** into `CITATION.cff` `identifiers` and into the manuscript
   Data and Code Availability statement.
3. Confirm the Zenodo record's version label matches the tag before citing it.
4. Never edit a tagged release in place. Cut a new patch tag instead.
