# Rules layout (`.cursor/`)

Project config for editors that load **rules**, **skills**, and **MCP** from a `.cursor/` directory at the repo root.

## Where files go

| Asset | Path |
|-------|------|
| Rules (always/glob) | `.cursor/rules/*.mdc` |
| Project skills | `.cursor/skills/<id>/SKILL.md` |
| MCP servers | `.cursor/mcp.json` |
| Sandbox network policy | `.cursor/sandbox.json` |
| Architecture doc | `AGENTS.md` |

## After scaffold

1. Open the project folder in your editor (not the starter repo unless testing)
2. Confirm project rules and skills are detected (wording varies by editor)
3. Add MCP env vars in your editor or shell settings
4. New agent chat → ask: "What rules and skills do you see in this project?"

## MCP environment variables

| Server | Variable |
|--------|----------|
| github | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| brave-search | `BRAVE_API_KEY` |

Restart the editor after changing MCP config or env vars.

## Recommended session habits

- Plan before non-trivial features
- Start a fresh chat when switching unrelated tasks
- One primary skill per turn (see `skills-routing` rule)
- Run tests before calling work complete

## Global vs project skills

This starter scaffolds **project** skills in `.cursor/skills/`. Some editors also support personal skill folders outside the repo — check your editor docs for the global path.

## Re-scaffold safely

The scaffold overwrites generated paths. Back up custom edits first:

```bash
python -m scaffold --brief brief.yaml --target . --dry-run
```
