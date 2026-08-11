.PHONY: smoke test

PYTHON ?= python3

smoke test:
	$(PYTHON) -m unittest discover -s harness -v
