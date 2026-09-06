# Manuscript table numbering (IEEE Access)

Sequential table numbers in the submitted manuscript (Gates round-2, 6 Sep 2026):

| Manuscript table | Content | Artifact primary file |
| --- | --- | --- |
| **Table I** | Evidence classes (E0–E3) | `codebook/incidents.json` (`evidence_classes`) |
| **Table II** | Claims supported by evidence class | manuscript only |
| **Table III** | Evidence strength by case | manuscript only |
| **Table IV** | Rule-bounded taxonomy (categories) | `codebook/taxonomy.json` |
| **Table V** | Operational priority class | `codebook/taxonomy.json` / `incidents.json` |
| **Table VI** | Protocol and edge callback artifact contrast | manuscript only |
| **Table VII** | Case catalog (N=11) | `codebook/incidents.json` |
| **Table VIII** | F5 threat model | manuscript only |
| **Table IX** | Practitioner checklist | `codebook/checklist.json` |
| **Table X** | Prior-work positioning | manuscript only |

Earlier artifact releases used non-sequential numbering (e.g. evidence classes as Table VI; protocol contrast as Table VIII only). From **v1.0.13** onward, the manuscript uses normal IEEE ordering I–X and the artifact tracks it via `incidents.json` → `manuscript_tables`.
