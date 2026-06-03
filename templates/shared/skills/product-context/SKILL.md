---
name: product-context
description: Use when writing marketing copy, defining ICP, positioning, or any work that needs product/audience context. Create or update .agents/product-marketing-context.md before other marketing skills.
---

# Product context

## Purpose

One canonical doc so every agent session shares the same product, audience, and positioning facts.

## Output file

`.agents/product-marketing-context.md`

## Template

When missing, create the file with these sections:

```markdown
# Product marketing context

## Product
- Name:
- One-line description:
- Primary value proposition:

## Audience
- ICP / primary buyer:
- Pain points:
- Alternatives they consider:

## Positioning
- Category:
- Differentiators (3 bullets max):
- Tone of voice:

## Proof
- Key metrics, customers, or credentials:

## Constraints
- Words/phrases to avoid:
- Compliance or legal notes:
```

## Workflow

1. Ask the user for gaps only if you cannot infer from the repo or brief
2. Write or update the context file
3. Reference it in later copy, UX, and SEO work

## Do not

- Duplicate this context across multiple markdown files
- Invent customer logos, metrics, or claims without source
