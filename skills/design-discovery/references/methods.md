# Research methods

## Contents
- Method picker
- Interview guide template
- Contextual inquiry guide template
- Screener pattern
- Survey rules
- Synthesis doc template

## Method picker

| Question | Method | Sample (rule of thumb) | Watch out for |
|---|---|---|---|
| What do people actually do, where? | Contextual inquiry, field observation | 5–8 sessions | Being in the room changes behaviour (Hawthorne effect) |
| How does behaviour change over days? | Diary study | 8–15 people, 1–2 weeks | Drop-off; keep entries tiny |
| Why do people do this? | Semi-structured interviews | 5–10 per segment | Stated reasons are post-hoc; probe stories |
| How many / how often? | Survey, product analytics | 100+ for rough proportions | Leading questions, social desirability bias |
| Can people use this? | Moderated usability test | 5 per round, iterate | Testing polish instead of the task |
| Will people want this? | Fake door, concierge, pre-order | Depends on traffic | Stated intent is weak evidence |
| What are people complaining about? | Support tickets, app reviews, sales notes | All of it | Loud minority; biased sample |
| How do competitors solve it? | Competitive teardown | 3–5 products | Copying their assumptions |

Numbers are rough heuristics for qualitative saturation or directional reads, not statistical guarantees.

## Interview guide template

```markdown
# Interview guide: [topic]
Decision this informs:
Research questions (3–5):

## Warm-up (5 min)
- Tell me a little about [relevant part of their life/work].

## Recent story (20 min)
- Tell me about the last time you [did the thing].
  - Where were you? What were you doing just before?
  - What did you use? What did you try first?
  - What was hardest? What did you do about it?
  - How did it end? How did you feel?

## Current workarounds (10 min)
- What do you do today when [problem]? Show me if you can.
- What have you tried that didn't work?

## Wrap-up (5 min)
- Anything I should have asked?
- Who else should I talk to?
```

Probes: "Why was that?", "Can you show me?", "What happened next?", "You said X, tell me more". Never "Would you use a product that...?".

## Contextual inquiry guide template

```markdown
# Field guide: [topic]
Setting: [where you'll observe]
Focus: [task or routine]

## Before
- What to bring (consent, recording, notes template)
- What to photograph (environment, tools, artefacts, workarounds) — with permission

## During
- Watch the task happen for real, as it normally would
- Note: environment, interruptions, devices, who else is involved, emotional moments
- Ask about what you see in the moment ("I noticed you...")
- Record what they DO separately from what they SAY

## After (within an hour)
- Top 3 surprises
- Context details for DESIGN-CONTEXT.md
```

## Screener pattern

- Screen on **behaviour**, not identity: "In the last month, how many times did you [behaviour]?"
- Include disqualifiers (works in the industry, participated recently).
- Hide the "right" answer: mix the target option among others.
- Aim for a spread across the variables that matter (experience level, device, frequency).

## Survey rules

- One idea per question; no double-barrelled questions.
- Neutral wording; balanced scales with a clear midpoint.
- Ask about specific recent behaviour, not general habits.
- Order: screener, context, core questions, one or two open questions, demographics last.
- Pilot with 3 people before sending.

## Synthesis doc template

```markdown
# [Study] synthesis
_Method, participants, dates_

## Summary
- Top 3–5 insights, one line each
- Recommendation

## Themes
### [Active theme label]
Insight statement.
Evidence (only where contested or surprising).
Design implication.

## Real-life context learned
(Also added to DESIGN-CONTEXT.md)

## Gaps and next research
```
