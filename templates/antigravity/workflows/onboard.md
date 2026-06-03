# Onboard this project

When the user runs `/onboard`, guide them through AI IDE setup:

1. Read `AGENTS.md` and summarize the stack in 5 bullets.
2. Read `docs/AI-IDE-SETUP-CHECKLIST.md` and tell them which steps are still unchecked based on file presence.
3. Offer to create `.agents/product-marketing-context.md` if missing (use the `product-context` skill).
4. Suggest one small first task to validate the setup (e.g. run tests or fix a TODO).

Keep responses concise and actionable. Do not scaffold over existing custom rules without asking.
