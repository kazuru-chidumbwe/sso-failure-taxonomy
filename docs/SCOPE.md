# Scope

## This artefact is

- A frozen codebook for a ten-category federated SSO classification instrument (inclusion, exclusion, tie-breakers, severity).
- Eleven fingerprint-safe incident summaries used as a demonstration of that scheme (`codebook/incidents.json` is the published catalog, including category, severity, and form).
- An **unblinded** independent-coding packet (`codebook/second-coder/PACKET.md`) with paraphrased cases and negative-evidence fields. Gold labels for the published catalog are in `incidents.json` (Table III). Send the packet standalone so coding is rule application, not transcription; do not claim blinding.
- A reliability summary (`codebook/reliability.json`) with raw agreement, Gwet’s AC1 (primary under severity skew), Cohen’s κ, and bootstrap CIs for that round.
- A standard-library callback-consume demonstration of the manuscript Fig. 3 claim (`harness/callback_consume.py`).
- An **evidence index** (`docs/EVIDENCE-INDEX.md`) mapping each Table III case to released material (honest when the entry is architect note only).
- An **open falsifiability path**: external fingerprint-safe incidents against Table I (`docs/EXTERNAL-INCIDENTS.md` + GitHub issue template). Outcomes are not claimed as manuscript evidence.

## This artefact is not

- A production IdP, portal, or estate config.
- A rate, a laboratory experiment on live IdPs, or statistical transfer across organizations.
- Independent taxonomy discovery. Second-coder agreement is label assignment given Table I.
- A hidden gold file. There is no separate public answer key that maps Case 01–11 to F/I ids. The catalog labels themselves are public because they are Table III. The Case→incident shuffle map stays author-only.
- Proof that the ten categories are complete. Completeness is not claimed; external submissions are the ongoing test.

## Fingerprint test

Procurement notices plus about ten minutes of search must not narrow the text to one organization. No geography, live hostnames, ticket IDs, or mail/collaboration product names.

## What stays out of a public tag

Programme notes (`upstream/`, gitignored). The Case→incident shuffle answer key lives only with the author, not in this tree.
