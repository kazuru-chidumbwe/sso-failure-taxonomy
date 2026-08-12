#!/usr/bin/env python3
"""Unit checks for I4 synthetic fixtures."""

from __future__ import annotations

import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "saml_post_body_8kib.txt": 8 * 1024,
    "saml_post_body_16kib.txt": 16 * 1024,
    "saml_post_body_32kib.txt": 32 * 1024,
    "saml_post_body_64kib.txt": 64 * 1024,
}


class TestI4Fixtures(unittest.TestCase):
    def test_sizes(self) -> None:
        for name, n in EXPECTED.items():
            path = HERE / name
            self.assertTrue(path.is_file(), name)
            self.assertEqual(path.stat().st_size, n, name)
            data = path.read_bytes()
            self.assertTrue(data.startswith(b"SAMLResponse="), name)

    def test_trace_is_synthetic(self) -> None:
        text = (HERE / "example_gateway_reject_trace.txt").read_text(encoding="utf-8")
        self.assertIn("synthetic", text.lower())
        self.assertIn("NOT a production log", text)


if __name__ == "__main__":
    unittest.main()
