# Component spec template

Use one spec per component. A component isn't done until every section is filled or marked N/A deliberately.

```markdown
# [Component name]

## Purpose
What it's for, in one sentence.

## When to use / when not to use
- Use when:
- Don't use when: (and what to use instead)

## Anatomy
Named parts (container, label, icon, helper text…)

## Variants
e.g. primary / secondary / tertiary; sizes. Keep to what real flows need.

## States
default · hover · focus-visible · pressed · disabled · loading · error · selected (as applicable)

## Tokens used
List the semantic tokens for colour, spacing, radius, type, motion.

## Behaviour
Interaction, keyboard support, touch target, motion (what it communicates, duration, reduced-motion fallback).

## Content guidelines
Label length, casing (sentence case), verb-first actions, error wording.

## Accessibility
Role, accessible name, focus order, contrast, not-colour-alone, screen reader announcement for changes.

## Do / Don't
One pair minimum, focused on the most common misuse.
```

## Common misuse to document

- **Button**: more than one primary on a screen; vague labels ("OK", "Submit"); disabled with no explanation.
- **Card**: used as the only structural device, making everything look equal; entire card clickable with nested buttons inside.
- **Modal / dialog**: used for simple actions that could be inline; stacked modals; no clear dismiss.
- **Toast**: carrying critical information that disappears; stacking many.
- **Badge**: on every tab or item, so none stand out.
- **Tabs**: more than about five; used for sequential steps.
