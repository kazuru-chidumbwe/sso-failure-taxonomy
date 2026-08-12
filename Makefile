.PHONY: smoke test

PYTHON ?= python3

smoke test:
	$(PYTHON) -m unittest discover -s harness -v
	$(PYTHON) -m unittest discover -s harness/fixtures/i4 -v
	$(PYTHON) harness/fixtures/i4/check_sizes.py --limit 16384
