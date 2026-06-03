# Agent IDE Starter

Scaffold AI agent IDE project configuration from a single brief file — skills, rules, MCP servers, and a human setup checklist.

Works with editors that use the **rules layout** (`.cursor/`) or the **agents layout** (`.agents/`).

## Who this is for

Clients or teams adopting an AI-native editor who want:

- A repeatable project setup they can clone and run
- Agent **skills** that teach good habits (plan → implement → verify)
- **Rules** for stack-specific conventions
- Optional **MCP** integrations (GitHub, docs lookup, memory)
- Both common config layouts from one brief

## Quick start

```bash
git clone https://github.com/tbsdigitallabs/agent-ide-starter.git
cd agent-ide-starter
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e .

# In YOUR project:
cp /path/to/agent-ide-starter/brief.example.yaml ./brief.yaml
# Edit brief.yaml — name, stack, layout targets, skills

python -m scaffold --brief ./brief.yaml --target .
```

Or use the wrapper scripts:

```bash
# Windows
scripts\scaffold.bat C:\path\to\brief.yaml C:\path\to\your-project

# macOS / Linux
bash scripts/scaffold.sh ./brief.yaml ../your-project
```

See [`docs/GETTING-STARTED.md`](docs/GETTING-STARTED.md) for the full client handoff walkthrough.

## What gets generated

| Output | Rules layout (`.cursor/`) | Agents layout (`.agents/`) |
|--------|----------------------------|----------------------------|
| Agent instructions | `AGENTS.md` | `.agents/agents.md` |
| Skills | `.cursor/skills/*/` | `.agents/skills/*/` |
| Rules | `.cursor/rules/*.mdc` | — (skills + agents.md) |
| MCP config | `.cursor/mcp.json` | configure in your editor |
| Setup guide | `docs/AI-IDE-SETUP-CHECKLIST.md` | same |
| Workflows | — | `.agents/workflows/onboard.md` |

## The brief file

`brief.yaml` is the single source of truth. See [`brief.example.yaml`](brief.example.yaml).

Key sections:

- **project** — name, description, profile (`web-app`, `marketing-site`, `python-api`)
- **stack** — language, framework, backend, deploy target
- **ide.targets** — `rules`, `agents`, or both (legacy aliases `cursor` / `antigravity` still work)
- **ide.skills** — which starter skills to copy
- **ide.rules** — which rule files to generate (rules layout only)
- **ide.mcp** — optional MCP servers
- **commands** — install/dev/test/lint/build (rendered into `AGENTS.md`)

Profiles in [`profiles/`](profiles/) merge under your brief so clients can start from a template and override only what differs.

## Included starter skills

| Skill | Purpose |
|-------|---------|
| `using-skills` | How to find and apply project skills |
| `product-context` | Canonical product/audience context doc |
| `brainstorming` | Design before implementation |
| `systematic-debugging` | Root-cause debugging workflow |
| `verification-before-completion` | Evidence before "done" |
| `frontend-polish` | UI spacing, hierarchy, styling cleanup |
| `copywriting` | Marketing copy with context |
| `seo-audit` | On-page SEO checklist |

## Client handoff flow

1. Clone this repo (or fork for your consultancy)
2. Copy `brief.example.yaml` into the client project
3. Fill in stack, profile, and layout targets
4. Run scaffold → open the project in their editor
5. Client follows `docs/AI-IDE-SETUP-CHECKLIST.md`
6. First agent session: run `/onboard` (agents layout) or ask the agent to walk the checklist

## Documentation

| Doc | Description |
|-----|-------------|
| [`docs/GETTING-STARTED.md`](docs/GETTING-STARTED.md) | End-to-end setup for new clients |
| [`docs/RULES-LAYOUT.md`](docs/RULES-LAYOUT.md) | Rules layout (`.cursor/`) — rules, skills, MCP |
| [`docs/AGENTS-LAYOUT.md`](docs/AGENTS-LAYOUT.md) | Agents layout (`.agents/`) — skills and workflows |
| [`docs/CUSTOMISING.md`](docs/CUSTOMISING.md) | Adding skills, rules, and profiles |

## Development

```bash
pip install -e ".[dev]"
pytest
python -m scaffold --brief brief.example.yaml --target .scaffold-test --dry-run
```

## Licence

MIT — use freely with clients; attribution appreciated.
