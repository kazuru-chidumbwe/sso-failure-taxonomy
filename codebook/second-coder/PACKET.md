# Independent coding packet — label assignment

**Task:** Assign one Table I category and one Table II severity to each case.  
**This is not taxonomy discovery.** Table I is normative. You apply the inclusion/exclusion rules and tie-breakers.  
**Time:** about one hour.  
**Order:** cases are in randomized order.  
**No estate access.** No NDA. Do not search for the paper.

**Isolation (mandatory):** Treat this file as self-contained. Do not clone, browse, or search the public repository until you have submitted this sheet. The published codebook in that repository includes per-incident category, severity, and form. Reading it would make this task a transcription exercise.

Return the filled response sheet. Do not discuss cases with the author until you submit.

---

## What you receive

1. This packet (instructions + cases).  
2. Table I (inclusion / exclusion).  
3. Table II (severity).  
4. Tie-breakers (below).  
5. Response sheet.

## What you do not receive in this packet

Incident IDs (F1… / I1…), gold category labels, and the manuscript’s one-line summaries. Those labels exist in the public codebook (`codebook/incidents.json`) for the published catalog. They are not hidden. Isolation is procedural: code from this file only, then submit.

Case texts are paraphrased. They are not the Table I inclusion sentences. Apply the rules; do not keyword-match the table.

---

## How to code

For each case, read **symptom**, **mechanism**, **resolution**, and **additional observations**.

The additional-observations field is evidence for Table I **excludes**. Use it. A match on the inclusion phrase alone is not enough.

1. Walk the tie-breaker order in Table I: first matching **Yes** wins.  
2. Assign **exactly one** category from Table I.  
3. Assign **exactly one** severity from Table II, written as `Sev-1`, `Sev-2`, or `Sev-3`. Severity is a second axis. It is not a substitute for mechanism. The same mechanism may appear at two severities.  
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

Write the code `Sev-1`, `Sev-2`, or `Sev-3` on the response sheet (not bare `1` / `2` / `3`).

---

## Cases (randomized order)

### Case 01

**Symptom:** Users who had just completed login at the identity product were asked again for directory credentials before they could use the network.  
**Mechanism:** Operators treated “already logged in at the identity product” as “already on the network.” Completing the identity product’s login did not, by itself, open the network path. The two clocks were independent; staff expected the first to skip the second.  
**Resolution:** Write the two clocks down as separate. Never treat identity-product login as permission to skip the network check.  
**Additional observations:** Replica nodes of the identity product agreed on the user’s login. Returning the user to a previous site did not change the prompt. Device addresses used for policy were stable and within quota. The network check itself succeeded when it ran. No second identity product was in the path. Login eventually completed after the extra prompt; the load was helpdesk tickets, not an outage.

### Case 02

**Symptom:** A copied callback value let a client obtain a network capability it should not have kept.  
**Mechanism:** A callback token meant to be used once was looked up and then removed in two separate steps. A second presentation of the same value in the gap still succeeded. Treating a signed token as finished because it had not yet expired was accepted as sufficient.  
**Resolution:** Read and remove the one-time value in a single store operation. Alarm if a copy is presented after that.  
**Additional observations:** On first use, the user’s identity was correct and the device address used for policy was stable and within quota. The network-opening step was not the failing step. Login messages reached the identity product intact. Directory lookups were timely. This was not helpdesk friction: a captured callback could re-enter after the first client had already succeeded.

### Case 03

**Symptom:** A subset of users never finished the second factor. Password check had already succeeded.  
**Mechanism:** Policy required a one-time code that arrived over the telephone text channel. Those messages did not arrive in time, or at all. Users with the right password were left with no other way through.  
**Resolution:** Prefer an authenticator app as the primary second factor. Keep the telephone channel as fallback. Provide a path that does not strand the user when the message never comes.  
**Additional observations:** Replica nodes of the identity product agreed. Returning the user to a previous site did not change the outcome. The stall was before any network-opening step; this was not a second clock after identity login. Device addresses were stable. Login messages reached the identity product intact. Directory lookups were timely. Operations had to change the second-factor path for the affected cohort.

### Case 04

**Symptom:** An application worked against identity product A and broke against identity product B, including at cutover.  
**Mechanism:** Both products looked up the same people. Token fields, lifetimes, or claim names still differed, and the application depended on the first product’s meaning.  
**Resolution:** Before cutover, check that tokens, claims, and lifetimes are equivalent for each application — not only that both products can find the user.  
**Additional observations:** User lookup in the shared people store succeeded on both products. Replica nodes within each product agreed. Login messages arrived intact. This was a live cutover with a broken application, not a laboratory matrix. Device addresses and the telephone second-factor channel were not in the failing path.

### Case 05

