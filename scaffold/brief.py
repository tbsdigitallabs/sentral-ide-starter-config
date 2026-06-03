"""Load and merge project brief YAML."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(base)
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged


def load_brief(path: Path, repo_root: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"Brief must be a YAML mapping: {path}")

    profile_name = raw.get("project", {}).get("profile")
    if profile_name:
        profile_path = repo_root / "profiles" / f"{profile_name}.yaml"
        if profile_path.exists():
            profile = yaml.safe_load(profile_path.read_text(encoding="utf-8")) or {}
            if isinstance(profile, dict):
                raw = _deep_merge(profile, raw)

    project_name = raw.setdefault("project", {}).get("name", "my-project")
    if isinstance(project_name, str) and "{{PROJECT_NAME}}" in project_name:
        raw["project"]["name"] = "my-project"

    return raw
