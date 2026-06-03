# Getting started

This guide is for clients (or your team) setting up a project with Sentral IDE Starter Config for the first time.

## What you need

- Python 3.11+
- Git
- An AI-native editor that supports either:
  - **Rules layout** — project config under `.cursor/`, or
  - **Agents layout** — project config under `.agents/`

## Step 1 — Clone the starter

```bash
git clone https://github.com/tbsdigitallabs/sentral-ide-starter-config.git
cd sentral-ide-starter-config
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Install the scaffold tool:

```bash
pip install -e .
```

## Step 2 — Create your project brief

In **your** project folder (not the starter repo):

```bash
cp /path/to/sentral-ide-starter-config/brief.example.yaml ./brief.yaml
```

Edit `brief.yaml`:

1. Set **project.name** and **project.description**
2. Pick a **profile** or fill in **stack** manually
3. Choose **ide.targets**:
   - `rules` — generates `.cursor/` config
   - `agents` — generates `.agents/` config
   - both — if your editor setup uses both layouts
4. Trim **ide.skills** and **ide.rules** if you want a lighter setup
5. Set **commands** to match your repo (`npm`, `pip`, etc.)

## Step 3 — Run the scaffold

From the starter repo (or anywhere with the tool installed):

```bash
python -m scaffold --brief /path/to/your-project/brief.yaml --target /path/to/your-project
```

Preview without writing files:

```bash
python -m scaffold --brief ./brief.yaml --target . --dry-run
```

## Step 4 — Open your project

Open the **target project folder** in your editor — not the starter repo.

You should see:

- `AGENTS.md` — stack, commands, constraints
- `docs/AI-IDE-SETUP-CHECKLIST.md` — tick-list for humans
- `.cursor/` and/or `.agents/` depending on your brief

## Step 5 — Complete the checklist

Work through [`AI-IDE-SETUP-CHECKLIST.md`](AI-IDE-SETUP-CHECKLIST.md) in your scaffolded project. At minimum:

1. Confirm rules and skills are visible to the agent
2. Fill in `AGENTS.md` gotchas
3. Create product context (ask the agent to run the `product-context` skill)
4. Set MCP environment variables if you enabled MCP servers
5. Run your test command once to validate the toolchain

## Step 6 — First agent session

Ask the agent:

> Read `AGENTS.md` and `docs/AI-IDE-SETUP-CHECKLIST.md`. Summarise what's configured and what's still missing.

If your editor supports workflows, try `/onboard`.

For new features, invoke **brainstorming** before implementation. Use **verification-before-completion** before calling work done.

## Layout reference

| Layout | Directory | Best for |
|--------|-----------|----------|
| Rules | `.cursor/` | Editors that load `.mdc` rules, project skills, and MCP from one folder |
| Agents | `.agents/` | Editors that load skills, workflows, and team docs from one folder |

See [`RULES-LAYOUT.md`](RULES-LAYOUT.md) and [`AGENTS-LAYOUT.md`](AGENTS-LAYOUT.md) for detail.

## Re-scaffold or update

Back up custom edits to `.cursor/` or `.agents/` first, then re-run:

```bash
python -m scaffold --brief ./brief.yaml --target .
```

## Customising the starter itself

Consultancies forking this repo should read [`CUSTOMISING.md`](CUSTOMISING.md).

## Help

- Starter issues: [github.com/tbsdigitallabs/sentral-ide-starter-config/issues](https://github.com/tbsdigitallabs/sentral-ide-starter-config/issues)
- Editor-specific behaviour: your editor's official documentation
