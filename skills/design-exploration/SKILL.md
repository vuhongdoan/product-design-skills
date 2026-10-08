---
name: "design-exploration"
description: Explore distinctive visual directions and solution concepts for screens, pages and apps before anything is built. Asks about brand, positioning, competitors, taste and references, frames the problems, compares structurally different concepts and 2-3 creative directions informed by current trends, checks palette contrast, then stops for the person to choose a direction. Use this skill whenever someone asks for visual direction, a look and feel, mood boards, "make this look better", "more modern", "more creative", or wants to explore options for a screen, landing page, website, app or dashboard before committing. Once a direction is chosen, the work continues in design-ui.
---

# Design exploration

Exploration decides what the product should look and feel like, and which concept solves the problem, before anything is built. Its output is a choice: one direction the person has seen and picked. Building the screens comes after that choice, in `design-ui`.

Before exploring, read:
- `references/standards/budgets.md`: the quality bar, including section 5 on character.
- `references/standards/problem-solving.md`: frame the problems, explore several different ideas, compare and decide.
- `references/standards/anti-patterns.md`: both clutter *and* the safe, forgettable, dated failure.
- `references/creative-direction.md`: brand intake, concepts, directions, signature elements.
- `references/trends.md`: the current design landscape and how to use it.
- `references/standards/accessibility.md`: the accessibility check. Read it before choosing colour and type, because contrast is easiest to fix at this stage.
- `references/standards/whitespace.md`: density and spacing as part of each direction's character.
- The platform file that fits: `references/mobile.md`, `references/web-app.md` or `references/marketing.md`.
- `DESIGN-CONTEXT.md` if it exists.

If no flow exists and the request spans several screens, sketch the flow first (or hand off to `design-flows`).

## Process

### 1. Understand the product and the brand

Get the product context (who, what situation, what job, which platform) and the **brand context** (positioning, existing brand assets, personality, competitors, taste, appetite for boldness). The questions are in `references/creative-direction.md`.

- **If the person is available** and the work is brand-facing (a marketing page, first impressions, onboarding, a new product, a redesign): ask the intake questions in **one message** before designing, with proposed answers they can confirm. Designing a brand's face without asking about the brand produces generic work. Wait for the answer.
- **References**: ask for any apps, sites or visual work they like, and any they dislike, with a line on what works in each. Use them as taste signals, never as templates to copy.
- **If they aren't available**, or the work is a small change inside an existing product with a design system: proceed, and write your assumptions at the top of the work.
- **If there's an existing brand or design system**, work within it and push its expression, rather than inventing a new identity.

### 2. Frame the problems and explore solution concepts

Before any visual direction, run the loop in `problem-solving.md` on *what the screen or page has to achieve*:

- **Challenge the brief**: is the requested screen or page the right answer to the real problem? Write "What you asked" and "What I think sits underneath", and keep the challenge light: one or two points, kindly put. If you can, build what was asked and show the alternative next to it.
- **Problems**: what must this screen or page solve for the person, ranked, and which business outcome must it serve (conversion, activation, retention, trust)? What assumptions are baked into the request or the existing design ("it's a scrolling landing page", "the dashboard shows every metric", "sign-up comes first")?
- **Solution concepts**: at least three structurally different ways to solve them: different layouts of the job, interaction models or entry points, not different colours. For a landing page that might be a classic scrolling story, a single interactive tool that *is* the page, and a page built around one live demo. For an app screen: a list, a single focused card, a system-made suggestion with a swap.
- **Compare and pick** for user value and business value (see `problem-solving.md`). Choose from the intersection, state it in one sentence, and borrow the best parts of the runners-up. Reject concepts that convert by pressuring people.

If a design already exists, it's one concept to beat, not the starting point. Redesign requests especially deserve at least one concept that rethinks the structure instead of restyling it.

Creative directions (step 4) then give the chosen concept its look, voice and character.

### 3. Check what's current

Read `references/trends.md`. If you have web access, spend a few minutes checking current trends for this category and looking at 3–5 category leaders and recent award-winning work. Note what the category looks like, so you can decide whether to fit in or deliberately break from it. Trends are vocabulary: choose one or two that fit the concept, never a collage.

### 4. Creative directions

Develop **2–3 genuinely different directions** using the template in `creative-direction.md`: concept, colour, type, **density and spacing** (how much room the direction gives content, and why that suits the brand and context), imagery, signature element, motion, trend fit and risk. Directions may differ in how airy or compact they feel, but none may be cramped. Concepts come from the subject (place, materials, rituals, vocabulary, the product's own artifacts), not from a style list.

- Person available: show the directions as a quick visual board (one HTML page with a hero sketch or mini mood board each), recommend one, and let them choose.
- Person unavailable: pick the best fit, say why, and keep the others in the notes.

Check each direction against the defaults: "Would I have produced this for any similar brief?" If yes, push it further toward the subject.

**Accessibility pass 1**: before the person chooses, test each direction's palette and type pairing for contrast (text on background, text on brand colour, UI borders, focus ring, error and success) using computed ratios, not by eye. Adjust a direction that fails and note what you changed. A direction that only works with inaccessible colour is not a real option.

### 5. Hand over the choice

Present the directions (and any concepts still in play) and stop. Ask the person one question: which direction do they want, or do they want to mix elements from two? Don't build screens yet. Once they confirm, the work moves to `design-ui`, which takes the chosen concept and direction through the hierarchy plan, brand kit, build, critique and handover.

Hand over in a few lines: the concepts compared and what each one bets on, the directions with their risks, the one recommended and why, the accessibility pass 1 results (contrast ratios and what changed), the references the person gave and how they shaped the directions, and the questions still open for them to answer before building.
