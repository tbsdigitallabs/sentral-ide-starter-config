"""Normalize IDE target names from brief YAML."""

from __future__ import annotations

# Brief target id -> internal layout key
TARGET_ALIASES: dict[str, str] = {
    "cursor": "rules",
    "antigravity": "agents",
    "rules": "rules",
    "agents": "agents",
}


def normalize_targets(raw_targets: list[str] | None) -> list[str]:
    if not raw_targets:
        return ["rules"]
    normalized: list[str] = []
    for target in raw_targets:
        key = TARGET_ALIASES.get(str(target).strip().lower())
        if key is None:
            raise ValueError(
                f"Unknown ide.targets entry '{target}'. "
                f"Use: {', '.join(sorted({'rules', 'agents', *TARGET_ALIASES}))}"
            )
        if key not in normalized:
            normalized.append(key)
    return normalized
