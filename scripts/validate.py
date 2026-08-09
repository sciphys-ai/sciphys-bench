#!/usr/bin/env python3
"""Validate SciPhys benchmark manifests and documentation contracts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
required = {"schemaVersion", "id", "version", "title", "techniques", "partition", "tasks", "metrics", "data", "review"}

for path in ROOT.rglob("*.json"):
    if ".git" in path.parts:
        continue
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        continue
    if path.parent.name == "manifests":
        missing = required - set(value)
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing {sorted(missing)}")
        if value.get("partition") == "synthetic-regression":
            data = value.get("data", {})
            if data.get("synthetic") is not True or not data.get("generator"):
                errors.append(f"{path.relative_to(ROOT)}: synthetic regression requires generator disclosure")
        if value.get("partition") != "synthetic-regression" and value.get("review", {}).get("expertCount", 0) < 2:
            errors.append(f"{path.relative_to(ROOT)}: real benchmark requires at least two experts")

for required_doc in ("benchmark-card.md", "SCORING.md", "DATA_GOVERNANCE.md"):
    if not (ROOT / required_doc).is_file():
        errors.append(f"missing {required_doc}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)
print("Benchmark contracts valid.")
