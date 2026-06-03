---
name: verification-before-completion
description: Use before claiming work is complete, fixed, or passing. Requires running verification commands and confirming output — evidence before assertions.
---

# Verification before completion

## Gate

Do not say "done", "fixed", or "tests pass" until you have fresh command output proving it.

## Checklist

1. Identify the right verify commands from `AGENTS.md` (test, lint, build, typecheck)
2. Run them in the project environment
3. Read full output — not just exit code
4. For UI work: confirm visually or describe what you checked
5. Report what you ran and what passed/failed

## If verification fails

- State what failed with relevant output excerpt
- Do not claim partial success as complete

## If verification cannot run

- Say exactly what blocked you (missing deps, env, credentials)
- List what the user should run locally
