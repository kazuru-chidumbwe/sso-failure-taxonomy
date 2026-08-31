# Tag policy

Cite a tag, never floating `main`.

| Tag | Role |
| --- | --- |
| `v1.0.9.1` | **IEEE Access / Zenodo cite pin.** `CITATION.cff` version DOI wired (`10.5281/zenodo.22214839`) |
| `v1.0.9` | Manuscript title + SCOPE wording; DOI procedure in TAGS.md |
| `v1.0.8` | Superseded — Fig. 3 `fig3-callback-consume.png`; version DOI on tag lagged until post-release commit |
| `v1.0.7` | Superseded — manuscript-aligned Table III / checklist / anonymization pass; `nonce_*` → `callback_*` in harness |
| `v1.0.0` – `v1.0.5` | Superseded — packaging and metadata iterations |
| `v0.1.6` | Superseded — explicit F3/F5 harness schedules + threat model |
| `v0.1.5` | Superseded — `edge_nonce` → `edge_callback_consume` rename (data layer only) |
| `v0.1.0` – `v0.1.4` | Superseded — first public pins |

## Release procedure

1. Cut tag `vX.Y.Z` and publish a **GitHub Release** (Zenodo archives on releases, not on tags).
2. Wait for Zenodo to mint the **version DOI** for that release.
3. Commit the version DOI into `CITATION.cff` (`url:` and `identifiers` "This version") on `main`.
4. Copy the same version DOI into the manuscript Data and Code Availability statement and ref [28].
5. Confirm the Zenodo record's version label matches the tag before citing it.
6. If the DOI commit must ship after the tag, cut a **patch tag** (e.g. `v1.0.9.1`) so the archived release ZIP includes the wired DOI.
7. Never edit a tagged release in place. Cut a new patch tag instead.
