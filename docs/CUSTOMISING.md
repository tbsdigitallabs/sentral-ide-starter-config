# Customising the starter

## Add a profile

1. Copy `profiles/web-app.yaml` → `profiles/my-profile.yaml`
2. Adjust default stack, skills, rules, commands
3. Set `project.profile: my-profile` in client `brief.yaml`

Profiles merge under the brief — brief values win.

## Add a skill

1. Create `templates/shared/skills/<skill-id>/SKILL.md`
2. Use YAML frontmatter with `name` and a precise `description` (trigger phrase)
3. Add `<skill-id>` to `ide.skills` in brief or profile

Skills copy to both layout directories when both targets are selected.

## Add a rule file (rules layout only)

1. Create `templates/rules-layout/rules/<rule-id>.mdc.j2` (Jinja2 template)
2. Add `<rule-id>` to `ide.rules` in brief or profile

Available template variables: `project_name`, `stack`, `commands`, `team`, `language`, `framework`, etc. See `scaffold/engine.py` → `build_context`.

## Add an MCP server

1. Add entry to `MCP_CATALOG` in `scaffold/engine.py`
2. Add server id to `ide.mcp` in brief

## Layout targets

| Brief value | Output |
|-------------|--------|
| `rules` | `.cursor/rules/`, `.cursor/skills/`, `.cursor/mcp.json` |
| `agents` | `.agents/agents.md`, `.agents/skills/`, workflows |

Legacy aliases `cursor` and `antigravity` map to `rules` and `agents`.

## White-label for your consultancy

Fork the repo and replace:

- README intro paragraph
- Checklist links (optional)
- Default profile stacks to match your typical client stack

Keep skill content vendor-neutral unless a client needs specifics.

## Test changes

```bash
pip install -e ".[dev]"
pytest
python -m scaffold --brief brief.example.yaml --target .scaffold-test
```

Inspect `.scaffold-test/` before deleting.
