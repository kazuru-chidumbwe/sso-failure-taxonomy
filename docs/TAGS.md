# Release tags

Annotated tags mark reproducible anchors. **`main` may advance** after a tag — always `git checkout <tag>` when reproducing a cited result.

| Tag | Purpose |
| --- | --- |
| `v0.1.4` | **Access / Zenodo cite pin** — evidence index + external-incident path; title aligned |
| `v0.1.3` | AC1 + κ in reliability.json — superseded for Availability file refs |
| `v0.1.2` | Reliability file (κ only) — superseded |
| `v0.1.1` | Unblinded packet wording — superseded |
| `v0.1.0` | First public pin — superseded |

## Tag policy

- **SemVer** → `v0.1.4` (see [`CHANGELOG.md`](../CHANGELOG.md)).
- Never cite floating `main` for published results.
- Mint Zenodo from the **GitHub release for `v0.1.4`**. Paste the DOI into `CITATION.cff` `identifiers` and into the manuscript Availability line.
