#!/usr/bin/env python3
"""Regression checks for the reference benchmark scorer."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from score import score


ROOT = Path(__file__).resolve().parents[1]
submission = json.loads((ROOT / "examples" / "xrd-synthetic-submission.v0.1.json").read_text(encoding="utf-8"))
report = score(submission)
assert report["verifiedWorkflowCompletionRate"] == 0.5
assert report["meanEvidenceCoverage"] == 0.875
assert report["unsupportedClaims"] == {"critical": 0, "major": 1, "minor": 0}

invalid = copy.deepcopy(submission)
invalid["cases"][1]["id"] = invalid["cases"][0]["id"]
invalid["cases"][1]["evidenceCoverage"] = 2
try:
    score(invalid)
except ValueError as error:
    assert "case ids must be unique" in str(error)
    assert "evidenceCoverage" in str(error)
else:
    raise AssertionError("Invalid submission was accepted")

print("Benchmark scorer regression suite: 2/2 passed")
