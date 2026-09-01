# Modeled schedules (F3 / F5)

This file states the **exact harness assumptions**. Outcomes are properties of these schedules, not of every check-then-delete implementation in the wild.

Threat model (narrow): the harness models an edge callback capability that an attacker or concurrent client can present more than once within its validity window. It does **not** model authorization-server compromise, authorization-code or access-token theft, browser isolation failure, or cryptographic failure of OAuth/OIDC artifacts.

## Schedule A — double acceptance (`jwt_only`, F5)

**Implementation assumption:** existence (or unexpired JWT-style presence) is treated as sufficient; the store never deletes / consumes the value; a failed or missing delete is not used to reject the second path.

**Interleaving:**

1. Path P1 checks that the callback capability is present → accepts.
2. Path P2 presents the same capability → still present → accepts.

**Observable in harness:** `mode=jwt_only`, `replay_accepted=true` (sequential `replay` scenario and leftover presence under concurrency).

## Schedule B — false reject of a legitimate path (`naive`, F3)

**Implementation assumption:** check-then-delete with a gap: existence is observed under a lock, the lock is released, an artificial delay models other work, then a separate delete/pop runs. A path that saw “present” but loses the race to `pop` returns failure.

**Interleaving:**

1. Path P1 and path P2 both observe that the capability is present.
2. Path P1 deletes/pops the value and accepts.
3. Path P2’s later pop finds nothing → rejects, even though P2 had a legitimate concurrent callback that already passed the existence check.

**Observable in harness:** `mode=naive`, concurrent workers, `observed_present > successes` → `f3_false_reject_risk=true`.

## Schedule C — single winner (`atomic`)

**Implementation assumption:** get-and-delete under one lock (single-winner pop) at the callback-consistency scope of this single-process store.

**Interleaving:** concurrent paths contend on one atomic pop; at most one returns the payload; subsequent presentations miss.

**Observable in harness:** `mode=atomic`, one concurrent success; sequential replay rejected.

## Non-claims

- Not a model of clustered replication, multi-primary writes, or failover.
- “One step” without atomic single-winner semantics at the relevant consistency scope is insufficient; the atomic schedule requires atomic get-and-delete at the callback-consistency scope.
- TTL expiry / TTL mismatch relative to callback RTT is in the category definition; this harness focuses on consume interleaving, not a full TTL simulator.

## Production extension (not modelled)

Extending single-winner consume across a replicated store requires a primitive that is linearizable at the callback-consistency scope: compare-and-swap on a versioned key, a fencing token carried into the release action, or a lease-based single-writer partition for the callback keyspace. Under partition or failover, where the consume outcome cannot be determined, the endpoint fails closed and rejects the callback.
