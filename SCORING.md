# Scoring and reporting

Every comparison must pin the dataset snapshot, scoring implementation, model, prompt or Skill revision, tools, runtime, and randomization settings.

Agent evaluations compare at least the same base model without SciPhys Skills and with the tested Skills. Report repeated runs and 95% intervals; do not select the best run. Include latency, token/tool cost, abstention, invalid-output rate, and evidence coverage alongside scientific metrics.

Technique tracks define their own metrics, but all end-to-end tracks report:

- task correctness and uncertainty;
- evidence coverage and dangling-reference rate;
- unsupported and contradicted claims by severity;
- reproducibility in a clean environment;
- required artifact completeness;
- expert acceptance with disagreement statistics;
- performance by declared artifact and sample subgroups.

Leaderboard entries must link to a machine-readable result bundle and code or a reproducible execution image. A single aggregate score may summarize a track, but cannot replace the component metrics.

The reference submission contract is `schemas/submission.v0.1.schema.json`. The
reference implementation in `scripts/score.py` computes Verified Workflow
Completion Rate only when a case is correct, reproducible, fully evidence
covered, free of critical/major unsupported claims, expert-accepted, and not an
abstention. Technique-specific metrics may be added alongside this invariant,
not substituted for it.
