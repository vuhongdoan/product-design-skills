---
name: "design-review"
description: Critique and audit any digital product design, then fix it. Reviews screens, flows, prototypes, live sites, Figma files, screenshots or front-end code against real-life context, clarity, attention, motion, usability heuristics, accessibility and product psychology, and returns prioritized findings with severity and evidence, the root problems behind them, and a comparison of patch, restructure and rethink options. Can apply fixes to existing HTML, CSS or Figma without rewriting everything. Use this skill whenever someone shares a design or screenshot and asks for feedback, a critique, a UX review, heuristic evaluation, accessibility check, "what's wrong with this", "how can I improve this", "does this work", "make this less cluttered" or "simplify this", or wants a design checked before handoff or launch.
---

# Design review

A review is useful when it changes what gets built. That means findings the team can act on: specific, evidence-based, prioritized, and with a fix. Opinions about taste without a reason ("I'd use a different blue") waste everyone's time.

Read these before reviewing:
- `references/standards/budgets.md`: the four budgets are the backbone of every review.
- `references/standards/heuristics.md`: Nielsen's heuristics, severity scale and accessibility baseline.
- `references/standards/psychology-lens.md`: to explain *why* something fails.
- `references/standards/problem-solving.md`: to go from findings to root problems and genuinely different fixes.
- `references/standards/anti-patterns.md`: known failure patterns.
- `references/standards/navigation.md`: how people move through the product; its anti-patterns list.
- `DESIGN-CONTEXT.md` if it exists.

## 1. Understand before judging

Establish, from the brief or by asking once:
- **Who** uses this, **in what situation**, to **do what**?
- **What stage** is it (sketch, prototype, pre-launch, live)? Critique a sketch for structure, not pixels.
- **What kind of review** they want: quick gut check, full audit, accessibility check, or fix-it-now.

If there's no context and the person wants speed, state your assumptions at the top and go.

## 2. Walk the task

Don't review screens as posters. Pick the main task and walk it step by step as the user in the context brief, noting where you hesitate, guess, get lost, or would give up. A screen that looks fine alone can fail as part of a flow.

For images, look closely at the image itself. For live sites or code, open and use it if you can; take screenshots at phone and desktop widths. For Figma, read the frames and components if a Figma connection is available.

## 3. Evaluate

Go through these lenses in order. The first four are the budgets and matter most.

1. **Context**: does it work in the real situation? One-handed, interrupted, slow network, bright light, first time, large text? Are empty, error, loading and offline states designed?
2. **Comprehension**: five-second test. Is it clear what this is, what to do, and what happens next? Do labels use the user's words? Is interactivity obvious?
3. **Attention**: one primary action? One focal point? What's competing for attention that shouldn't be? Squint test.
4. **Motion**: does every animation tell the person something? Anything decorative, slow, or ignoring reduced motion?
5. **Navigation and wayfinding**: can people find this, reach it from where they are, and get back? Check entry points (tab, notification, deep link, search), back behaviour at every step, kept state (scroll, filters, drafts), dead ends, depth, stacked modals, and whether the current location is always clear. Look beyond the screen you were given: what does it do to the rest of the app's navigation?
6. **Usability heuristics**: Nielsen's ten, briefly.
7. **Accessibility**: contrast, target size, labels, focus, not colour alone, text scaling.
8. **Psychology and ethics**: which principles are helping or hurting? Any dark patterns?
9. **Character and craft**: is it unmistakably this product (cover-the-logo test), with a concept and a signature element? Does it feel current, or dated, generic or text-heavy? Then hierarchy, alignment, spacing rhythm, type scale and consistency. Fix clarity first, but a clear design that nobody remembers still needs work.

## 4. Write findings

Each finding follows this format:

```markdown
### [Short title of the problem]
**Severity**: 4 blocker / 3 major / 2 minor / 1 cosmetic
**Where**: [screen, element]
**What happens**: [the problem, from the user's point of view]
**Why it matters**: [principle or heuristic, tied to this specific case]
**Fix**: [concrete change, not "improve clarity"]
```

