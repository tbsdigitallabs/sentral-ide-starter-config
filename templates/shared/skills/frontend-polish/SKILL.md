---
name: frontend-polish
description: Use when improving UI layout, spacing, typography, color, hierarchy, or Tailwind styling. One primary visual pass — systematic polish without generic AI template aesthetics.
---

# Frontend polish

## Workflow

1. Audit the screen: hierarchy, spacing rhythm, contrast, alignment
2. Identify the top 3 issues hurting clarity or trust
3. Fix using existing design tokens and components first
4. Verify responsive behavior at mobile and desktop widths

## Standards

- Consistent spacing scale (avoid random pixel values)
- Clear typographic hierarchy (one H1, restrained font sizes)
- Accessible contrast and focus states
- Restrained shadows and borders — depth with purpose

## Avoid

- Purple-gradient-on-white "AI slop" defaults
- Adding new UI libraries without approval
- Cards-inside-cards nesting without reason

## Pairing

For usability concerns after polish, suggest a separate pass with explicit user request — do not stack full heuristic audits in the same turn.
