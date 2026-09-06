# External narrative coding packet — raw text

**Task:** Assign one **Table IV** primary category label to each narrative (or `outside_taxonomy` when no cell fits).  
**This is not taxonomy discovery.** Table IV is normative. Apply inclusion/exclusion rules and tie-breakers.  
**Time:** ~2–3 hours for your assigned subset.  
**No estate access.** No NDA.

**Working protocol:** Do **not** clone, browse, or search the public `sso-failure-taxonomy` repository before you submit this sheet. The published codebook and case catalog exist online; reading them would change the exercise. We measure agreement on applying Table IV to **raw operator narratives**, not transcription from a catalog.

Return the filled response sheet. Do not discuss narratives with the author until you submit.

---

## What you receive

1. This packet (instructions).  
2. Your assigned narratives (separate file or e-mail attachment — IDs `EN001`…).  
3. Table IV summary (below).  
4. Tie-breakers (below).  
5. Response sheet (bottom).

## What you do not receive

- Structured symptom/mechanism/negative-evidence fields (those were used in the N=11 structured-packet pilot only).  
- Gold labels or author assignments.  
- Estate incident IDs (F1…I6).

Narratives are paraphrased public operator text. Apply the rules; do not keyword-match category names alone.

---

## How to code

For each narrative:

1. Read the full text once.  
2. Walk Table IV in fixed order; first satisfied inclusion rule wins unless tie-breakers apply.  
3. Assign **exactly one** primary label from the ten categories, or `outside_taxonomy` if no rule fits or two cells remain equally plausible after tie-breakers.  
4. Optional one-line note explaining excluded neighbors.  
5. Do not invent facts not in the narrative.

**Frame (honest):** descriptive pilot rule-application on raw text under less favorable information conditions — not population reliability or construct validation.

---

## Tie-breakers (mandatory)

1. **Identifier instability** → `edge_identifier` even when failure looks like authorize/release.  
2. `edge_side_effect` only when identity and identifier handling are correct and failure is non-transactional edge commit/release.  
3. `mfa_delivery` excludes to `cluster_state`, `multi_site_affinity`, `session_plane` — not an unnamed HA bucket.  
4. `edge_callback_consume` = single-use edge callback capability lifecycle (not OAuth `state`, OIDC `nonce`, authorization code, or access token interchangeability).  
5. `directory_federation` vs `protocol_gateway` — if equally plausible after tie-breakers → `outside_taxonomy`.  
6. `multi_site_affinity` vs `cluster_state` — in-cluster cache split only when affinity ruled out.

---

## Table IV — Category summary

| Category | Includes (compressed) |
| --- | --- |
| edge_side_effect | IdP success but edge authorize/release fails; non-transactional boundary |
| edge_identifier | Cap/quota on unstable device identifiers |
| edge_callback_consume | Single-use callback capability lifecycle failure |
| session_plane | Identity session vs network/edge session confusion |
| directory_federation | LDAP/AD over WAN bind/search/timeout |
| multi_site_affinity | Cross-site stickiness / session visibility |
| cluster_state | IdP cluster membership / cache divergence |
| protocol_gateway | Middlebox damages SAML/OIDC before IdP logic |
| mfa_delivery | MFA completion path failure (e.g. OTP/SMS) while password OK |
| dual_idp_boundary | Shared directory but divergent token/claim semantics |

**Terminal outcome:** `outside_taxonomy` — no inclusion rule applies, or two categories remain equally plausible after tie-breakers.

*(Full inclusion/exclusion table: manuscript Table IV or author-supplied excerpt.)*

---

## Response sheet

| Narrative ID | Primary label (Table IV or outside_taxonomy) | One-line note (optional) |
| --- | --- | --- |
| | | |
| | | |

**Coder descriptor** (for acknowledgment) or **anonymous** (e.g. "independent coder, IAM/SSO operations"):  

**Date completed:**  

**Minutes spent:**  
