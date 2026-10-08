---
name: "design-flows"
description: Design user flows, journeys and information architecture for digital products and features. Frames the problems, compares several structurally different flow concepts before choosing one, maps the steps, decisions and screens a task needs, defines every state (empty, loading, error, partial, offline, first use), finds edge cases, places the feature in the whole app (entry points, back behaviour, app map), structures navigation, and simplifies flows with too many steps. Use this skill whenever someone asks to map a user flow, journey, onboarding, checkout, sign-up, settings or any multi-step task, plan screens for a feature, restructure navigation or IA, write a screen inventory, find edge cases, or asks "what screens do I need" or "how should this feature work", even before any visual design exists.
---

# Design flows

A flow is the design. Screens are how it's drawn. Most products that "look neat but are hard to follow" fail here: steps in the wrong order, decisions asked too early, states nobody designed, no plan for the person who leaves halfway and comes back, and features that make sense alone but are hard to find, reach or leave within the whole app.

Read `references/standards/budgets.md` (especially the context and comprehension budgets), `references/standards/problem-solving.md`, `references/standards/navigation.md` and `references/standards/psychology-lens.md` before starting. Read `DESIGN-CONTEXT.md` if it exists; if not, capture at least who the user is, their situation, and the job to be done before mapping anything.

## Problems and flow concepts first

Before mapping any single flow in detail, run the loop in `problem-solving.md`:

1. **Challenge the problem as handed over** ("What you asked" and "What I think sits underneath", raised kindly and briefly; see "How to challenge without overwhelming"), then **frame the problems** the flow must solve for the person, ranked, and the business outcome it should move (activation, retention, cost to serve...). List the assumptions baked into the request (for example "the user photographs each item", "the user must confirm every field", "this happens in the app").
2. **Explore at least three structurally different flow concepts**, each as a rough 3–6 step outline, and where it helps a quick wireflow from the renderer. Different structure means a different model, not the same steps reordered: one-by-one versus batch, capture now versus later, the user deciding versus the system deciding and the user correcting, in-app versus a widget, share sheet or email. Include the solid baseline and one bold concept that breaks an assumption.
3. **Compare** them for user value (solves the top problem, steps and decisions, real-life fit, recovery) and business value (the metric it moves, build and running cost, risk), and **pick from the intersection** where both are high. State the intersection in one sentence, and borrow the best parts of the other concepts.

Then map the chosen concept in full. If the request describes a specific flow, or a flow already exists, treat it as one of the concepts, not the answer.

## Pick the mode

| Request | Mode |
|---|---|
| "How should this feature work?", a new task to design | **Map** a flow |
| Navigation, menus, content organization, "where does this live" | **Structure** the IA |
| A flow exists and needs to be buildable | **Specify** screens and states |
| "This has too many steps", drop-off, a flow feels heavy | **Simplify** |

## Map

1. **Start from the goal and the trigger.** What does the person want, and what made them start right now? Where are they physically?
2. **List the happy path** as steps in the user's language: verb plus object ("Pick an occasion", "See three outfits"). Keep it to the fewest steps that complete the job.
3. **Mark decision points.** At each, ask: can we decide for them with a good default (default bias)? Can the decision be deferred until it matters (progressive disclosure)?
4. **Add the unhappy paths**: errors, cancellations, missing data, permissions denied, going back, leaving and returning. See `references/states-and-edge-cases.md`.
5. **Find the moment of value.** How many steps until the person gets something worthwhile (aha moment)? Move it earlier if you can. Ask for commitment (sign-up, permissions, payment) *after* value, not before, unless there's a real reason.
6. **Design the ending.** The last step is remembered (peak-end rule). It should confirm what happened, and offer one natural next step or a good place to stop.

Output a **visual flow** (see "Show the flow" below) plus a numbered step list with the purpose of each step. See `references/flow-notation.md` for conventions.

## Place it in the app (every mode)

A flow starts before its first screen and ends after its last. Using `navigation.md`, answer for the whole feature:

