# White space

White space is a design material, not what's left over after the content is placed. It does more structural work than borders, boxes, colour or dividers: it tells people what belongs together, what leads, where to rest, and how the product feels. Decide it on purpose at every stage. Never let it fall out of default margins.

## What white space does

- **Groups.** Things that sit closer together read as related (law of proximity). Spacing is the cheapest and quietest way to show structure, so reach for it before a border, card or divider.
- **Leads.** The space around an element sets its importance as much as its size. A focal point surrounded by room leads; the same element crowded by neighbours competes.
- **Paces reading.** Comfortable line height, a readable line length and pauses between sections let people take in one idea before the next.
- **Sets tone.** Generous space reads as calm, confident and premium. Tight space reads as busy, efficient or cheap. Choose the tone the brand and the context call for.
- **Protects touch.** Space between targets prevents mis-taps, especially one-handed and on the move.

## The two failures

- **Cramped**: elements packed edge to edge, small margins, tight line height, everything boxed in to compensate. The eye has nowhere to rest and no grouping to follow.
- **Empty or flat**: the same gap everywhere, so nothing groups; or huge gaps that separate things that belong together, leaving labels floating away from their fields and headings drifting away from their content. More space is not automatically better. Space without structure is just distance.

Both are failures of *relationships*, not of amount. The fix is a clear spacing system with deliberate contrast between small and large gaps.

## Default minimums

These are floors, not targets. Most of the time you'll go above them; go below only with a stated reason.

| Where | Minimum |
|---|---|
| Page side margin, mobile | 16 pt (20 is usually better) |
| Page side margin, desktop content | 24 px, with a max content width so lines don't stretch |
| Padding inside a card or container | 16 |
| Gap between unrelated adjacent controls | 8 |
| Label to its field | 4–8, always less than field to next field |
| Between groups within a screen | 24 |
| Between major sections, app screens | 32 |
| Between major sections, marketing pages | 64 mobile, 96 desktop |
| Around the primary action and focal point | one step more than its neighbours get |

## Rules

1. **Use a scale, never arbitrary values.** If the product already has a spacing scale, use it. Otherwise use the default 4 pt scale: **4, 8, 12, 16, 24, 32, 48, 64, 96, 128**. Every margin, padding and gap comes from it, because arbitrary values (13, 22, 37) are what make layouts feel slightly off and impossible to keep consistent. Define it in the brand kit as CSS custom properties (`--space-1` … `--space-10`) plus a few semantic names where useful (`--space-inset-card`, `--space-stack-sm`, `--space-section`). In Figma, create spacing variables and bind every auto layout gap and padding to them, never raw numbers. In native code, the same scale becomes a `Spacing` enum in SwiftUI (pt) and a `Spacing` object in Compose (dp); see `../native.md`.
2. **Inner space is smaller than outer space.** Space inside a group is clearly smaller than space between groups, roughly half or less. A label sits closer to its field than to the previous field; a heading sits closer to its own content than to the section above. If two gaps are almost the same, the grouping is ambiguous: make them clearly different.
3. **Contrast in spacing, like contrast in type.** A page that uses only two or three similar gaps looks flat. Mix tight clusters with generous breaks so the structure is visible at a glance.
4. **Give the focal point room.** The one thing that leads in each view gets the most space around it. When something must stand out, try adding space before adding size, weight or colour.
5. **Let space replace lines and boxes.** Before adding a divider, border or card, ask whether a bigger gap does the job. Keep containers for things that are genuinely separate objects (a draggable card, a selectable item), not as a substitute for spacing.
6. **Text needs space too.** Body line height about 1.4–1.6, headings about 1.1–1.25. Keep paragraphs to roughly 45–75 characters per line. Put more space above a heading than below it, so it attaches to what follows.
7. **Adjust optically.** Equal numbers don't always look equal: icons, round shapes, all-caps text and text with descenders often need a small nudge. Trust the eye after the scale.
8. **Scale space with the viewport.** Large gaps shrink on small screens, but the ratios between them hold. Use `clamp()` or breakpoint tokens for section spacing rather than fixed pixels.
9. **Edges are part of the layout.** Keep consistent page margins and gutters. Content touching the screen edge (except intentional full-bleed imagery) feels unfinished.

## Density by context

Choose a density level on purpose and write it down. It is part of the creative direction.

- **Marketing and brand pages**: generous. Let sections breathe (roughly 96–160 px between sections on desktop, 56–96 px on mobile). A hero with one idea and lots of room beats a hero filled to the edges. Space is a big part of what makes a page feel confident.
- **Mobile apps**: page margins of 16–24 pt (follow platform norms), comfortable list rows, clear separation between sections, extra room around the primary action. Small screens tempt cramming; resist it by cutting content, not space.
- **Web apps and dashboards**: denser is fine when it serves repeated work, but dense is not cramped. Use tight spacing inside a group and clear space between groups, so a dense screen still scans as a few areas rather than one mass. Minimums still hold: at least 8 px between unrelated controls, at least 12 px cell padding horizontally, at least 24 px between panels or groups, and page gutters of at least 16 px.

## Space and accessibility

- Use relative units (`rem`, `em`) and let containers grow. Layouts with fixed heights break when text scales to 200% or when users increase line, letter or word spacing (WCAG 1.4.12 Text Spacing).
- Keep space between adjacent targets so each is at least 24×24 CSS px including spacing, and aim for 44×44 on touch.
- Keep a label visibly closer to its own input than to the next one, so screen-magnifier users and everyone else can tell which goes with which.

## How to check

- **Squint or blur test**: blur the screenshot. Can you still see the groups and the one focal point? If it reads as an even grey texture, the spacing has no contrast.
- **Proximity check**: for every label, heading and caption, is it clearly closer to the thing it describes?
- **Scale audit**: list the spacing values in the build. Every one should come from the scale. Odd values (13 px, 22 px) are defects unless they are deliberate optical adjustments.
- **Remove-a-line test**: take out each divider and border. If the structure still reads, leave it out.
- **One-more-step test**: around the focal point and between major sections, try one step up the scale. If it looks better, keep it.
- **Small-screen and large-text check**: at 320 px wide and at 200% text, is the spacing still proportional and nothing overlapping or cut off?
