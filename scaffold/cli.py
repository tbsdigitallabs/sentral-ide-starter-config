"""CLI for sentral-ide-starter-config."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from scaffold.brief import load_brief
from scaffold.engine import scaffold_project

app = typer.Typer(
    name="sentral-ide-scaffold",
    help="Scaffold agent IDE skills, rules, and docs from brief.yaml",
)
console = Console()


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


@app.command()
def run(
    brief: Path = typer.Option(..., "--brief", "-b", help="Path to brief.yaml"),
    target: Path = typer.Option(Path("."), "--target", "-t", help="Project directory to scaffold into"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be created without writing files"),
) -> None:
    """Generate IDE configuration from a project brief."""
    repo_root = _repo_root()
    brief = brief.resolve()
    target = target.resolve()

    if not brief.exists():
        raise typer.BadParameter(f"Brief not found: {brief}")

    target.mkdir(parents=True, exist_ok=True)
    loaded = load_brief(brief, repo_root)
    created = scaffold_project(
        brief=loaded,
        target=target,
        repo_root=repo_root,
        dry_run=dry_run,
    )

    project_name = loaded.get("project", {}).get("name", "project")
    targets = loaded.get("ide", {}).get("targets", [])

    table = Table(title=f"Scaffolded files for {project_name}")
    table.add_column("Path")
    for path in created:
        table.add_row(path)

    console.print(table)
    console.print(
        Panel(
            "\n".join(
                [
                    f"Target IDE(s): {', '.join(targets)}",
                    f"Output directory: {target}",
                    "",
                    "Next steps:",
                    "1. Open the target folder in your AI-native editor",
                    "2. Read docs/AI-IDE-SETUP-CHECKLIST.md",
                    "3. Fill in .agents/product-marketing-context.md or AGENTS.md stack details",
                    "4. Add MCP API keys to your environment (see checklist)",
                    "5. Run your first agent task with Plan mode, then implement",
                ]
            ),
            title="Setup complete" if not dry_run else "Dry run complete",
            border_style="green" if not dry_run else "yellow",
        )
    )


def main() -> None:
    app()


if __name__ == "__main__":
    main()
