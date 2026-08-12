# Release tags

Annotated tags mark reproducible anchors. **`main` may advance** after a tag — always `git checkout <tag>` when reproducing a cited result.

| Tag | Purpose |
| --- | --- |
| `v0.1.5` | **Access / Zenodo cite pin** — `edge_callback_consume` rename + protocol distinction |
| `v0.1.4` | Evidence index + external-incident path — superseded for category id |
| `v0.1.3` | AC1 + κ in reliability.json — superseded |
| `v0.1.2` | Reliability file (κ only) — superseded |
| `v0.1.1` | Unblinded packet wording — superseded |
| `v0.1.0` | First public pin — superseded |

## Tag policy

- **SemVer** → `v0.1.5` (see [`CHANGELOG.md`](../CHANGELOG.md)).
- Never cite floating `main` for published results.
- Mint Zenodo from the **GitHub release for `v0.1.5`**. Paste the DOI into `CITATION.cff` `identifiers` and into the manuscript Availability line.
