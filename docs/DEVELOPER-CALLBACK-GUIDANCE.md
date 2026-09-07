# Developer guidance: edge callback capability vs OAuth/OIDC artifacts

**Manuscript:** Table VI · Section IV-H · Table XI item 3a

## Do not conflate

| Artifact | Store separately? | Typical mistake |
| --- | --- | --- |
| OAuth `state` | Yes — request/session scoped | Reusing `state` as edge-release authorization |
| OIDC `nonce` | Yes — bound to ID Token | Treating nonce validation as network-release consume |
| Authorization code | AS-scoped, single-use at AS | Storing code where edge expects callback capability |
| Access token | RS authorization | Presenting access token to edge release endpoint |
| **Edge callback capability** | Dedicated key namespace at edge RP | Presence check without atomic consume (F5 schedule) |

## Implementation patterns

1. **Namespace:** Use a dedicated store key prefix (e.g. `edge-callback:`) never shared with OAuth state tables.
2. **Atomic consume:** Single-winner get-and-delete at the release consistency scope (see harness `atomic` schedule).
3. **Fail closed:** If consume outcome is uncertain after partition/failover, reject callback completion.
4. **TTL:** Derive from measured authorization round-trip high percentile, not IdP SSO session TTL.
5. **Logging:** Log consume outcome (accepted / rejected / duplicate) separately from IdP authentication success.

## RP stack checklist

- [ ] Callback handler does not read OAuth `state` to authorize network release.
- [ ] OIDC nonce validation occurs in ID Token verification path only.
- [ ] Edge capability is invalidated exactly once before network grant is committed.
- [ ] Concurrent duplicate callbacks tested (Table XI item 3e).
