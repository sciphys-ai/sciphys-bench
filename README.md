# SciPhys Bench

[![Validate benchmark contracts](https://github.com/sciphys-ai/sciphys-bench/actions/workflows/validate.yml/badge.svg)](https://github.com/sciphys-ai/sciphys-bench/actions/workflows/validate.yml)

Open evaluation protocols for trustworthy agents and tools in experimental science.

SciPhys Bench measures the complete path from instrument bytes to scientific claims. It is deliberately broader than XRD and stricter than a leaderboard built from self-generated fixtures.

## What is evaluated

| Level | Target | Representative checks |
|---|---|---|
| B0 | Contract conformance | schemas, licenses, hashes, required artifacts |
| B1 | Format handling | parser success, metadata and unit fidelity, rejection behavior |
| B2 | Scientific primitives | numerical error, uncertainty calibration, artifact handling |
| B3 | Technique analysis | labels, estimates, alternatives, false discoveries |
| B4 | Agent behavior | tool choice, parameter use, abstention, traceability |
| B5 | End-to-end workflow | evidence coverage, reproducibility, figure and report integrity |
| B6 | Expert validity | blinded acceptance, severity-weighted unsupported claims |

Tracks can cover spectra, time series, images, volumes, structures, or tabular measurements. The first design track is [XRD](benchmarks/xrd/README.md); proposed Raman and electrochemistry tracks should reuse the same manifest and evidence contracts.

## Dataset partitions

- `synthetic-regression`: public generated cases for deterministic code regressions; never an external accuracy benchmark.
- `public-dev`: licensed real or synthetic cases with visible labels for method development.
- `public-test`: frozen, versioned cases with visible scoring and reproducible baselines.
- `challenge`: time-bounded blind tasks whose labels are released after closure.
- `hidden-holdout`: governed cases used to test generalization; never committed to this repository.

Every released snapshot has a manifest, dataset card, immutable hashes, data license, expert-label protocol, artifact/subgroup tags, scoring version, and DOI when mature. See [DATA_GOVERNANCE.md](DATA_GOVERNANCE.md).

## Repository contents

- [`schemas/benchmark-manifest.v0.1.schema.json`](schemas/benchmark-manifest.v0.1.schema.json): benchmark snapshot contract.
- [`manifests/xrd-synthetic-regression.v0.1.json`](manifests/xrd-synthetic-regression.v0.1.json): honest metadata for the current self-generated XRD regression suite.
- [`benchmark-card.md`](benchmark-card.md): proposal template for a new track or snapshot.
- [`SCORING.md`](SCORING.md): reporting and comparison requirements.
- [`scripts/validate.py`](scripts/validate.py): dependency-free repository conformance check.

## A score is not enough

Submissions report task metrics, 95% uncertainty intervals, repeated-run variance for agents, time/token/tool cost, failure and abstention rates, subgroup performance, evidence coverage, and a signed result artifact. Model, prompt/Skill version, tool versions, environment, and data snapshot must be pinned.

The north-star metric is **Verified Workflow Completion Rate**: the fraction of cases that are correct, reproducible, evidence-covered, free of disallowed unsupported claims, and accepted by the declared review protocol.

## Related repositories

- [sciphys-os](https://github.com/sciphys-ai/sciphys-os): runtime, tools, and Skills.
- [sciphys-formats](https://github.com/sciphys-ai/sciphys-formats): measurement and Evidence Bundle contracts.
- [sciphys-recipes](https://github.com/sciphys-ai/sciphys-recipes): reproducible workflow fixtures.

Benchmark code is Apache-2.0. Each dataset has its own declared license.
