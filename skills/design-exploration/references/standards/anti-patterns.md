# Anti-patterns

Patterns that make design weak, whether a person or an AI produced it. They're grouped by the failure they cause, because the failure is what matters. A pattern is only a problem when it hurts the person using the product. Something on this list can be the right call for a specific brief; if you use it, say why.

Don't respond to an anti-pattern by reaching for its fashionable opposite. Swapping "three equal cards" for "asymmetric bento grid" just trades one default for another. And don't respond by stripping the design bare: removing everything generic leaves something plain, which is its own failure (see "Safe, forgettable and dated"). Fix the underlying problem with a real idea.

## Ignores real life (context)

- **Desk-only thinking.** Designed on a large monitor, used on a phone in a queue. Key actions sit at the top of a tall phone screen, out of thumb reach.
- **Perfect-conditions data.** Mockups with short names, round numbers, fast loads and ideal photos. Real names are long, lists are empty or have 3,000 items, photos are dark and skewed.
- **No interruption plan.** Leaving mid-task loses the work. Forms reset. Nobody designed "come back later".
- **Offline and slow are ignored.** Spinners forever, no cached state, no indication of what's saved.
- **Missing states.** Empty, loading, error, partial, no-permission and first-use states are absent or an afterthought.
- **Assumed abilities.** Tiny tap targets, low contrast, information only in colour, text that breaks at larger sizes.
- **Notifications and prompts at the wrong moment.** Permission asks on launch, ratings prompts mid-task.

## Neat but hard to follow (comprehension)

- **System vocabulary.** Labels name the database, not the user's goal: "Entities", "Sync config", "Submit".
- **Ambiguous icons without labels.** Nobody knows what the squiggle does.
- **Invisible interactivity.** Things that are tappable don't look it; things that look tappable aren't.
- **Hidden state.** No clear sign of where you are, what's selected, or whether an action worked.
- **Structure that follows the org chart**, not the task.
- **Clever over clear.** Playful copy or novel patterns where the familiar one would be understood at once.
- **Consistency on the surface only.** Same spacing and colours, but the same action is named three different things in three places.

## Too much at once (attention)

- **Several primary buttons.** Two or three filled buttons shouting at once.
- **Everything emphasized**, so nothing is: multiple accent colours, bold everywhere, badges on every tab.
- **Dashboard soup.** Every metric on one screen, none answering a question.
- **Stacked promos**: banner, modal, tooltip and coach mark in the same session.
- **Choice overload**: long, flat lists of equal options at the moment of decision.
- **Feature-count thinking.** Adding a setting instead of making a decision.

## Too much motion

- **Entrance animation on every section**, fade-and-slide on scroll, staggered cascades.
- **Parallax, scroll-jacking, smooth-scroll overrides.**
- **Spring physics and hover effects on everything.**
- **Looping ambient animation** competing with content.
- **Slow transitions** that make the product feel sluggish.
- **Motion carrying meaning** with no still equivalent, and reduced-motion settings ignored.

## Cramped and arbitrary spacing

- **Cramped layouts**: content packed to the edges, small margins, tight line height, no room around the primary action. Usually caused by trying to fit too much on one screen. Cut or defer content; don't shrink the gaps.
- **Arbitrary values**: 13 px here, 22 px there, nothing from a scale, so the layout feels slightly off and can't be kept consistent.
- **Ambiguous grouping**: gaps inside groups as large as gaps between them, labels floating midway between two fields, headings closer to the section above than their own.
- **Boxes instead of space**: borders, cards and dividers around everything to separate content that a larger gap would separate more quietly.
- **Dense without rhythm**: dashboards and tables where every gap is the minimum, so the screen reads as one mass instead of a few areas.

See `whitespace.md` for the fix.

## Safe, forgettable and dated

The opposite failure to clutter. It often comes from following "keep it simple" too literally.
- **Text walls**: sections that are paragraphs and bullet lists with nothing to look at, try or feel.
- **No brand**: default system font, grey-and-one-accent palette, no logo mark, no imagery, no motif. It could be anyone's page.
- **Document layout on a brand page**: hairline rules, left-aligned headings and body text section after section, like a spec or a wiki.
- **Old-school UI**: small type with little scale contrast, thin borders boxing everything in, flat grey panels, table-like layouts, cramped density on a page that should breathe.
- **Describing instead of showing**: explaining the product in words when a mockup, a demo or an illustration would show it in a glance.
- **Nothing to interact with**: a static page for a product whose value is easy to demonstrate.
- **Asking nothing**: designing a brand-facing page without asking about positioning, existing brand assets, competitors or taste.

Fix these with a concept, a brand system and visuals, not by adding decoration or motion for its own sake.

## Generic visual defaults

These signal "nobody made a decision here". None is wrong in itself; it's wrong when it appears regardless of the subject.
- The same default typeface and a single border radius on everything regardless of hierarchy.
- Identical rounded cards with the same soft grey shadow as the only structural device.
- Purple-to-blue gradients, glassmorphism and glow as decoration.
- Tracked-out all-caps eyebrow labels above every heading.
- Three equal feature columns with an icon, a heading and two lines of text.
- Numbered markers (01, 02, 03) on content that isn't a sequence.
- A big number, a small label and a gradient accent as the default hero.
- Placeholder content: "John Doe", "Acme Corp", "Lorem ipsum", round fake numbers.
- Marketing clichés in copy: "seamless", "elevate", "unleash", "next-gen", "game-changer".
- Cheerful exclamation marks on success and "Oops!" on errors.

## Manipulative patterns (never)

Confirm-shaming, fake scarcity or countdowns, pre-checked upsells, hidden costs revealed late, roach-motel cancellations, nagging permission loops, disguised ads. These may lift a metric and they damage trust. Treat them as defects.
