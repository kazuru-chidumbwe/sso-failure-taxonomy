# Manuscript table numbering (IEEE Access)

Sequential table numbers in the submitted manuscript (31 Aug 2026 Gates pass):

| Manuscript table | Content | Artifact primary file |
| --- | --- | --- |
| **Table I** | Evidence classes (E0–E3) | `codebook/incidents.json` (`evidence_classes`) |
| **Table II** | Rule-bounded categories | `codebook/taxonomy.json` |
| **Table III** | Operational priority class | `codebook/taxonomy.json` / `incidents.json` (`operational_priority_class` mapping) |
| **Table IV** | Case catalog | `codebook/incidents.json` |
| **Table V** | Practitioner checklist | `codebook/checklist.json` |
| **Table VI** | Prior-work comparison | manuscript only |
| **Table VII** | F5 threat model | manuscript only |
| **Table VIII** | Protocol and edge callback artifact contrast | manuscript only |

Earlier artifact releases used non-sequential numbering (evidence classes as Table VI). From this revision onward, the manuscript uses normal IEEE ordering and the artifact tracks it via `incidents.json` → `manuscript_tables`.