Rules:
- Be specific. "The Save button is below the fold on a 667px-tall phone" beats "the CTA is hard to find".
- Explain with principles, but don't pad: one or two per finding.
- Separate evidence from opinion. If something is a hunch, say so and suggest how to test it.
- Don't list twenty cosmetic items to look thorough. Group small issues.
- Critique the work, never the people. Assume good reasons behind every decision, and phrase findings as what happens to the user, not what the team did wrong.
- The budgets, heuristics and principles are your lenses, not the reader's vocabulary. Write findings in plain product language ("people can't tell which button starts their day") rather than framework labels ("attention budget: ❌").

## 5. Find the root problems and explore fixes

Findings are symptoms. First check the brief (gently: the team's instinct is usually pointing at something real): is the problem the team named ("it feels busy") the real one, or a symptom of something else ("the screen serves the business's promotions instead of the user's morning")? Then group the findings into the **2–3 root problems** behind them, and note each one's cost to users and to the business (lost retention, support load, conversion, trust) (for example: "the screen tries to do three jobs", "the product speaks in system vocabulary", "nothing was designed for the first morning"). Use the problem form from `references/standards/problem-solving.md`.

For the biggest root problem, run the loop in `problem-solving.md`. Don't just propose the obvious patch. Offer at least three genuinely different fixes:
- **Patch**: the smallest change within the current design.
- **Restructure**: a different layout, flow or information model for the same job.
- **Rethink**: a bold option that questions whether this screen or step should exist in this form (let the system decide, move it to another moment or surface, split or merge screens).

Compare them briefly for user value and business value (impact on the problem, the metric it moves, effort, risk, what it keeps from what already works), then recommend one from the intersection, stated in one sentence. Where the current design serves the business at users' expense, say so and show an option that serves both. It's often fine to recommend the patch now and the restructure next. Say so, and why.

## 6. Report

```markdown
# Design review: [what was reviewed]
_Context assumed: [who, situation, task]. Stage: [stage]._

## Verdict
Two or three sentences: does it do its job, and the biggest thing standing in the way.

## What already works (keep these)
3–5 specific strengths, each with why it works for the user. Name the element
("The streak number is the largest thing on screen, so progress reads in one glance"),
not generic praise ("clean design"). These are the things the next iteration must not lose.

## Root problems
1–3 root problems behind the findings, most important first.

## Options for [the biggest root problem]
Patch / Restructure / Rethink, one short paragraph each, a comparison table,
and the recommendation with its reasoning.

## Top fixes (in priority order)
1. ...
2. ...
3. ...

## All findings
(grouped by severity, using the finding format)

## What to test with users
-
```

"What already works" is not a courtesy. Teams redesign away their best decisions when nobody names them, and a review that only lists problems reads as "start over". Look for real strengths even in weak work: a good piece of copy, a sensible default, a clear structure in one section. If you truly find nothing, say what's salvageable.

Prioritize by severity × how many people hit it × how often. The top three fixes should be doable and make the biggest difference.

## 7. Fix mode (when asked to apply changes)

When the person wants fixes applied, not just listed:

1. **Work with what's there.** Keep the existing stack, framework, design system and brand. Don't migrate or rewrite from scratch.
2. **Fix in priority order**, and in this order of type: comprehension and flow issues first, then attention (remove and demote), then accessibility, then missing states, then motion, then character and visual polish.
3. **Remove noise, add character.** For cluttered designs, cutting competing elements, extra emphasis and decorative motion is usually the biggest win. For plain or generic designs, the fix is the opposite: a concept, real imagery, a signature element. Know which problem you're fixing.
4. **Small, reviewable changes.** Group changes by finding so each can be accepted or reverted.
5. **Verify** after changing: look at the result, re-run the five-second and squint tests, and check nothing that worked is broken.
6. **Report** what changed and what's left, mapped to the findings.

Don't fix a generic pattern by applying a different fashionable one. The fix comes from the context and the task.

## Quick review

For a fast gut check, skip the full report. Give: the verdict, what already works, the root problem with a one-line patch, restructure and rethink option, and the top three fixes.
