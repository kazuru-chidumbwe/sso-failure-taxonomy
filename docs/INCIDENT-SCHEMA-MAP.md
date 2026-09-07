# Incident-schema bridge (Table IV → operations practice)

**Manuscript:** Table XIII · Section II-H  
**Status:** Suggestive mapping for adoption — **not** validated against production telemetry in this study.

Common schemas classify at **incident / actor / control** level. Table IV classifies **authenticated-path mechanism cells** in a bounded dual-IdP + edge-release estate.

| Table IV category | Illustrative placement in VERIS-like / ITSM practice | Primary telemetry hooks |
| --- | --- | --- |
| edge_side_effect | Authentication action succeeded; downstream grant/release failed | IdP auth OK → edge pending/failed counters |
| edge_identifier | Policy/quota action on unstable identifier | Device-cap tables; identifier churn metrics |
| edge_callback_consume | Replay or duplicate completion of edge release | Callback audit; second-accept events |
| session_plane | Session binding mismatch (identity vs network plane) | Separate IdP vs network-session TTL drift |
| directory_federation | Directory bind/search/timeout on WAN path | LDAP latency; bind error codes by site |
| multi_site_affinity | Stickiness / cross-site session visibility | LB failover events; missing app session after SSO cookie |
| cluster_state | In-cluster auth/cache divergence | Per-node auth outcome mismatch |
| protocol_gateway | Middlebox buffer/size handling on federation wire | Gateway 413/414; payload-size class |
| mfa_delivery | MFA completion path failure | OTP verifier errors with password auth OK |
| dual_idp_boundary | Semantic/token mismatch across co-deployed IdPs | iss/aud/claim encoding diffs for same directory subject |
| outside_taxonomy | Symptom-only or adjacent surface (DNS, clock, CDN/WAF) | Upstream resolution; CDN edge errors before gateway |

See also [`OBSERVABILITY-MAP.md`](OBSERVABILITY-MAP.md) for case-linked examples.
