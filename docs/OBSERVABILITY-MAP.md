# Observability map (category → signals)

**Manuscript:** Section VII checklist · Section IX conclusion  
**Purpose:** Suggest operator-visible signals that **support triage** toward a Table IV primary label. This map does **not** define automatic classification rules and is not validated against production telemetry in this study.

| Category | Example signals / probes | Cases |
| --- | --- | --- |
| edge_side_effect | Edge grant/commit split; ACL applied before IdP callback completes; stage counters show IdP success then edge pending | F1 |
| edge_identifier | Identifier churn (MAC randomization); cap tables keyed on unstable identifiers | F2 |
| edge_callback_consume | Duplicate callback acceptance; consume audit shows second winner; harness schedules F3/F5 | F3, F5 |
| session_plane | Warm SSO without edge re-auth after ACL change; separate IdP session vs network-session TTL mismatch | F4 |
| directory_federation | WAN LDAP bind latency; directory timeout aligned with site link loss; not explained by gateway 4xx alone | I1 |
| multi_site_affinity | Post-failover landing on cold site; SSO cookie present but app session empty | I2 |
| cluster_state | Divergent auth outcomes across IdP cluster nodes; cache/coherence alarms | I3 |
| protocol_gateway | Gateway 413/414 or buffer-limit rejection on ACS/SAML POST; size-class checker (`harness/fixtures/i4/`) | I4 |
| mfa_delivery | OTP verifier failures with successful password auth; SMS/PSTN delivery gaps | I5 |
| dual_idp_boundary | Same directory, divergent claim encodings across co-deployed IdPs; iss/aud stable but authZ fails | I6 |
| outside_taxonomy | Symptom-only or adjacent surface (clock/JWKS, DNS, ITP, PKCE) with no inclusion rule primary | S1–S4 |

## Suggested counters (deployment-local)

- Stage-localized authentication counters (IdP auth OK → edge callback → network grant).
- Gateway rejection codes with payload-size class (not raw payloads).
- Category-stamped triage counters when operators apply Table IV manually.

Thresholds are **deployment-specific**; the artifact does not prescribe universal alert values.
