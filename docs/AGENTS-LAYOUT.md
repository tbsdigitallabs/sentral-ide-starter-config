# Agents layout (`.agents/`)

Project config for editors that load **skills**, **workflows**, and team docs from a `.agents/` directory.

## Where files go

| Asset | Path |
|-------|------|
| Agent team doc | `.agents/agents.md` |
| Project skills | `.agents/skills/<id>/SKILL.md` |
| Workflows (slash commands) | `.agents/workflows/*.md` |
| Shared architecture | `AGENTS.md` |

Skills are discovered lazily from the `description` field in each `SKILL.md` frontmatter.

## After scaffold

1. Open the project folder in your editor
2. Run `/skills` if your editor supports it — workspace skills should list `.agents/skills/`
3. Run `/onboard` — starter workflow walks first-time setup
4. Confirm `AGENTS.md` matches your stack

## Global skills (optional)

Some editors read shared skill folders outside the repo (e.g. under `~/.gemini/skills/`). Use your editor's `/skills` output to confirm paths.

Keep project-specific skills in `.agents/skills/` inside the repo so they travel with the codebase.

## MCP

MCP setup is editor-specific and separate from the rules layout's `.cursor/mcp.json`. Configure MCP in your editor's settings or shared config directory per its documentation.

## Workflows

Starter workflow `onboard` lives at `.agents/workflows/onboard.md`. Add more for your delivery process:

- `/spec` — brainstorm + write design doc
- `/ship` — test + lint + checklist

## Re-scaffold safely

Back up `.agents/` customisations before re-running scaffold. Use `--dry-run` to preview.

```bash
python -m scaffold --brief brief.yaml --target . --dry-run
```
