---
name: "design-system"
description: Create, audit and extend design systems for any platform (iOS, Android, web, cross-platform). Covers design tokens (primitive, semantic, component), foundations (colour, type, spacing, radius, elevation, motion), components with all states and accessibility, usage documentation with do and don't guidance, and consistency audits of existing products or Figma files. Use this skill whenever someone mentions a design system, tokens, variables, theming, dark mode, a component library, style guide, UI kit, design consistency, "our screens look inconsistent", or wants to turn existing screens into reusable components, in Figma or in code.
---

# Design system

A design system exists so that the right decision is the easy one. It should make every screen clearer and calmer, not just more uniform. A system full of components that encode generic defaults, or that makes it easy to put three primary buttons on a screen, spreads the problem faster.

Read `references/standards/problem-solving.md` too: before building or consolidating, challenge the request (is a design system the real fix, or is it a process or ownership problem?), then name the problems the system must solve for users (consistency, accessibility) and for the business (speed to ship, cost of maintenance, brand coherence, multi-brand theming), and compare genuinely different approaches, such as a small core system plus patterns, adopting and theming an existing open system (Material, Radix, shadcn and the like), or a full custom library. Don't default to building every component from scratch, and don't default to copying what exists.

Read `references/standards/budgets.md` first: the system should make the four budgets easy to keep (one primary button style, one accent, restrained motion tokens, accessible defaults). Read `DESIGN-CONTEXT.md` if it exists.

## Pick the mode

| Situation | Mode |
|---|---|
| No system yet, or starting a new product | **Create** |
| Something exists; is it any good, what's missing, what's inconsistent | **Audit** |
| A system exists and needs new tokens, components or a theme | **Extend** |

If unclear, ask one question: "Are we starting fresh, or working from existing screens or a library?"

## Create

Build in this order, checking in with the person between steps. Each layer depends on the one before, so mistakes early are expensive later.

1. **Intake**: product, audience and context; platforms; brand inputs (colours, typefaces, personality); constraints (existing code, Figma plan limits); reference and anti-reference products.
2. **Foundations and tokens**: primitives, then semantic tokens (with light and dark modes if needed), then component tokens where they earn their place. See `references/token-architecture.md`.
3. **Core components**: start with the ones the product's main flows actually use, not a catalogue of everything. Typical first set: button, text input, select, checkbox and radio, toggle, list item, card or container, dialog or sheet, toast or banner, empty state, and the **navigation components** (tab bar or rail, top bar with back, breadcrumbs or section headers, search) with their selected, badge and overflow states. Document the navigation patterns too: when to push a screen versus open a sheet, how back behaves, how deep links land (see `references/standards/navigation.md`). See `references/component-spec.md`.
4. **Patterns**: forms, empty and error states, loading, confirmation; the combinations teams get wrong.
5. **Documentation**: for each foundation and component, what it's for, when not to use it, a do and don't pair, and accessibility notes.

## Audit

Inventory what exists, then report. See `references/audit-checklist.md` for the full checklist.

1. **Inventory**: colours, type styles, spacing values, radii, shadows, icons and components actually in use. Count variants of the same thing (for example, 14 greys, 6 button styles).
2. **Compare** against the ideal: tokens used or hard-coded values? Semantic naming? States complete? Accessible?
3. **Check the budgets at system level**: does the system make it easy to over-emphasize (many accent colours, several "primary" styles)? Is motion tokenized and restrained? Are empty, loading and error patterns provided?
4. **Report** with a clear status per area: present and good, present but inconsistent, or missing. Show evidence (counts, examples). Prioritize by impact on users and on the team.
5. **Offer consolidation options**, not just one plan: for example, a gradual merge of values into tokens, a new token layer mapped over the old values, or a clean-slate rebuild of the core components. Compare effort, risk and disruption, and recommend one with the order of work and what breaks.

In Figma: if a Figma connection is available, read the file's variables, styles and components, and use the library search before proposing anything new. In code: search for hard-coded colours, font sizes, spacing and z-index values.

## Extend

- Search the existing system first. Reuse or extend a variant before creating a new component.
- New tokens follow the existing naming. If the naming is broken, propose the fix separately rather than mixing conventions.
- Every new component ships with all its states, accessibility notes and usage guidance, or it isn't done.

## Output formats

- **Tokens in code**: CSS custom properties or a token JSON file (W3C design tokens format works across tools), with light and dark modes.
- **Figma**: variables in collections (primitives, semantic with modes, component where needed), components with variants and auto layout, a documentation page. Use a Figma connection if available; search existing libraries first.
- **Docs**: a system reference with foundations, components, patterns, and contribution rules.

## Quality bar

- Semantic tokens, not raw values, everywhere in components.
- Every component has default, hover, focus, pressed, disabled, loading and error states where they apply.
- Contrast and target sizes pass by default; accessibility can't be switched off by using a component normally.
- Exactly one primary button style; one accent in the semantic palette; motion tokens with short durations and a reduced-motion path.
- Usage guidance explains *when not* to use a component, not only how.
- The system stays small. Every component earns its place by appearing in real flows.