**Symptom:** After a user moved between sites, or after failover, they were asked to log in again or saw a session that looked out of date.  
**Mechanism:** Request routing did not consistently return a user to the node holding their session, and session state was not uniformly visible across the routing tier.  
**Resolution:** Pin a user to the node that holds their session where that is required. Confirm that the store those nodes share actually answers. Expect a re-login window on failover rather than claiming it cannot happen.  
**Additional observations:** Within one site, replica nodes did not disagree on who was a member of the set. Directory lookups were timely. Login messages reached the identity product intact. Device addresses were stable. The telephone second-factor channel was not involved. Operators had to intervene at the affected site.

### Case 06

**Symptom:** Two replica nodes of the same identity product gave the same user different “already logged in” answers.  
**Mechanism:** After a brief split, both nodes accepted writes. One node still served an older login record while the other had moved on.  
**Resolution:** Run a quorum. Do not allow two writers. Treat disagreement among replica nodes as an authentication health failure, not only as a cluster health failure.  
**Additional observations:** The user was not being sent to a different site; the disagreement was among replicas of one product. Directory lookups were timely. Login messages arrived intact. Device addresses were stable. The telephone second-factor channel was not involved. Operators had to repair the replica set before login was trustworthy again.

### Case 07

**Symptom:** The identity product logged no complete login request; the reverse proxy reported a truncated or invalid body.  
**Mechanism:** The message that should have reached the identity product’s application code was cut off or closed on the path in front of it. The same class of message succeeded on a path that would accept a larger body and a longer idle wait.  
**Resolution:** Raise body and idle limits to at least twice the largest login message in use. Alert when the proxy rejects a login body.  
**Additional observations:** User lookup in the directory was not the failing step; the identity product never saw the request. Replica nodes were not split. Device addresses were stable. The telephone second-factor channel was not involved. A user cohort behind that reverse proxy could not authenticate until operators changed the proxy limits.

### Case 08

**Symptom:** After a release, legitimate callbacks were rejected as already used or unknown. A spike of failed logins followed.  
**Mechanism:** A callback token meant to be used once was looked up and then removed in two separate steps. Under concurrent retries, both requests could pass the existence check; the loser was then told the value was gone. Under load, the stored value also disappeared before the browser returned.  
**Resolution:** Read and remove the one-time value in a single store operation. Keep it long enough for the round trip. Confirm the path still works when the user is not pinned to one node.  
**Additional observations:** No evidence that a third party presented a captured token. On first use, identity and device handling were correct. Login messages reached the identity product intact. Directory lookups were timely. Users were locked out until operations rolled or patched the consume path; this was not a bypass and not helpdesk-only friction.

### Case 09

**Symptom:** At a distant office, login failed or hung, while the identity product process at the hub was healthy.  
**Mechanism:** Looking up the user in the central people store took longer than the login path would wait. The link to that store was lossy. Hub processes were up; the lookup step was not.  
**Resolution:** Lengthen the wait to match the link. Keep a nearer copy of the people store, or say clearly that login will degrade when the link is bad.  
**Additional observations:** Login messages reached the identity product intact; the stall was the user-lookup step, not a truncated body at a proxy. Replica nodes at the hub agreed. Device addresses were stable. The telephone second-factor channel was not the failing step. Operators had to change timeouts or placement before that office could log in reliably.

### Case 10

**Symptom:** A user who had already completed identity login was blocked for exceeding a device allowance.  
**Mechanism:** Policy counted “devices” by the hardware address the client presented. Phones that change that address on their own were counted as many devices, and a real person exhausted the allowance.  
**Resolution:** Do not key the allowance on an address the client can change without the user noticing. Design the path for that change. Give a remediation experience that is not “buy another licence.”  
**Additional observations:** Identity login had succeeded. The network-opening step ran; the block was the count keyed on the address, not a grant that failed to complete after a correct identity. Replica nodes agreed. Login messages arrived intact. Directory lookups were timely. The address was not stable across reconnects. Operations had to clear or redesign the allowance for the affected users.

### Case 11

**Symptom:** Federated login at the identity product succeeded; the client remained walled off from the network.  
**Mechanism:** The identity product recorded a successful login. The later step that was supposed to open the network never completed, and that recorded success was not undone. The user held a valid login and still could not pass the wall.  
**Resolution:** Do not record success until the network-opening step acknowledges. If that step fails, undo the recorded login. Reconcile leftovers.  
**Additional observations:** The hardware address used for policy was stable and within quota. The one-time callback value was used once and was not replayed. Replica nodes agreed. Login messages reached the identity product intact. Directory lookups were timely. Identity handling was correct; the gap was the later network-opening step with no undo. Operators had to reconcile the two sides before the user could pass.

---

## Response sheet

Copy this table. One category and one severity per row. Severity must be `Sev-1`, `Sev-2`, or `Sev-3`.

| Case | Category (Table I or NEW_LABEL) | Severity (Sev-1 / Sev-2 / Sev-3) | One-line note (optional) |
| ---: | --- | --- | --- |
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
