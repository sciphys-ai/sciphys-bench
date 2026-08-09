#!/usr/bin/env python3
"""Score a SciPhys benchmark submission from per-case audit records."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def ratio(count: int, total: int) -> float:
    return count / total if total else 0.0


def validate_case(case: object, index: int) -> list[str]:
    if not isinstance(case, dict):
        return [f"cases[{index}] must be an object"]
    errors: list[str] = []
    required = {"id", "taskCorrect", "reproducible", "evidenceCoverage", "unsupportedClaims", "expertDecision", "abstained", "cost"}
    missing = required - set(case)
    if missing:
        errors.append(f"cases[{index}] missing {sorted(missing)}")
    coverage = case.get("evidenceCoverage")
    if not isinstance(coverage, (int, float)) or isinstance(coverage, bool) or not 0 <= coverage <= 1:
        errors.append(f"cases[{index}].evidenceCoverage must be between 0 and 1")
    unsupported = case.get("unsupportedClaims")
    if not isinstance(unsupported, dict) or any(not isinstance(unsupported.get(level), int) or unsupported[level] < 0 for level in ("critical", "major", "minor")):
        errors.append(f"cases[{index}].unsupportedClaims must contain non-negative integer severity counts")
    if case.get("expertDecision") not in {"accept", "revise", "reject", "not-reviewed"}:
        errors.append(f"cases[{index}].expertDecision is invalid")
    for field in ("taskCorrect", "reproducible", "abstained"):
        if not isinstance(case.get(field), bool):
            errors.append(f"cases[{index}].{field} must be boolean")
    cost = case.get("cost")
    if not isinstance(cost, dict) or not isinstance(cost.get("latencySeconds"), (int, float)) or cost["latencySeconds"] < 0 or not isinstance(cost.get("toolCalls"), int) or cost["toolCalls"] < 0:
        errors.append(f"cases[{index}].cost needs non-negative latencySeconds and toolCalls")
    return errors


def score(submission: dict) -> dict:
    if submission.get("schemaVersion") != "sciphys.benchmark-submission.v0.1":
        raise ValueError("unsupported or missing schemaVersion")
    cases = submission.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("submission needs at least one case")
    errors = [error for index, case in enumerate(cases) for error in validate_case(case, index)]
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if len(set(ids)) != len(ids):
        errors.append("case ids must be unique")
    if errors:
        raise ValueError("; ".join(errors))

    total = len(cases)
    verified = [
        case for case in cases
        if case["taskCorrect"]
        and case["reproducible"]
        and math.isclose(case["evidenceCoverage"], 1.0)
        and case["unsupportedClaims"]["critical"] == 0
        and case["unsupportedClaims"]["major"] == 0
        and case["expertDecision"] == "accept"
        and not case["abstained"]
    ]
    severity_totals = {
        level: sum(case["unsupportedClaims"][level] for case in cases)
        for level in ("critical", "major", "minor")
    }
    return {
        "schemaVersion": "sciphys.benchmark-score.v0.1",
        "benchmark": submission.get("benchmark"),
        "system": submission.get("system"),
        "caseCount": total,
        "verifiedCaseCount": len(verified),
        "verifiedWorkflowCompletionRate": ratio(len(verified), total),
        "taskCorrectRate": ratio(sum(case["taskCorrect"] for case in cases), total),
        "reproducibleRate": ratio(sum(case["reproducible"] for case in cases), total),
        "meanEvidenceCoverage": sum(case["evidenceCoverage"] for case in cases) / total,
        "expertAcceptanceRate": ratio(sum(case["expertDecision"] == "accept" for case in cases), total),
        "abstentionRate": ratio(sum(case["abstained"] for case in cases), total),
        "unsupportedClaims": severity_totals,
        "cost": {
            "meanLatencySeconds": sum(case["cost"]["latencySeconds"] for case in cases) / total,
            "meanToolCalls": sum(case["cost"]["toolCalls"] for case in cases) / total,
            "totalInputTokens": sum(case["cost"].get("inputTokens", 0) for case in cases),
            "totalOutputTokens": sum(case["cost"].get("outputTokens", 0) for case in cases),
            "estimatedUsd": sum(case["cost"].get("estimatedUsd", 0) for case in cases),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path)
    parser.add_argument("--expect-vwcr", type=float)
    args = parser.parse_args()
    try:
        submission = json.loads(args.submission.read_text(encoding="utf-8"))
        report = score(submission)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(json.dumps({"valid": False, "error": str(error)}, indent=2))
        return 1
    print(json.dumps(report, indent=2))
    if args.expect_vwcr is not None and not math.isclose(report["verifiedWorkflowCompletionRate"], args.expect_vwcr):
        print(f"Expected VWCR {args.expect_vwcr}, got {report['verifiedWorkflowCompletionRate']}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
