from pathlib import Path

import yaml

from scaffold.brief import load_brief
from scaffold.engine import build_context, scaffold_project


def test_load_brief_merges_profile(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parent.parent
    brief_path = tmp_path / "brief.yaml"
    brief_path.write_text(
        yaml.dump(
            {
                "project": {"name": "Acme", "profile": "web-app"},
                "stack": {"framework": "Remix"},
            }
        ),
        encoding="utf-8",
    )
    loaded = load_brief(brief_path, repo_root)
    assert loaded["project"]["name"] == "Acme"
    assert loaded["stack"]["framework"] == "Remix"
    assert "using-skills" in loaded["ide"]["skills"]


def test_scaffold_creates_cursor_and_antigravity_files(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parent.parent
    brief = load_brief(repo_root / "brief.example.yaml", repo_root)
    target = tmp_path / "out"
    created = scaffold_project(brief=brief, target=target, repo_root=repo_root)
    joined = "\n".join(created)
    assert "AGENTS.md" in joined
    assert "bootstrap.mdc" in joined
    assert "agents.md" in joined
    assert (target / ".cursor" / "skills" / "using-skills" / "SKILL.md").exists()


def test_build_context_defaults() -> None:
    ctx = build_context({"project": {"name": "X"}, "stack": {}, "ide": {}, "commands": {}})
    assert ctx["project_name"] == "X"
    assert ctx["team"]["conventions"]["commit_style"]
