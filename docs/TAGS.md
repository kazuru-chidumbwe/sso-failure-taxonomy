# Tag policy

Cite a tag, never floating `main`.

| Tag | Role |
| --- | --- |
| `v1.0.8` | **IEEE Access / Zenodo cite pin.** Fig. 3 filename `fig3-callback-consume.png` (completes `callback_*` rename); no taxonomy or case-data changes |
| `v1.0.7` | Superseded — manuscript-aligned Table III / checklist / anonymization pass; `nonce_*` → `callback_*` in harness |
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
