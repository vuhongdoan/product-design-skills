# Accessibility check

Accessibility is part of the design, decided while choosing colour, type, layout and interaction. Checking only at the end means the fixes cost the most and tend to flatten the character of the work. Many of the people who need these things are in ordinary situations: bright sun, one hand free, a cracked screen, a noisy train, a tired evening, a temporary injury. Designing for them improves the product for everyone.

This is a design-level check against WCAG 2.2 AA, not a compliance audit. Say so in the hand-over, and recommend testing with real assistive technology before release.

## When to run it

Three passes, each cheap when done at the right moment:

1. **Direction** (step 4): test the palette and type pairing before committing. A brand colour that fails contrast on its own background is a direction problem, not a polish problem. Pick the accessible variant of each colour role now (text, text-on-brand, link, border, disabled, error, success) and write them into the brand kit.
2. **Build** (steps 5 and 6): note per screen the reading order, the focus order, the names of non-text controls and the states that need more than colour. Build with real elements (`button`, `a`, `label`, `input`, `nav`, `main`, headings in order), because that gives most of the accessibility for free.
3. **Critique** (step 7): run the checklist below on the finished work and list what you found and fixed.

## Checklist

Group by what the person is doing. Mark each item pass, fixed, or open (with the reason).

### See it
- [ ] Body text at least 4.5:1 against its actual background, including text over images, gradients and brand colours. Large text (about 24px, or 18.5px bold) and essential UI parts (input borders, icons that carry meaning, focus rings, chart marks) at least 3:1.
- [ ] Contrast checked for every theme (light, dark, any brand-coloured surface) and for states: hover, pressed, selected, disabled-but-readable placeholder, error.
- [ ] Meaning never carried by colour alone. Status, errors, required fields, selected items and chart series also have text, an icon, a shape or a pattern.
- [ ] Text survives 200% size and, on iOS and Android, the system's largest text settings, without clipped text, overlapping elements or lost actions. Use relative units on the web; layouts reflow instead of truncating essential information.
- [ ] Content works at 320 CSS px wide without horizontal scrolling and without needing pinch-zoom (never disable zoom).
- [ ] Body text is comfortable to read: roughly 16px or larger on the web, 17pt on iOS, 16sp on Android, line height about 1.4 or more, line length about 45-80 characters.
- [ ] Text inside images is avoided, or has a live-text equivalent.

### Reach it and tap it
- [ ] Targets at least 24x24 CSS px (WCAG 2.2 minimum), with 44x44 pt on iOS and 48x48 dp on Android as the design target. Small visual icons get a larger hit area.
- [ ] Enough space between neighbouring targets that a thumb or a tremor does not hit the wrong one. Destructive actions are never squeezed next to common ones.
- [ ] Anything done by dragging, swiping, long-press, pinch or hover has a plain tap or click alternative. Gestures are shortcuts, not the only route.
- [ ] Primary actions are within thumb reach on phone layouts, and the layout does not depend on a particular hand.
- [ ] Nothing important is hidden under the keyboard, notch, home indicator or a sticky bar. Respect safe areas.

### Use it with a keyboard or switch
- [ ] Every action works by keyboard, with a logical tab order that follows the visual order.
- [ ] Focus is clearly visible (a ring or outline of at least 3:1 contrast, not removed by `outline: none` without a replacement) and never hidden behind sticky headers or footers.
- [ ] Modals, sheets and menus move focus in, trap it while open, close on Escape or an obvious close control, and return focus to the trigger.
- [ ] A "skip to content" link or an equivalent exists on pages with repeated navigation.
- [ ] No keyboard traps; custom widgets (tabs, menus, sliders, carousels) follow the common keyboard patterns.

### Hear it (screen readers and voice control)
- [ ] Real semantic elements and landmarks (`header`, `nav`, `main`, `footer`), one `h1`, and headings in a sensible order. Headings describe structure, not size.
- [ ] Every input has a visible label (not placeholder-only) and every icon-only button has an accessible name that says what it does ("Add to outfit", not "plus").
- [ ] Visible text and accessible name agree, so voice-control users can say what they see.
- [ ] Meaningful images have a short description; decorative images are hidden from assistive tech (`alt=""`, `aria-hidden`).
- [ ] State is announced: selected, expanded, checked, current page, loading, and errors or toasts that appear without a page change (live regions).
- [ ] Reading order matches the visual order. For mobile screens, note the order a screen reader would move in.
- [ ] Charts and data visuals have a text summary or a table alternative.

### Understand it
- [ ] Errors name the field, say what is wrong in text and suggest the fix; focus moves to the first error on submit.
- [ ] Instructions do not rely on sensory words alone ("the green button on the right").
- [ ] Plain language, short sentences, consistent names for the same thing. Set the page language.
- [ ] Forms support autofill, paste and password managers, with the right input types and `autocomplete` values. No forced memorizing or retyping of codes when a paste or passkey works.
- [ ] Time limits warn and can be extended. Auto-advancing carousels and auto-playing media can be paused.
- [ ] Destructive or financial actions can be undone or confirmed, and entered data is not lost on error.

### Motion and sensory
- [ ] `prefers-reduced-motion` is honoured, with a still equivalent for every animation that carries meaning (see the motion budget).
- [ ] Nothing flashes more than three times a second. No parallax or full-screen movement without a way to turn it off.
- [ ] Video has captions and a transcript where it carries information; audio never plays on its own; haptic or sound cues are never the only signal.

## How to record the result

Add a short **Accessibility notes** block to the hand-over:

- Contrast pairs that matter and their ratios (for example "text on brand green 5.1:1").
- What was fixed during the check, and what changed because of it (for example "darkened the accent from X to Y so button text passes").
- Anything open, why, and who has to decide.
- What needs real-device or assistive-technology testing: screen reader pass (VoiceOver, TalkBack, NVDA), keyboard-only pass, largest text size, reduced motion on.

## Keeping character while meeting contrast

Contrast limits are a constraint to design inside, not a reason for grey, timid colour:

- Keep the saturated brand colour for large areas, backgrounds and illustration, and use a deeper tint of the same hue for text and thin UI.
- Choose the text colour on a brand background first (usually near-black or near-white with a hint of the hue), then tune the background to match.
- A strong focus ring in the accent colour is a chance for a signature detail.
- Use shape, icon and weight along with colour for status, so the colour can stay expressive.

## Checking the numbers

Do not eyeball contrast. Compute it. In a prototype, a few lines of script or a contrast checker is enough:

```js
// WCAG relative luminance and contrast ratio for two hex colours
const lum = h => {
  const [r, g, b] = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255)
    .map(c => c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const contrast = (a, b) => {
  const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
};
// contrast('#1F4D3A', '#F6F3EC') -> compare with 4.5 (text) or 3 (large text, UI)
```

For text over images or gradients, check the worst spot, or add a scrim so the worst spot passes.
