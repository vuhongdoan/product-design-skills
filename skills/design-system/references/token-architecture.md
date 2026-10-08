# Token architecture

Three layers. Components reference semantic tokens; semantic tokens reference primitives. Changing a theme means remapping semantics, never editing components.

## 1. Primitives (raw values, no meaning)

```
color.neutral.0 … color.neutral.1000   (one hue family for greys, warm or cool, not both)
color.brand.100 … color.brand.900
color.red / green / amber / blue scales for status
space.0, 1 (4), 2 (8), 3 (12), 4 (16), 5 (20), 6 (24), 8 (32), 10 (40), 12 (48), 16 (64)
radius.none, sm, md, lg, full
font.family.*, font.size.*, font.weight.*, font.lineHeight.*
duration.fast (100–150ms), duration.base (200ms), duration.slow (300ms)
easing.standard, easing.enter, easing.exit
```

## 2. Semantic (meaning, with modes)

```
color.bg.default / subtle / inset
color.surface.default / raised / overlay
color.text.primary / secondary / disabled / inverse / onAccent
color.border.default / subtle / strong / focus
color.action.primary.bg / hover / pressed / disabled
color.action.secondary.*
color.status.success / warning / danger / info  (+ .subtle backgrounds)
space.inset.*, space.stack.*, space.inline.*
radius.control, radius.container, radius.sheet   (hierarchy, not one value)
elevation.raised, elevation.overlay
motion.feedback, motion.transition   (+ reduced-motion variants set to 0 or a fade)
type.display / title / heading / body / label / caption
```

Each colour token has **light** and **dark** values. Dark mode is not inverted light mode: lower the contrast of large surfaces, keep text contrast, desaturate accents slightly.

## 3. Component (only when needed)

```
button.primary.bg → color.action.primary.bg
button.radius → radius.control
input.border.focus → color.border.focus
```

Add component tokens when a component must deviate from semantics or when teams need to theme it independently. Don't create them for every property by default.

## Naming rules

- `category.property.variant.state`, lower camel or kebab, consistent across the system.
- Names describe purpose, not appearance: `color.status.danger`, not `color.red`.
- One primary action colour. Additional "accent" tokens need a documented reason.

## Formats

- **CSS**: `--color-text-primary: var(--color-neutral-900);` with a `[data-theme="dark"]` or `prefers-color-scheme` override.
- **JSON**: W3C Design Tokens format (`$value`, `$type`), convertible with tools like Style Dictionary.
- **Figma**: variable collections `Primitives`, `Semantic` (modes: Light, Dark), optional `Component`; scope variables so colour tokens only appear in fill and stroke pickers.

## Accessibility built into tokens

- Every text/background pairing in the semantic set is checked for contrast (4.5:1 body, 3:1 large text and UI).
- Focus colour meets 3:1 against adjacent colours.
- Status colours are always paired with an icon or text in components.
