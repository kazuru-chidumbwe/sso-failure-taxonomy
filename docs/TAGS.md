# Release tags

Annotated tags mark reproducible anchors. **`main` may advance** after a tag — always `git checkout <tag>` when reproducing a cited result.

| Tag | Purpose |
| --- | --- |
| `v0.1.1` | **Access cite pin** — unblinded packet wording + paraphrased cases |
| `v0.1.0` | First public pin (paraphrased packet; still said “Isolation”) — superseded for Availability |

## Tag policy

- **SemVer** → `v0.1.1` (see [`CHANGELOG.md`](../CHANGELOG.md)).
- Never cite floating `main` for published results.
- New SemVer tags when the release boundary changes — not on every doc commit.
- Mint Zenodo from the **GitHub release for `v0.1.1`**. Paste the DOI into `CITATION.cff` `identifiers` and into the manuscript Availability line.
