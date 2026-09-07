# Rejected / excluded estate vignettes (not N=11)

**File:** [`codebook/rejected-estate-vignettes.json`](../codebook/rejected-estate-vignettes.json)  
**Manuscript:** Section IV-D (Layer 1.5) · worked examples in Section IV-I

These anonymized vignettes were **considered** during estate case selection but are **not** rows in Table IX. They show that the instrument can route to *outside taxonomy* on operational-adjacent material without expanding the byte-frozen N=11 catalog.

| ID | Expected label | Why not in N=11 |
| --- | --- | --- |
| R1 | outside_taxonomy | DNS/upstream resolution fails before any Table IV inclusion rule applies |
| R2 | outside_taxonomy | Multi-causal WAN LDAP + gateway deadlock (parallel to S2); tie-breakers do not privilege one primary |

Verified at release by `codebook/validate_catalog_assignments.py` (`make smoke`).
