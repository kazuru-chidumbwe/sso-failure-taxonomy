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

    def test_naive_concurrent_false_reject(self) -> None:
        r = concurrent_consume("naive", workers=12)
        self.assertGreaterEqual(r.successes, 1)
        self.assertGreater(r.observed_present, r.successes)
        self.assertTrue(r.as_dict()["f3_false_reject_risk"])


class NaiveTests(unittest.TestCase):
    def test_replay_after_clean_consume_usually_safe(self) -> None:
        store = NaiveCallbackStore()
        store.put("n", "p")
        self.assertEqual(store.consume("n"), "p")
        self.assertIsNone(store.consume("n"))

    def test_jwt_only_replay_accepted(self) -> None:
        r = replay_after_one("jwt_only")
        self.assertTrue(r.replay_accepted)

    def test_atomic_pop_is_getdel(self) -> None:
        store = AtomicCallbackStore()
        store.put("n", "p")
        self.assertEqual(store.consume("n"), "p")
        self.assertIsNone(store.consume("n"))


if __name__ == "__main__":
    unittest.main()
