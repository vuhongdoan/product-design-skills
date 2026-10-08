# HTML prototype checklist

For native or web code, the same checklist applies to the rendered app, plus the checks in `code-output.md`.

A prototype is for testing ideas with people, so realism beats polish.

## Content
- [ ] Real copy in the user's language; no lorem ipsum, no "John Doe", no "Acme"
- [ ] Realistic data: long names, odd numbers, missing images, many and zero items
- [ ] Copy for errors, empty states and confirmations written, not placeholder

## States
- [ ] Default, empty, loading, error, success reachable (a small state switcher is fine, clearly marked as prototype chrome)
- [ ] The main task can be completed start to finish

## Layout
- [ ] Works at 320–390 px wide; no horizontal scroll
- [ ] Works at desktop width if in scope
- [ ] Primary action in thumb reach on mobile layouts

## White space
Full guidance in `standards/whitespace.md`.
- [ ] One spacing scale (the product's, or the default 4 pt scale) defined as tokens; no one-off values
- [ ] Default minimums met: side margins, container padding, gaps between controls, groups and sections
- [ ] Inner space clearly smaller than outer space; labels and headings sit closest to what they describe
- [ ] The focal point and primary action have the most room around them
- [ ] Nothing cramped at 320 px wide or at 200% text; section spacing scales with the viewport
- [ ] Gaps used before borders, cards and dividers to separate things

## Navigation
- [ ] Navigation chrome shown (tab bar, top bar with back, close on sheets); current tab or section selected
- [ ] Tabs, back and cross-links actually work in the prototype; state is kept when returning
- [ ] At least one non-tab entry point shown where relevant (notification, deep link, empty state)

## Accessibility
Full check in `standards/accessibility.md`. Minimum for any prototype:
- [ ] Contrast computed, not eyeballed: text 4.5:1, large text and UI parts 3:1, in every theme and state
- [ ] Status, errors and selection not shown by colour alone
- [ ] Targets at least 44x44 px on mobile layouts (24x24 CSS px absolute minimum); no hover-only or gesture-only actions
- [ ] Real elements: buttons are buttons, links are links, one `h1`, headings in order, landmarks present
- [ ] Visible focus; logical tab order; modals and sheets trap and return focus; Escape closes
- [ ] Labels on inputs (not placeholder-only); accessible names on icon buttons; alt text or `alt=""` on images
- [ ] Layout holds at 200% text and 320 px wide; zoom not disabled
- [ ] Errors say which field, what is wrong and how to fix it; announced to assistive tech
- [ ] `prefers-reduced-motion` respected, with a still equivalent

## Character
- [ ] A named concept, visible in type, colour, imagery and motif
- [ ] Brand kit defined (mark, palette, type, motif, voice)
- [ ] Real imagery built in HTML/CSS/SVG (hero object, product mockup, illustration), not grey placeholder boxes
- [ ] At least one meaningful interaction (product slice, calculator, configurator, before/after, working flow)
- [ ] No section is only paragraphs or bullet lists
- [ ] Passes the cover-the-logo test

## Motion
- [ ] Every animation has a job: feedback, change, progress, explaining, play or one signature moment
- [ ] Feedback 150–300 ms; no default fade-ins, pulses or loops

## Build
- [ ] One self-contained file: markup, styles and script together
- [ ] Design values as CSS custom properties (colour, type, spacing, radius), so they can become tokens later
- [ ] No external dependencies that might fail to load, beyond fonts if needed
- [ ] Opened and checked visually before handing over
