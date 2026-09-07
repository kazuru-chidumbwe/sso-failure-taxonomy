# Tag policy

Cite a tag, never floating `main`.

| Tag | Role |
| --- | --- |
| `v1.0.20` | **Sponsor round-7 CI fix.** `compute_reliability.py` fixed q=10/3 for N=11 bootstrap; CI verification in smoke; F3 flag concurrent-only. Wire Zenodo version DOI after GitHub Release. |
| `v1.0.19` | **Sponsor artifact alignment.** Table map I–XII; checklist 14 rows; `compute_reliability.py`; harness `PresenceOnlyCallbackStore`; title/cite pin sync. Zenodo `10.5281/zenodo.22644754`. N=11 frozen at `v1.0.12`. |
| `v1.0.18` | **Gates/Ng convergent revision.** Evidence-sufficiency rule in `taxonomy.json`; stress vignettes S6–S8; fingerprint-safe procedure in `external-eval/README.md`. Zenodo `10.5281/zenodo.22550779`. N=11 frozen at `v1.0.12`. |
| `v1.0.17` | **Coder independence provenance.** `author_coded: false` on external-eval coder JSON; `PROVENANCE.md` corrects `e34f848` commit subject. Zenodo `10.5281/zenodo.22546805`. N=11 frozen at `v1.0.12`. |
| `v1.0.16` | **Corpus provenance v2.** 35 live-harvested + 30 author-constructed; `validate_corpus_provenance.py`. Zenodo `10.5281/zenodo.22544498`. N=11 frozen at `v1.0.12`. |
| `v1.0.15` | **Sponsor recount fix.** Coder B outside-taxonomy 36/39 (92.3%). Zenodo `10.5281/zenodo.22544249`. *(Corpus URL honesty superseded by v1.0.16.)* |
| `v1.0.14` | **A2 complete.** Human `coder-a.json` + `coder-b.json`; `reliability-external-v1.json` overlap stats. Zenodo version DOI `10.5281/zenodo.22544007`. N=11 frozen at `v1.0.12`. *(Coder B outside count superseded by v1.0.15.)* |
| `v1.0.13` | **Gates round-2 batch.** Tables I–X mapping; `presence_only` harness rename; `codebook/external-eval/`; `docs/QUICK-START.md`. Zenodo version DOI `10.5281/zenodo.22542638`. N=11 catalog frozen at `v1.0.12`. |
| `v1.0.12` | **Manuscript cite pin** (submit pass). Figure render fix; Table VIII tracking; `SCHEDULES.md` production extension. Wire Zenodo version DOI into manuscript Availability / ref [38] after GitHub release. |
| `v1.0.11` | Gates pass. Sequential table numbering I–VII; `operational_priority_class` mapping; figure ideal pass (content). Version DOI `10.5281/zenodo.22215468`. |
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
