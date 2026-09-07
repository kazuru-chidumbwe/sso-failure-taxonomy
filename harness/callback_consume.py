#!/usr/bin/env python3
"""Illustrate F3/F5 edge callback-consume race: naive check-then-delete vs atomic consume.

Stdlib only. Not a production IdP. Synthetic callback capabilities; no estate data.
Maps to manuscript edge_callback_consume incidents F3 (false reject) and F5 (replay).

Exact modeled schedules: harness/SCHEDULES.md
  Schedule A (presence_only): presence without consume → second path accepts.
  Schedule B (naive): check, release, delay, pop → loser false-rejects after seeing present.
  Schedule C (atomic): single-winner pop under one lock.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import threading
import time
from dataclasses import dataclass, field
from typing import Literal

Mode = Literal["naive", "presence_only", "atomic"]


class NaiveCallbackStore:
    """Schedule B: check-then-delete with gap. Concurrent losers false-reject (F3)."""

    def __init__(self) -> None:
        self._data: dict[str, str] = {}
        self._lock = threading.Lock()
        self.observed_present = 0

    def put(self, capability: str, payload: str) -> None:
        with self._lock:
            self._data[capability] = payload

    def consume(self, capability: str) -> str | None:
        with self._lock:
            present = capability in self._data
            if present:
                self.observed_present += 1
        time.sleep(0.004)
        if not present:
            return None
        with self._lock:
            return self._data.pop(capability, None)


class PresenceOnlyCallbackStore:
    """Schedule A: presence treated as sufficient; never consumes. Second path accepts (F5)."""

    def __init__(self) -> None:
        self._data: dict[str, str] = {}
        self._lock = threading.Lock()
        self.observed_present = 0

    def put(self, capability: str, payload: str) -> None:
        with self._lock:
            self._data[capability] = payload

    def consume(self, capability: str) -> str | None:
        with self._lock:
            if capability in self._data:
                self.observed_present += 1
            return self._data.get(capability)


class AtomicCallbackStore:
    """Schedule C: single-lock pop. One winner; replay misses."""

    def __init__(self) -> None:
        self._data: dict[str, str] = {}
        self._lock = threading.Lock()
        self.observed_present = 0

    def put(self, capability: str, payload: str) -> None:
        with self._lock:
            self._data[capability] = payload

    def consume(self, capability: str) -> str | None:
        with self._lock:
            if capability in self._data:
                self.observed_present += 1
            return self._data.pop(capability, None)


@dataclass
class RunResult:
    mode: Mode
    successes: int = 0
    misses: int = 0
    observed_present: int = 0
    winners: list[str] = field(default_factory=list)
    leftover: bool = False
    replay_accepted: bool = False

    def as_dict(self, scenario: str = "concurrent") -> dict:
        f3 = scenario == "concurrent" and self.observed_present > self.successes
        return {
            "mode": self.mode,
            "successes": self.successes,
            "misses": self.misses,
            "observed_present": self.observed_present,
            "winners": self.winners,
            "leftover": self.leftover,
            "replay_accepted": self.replay_accepted,
            "f3_false_reject_risk": f3,
            "f5_replay_risk": self.replay_accepted,
        }


def _store(mode: Mode) -> NaiveCallbackStore | PresenceOnlyCallbackStore | AtomicCallbackStore:
    if mode == "naive":
        return NaiveCallbackStore()
    if mode == "presence_only":
        return PresenceOnlyCallbackStore()
    return AtomicCallbackStore()


def concurrent_consume(mode: Mode, workers: int = 8) -> RunResult:
    store = _store(mode)
    capability = hashlib.sha256(secrets.token_bytes(16)).hexdigest()
    store.put(capability, "auth-code-placeholder")
    barrier = threading.Barrier(workers)
    got: list[str | None] = []
    lock = threading.Lock()

    def worker(name: str) -> None:
        barrier.wait()
        val = store.consume(capability)
        with lock:
            got.append(val)

    threads = [threading.Thread(target=worker, args=(f"cb-{i}",)) for i in range(workers)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    successes = [v for v in got if v is not None]
    leftover = capability in store._data  # noqa: SLF001 — demo introspection
    observed = store.observed_present
    replay = store.consume(capability) is not None
    return RunResult(
        mode=mode,
        successes=len(successes),
        misses=len(got) - len(successes),
        observed_present=observed,
        winners=[f"callback-{i}" for i, v in enumerate(got) if v is not None],
        leftover=leftover,
        replay_accepted=replay,
    )


def replay_after_one(mode: Mode) -> RunResult:
    """One legitimate consume, then attacker replays the same state."""
    store = _store(mode)
    capability = "state-" + secrets.token_hex(8)
    store.put(capability, "legit")
    first = store.consume(capability)
    second = store.consume(capability)
    return RunResult(
        mode=mode,
        successes=1 if first else 0,
        misses=0 if second is None else 1,
        observed_present=store.observed_present,
        winners=["legit"] if first else [],
        leftover=False,
        replay_accepted=second is not None,
    )


def main() -> int:
    p = argparse.ArgumentParser(description="F3/F5 callback-consume demo (stdlib)")
    p.add_argument("scenario", choices=["concurrent", "replay", "both"])
    p.add_argument("--mode", choices=["naive", "presence_only", "atomic", "both"], default="both")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.workers < 2:
        p.error("--workers must be >= 2")

    modes: list[Mode]
    if args.mode == "both":
        modes = ["naive", "presence_only", "atomic"]
    else:
        modes = [args.mode]  # type: ignore[list-item]

    out = []
    for mode in modes:
        if args.scenario in ("concurrent", "both"):
            out.append(("concurrent", concurrent_consume(mode, args.workers)))
        if args.scenario in ("replay", "both"):
            out.append(("replay", replay_after_one(mode)))

    if args.json:
        print(json.dumps([{"scenario": s, **r.as_dict(s)} for s, r in out], indent=2))
        return 0

    for scenario, r in out:
        d = r.as_dict(scenario)
        print(f"{scenario:11} mode={d['mode']:8}  ok={d['successes']}  miss={d['misses']}  "
              f"saw={d['observed_present']}  replay={d['replay_accepted']}  "
              f"F3={d['f3_false_reject_risk']}  F5={d['f5_replay_risk']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
