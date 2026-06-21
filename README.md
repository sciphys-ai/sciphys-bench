# SciPhys Bench

Open benchmarks for experimental materials and physics analysis.

SciPhys Bench exists to make AI-for-science claims measurable. The first focus
is XRD phase identification, where benchmark cases should test evidence quality,
not just whether the top label looks plausible.

## Benchmark Philosophy

Benchmarks should evaluate:

- parser compatibility with real instrument files;
- phase top-1 and top-3 accuracy;
- matched and unmatched peak evidence;
- false impurity detection;
- substrate and artifact handling;
- refinement diagnostics such as Rwp, GOF, and residual structure;
- whether expert feedback can be converted into reusable labels.

## Current Tracks

- `benchmarks/xrd/`: XRD phase identification, impurity detection, and parser coverage.
- `benchmark-card.md`: standard metadata template for new benchmark cases.

## What Makes a Good Case

A good benchmark case has:

- clear scientific purpose;
- public, synthetic, or approved data;
- expected labels and known artifacts;
- enough metadata to reproduce the result;
- no private sample, operator, institution, or project identifiers.

## Related Repositories

- [sciphys-os](https://github.com/sciphys-ai/sciphys-os): parser and algorithm implementation.
- [sciphys-formats](https://github.com/sciphys-ai/sciphys-formats): schemas for benchmark metadata.
- [sciphys-recipes](https://github.com/sciphys-ai/sciphys-recipes): reproducible workflows.

## License

Apache-2.0.
