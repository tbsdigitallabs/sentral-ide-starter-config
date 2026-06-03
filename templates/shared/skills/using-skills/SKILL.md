---
name: using-skills
description: Use when starting any session or when unsure which project skill applies. Establishes how to find and follow skills under .cursor/skills and .agents/skills before answering or coding.
---

# Using skills

## Rule

Before substantive work, check whether any project skill applies — even ~1% chance means you should read it.

## How to find skills

| Layout | Path |
|--------|------|
| Rules layout | `.cursor/skills/<skill-id>/SKILL.md` |
| Agents layout | `.agents/skills/<skill-id>/SKILL.md` |

Read the skill file when triggered. User instructions override skills.

## Priority

1. User's explicit instructions
2. Process skills (brainstorming, systematic-debugging)
3. Domain skills (frontend-polish, copywriting, seo-audit)
4. Default agent behaviour

## Announce

Briefly state which skill you are applying and why.

## Do not

- Skip skill checks because the task "seems simple"
- Stack competing primary skills in one turn (see skills-routing rule)
- Paraphrase user-provided skill text when a skill says to use verbatim copy
