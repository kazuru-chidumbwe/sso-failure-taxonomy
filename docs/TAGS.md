# Tag policy

Cite a tag, never floating `main`.

| Tag | Role |
| --- | --- |
| `v1.0.11` | **Manuscript cite pin** for IEEE Access submission (Gates pass). Sequential table numbering I–VII; `operational_priority_class` mapping in `incidents.json`; figure ideal pass; refs [29]–[34] in manuscript only. Wire version DOI into manuscript ref [28] after Zenodo mints for this release. |
| `v1.0.10` | **CITATION.cff policy fix.** `url:` and `identifiers` use concept DOI only (`10.5281/zenodo.21950901`). Version DOI belongs in the manuscript, not in the artifact metadata. |
| `v1.0.9` | **IEEE Access / Zenodo cite pin** for manuscript Availability and ref [28]. Version DOI `10.5281/zenodo.22214839`. Tag snapshot's `CITATION.cff` still carried v1.0.8 DOI — superseded by v1.0.10 policy. |
| `v1.0.9.1` | Superseded post-tag DOI wire attempt; do not cite this tag in the paper. |
| `v1.0.8` | Superseded — Fig. 3 `fig3-callback-consume.png` |
| `v1.0.7` | Superseded — manuscript-aligned Table III / checklist / anonymization pass |
| `v1.0.0` – `v1.0.5` | Superseded — packaging and metadata iterations |
| `v0.1.6` | Superseded — explicit F3/F5 harness schedules + threat model |
| `v0.1.5` | Superseded — `edge_nonce` → `edge_callback_consume` rename (data layer only) |
| `v0.1.0` – `v0.1.4` | Superseded — first public pins |

## Release procedure

1. Cut tag `vX.Y.Z` and publish a **GitHub Release** (Zenodo archives on releases, not on tags).
2. Wait for Zenodo to mint the **version DOI** for that release.
3. **Manuscript only:** wire the version DOI and tag into Data and Code Availability and ref [28]. Confirm in a browser that the Zenodo record's version label matches the tag before submitting.
4. **`CITATION.cff`:** keep `url:` and `identifiers` on the **concept DOI** (`10.5281/zenodo.21950901`) only. Do **not** put the version DOI in the artifact — it cannot be correct inside the first tagged snapshot.
5. Bump `version:` and `date-released:` in `CITATION.cff` when cutting a new tag; no post-tag DOI commit is required.
6. Never edit a tagged release in place. Cut a new patch tag instead.
