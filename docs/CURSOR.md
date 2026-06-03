# Cursor setup notes

## Where files go

| Asset | Path |
|-------|------|
| Rules (always/glob) | `.cursor/rules/*.mdc` |
| Project skills | `.cursor/skills/<id>/SKILL.md` |
| MCP servers | `.cursor/mcp.json` |
| Sandbox network policy | `.cursor/sandbox.json` |
| Architecture doc | `AGENTS.md` |

## After scaffold

1. Open the project folder in Cursor (not the starter repo unless testing)
2. Settings → Rules — confirm project rules appear
3. Settings → Tools & MCP — confirm servers from `mcp.json`; add env vars
4. New Agent chat → ask: "What rules and skills do you see?"

## MCP environment variables

| Server | Variable |
|--------|----------|
| github | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| brave-search | `BRAVE_API_KEY` |

Restart Cursor after changing MCP config or env vars.

## Recommended session habits

- Plan mode for non-trivial features
- `/clear` or new chat when switching tasks
- One primary skill per turn (see `skills-routing` rule)
- Run tests before calling work complete

## Global vs project skills

This starter scaffolds **project** skills in `.cursor/skills/`. For personal skills available everywhere, add folders under:

```
~/.cursor/skills/<skill-id>/SKILL.md
```

Do not write to `~/.cursor/skills-cursor/` — that is reserved for Cursor built-ins.

## Re-scaffold safely

The scaffold overwrites generated paths. Back up custom edits first, or maintain overrides in a separate brief and re-run:

```bash
python -m scaffold --brief brief.yaml --target . --dry-run
```
