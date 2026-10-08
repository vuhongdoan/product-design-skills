---
name: "design-discovery"
description: Frame product problems and run design discovery for working designers. Covers problem statements, jobs to be done, assumption mapping, choosing research methods, interview and contextual-inquiry guides, screeners, synthesizing notes into themes and insights, and turning insights into prioritized opportunities. Use this skill whenever someone is figuring out what to build or why, has raw research notes, interview transcripts or survey results to make sense of, wants to validate an idea or assumption, asks "is this a real problem", "who is this for", "what should we research", or needs a problem brief before designing, even if they don't say "discovery" or "research".
---

# Design discovery

Discovery decides whether the rest of the design work is aimed at something real. Its job is to replace assumptions with evidence, and to capture the **real-life context** people will use the product in, because that context is what most designs get wrong.

Read `references/standards/context-brief.md`, `references/standards/problem-solving.md` and `references/standards/psychology-lens.md` (especially the ethics rule) before starting. If `DESIGN-CONTEXT.md` exists, read it; update it at the end with what you learned.

## Pick the mode

| The person has... | Mode |
|---|---|
| An idea or a request, and little evidence | **Frame** |
| Questions they need answered | **Plan research** |
| Notes, transcripts, survey data, tickets, reviews | **Synthesize** |
| Insights, and needs to decide what to design | **Prioritize opportunities** |

Modes chain naturally: frame, then plan, then synthesize, then prioritize. Start wherever the person is.

## Frame

Produce a one-page **problem brief**. Start by challenging the problem you were handed: write "What you asked" and "What I think sits underneath" (see `problem-solving.md`), with the evidence for each. Challenge the way that guide describes: kindly, one or two points that matter, answer first.

1. **Problem statement** from the user's point of view: *[Who] needs a way to [do something] when [situation] because [reason], but today [what gets in the way].* Avoid solutions in the statement.
2. **Job to be done**: *When [situation], I want to [motivation], so I can [outcome].* Write it in the words a user would use.
3. **Real-life context**: where, when, hands and attention, state of mind, constraints (see the context brief). Include how people move between tasks and tools today: what they switch between, where they start, what brings them back, and where they get lost.
4. **Assumption map**: list the assumptions the idea depends on, and sort them by *how much the idea depends on it* and *how much evidence we have*. The high-dependence, low-evidence ones are what to test first.
5. **Business outcome**: which business result this problem affects (acquisition, retention, revenue, cost to serve) and the metric that would show it.
6. **What we'd need to believe** for this to be worth building, and the cheapest way to find out.

Push back gently on solution-first framing. "Users need an AI outfit generator" is a solution. The problem might be "people with full wardrobes still feel they have nothing to wear on busy mornings".

## Plan research

Choose methods by the question, not by habit. See `references/methods.md` for a method picker, guide templates and screener patterns.

- Questions about **behaviour in context** (what people actually do, where, with what) → contextual inquiry, diary studies, observation. These are the best sources for real-life context.
- Questions about **why** → interviews.
- Questions about **how many / how often** → surveys, analytics.
- Questions about **can they use it** → usability tests (hand off to `design-review` for the evaluation frame).
- Questions about **will they want it** → fake-door tests, concierge tests, pre-orders; stated intent in interviews is weak evidence.

Every plan states: the decision it informs, the questions, the method and why, who to recruit (screener), how many sessions, and what result would change the decision.

Interview guides ask about **past behaviour, not future intentions** ("Tell me about the last time you..." rather than "Would you use..."). Avoid leading questions. Ask for stories and specifics.

## Synthesize

1. **Read everything first.** If only a fragment was shared, ask for the rest or say the synthesis is partial.
2. **Pull observations** as atomic notes: one fact, quote or behaviour per note, tagged with its source.
3. **Cluster** into themes with active labels: "People plan outfits the night before, not the morning of", not "Planning".
4. **Write insight statements**: *[Who] [does or believes X] because [underlying reason], which means [implication for the design].*
5. **Separate what people do from what they say.** When they diverge, trust behaviour and note the gap.
6. **Count honestly**: "most" (a clear majority), "several" (a few), "one participant". Never inflate. Never invent quotes, behaviours or numbers.
7. **Show evidence where it's contested or surprising.** Clean confident summaries elsewhere.
8. **Note navigation evidence**: where people looked for things and didn't find them, paths they took, what they bookmarked, searched for or asked support about. It feeds `design-flows` and the app map.
9. **Capture context details** (places, devices, interruptions, emotions) into `DESIGN-CONTEXT.md`.
10. **Name the gaps**: what the data doesn't tell us, and how to find out.

Deliver as a synthesis doc: summary of top insights, themes with evidence, implications for design, open questions, and suggested next research.

## Prioritize opportunities

Turn insights into **How might we** questions at more than one altitude (narrow: "make adding an item faster"; broad: "never need to add items by hand"). Then, for the top two or three, run the loop in `problem-solving.md`: sketch at least three genuinely different solution ideas each, including one that breaks an assumption in the current product or the request, and compare them. Don't let the existing product or the requested feature quietly become the only option.

For each opportunity, note:

- The insight it comes from
- Who benefits and how often they hit the problem (user value)
- What it does for the business, and which metric it moves (business value)
- Whether it sits in the intersection of both, or is a user bet or a business-only idea
- Evidence strength (strong, some, assumed)
- Rough effort and risk
- The ideas considered, how they compare, and the one worth testing first
- The smallest thing we could design to test it

Recommend a short list (two or three), not a ranked list of twenty. Explain the trade-offs. Hand the chosen opportunity to `design-flows` with the problem brief attached.

## Quality bar

- Every claim traces back to evidence or is marked as an assumption.
- The real-life context is specific enough to design against ("on the tram, one-handed, 2 minutes").
- Psychology is used to understand people, never to plan how to pressure them.
- The output ends with what to do next and what would change the recommendation.
