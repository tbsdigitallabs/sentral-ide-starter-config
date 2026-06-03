# Antigravity setup notes

## Where files go

| Asset | Path |
|-------|------|
| Agent team doc | `.agents/agents.md` |
| Project skills | `.agents/skills/<id>/SKILL.md` |
| Workflows (slash commands) | `.agents/workflows/*.md` |
| Shared architecture | `AGENTS.md` |

Antigravity discovers skills lazily from the `description` field in each `SKILL.md` frontmatter.

## After scaffold

1. Open the project folder in Antigravity
2. Run `/skills` — workspace skills should list folders from `.agents/skills/`
3. Run `/onboard` — starter workflow walks first-time setup
4. Confirm `AGENTS.md` matches your stack

## Global skills (optional)

For skills shared across all projects on a machine, Antigravity also reads global locations under `~/.gemini/skills/` (exact layout can vary by Antigravity version — use `/skills` to confirm what your install sees).

Keep client-specific skills in `.agents/skills/` inside the repo so they travel with the project.

## MCP

Antigravity MCP config is separate from Cursor's `.cursor/mcp.json`. See [Google's MCP docs](https://codelabs.developers.google.com/) for your Antigravity version. Common pattern: shared config under `~/.gemini/config/mcp_config.json`.

This starter does not auto-write Antigravity global MCP config — only project-local agent files.

## Workflows

Starter workflow `onboard` lives at `.agents/workflows/onboard.md`. Add more workflows for your delivery process:

- `/spec` — brainstorm + write design doc
- `/ship` — test + lint + checklist

## Re-scaffold safely

Back up `.agents/` customizations before re-running scaffold. Use `--dry-run` to preview.

```bash
python -m scaffold --brief brief.yaml --target . --dry-run
```
