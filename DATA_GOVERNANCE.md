# Benchmark data governance

Benchmark defensibility depends on independent, lawful, well-characterized data.

Public releases require explicit redistribution rights, immutable hashes, provenance, dataset card, privacy review, sample and artifact coverage, label protocol, and known limitations. A citation is not redistribution permission.

Hidden holdouts are never stored in the public repository. A named steward controls access, records every evaluation, prevents training-set reuse, rotates compromised cases, and publishes aggregate composition and scoring rules. Sponsors and maintainers disclose conflicts of interest.

Real scientific labels should be independently reviewed by at least two qualified experts. Disagreement is retained and adjudication is documented; ambiguous cases may use set-valued labels or be excluded from metrics that assume unique ground truth.

Synthetic data is valuable for regression, coverage, and stress tests. It must declare the generator and any shared code, models, or reference libraries with the evaluated system. It cannot substantiate real-world accuracy by itself.
