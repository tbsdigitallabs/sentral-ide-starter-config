---
name: brainstorming
description: Use before creative work — new features, components, behavior changes, or ambiguous requirements. Explore intent and propose a short design before implementation.
---

# Brainstorming

## When required

Use before:
- New features or user-facing flows
- Non-trivial refactors
- Anything with multiple valid approaches

## Process

1. **Context** — read relevant files and `AGENTS.md`
2. **Clarify** — ask one focused question if a key decision is unclear
3. **Options** — propose 2–3 approaches with trade-offs; recommend one
4. **Design** — short spec: scope, files touched, data flow, test plan
5. **Approval** — get user sign-off before coding (unless user said "just do it")

## Output size

Match complexity:
- Small change: 3–5 sentences
- Medium feature: half-page spec
- Large feature: suggest breaking into phases

## YAGNI

Cut nice-to-haves from v1 unless the user explicitly wants them.

## Do not

- Jump to code on ambiguous product decisions
- Over-document trivial one-file changes
