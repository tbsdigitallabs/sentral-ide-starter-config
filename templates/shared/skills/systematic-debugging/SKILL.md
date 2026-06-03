---
name: systematic-debugging
description: Use when encountering bugs, test failures, or unexpected behavior. Follow root-cause investigation before proposing fixes.
---

# Systematic debugging

## Phase 1 — Reproduce

- Get exact steps, input, and expected vs actual
- Reproduce locally or with a minimal test case

## Phase 2 — Gather evidence

- Read error messages and stack traces fully
- Check recent diffs and config changes
- Add temporary logging only if needed; remove after fix

## Phase 3 — Hypothesize

- List 2–3 plausible causes ranked by likelihood
- Test one hypothesis at a time

## Phase 4 — Fix minimally

- Fix root cause, not symptoms
- Smallest diff that solves the problem
- Add a regression test when practical

## Phase 5 — Verify

- Run the failing test/command again
- Check adjacent paths did not break

## Do not

- Guess-and-patch in a loop without new evidence
- Mark fixed without running verification commands
