# Agent IDE Starter

Scaffold **Cursor** and **Google Antigravity** project configuration from a single brief file — rules, skills, MCP servers, and a human setup checklist.

Modeled on a production agent-IDE workflow (skills routing, bootstrap rules, verification gates) without vendor-specific branding.

## Who this is for

Clients or teams starting with an AI-native IDE who want:

- A repeatable project setup they can clone and run
- Agent **skills** that teach good habits (plan → implement → verify)
- **Rules** for stack-specific conventions
- Optional **MCP** integrations (GitHub, docs lookup, memory)
- Support for **both Cursor and Antigravity** from one brief

## Quick start

```bash
git clone https://github.com/SLAMx/agent-ide-starter.git
cd agent-ide-starter
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e .

# In YOUR project:
cp /path/to/agent-ide-starter/brief.example.yaml ./brief.yaml
# Edit brief.yaml — name, stack, IDE targets, skills

python -m scaffold --brief ./brief.yaml --target .
```

Or use the wrapper scripts:

```bash
# Windows
scripts\scaffold.bat C:\path\to\brief.yaml C:\path\to\your-project

# macOS / Linux
bash scripts/scaffold.sh ./brief.yaml ../your-project
```

## What gets generated

| Output | Cursor | Antigravity |
|--------|--------|-------------|
| Agent instructions | `AGENTS.md` | `.agents/agents.md` |
| Skills | `.cursor/skills/*/` | `.agents/skills/*/` |
| Rules | `.cursor/rules/*.mdc` | — (use skills + agents.md) |
| MCP config | `.cursor/mcp.json` | configure via Gemini MCP separately |
| Setup guide | `docs/AI-IDE-SETUP-CHECKLIST.md` | same |
| Workflows | — | `.agents/workflows/onboard.md` |

## The brief file

`brief.yaml` is the single source of truth. See [`brief.example.yaml`](brief.example.yaml).

Key sections:

- **project** — name, description, profile (`web-app`, `marketing-site`, `python-api`)
- **stack** — language, framework, backend, deploy target
- **ide.targets** — `cursor`, `antigravity`, or both
- **ide.skills** — which starter skills to copy
- **ide.rules** — which Cursor rules to generate
- **ide.mcp** — optional MCP servers
- **commands** — install/dev/test/lint/build (rendered into AGENTS.md)

Profiles in [`profiles/`](profiles/) merge under your brief so clients can start from a template and override only what differs.

## Included starter skills

| Skill | Purpose |
|-------|---------|
| `using-skills` | How to find and apply project skills |
| `product-context` | Canonical `.agents/product-marketing-context.md` |
| `brainstorming` | Design before implementation |
| `systematic-debugging` | Root-cause debugging workflow |
| `verification-before-completion` | Evidence before "done" |
| `frontend-polish` | UI spacing, hierarchy, Tailwind cleanup |
| `copywriting` | Marketing copy with context |
| `seo-audit` | On-page SEO checklist |

## Client handoff flow

1. Clone this repo (or fork for your consultancy)
2. Copy `brief.example.yaml` into the client project
3. Fill in stack + pick profile
4. Run scaffold → open project in Cursor/Antigravity
5. Client follows `docs/AI-IDE-SETUP-CHECKLIST.md`
6. First agent session: run `/onboard` (Antigravity) or ask agent to walk the checklist (Cursor)

## Docs

- [`docs/CURSOR.md`](docs/CURSOR.md) — Cursor-specific notes
- [`docs/ANTIGRAVITY.md`](docs/ANTIGRAVITY.md) — Antigravity-specific notes
- [`docs/CUSTOMIZING.md`](docs/CUSTOMIZING.md) — Adding skills, rules, profiles

## Development

```bash
pip install -e ".[dev]"
pytest
python -m scaffold --brief brief.example.yaml --target .scaffold-test --dry-run
```

## License

MIT — use freely with clients; attribution appreciated.
