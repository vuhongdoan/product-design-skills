---
name: "design-ui"
description: Build a chosen visual direction into finished screens and prototypes. Covers hierarchy and white space, the brand kit, interactive HTML prototypes, Figma screens, production-ready native (SwiftUI, Jetpack Compose, Flutter, React Native) or web code, every key state, real copy, accessibility checks, critique and handover. Use this skill whenever someone asks to design, mock up, prototype, build or restyle a screen, page, landing page, app, onboarding or UI, or to turn a chosen direction into code, even if they only describe the product. If no direction has been chosen yet, route to design-exploration first.
---

# Design UI

Great UI does two things at once: it makes the next action obvious to a person in a real situation, and it is unmistakably *this* product. Clarity without character is forgettable; character without clarity is a pretty dead end. Work toward both, deliberately.

This skill starts from a chosen direction: the concept, look and voice that the person picked in `design-exploration`. If there isn't one yet, stop and route back there, so the build isn't made on a direction nobody has chosen.

Before designing, read:
- `references/standards/budgets.md`: the quality bar, including section 5 on character. Restraint is about noise, never about being plain.
- `references/standards/problem-solving.md`: frame the problems, explore several different ideas, compare and decide.
- `references/standards/anti-patterns.md`: both clutter *and* the safe, forgettable, dated failure.
- `references/creative-direction.md`: the chosen direction's template, signature elements and brand kit.
- `references/standards/navigation.md`: how people reach, leave and find their way around the screens you design.
- `references/standards/whitespace.md`: white space as structure. The spacing scale, default minimums, density by context and how to check it. Cramped layouts and arbitrary spacing values are the failures to avoid.
- `references/standards/accessibility.md`: the accessibility check, run at build and critique. Colour roles checked during exploration carry over.
- `references/code-output.md` when the deliverable is native or web code: choosing the framework, tokens, states, accessibility APIs and checks for SwiftUI, Jetpack Compose, Flutter, React Native and web.
- The platform file that fits: `references/mobile.md`, `references/web-app.md` or `references/marketing.md`.
- `references/native.md` only when the person asks for a native result (native app, SwiftUI, Jetpack Compose, "feel like a real iPhone/Android app").
- `references/prototype-checklist.md` when building the HTML prototype.
- `DESIGN-CONTEXT.md` if it exists.

## Process

### 0. Start from the chosen direction

Restate the direction the person chose, the concept behind it, and any mix they asked for, in two or three lines. If they changed anything, note it. Everything below builds on that choice.

### 5. Hierarchy plan

