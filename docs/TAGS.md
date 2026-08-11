# Release tags

Annotated tags mark reproducible anchors. **`main` may advance** after a tag — always `git checkout <tag>` when reproducing a cited result.

| Tag | Purpose |
| --- | --- |
| `v0.1.0` | First public cite pin (paraphrased coding packet; honest catalog disclosure) |

## Tag policy

- **SemVer** → `v0.1.0` (see [`CHANGELOG.md`](../CHANGELOG.md)).
- Never cite floating `main` for published results.
- New SemVer tags when the release boundary changes — not on every doc commit.
- Zenodo DOI is minted from a tagged GitHub release, not instead of GitHub. Insert the DOI in `CITATION.cff` once Zenodo returns it.
