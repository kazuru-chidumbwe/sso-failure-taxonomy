# External narrative evaluation (Gates round-2 / sponsor Hold)

Public-narrative feasibility corpus for IEEE Access §IV-K. **Not part of N=11.**

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

## Status (6 Sep 2026)

- **Coder A:** independent practitioner — complete (`coder-a.json`, 95 min).
- **Coder B:** independent practitioner — complete (`coder-b.json`, 120 min).
- **Overlap (n=13):** 11/13 agreement (84.6%); Gwet AC1 = 0.83; Cohen κ = 0.61 (bootstrap CI includes zero).
- Outside-taxonomy on assigned narratives: Coder A 14/39 (35.9%); Coder B 36/39 (92.3%).
- Disagreements: EN027 (author-constructed), GH004 (live-harvested).

N=11 structured-packet pilot remains in `codebook/reliability.json` (frozen at `v1.0.12` audit).