- **Where it lives** in the product's navigation model (tab, section, detail view, sheet, settings), and why that's where people would look for it.
- **Every entry point**: tab or menu, home card, search, notification, email or deep link, widget or share sheet, cross-links from other features, empty states, and resuming after an interruption. For each: where exactly people land, what context they need on arrival, and what back does from there.
- **Where people go next** after finishing, and how they get back to where they started.
- **Back behaviour at every step**, matching the platform (swipe-back, system back, browser back), and what state is kept (scroll position, filters, drafts, the tab's own stack).
- **Impact on the rest of the app**: does it add a tab, a badge, a home card or a menu item? What does that cost other features' attention and findability?
- **Findability tomorrow**: how would someone find this again without remembering the path?

Deliver an **app map** with the flow (see "Show the flow"): the product's top-level structure, where this work sits, its entry points and anything that moved. When navigation itself is the question, explore navigation models as concepts (for example a new tab versus a home card versus a contextual entry point) and compare them with the problem-solving loop.

## Structure

- Organize by **the user's tasks and mental model**, not by the company's teams or data model.
- Keep top-level navigation to the few things people do most (platform limits help: about five tabs on mobile).
- Name sections with words users would search for. If you can, test labels with card sorting or tree testing.
- Every screen answers "where am I, how did I get here, how do I get back?"
- Choose the navigation model deliberately (tab bar, hub and spoke, drill-down, sheets, search-first; see `navigation.md`) and respect the navigation budget: frequent tasks within one or two taps, three levels deep at most, one modal layer.
- Compare at least three structures before choosing (problem-solving loop), including one that removes or merges a top-level area.
- Output the app map and the rationale for each top-level item.

## Specify

Produce a **screen inventory** and a **state matrix** so nothing is designed for ideal conditions only.

For each screen:

```markdown
### [Screen name]
- **Purpose** (one sentence):
- **Arrives from** (all entry points) / **goes to**:
- **Back goes to** (and what state is kept on return):
- **Navigation chrome**: tab bar visible? full screen, pushed or sheet? title?
- **Primary action** (exactly one):
- **Secondary actions**:
- **Content and data shown**:
- **States**: default, empty, loading, error, partial, offline, first-use, no-permission (mark N/A deliberately)
- **Edge cases**: long text, many items, zero items, slow network, interrupted
- **Copy notes**: button labels say what happens; errors say what went wrong and how to fix it
```

Then a matrix of screens × states so gaps are visible. Hand it to `design-ui` for visuals.

## Simplify

First ask whether the flow should exist in this shape at all: could a different structure (see "Problems and flow concepts first") remove most of the steps rather than trimming them? Then, for each step, ask in order:

1. **Remove**: does the user need this step at all? Can we infer or default it?
2. **Combine**: can two steps become one without overloading the screen?
3. **Defer**: can it happen later, only when needed (after value, at first use)?
4. **Reorder**: would a different order match the user's mental model better?
5. **Simplify the step**: fewer fields, smart defaults, recognition instead of recall.

Watch for Tesler's law: complexity doesn't disappear, it moves. Don't "simplify" by pushing work onto the user or hiding something they need. State the before-and-after step count and what moved where.

## Show the flow (every mode that produces a flow)

People understand a flow by seeing it, not by reading a spec. Diagram source code (a Mermaid block in a markdown file) is not a visual: most viewers show it as code. Every flow you deliver comes with a **rendered visual** that someone can open and look at, and it's the first thing they see.

The visual has two parts:
1. **A wireflow**: low-fidelity screen thumbnails of the happy path, left to right, each labeled with its purpose and its one primary action. Seeing screens in sequence reveals problems a box diagram hides (a screen doing too much, a primary action that moves around, a step with nothing on it).
2. **The full flow diagram**: every screen and decision, with unhappy paths (errors, recovery, alternatives) drawn differently from the main path.

A third part appears when you include it in the spec: 3. **The app map**: the product's top-level areas, where this work sits, new or changed items highlighted, and the entry points into it.

To produce it, write a small JSON spec of the screens, transitions, entry points and app map, and run the bundled renderer:

```bash
python scripts/render_flow.py --spec flow.json --out flow.html --png flow.png
```

It creates a self-contained `flow.html` (works offline and in previews), a `flow.mmd` Mermaid file for pasting into docs or FigJam, and optionally a PNG screenshot. The spec format is documented at the top of the script. Screen `blocks` are rough layout hints (header, image, text, chips, input, list, button, link, sheet, tabbar), listed top to bottom. Keep them honest to the real layout: the primary button where the thumb reaches it, optional content collapsed.

If the person works in Figma or FigJam and a Figma connection is available, also offer the diagram there. If you can't run scripts, build the same two views by hand in one HTML file.

Order the deliverable: problems and the concepts compared (short), then the visual of the chosen flow, then the step list, then the screen specs and state matrix. Look at the rendered result before handing over: if the diagram is tangled, the flow probably is too.

## Real-life stress test (always run at the end)

Walk the flow as the person in the context brief and check:

- One-handed, on a small phone, in a hurry: are the main actions reachable and quick?
- Interrupted at any step: is progress kept, and is resuming obvious?
- Slow or no connection: what do they see, and what is saved?
- First time versus hundredth time: is it clear for the novice and fast for the expert?
- Screen reader and large text: does the order still make sense?
- Something went wrong: can they recover without starting over?
- Arriving from a notification or a shared link: do they land on the right thing, understand where they are, and does back make sense?
- Pressing back at every step, and switching tabs mid-flow then returning: is anything lost or surprising?
- Coming back tomorrow: can they find it again without remembering the path?

Report failures as fixes to the flow, not as caveats.

## Quality bar

- The problems are named and at least three structurally different concepts were compared before one was chosen.
- A rendered visual of the chosen flow, not just diagram code, with an app map showing where it lives and how people reach it.
- Every entry point, the back behaviour and the kept state are defined; no dead ends.
- One primary action per screen.
- Every state and edge case is designed or deliberately marked N/A.
- Steps and labels use the user's words.
- The flow survives the real-life stress test.
- No dark patterns: cancelling is as easy as starting, costs are shown before commitment.
