# Manuscript table numbering

Sequential table numbers in the submitted manuscript (round 6, Sep 2026):

| Manuscript table | Content | Artifact primary file |
| --- | --- | --- |
| **Table I** | Evidence classes (E0–E3) | `codebook/incidents.json` (`evidence_classes`) |
| **Table II** | Claims supported by evidence class | manuscript only |
| **Table III** | Evidence strength by case | manuscript only |
| **Table IV** | Rule-bounded taxonomy (categories) | `codebook/taxonomy.json` |
| **Table V** | Operational priority class | `codebook/taxonomy.json` / `incidents.json` |
| **Table VI** | Protocol and edge callback artifact contrast | manuscript only |
| **Table VII** | Release cite pins and freeze points | manuscript only |
| **Table VIII** | Decision-test battery expected labels (S1–S8) | `codebook/stress-cases.json` |
| **Table IX** | Case catalog (N=11) | `codebook/incidents.json` |
| **Table X** | F5 threat model | manuscript only |
| **Table XI** | Practitioner checklist | `codebook/checklist.json` |
| **Table XII** | Prior-work positioning | manuscript only |

The artifact tracks this map in `codebook/corpus.json` → `manuscript_tables` (mirrored in `codebook/incidents.json` for convenience). **Table IX** in the manuscript is authoritative for case-catalog rows; internal cross-reference notes in JSON are informative only.
