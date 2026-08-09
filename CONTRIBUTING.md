# Contributing to SciPhys Bench

Start with one well-documented scientific failure mode, not a large unlabeled upload. Submit a benchmark card and manifest before adding data.

Required: clear task, lawful provenance, license, privacy review, immutable hashes, acquisition metadata, ground-truth protocol, artifact/subgroup tags, metrics, baselines, limitations, and expert conflicts. Do not submit unpublished lab data without explicit authority.

Run `python -m pip install -r requirements-dev.txt` and then
`python scripts/validate.py`. CI checks repository structure and full JSON
Schema conformance; maintainers and domain reviewers separately assess data
rights, leakage, label validity, and scientific relevance.
