# Independent coding packet — label assignment

**Task:** Assign one Table I category and one Table II severity to each case.  
**This is not taxonomy discovery.** Table I is normative. You apply the inclusion/exclusion rules and tie-breakers.  
**Time:** about one hour.  
**Blind:** cases are in randomized order. Category names and publishable summaries are stripped.  
**No estate access.** No NDA. Do not search for the paper.

Return the filled response sheet. Do not discuss cases with the author until you submit.

---

## What you receive

1. This packet (instructions + cases).  
2. Table I (inclusion / exclusion).  
3. Table II (severity).  
4. Tie-breakers (below).  
5. Response sheet.

## What you do not receive

Incident IDs (F1… / I1…), category labels, publishable one-liners, documentation pointers. Gold labels are not in this repository.

## How to code

For each case, read **symptom**, **mechanism**, and **resolution**.

1. Walk the tie-breaker order in Table I: first matching **Yes** wins.  
2. Assign **exactly one** category from Table I.  
3. Assign **exactly one** severity from Table II. Severity is a second axis. It is not a substitute for mechanism. The same mechanism may appear at two severities.  
4. If no Table I cell fits, write `NEW_LABEL` and one sentence why.  
5. Do not invent incidents. Do not recode another coder’s sheet.

**Frame (honest):** agreement on label assignment given a normative decision table.

---

## Tie-breakers (mandatory)

1. If the root cause is **identifier instability**, classify as `edge_identifier` even when the failure looks like authorize or release.  
2. Use `edge_side_effect` only when identity and identifier handling are correct and the failure is a non-transactional edge commit or release.  
3. `mfa_delivery` excludes to `cluster_state`, `multi_site_affinity`, or `session_plane` — not to an unnamed HA bucket.  
4. `edge_nonce` is mechanism-defined (broken one-use `state`/nonce consume, including missing atomic consume). It may be Severity-2 or Severity-3.

---

## Table I — Closed category inclusion and exclusion

| Category | Includes | Excludes (goes to…) |
| --- | --- | --- |
| edge_side_effect | IdP/session success but edge enforcement side-effect fails (authorize/release); non-transactional boundary | Identifier policy false blocks → edge_identifier; nonce/replay → edge_nonce |
| edge_identifier | Cap/quota/policy keyed on unstable device identifiers (e.g., MAC randomization) | Side-effect after correct identity → edge_side_effect |
| edge_nonce | OIDC/`state` single-use/replay lifecycle broken (concurrency, TTL, missing atomic consume); mechanism-defined | Session-plane confusion without replay → session_plane |
| session_plane | Confusion or unsafe shortcut between identity session and network/edge session (independent TTLs) | Cluster cache divergence inside IdP → cluster_state |
| directory_federation | Auth fails because LDAP/AD federation path latency/availability over WAN breaks bind/search/timeouts | Gateway truncates assertion before IdP logic → protocol_gateway |
| multi_site_affinity | Cross-site / load-balancer stickiness or session visibility causes re-auth or stale UX after hop/failover | In-cluster membership/cache split → cluster_state |
| cluster_state | IdP cluster membership / distributed-cache divergence (stale or conflicting auth state across nodes) | Load-balancer affinity only → multi_site_affinity |
| protocol_gateway | Middlebox buffer/timeout damages SAML/OIDC payloads before IdP application logic | Directory bind timeout → directory_federation |
| mfa_delivery | MFA fails because delivery channel (e.g., SMS) is unreliable; password/IdP otherwise OK | IdP HA/session bugs → cluster_state, multi_site_affinity, or session_plane |
| dual_idp_boundary | Shared directory / same profile but token/claim/lifetime semantics differ across co-deployed IdPs → application break | Synthetic lab matrix without ops incident → out of corpus |

---

## Table II — Severity axis

| Code | Meaning |
| --- | --- |
| Sev-1 | Friction / helpdesk noise; authentication eventually succeeds or workaround is trivial |
| Sev-2 | Authentication or service failure for a user cohort or site; operations intervention required |
| Sev-3 | Security-boundary risk (bypass, wrong trust) or widespread multi-site authentication outage |

---

## Cases (randomized order)

### Case 01

**Symptom:** Re-prompt for directory credentials despite recent SSO.  
**Mechanism:** Identity session is not the network session; operators expected SSO to skip edge re-authorization.  
**Resolution:** Document two planes; never skip edge re-authorize.

### Case 02

**Symptom:** Capability bypass via replayed `state`.  
**Mechanism:** JWT expiry was accepted; the nonce was not atomically consumed.  
**Resolution:** Mandatory nonce store + atomic consume; security telemetry.

### Case 03

**Symptom:** MFA never completes for a subset of users.  
**Mechanism:** SMS delivery unreliable; policy assumed prompt delivery.  
**Resolution:** Authenticator-first; SMS as fallback; path that does not strand the user.

### Case 04

**Symptom:** Application works on IdP A and breaks on IdP B or at cutover.  
**Mechanism:** Token shape, lifetimes, or claims were not equated across co-deployed IdPs that share a directory.  
**Resolution:** Equivalence checklist before cutover.

### Case 05

**Symptom:** Re-authentication or a stale session after site hop or failover.  
**Mechanism:** Imperfect multi-site affinity / session visibility.  
**Resolution:** Sticky where required; validate shared store; expect re-auth windows.

### Case 06

**Symptom:** Conflicting authentication state across secondary IdP nodes.  
**Mechanism:** Cluster membership or cache divergence under partition.  
**Resolution:** Quorum runbook; no dual-writer; treat cluster coherence as an authentication health check.

### Case 07

**Symptom:** Truncated or invalid assertion at the gateway.  
**Mechanism:** Load-balancer buffer or idle timeout undersized for large assertions.  
**Resolution:** Buffer at least twice maximum assertion size; raise idle timeouts; alert.

### Case 08

**Symptom:** Replay or nonce reject spike after a deploy.  
**Mechanism:** Non-atomic nonce consume and TTL skew under concurrency.  
**Resolution:** Atomic consume (e.g. GETDEL); TTL at least round-trip; sticky-independence test.

### Case 09

**Symptom:** Intermittent login and slow binds at a remote site.  
**Mechanism:** LDAP/AD federation over intermittent WAN exceeded timeouts.  
**Resolution:** Tune timeouts; cache or replica; degrade messaging.

### Case 10

**Symptom:** Legitimate user hits a device cap.  
**Mechanism:** MAC randomization inflated the active-device count.  
**Resolution:** Stable identifiers; design for randomization; remediation user experience.

### Case 11

**Symptom:** Federated login succeeded; the client remained walled from the network.  
**Mechanism:** Edge authorize failed after the session or capability commit; no rollback.  
**Resolution:** Acknowledgment-before-commit; rollback; reconcile.

---

## Response sheet

Copy this table. One category and one severity per row.

| Case | Category (Table I or NEW_LABEL) | Severity (1 / 2 / 3) | One-line note (optional) |
| ---: | --- | ---: | --- |
| 01 |  |  |  |
| 02 |  |  |  |
| 03 |  |  |  |
| 04 |  |  |  |
| 05 |  |  |  |
| 06 |  |  |  |
| 07 |  |  |  |
| 08 |  |  |  |
| 09 |  |  |  |
| 10 |  |  |  |
| 11 |  |  |  |

**Coder name** (for Acknowledgment) or **anonymous descriptor** (e.g. “independent coder, N years IAM operations”):  

**Date:**  

**Minutes spent:**  
