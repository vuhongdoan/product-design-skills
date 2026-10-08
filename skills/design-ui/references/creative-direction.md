# Creative direction

A creative direction is a single idea that decides how everything looks, reads and moves. Without one, design falls back on defaults and looks generic or plain.

## Contents
- Brand intake questions
- Where concepts come from
- Direction template
- Signature elements
- Brand kit
- Presenting directions

## Brand intake questions

Ask these in **one message** before brand-facing work (marketing pages, first-run experiences, new products, rebrands). Offer a proposed answer for each so the person can just confirm or correct.

1. **Positioning**: who is it for, what's different, and what's the main alternative (including DIY or doing nothing)?
2. **Existing brand**: logo, colours, typefaces, illustration or photo style, voice? Attach or link them, or say "none yet".
3. **Personality**: three words it should be, three it must never be.
4. **Feeling and action**: what should people feel in the first five seconds, and what's the one thing they should do?
5. **Competitors**: who are they, and should we look like the category or deliberately break from it?
6. **Taste**: 2–3 brands, sites or apps you love (and why), and anything you dislike.
7. **Boldness**: safe and familiar, confident, or experimental?
8. **Content and assets**: real photos, product screenshots, customer stories, numbers we're allowed to use?

If there's an existing brand, work within it and push its expression. Don't invent a new identity over the top of one.

## Where concepts come from

Look in the subject, not in a trend list:
- **Place**: the city, climate, light, streets and seasons of where it's used ("Stockholm in November: dark at 3pm, wet asphalt, reflective strips, studded tyres").
- **Materials and tools**: what the work physically involves (chain grease, spoke wrenches, receipt paper, fabric labels).
- **Rituals and moments**: when people use it and how that feels (the 7:40 commute, Sunday wardrobe clear-out).
- **Vocabulary**: the words insiders use; signage, labels, instruments of the domain.
- **The product's own artifacts**: its outputs made into visuals (a service card, a route, a streak, an outfit).
- **The opposite of the category**: what every competitor does, and what it would look like to do the reverse.

A good concept is one sentence that a designer could run with: "A commuter's winter kit: hi-vis signal colour, reflective type, and the service card as the hero object."

## Direction template

```markdown
### Direction [A]: [short name]
**Concept**: one sentence.
**Why it fits**: link to positioning, audience and context.
**Mood**: 3–5 words.
**Colour**: 4–6 named hex values, with roles (ground, ink, signal, support).
**Type**: display and text families (Google Fonts or the brand's), and how type behaves (scale, weight, case, motion).
**Density and spacing**: how much room content gets (airy, balanced or compact), the section rhythm, and why that suits the brand and context. Never cramped; see `standards/whitespace.md`.
**Imagery**: photography, illustration, 3D, product mockups; style and subject.
**Signature element**: the one thing people will remember or play with.
**Motion**: the jobs motion does here, and the one signature moment.
**Trend fit**: which current trends it uses, and why they fit.
**Risk**: what could go wrong or feel off-brand.
```

Make the directions **genuinely different** (for example: one expressive and bold, one calm and premium, one playful or unexpected), not three shades of one idea.

## Signature elements

Pick one per page or flow and do it properly:
- **Playable product slice**: the core interaction running in the page (swap an outfit, pick a time slot, drag a slider to see the saving).
- **Calculator or configurator** tied to the real value ("How many flats did you get last winter?").
- **Hero object**: an artifact from the product rendered as the main visual (a receipt, a card, a ticket, a map), built in HTML/CSS/SVG so it's crisp and can respond.
- **Illustration system**: a consistent drawn world (line weight, palette, characters or objects) used across sections.
- **Type as image**: a headline treatment that is the visual identity, possibly kinetic.
- **Before and after**: a comparison slider or toggle that shows the change the product makes.
- **Scroll story**: one sequence that assembles or transforms as you scroll, with a still fallback.

## Brand kit

Before building pages, define the minimum identity:
- **Wordmark or logo mark** (a simple, custom SVG is fine for a prototype; say it's a placeholder).
- **Palette** with roles and contrast checked.
- **Type pairing** with a scale.
- **Spacing scale**: the product's own, or the default 4 pt scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128), with semantic names for section, group and inset spacing.
- **Motif**: a shape, texture, pattern or graphic device that repeats (stripes from reflective tape, a stitched line, a ticket perforation).
- **Imagery rules**.
- **Voice**: three sample lines (headline, button, error).

Write these as CSS custom properties so the page and later the design system share them.

## Presenting directions

When the person is available: show 2–3 directions as a quick visual board (a hero sketch or mini mood board for each, in one HTML page), recommend one with reasons, and let them choose before building the full design.

When they aren't: choose the direction that best fits the brief, build it, and include the other directions as a short board or in the notes so they can switch.
