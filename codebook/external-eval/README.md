# External narrative evaluation (exploratory archive)

> **Manuscript note (Path D, Sep 2026):** This corpus and coder responses were collected for an exploratory routing pilot. They are **not cited as study evidence** in the IEEE Access manuscript. Open falsifiability for operators uses `docs/EXTERNAL-INCIDENTS.md` instead.

Public-narrative feasibility corpus (archived). **Not part of N=11.**

| File | Role |
| --- | --- |
| `narratives.json` | 65 narratives — **35 live-harvested** + **30 author-constructed** (schema v2) |
| `PACKET.md` | Standalone coder instructions + response sheet template |
| `RECRUITMENT.md` | Outreach blurb and eligibility |
| `coder-a.json` | Independent practitioner Coder A (`author_coded: false`, 39 narratives) |
| `coder-b.json` | Independent practitioner Coder B (`author_coded: false`, 39 narratives) |
| `reliability-external-v1.json` | Overlap agreement + outside-taxonomy summary |
| `PROVENANCE.md` | Coder independence + correction for erroneous `e34f848` commit subject |

## Corpus provenance (v2)

| Class | n | Artifact fields |
| --- | ---: | --- |
| **Live-harvested** | 35 | `provenance: live-harvested`, traceable `url` (12 Keycloak GitHub issues, 23 ServerFault) |
| **Author-constructed** | 30 | `provenance: author-constructed`, `url: null`, `source_style` only (EN001–EN030) |

**Overlap block (n=13):** 9 live-harvested + 4 author-constructed (`EN027`–`EN030`).

Author-constructed vignettes resemble operator text in named source styles; they are **not** traceable to a single public thread (same honesty class as design-derived estate scenarios).

## Fingerprint-safe paraphrase procedure (v1.0.18+)

Live-harvested rows are **not** verbatim copies of public threads in the published corpus.

| Step | Procedure |
| --- | --- |
| 1. Source eligibility | Only **publicly readable** threads (Keycloak GitHub issues, ServerFault questions) with no paywall or private attachment requirement. |
| 2. Archive policy | **Originals are not archived** in the repository. Only the paraphrase text, provenance class, and (when permitted) a traceable public URL are retained. |
| 3. Paraphrase | Rewrite operator symptoms and mechanism cues in neutral third person; remove usernames, hostnames, organization names, IP addresses, e-mail addresses, ticket IDs, configuration secrets, access tokens, and other unique identifiers. |
| 4. Fingerprint check | Author review scans each row for surviving identifiers or reconstructable fingerprints before release. |
| 5. Ground truth | Public-thread narratives are **not verified incident ground truth**; they test routability of the codebook on operator-style text. |

The one-line `fingerprint_policy` field in `narratives.json` summarizes this discipline for machine readers.

## Status (6 Sep 2026)

- **Coder A:** independent practitioner — complete (`coder-a.json`, 95 min).
- **Coder B:** independent practitioner — complete (`coder-b.json`, 120 min).
- **Overlap (n=13):** 11/13 agreement (84.6%); Gwet AC1 = 0.83; Cohen κ = 0.61 (bootstrap CI includes zero).
- **Outside-taxonomy (assigned sets):** Coder A 14/39 (35.9%); Coder B 36/39 (92.3%). Rates predate evidence-sufficiency rule in `codebook/taxonomy.json` (v1.0.18+).
