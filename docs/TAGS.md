# Release tags

Annotated tags mark reproducible anchors. **`main` may advance** after a tag — always `git checkout <tag>` when reproducing a cited result.

| Tag | Purpose |
| --- | --- |
| `v0.1.2` | **Access / Zenodo cite pin** — reliability.json + unblinded packet + plain README |
| `v0.1.1` | Unblinded packet wording (no reliability file) — superseded |
| `v0.1.0` | First public pin — superseded |

## Tag policy

- **SemVer** → `v0.1.2` (see [`CHANGELOG.md`](../CHANGELOG.md)).
- Never cite floating `main` for published results.
- New SemVer tags when the release boundary changes — not on every doc commit.
- Mint Zenodo from the **GitHub release for `v0.1.2`**. Paste the DOI into `CITATION.cff` `identifiers` and into the manuscript Availability line.
