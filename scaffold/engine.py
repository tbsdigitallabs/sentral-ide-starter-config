"""Render templates into a target project directory."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from scaffold.targets import normalize_targets

MCP_CATALOG: dict[str, dict[str, Any]] = {
    "context7": {
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp@latest"],
    },
    "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"},
    },
    "memory": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"],
    },
    "brave-search": {
        "command": "npx",
        "args": ["-y", "@brave/brave-search-mcp-server"],
        "env": {"BRAVE_API_KEY": "${BRAVE_API_KEY}"},
    },
}


def _jinja_env(template_root: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_root)),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
    )


def _render_text(env: Environment, template_name: str, context: dict[str, Any]) -> str:
    return env.get_template(template_name).render(**context)


def _write(path: Path, content: str, *, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _copy_tree(src: Path, dst: Path, *, dry_run: bool) -> None:
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def build_context(brief: dict[str, Any]) -> dict[str, Any]:
    project = brief.get("project", {})
    stack = brief.get("stack", {})
    team = brief.get("team", {})
    ide = brief.get("ide", {})
    commands = brief.get("commands", {})
    team.setdefault("conventions", {})
    team["conventions"].setdefault("commit_style", "[scope] short description")
    team["conventions"].setdefault("pr_max_loc", 400)

    return {
        "project_name": project.get("name", "my-project"),
        "project_description": project.get("description", ""),
        "profile": project.get("profile", "web-app"),
        "stack": stack,
        "team": team,
        "ide": ide,
        "commands": commands,
        "notes": brief.get("notes", "").strip(),
        "language": stack.get("language", "TypeScript"),
        "framework": stack.get("framework", "Next.js"),
        "backend": stack.get("backend", "none"),
        "deploy": stack.get("deploy", "Vercel"),
        "testing": stack.get("testing", "Vitest"),
    }


def scaffold_project(
    *,
    brief: dict[str, Any],
    target: Path,
    repo_root: Path,
    dry_run: bool = False,
) -> list[str]:
    created: list[str] = []
    context = build_context(brief)
    ide = brief.get("ide", {})
    targets = normalize_targets(ide.get("targets"))
    context["ide"] = {**ide, "targets": targets}
    template_root = repo_root / "templates"
    env = _jinja_env(template_root)

    # Shared docs
    agents_md = _render_text(env, "shared/AGENTS.md.j2", context)
    agents_path = target / "AGENTS.md"
    _write(agents_path, agents_md, dry_run=dry_run)
    created.append(str(agents_path.relative_to(target)))

    checklist = _render_text(env, "shared/SETUP-CHECKLIST.md.j2", context)
    checklist_path = target / "docs" / "AI-IDE-SETUP-CHECKLIST.md"
    _write(checklist_path, checklist, dry_run=dry_run)
    created.append(str(checklist_path.relative_to(target)))

    if "rules" in targets:
        created.extend(_scaffold_rules_layout(target, repo_root, env, context, ide, dry_run))

    if "agents" in targets:
        created.extend(_scaffold_agents_layout(target, repo_root, context, ide, dry_run))

    return created


def _scaffold_rules_layout(
    target: Path,
    repo_root: Path,
    env: Environment,
    context: dict[str, Any],
    ide: dict[str, Any],
    dry_run: bool,
) -> list[str]:
    created: list[str] = []
    rules_dir = target / ".cursor" / "rules"
    skills_dir = target / ".cursor" / "skills"

    for rule_name in ide.get("rules", []):
        template = f"rules-layout/rules/{rule_name}.mdc.j2"
        output = rules_dir / f"{rule_name}.mdc"
        content = _render_text(env, template, context)
        _write(output, content, dry_run=dry_run)
        created.append(str(output.relative_to(target)))

    for skill_name in ide.get("skills", []):
        src = repo_root / "templates" / "shared" / "skills" / skill_name
        dst = skills_dir / skill_name
        if src.exists():
            _copy_tree(src, dst, dry_run=dry_run)
            created.append(str(dst.relative_to(target)))

    mcp_names = ide.get("mcp", [])
    if mcp_names:
        servers = {name: MCP_CATALOG[name] for name in mcp_names if name in MCP_CATALOG}
        mcp_path = target / ".cursor" / "mcp.json"
        _write(mcp_path, json.dumps({"mcpServers": servers}, indent=2) + "\n", dry_run=dry_run)
        created.append(str(mcp_path.relative_to(target)))

    sandbox_src = repo_root / "templates" / "rules-layout" / "sandbox.json"
    sandbox_dst = target / ".cursor" / "sandbox.json"
    if sandbox_src.exists():
        if not dry_run:
            sandbox_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sandbox_src, sandbox_dst)
        created.append(str(sandbox_dst.relative_to(target)))

    return created


def _scaffold_agents_layout(
    target: Path,
    repo_root: Path,
    context: dict[str, Any],
    ide: dict[str, Any],
    dry_run: bool,
) -> list[str]:
    created: list[str] = []
    agents_dir = target / ".agents"
    skills_dir = agents_dir / "skills"

    env = _jinja_env(repo_root / "templates")
    agents_md = _render_text(env, "agents-layout/agents.md.j2", context)
    agents_path = agents_dir / "agents.md"
    _write(agents_path, agents_md, dry_run=dry_run)
    created.append(str(agents_path.relative_to(target)))

    for skill_name in ide.get("skills", []):
        src = repo_root / "templates" / "shared" / "skills" / skill_name
        dst = skills_dir / skill_name
        if src.exists():
            _copy_tree(src, dst, dry_run=dry_run)
            created.append(str(dst.relative_to(target)))

    workflows_src = repo_root / "templates" / "agents-layout" / "workflows"
    workflows_dst = agents_dir / "workflows"
    if workflows_src.exists():
        _copy_tree(workflows_src, workflows_dst, dry_run=dry_run)
        created.append(str(workflows_dst.relative_to(target)))

    return created
