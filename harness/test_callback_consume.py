#!/usr/bin/env python3
"""Unit tests for the F3/F5 callback-consume demo (unittest, stdlib)."""
from __future__ import annotations

import unittest

from callback_consume import (
    AtomicCallbackStore,
    NaiveCallbackStore,
    concurrent_consume,
    replay_after_one,
)


class NaiveConcurrentTests(unittest.TestCase):
    def test_naive_concurrent_false_reject(self) -> None:
        r = concurrent_consume("naive", workers=12)
        self.assertGreaterEqual(r.successes, 1)
        self.assertGreater(r.observed_present, r.successes)
        self.assertTrue(r.as_dict("concurrent")["f3_false_reject_risk"])

    def test_naive_replay_after_clean_consume_usually_safe(self) -> None:
        store = NaiveCallbackStore()
        store.put("n", "p")
        self.assertEqual(store.consume("n"), "p")
        self.assertIsNone(store.consume("n"))


class PresenceOnlyTests(unittest.TestCase):
    def test_replay_after_one_accepted(self) -> None:
        r = replay_after_one("presence_only")
        d = r.as_dict("replay")
        self.assertTrue(r.replay_accepted)
        self.assertTrue(d["f5_replay_risk"])
        self.assertFalse(d["f3_false_reject_risk"])

    def test_concurrent_observes_multiple_present(self) -> None:
        r = concurrent_consume("presence_only", workers=12)
        self.assertGreaterEqual(r.successes, 1)
        self.assertGreaterEqual(r.observed_present, r.successes)


class AtomicTests(unittest.TestCase):
    def test_replay_rejected(self) -> None:
        r = replay_after_one("atomic")
        self.assertEqual(r.successes, 1)
        self.assertFalse(r.replay_accepted)

    def test_concurrent_single_winner(self) -> None:
        r = concurrent_consume("atomic", workers=12)
        self.assertEqual(r.successes, 1)
        self.assertEqual(r.misses, 11)
        self.assertFalse(r.replay_accepted)
        self.assertFalse(r.leftover)

    def test_atomic_pop_is_getdel(self) -> None:
        store = AtomicCallbackStore()
        store.put("n", "p")
        self.assertEqual(store.consume("n"), "p")
        self.assertIsNone(store.consume("n"))


if __name__ == "__main__":
    unittest.main()