For each screen or section, write down:
- **Purpose** in one sentence.
- **The one primary action.**
- **The focal point**: what leads at this moment (it can be big and bold).
- **Show, don't tell**: what visual, demo or interaction carries the message instead of a paragraph.
- **What's cut or deferred.** Cutting content is how you make room; never solve a crowded screen by shrinking the gaps.
- **Space plan**: the density level, the groups on the screen (what sits together, what is separated), and which element gets the most room around it. Inner space smaller than outer space; see `whitespace.md`.
- **Navigation context**: where this screen sits in the app, how people arrive (tab, notification, deep link, cross-link), the navigation chrome it shows (tab bar, back with the parent's name, close for sheets), the selected tab or section, and where people go next. A screen designed without its navigation chrome isn't finished.
- **Accessibility notes**: the reading and focus order, the accessible names of icon-only controls, which states need more than colour (error, selected, status), and what happens at the largest text size. Decide these here so the build has them from the start.

### 6. Build the brand kit, then the design

First the minimum identity: wordmark or mark, palette with roles, type pairing and scale, **spacing scale** (the product's own, or the default 4 pt scale in `whitespace.md`), a repeating motif, imagery rules, three sample lines of voice. Write them as CSS custom properties (or Figma variables). Define the accessible colour roles at this point too: text, text on brand, link, border, focus ring, error, success and disabled, each with its checked contrast ratio.

Then build what the person needs. Infer the output from context: an existing repo or a named platform or framework means code in that stack; a mobile app with no framework named means asking once (SwiftUI, Compose, Flutter or React Native); no code requested means the HTML prototype, with code offered as a next step. Ask only when it's genuinely unclear.

- **HTML prototype**: one self-contained file. Characterful type (Google Fonts is fine), real imagery made in HTML/CSS/SVG (product mockups, hero objects, illustration) instead of grey boxes or stock clichés, real copy, and **at least one meaningful interaction**: a playable product slice, calculator, configurator, before/after or working flow. Every key state reachable. Use real semantic elements (buttons, links, labels, headings, landmarks), visible focus styles and `prefers-reduced-motion`. Every margin, padding and gap uses a spacing token, never a one-off number, and section spacing scales with the viewport (`clamp()`) while keeping its ratios. See `references/prototype-checklist.md`.
- **Figma**: if a Figma connection is available, search the existing library and variables first and reuse them; build with auto layout and variables, with every gap and padding bound to a spacing variable; put states and directions side by side.
- **Native app code**: SwiftUI (iOS), Jetpack Compose (Android), Flutter or React Native / Expo. Production-ready UI: a token file (colour, type, spacing, radius, motion), reusable components, every key state with previews, working navigation and the platform's accessibility APIs, with data stubbed behind a clear seam. Follow `references/code-output.md`.
- **Web code**: production-ready front end in the project's own framework and styling (React + TypeScript with CSS custom properties when there's no project), semantic HTML, responsive from 320 px, tokens mapped onto the project's system. Follow `references/code-output.md`.
- **Spec**: annotated layout, components, states, copy and behaviour, when the person builds it themselves.
- **Native app** (only when asked): for iOS and Android, a native-faithful HTML prototype with real platform chrome, and SwiftUI and Jetpack Compose code with the brand kit and spacing scale as native tokens, navigation and every key state in previews. Produce both unless the person names one. Follow `references/native.md`.

**Text budget for brand-facing pages**: headlines of about 3–8 words, supporting lines under ~25 words, no section that's only paragraphs or bullet lists. If a section needs a lot of words, turn it into a visual, a comparison, an interaction or an FAQ.

**White space**: give the layout room before adding anything to it. When something needs separating, try a larger gap before a border, card or divider. When something needs to stand out, try more space around it before more size or colour. If a screen feels crowded, cut or defer content rather than tightening the spacing.

**Motion**: every motion has a job (see the motion budget). One signature moment per page or flow is encouraged: the thing people remember. Interactive elements respond to the person. Nothing loops, pulses or fades in by default, and reduced motion always has a still equivalent.

### 7. Critique before handing over

Look at what you built: take screenshots at phone and desktop widths if your environment can. For native or web code, build or run it and critique the rendered result (previews, simulator or browser), not the source. Then check:

- **Five-second test**: would a first-time visitor know what this is, who it's for and what to do?
- **Cover-the-logo test**: hide the name. Is it still recognizably this brand, or could a competitor swap their logo in?
- **Squint test**: one clear focal point per view; the primary action stands out.
- **White-space test**: run the checks in `whitespace.md`. Blur the screenshot: do the groups and the one focal point still read, or is it an even grey mass? Is every label closer to its own field and every heading closer to its own content? Are all spacing values from the scale, and are the default minimums met? Does anything feel cramped at 320 px or at 200% text? Fix what fails.
- **Show-don't-tell test**: count the sections that are mostly text. Convert them.
- **Current, not trendy**: does it feel of this moment? Is any trend used only as decoration?
- **Real-life test**: one-handed, bright light, large text, slow network, interrupted.
- **Wayfinding test**: arriving cold from a notification or link, can people tell where they are, what this is, and how to get back? Is the current tab or section visibly selected? Does the prototype's navigation actually work (tabs switch, back returns, state is kept)?
- **Accessibility**: run the full checklist in `references/standards/accessibility.md`: contrast (computed), not colour alone, target sizes, text scaling to 200%, keyboard and focus, labels and accessible names, reading order, error messages, reduced motion. Fix what fails, then record the results.
- **Problem test**: does the design actually solve the ranked problems from step 2, or did it drift into styling?
- **Portfolio test**: would a strong design lead be proud to show this? If it's merely correct, find what's missing: usually a concept, a signature element or real imagery.

For significant work, hand off to `design-review` for an independent critique.

### 8. Hand over

In a few lines: what was delivered (prototype, Figma, spec, or which native or web stack, and how to run it), the problems addressed, the solution concepts compared and why this one won, the creative concept and why it fits, the key decisions, the assumptions, the states covered, the other directions considered, a one-line **Spacing** note (the scale used, the density level and any deliberate exceptions to the minimums), an **Accessibility notes** block (key contrast ratios, what the check changed, what is still open), and what to test with real users, including a screen reader pass, a keyboard-only pass and the largest text size. For mobile app work where no native result was requested, add one line offering native-faithful prototypes and SwiftUI/Compose code.

## Copy rules

For any copy beyond these rules (labels, error messages, notifications, tone), follow `design-ux-writing`. Use its review checklist before handing over.

- Specific beats impressive; the reader's words, not marketing clichés.
- Sentence case, plain verbs, active voice.
- A CTA says what happens ("Check my address"); confirmation echoes it.
- Errors state the problem and the fix, without apology or jokes.
- Empty states invite one action.
- Voice has personality when the brand does: a confident line beats a neutral one, as long as it's clear.
