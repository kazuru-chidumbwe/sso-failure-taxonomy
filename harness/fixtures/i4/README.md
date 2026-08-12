# I4 synthetic fixtures (`protocol_gateway` size class)

**Not estate evidence.** These objects are synthetic request-body size classes for discussing gateway request limits (manuscript I4 / Section VI-H). They contain **no** production SAML assertions, hostnames, cookies, or configuration fragments.

## Files

| File | Approx. body size | Intended class |
| --- | --- | --- |
| `saml_post_body_8kib.txt` | 8 KiB | Below common 16 KiB buffer defaults |
| `saml_post_body_16kib.txt` | 16 KiB | Near `tune.bufsize`-class default (HAProxy 3.2 documents 16384) |
| `saml_post_body_32kib.txt` | 32 KiB | Above 16 KiB default; should exercise limit/reject paths |
| `saml_post_body_64kib.txt` | 64 KiB | Large federation POST class |
| `example_gateway_reject_trace.txt` | — | Synthetic reject log line (not a real proxy log) |

Bodies are `SAMLResponse=` plus base64-alphabet filler (not a valid assertion).

## Checker

```bash
python3 harness/fixtures/i4/check_sizes.py
python3 harness/fixtures/i4/check_sizes.py --limit 16384
```

Exit code 0 prints a table of sizes vs a configured limit (default 16384). This is a **size-class helper**, not a claim that any specific proxy setting caused the architect-note case.
