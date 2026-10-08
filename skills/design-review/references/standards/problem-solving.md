# Problems, ideas, decision

Weak design work accepts the problem it was handed, jumps to the first solution, or polishes whatever already exists. Strong work first checks that it's solving the right problem, then explores genuinely different ways to solve it, weighs them for both the people using the product and the business behind it, and commits to the option where the two meet. Every skill in this set runs this loop before it produces the main deliverable.

## Contents
- Scale it to the task
- How to challenge without overwhelming
- 1. Challenge the problem
- 2. Frame the problems, for users and for the business
- 3. Explore ideas
- 4. Compare and find the intersection
- Output format
- Traps

## Scale it to the task

- **Small** (one component, a copy fix, a single finding): a few lines. Check the problem, list 2–3 one-line options with their user and business upside, pick one.
- **Medium** (a screen, a flow, a page): the full loop, kept to about a page.
- **Large** (a product, a redesign, a system): the full loop, shown to the person as a visual comparison before building, when they're available.

The loop is thinking made visible, not paperwork. If a section adds nothing, keep it to one line.

## How to challenge without overwhelming

Challenging the brief and the status quo is part of the job. How you do it decides whether it helps. The person should come away feeling their thinking got sharper, not that it was marked wrong or that they now have homework. Keep challenging, and keep it light:

- **Start from what's right.** Name what's solid in their input before questioning it. There's almost always a good goal behind a request ("the investor is right that the free tier needs a real limit").
- **Curious, not corrective.** Frame challenges as questions or "what if", in plain words: "Before I design the cap, one thing worth checking: do most people ever reach 20 items?" Never "that's the wrong problem" or "actually, you should...".
- **Pick your battles.** Raise at most one or two challenges that would really change the outcome. Everything else goes into the reasoning further down, or is dropped. Ten small objections read as nitpicking.
- **Don't block the work.** Unless the challenge would make the work pointless, do what they asked *and* show the alternative next to it ("Here's the paywall at item 20 as asked, and a variant I think converts better. Happy to go with either."). They get their deliverable and a better option to consider.
- **Ask only when it matters.** If a reframe would change the work substantially and they're available, ask one short question, with your recommended answer, before going far. Otherwise proceed and flag it.
- **Tie it to their goals.** Challenge in terms of what they care about (their users, their metric, their deadline), not design principles for their own sake.
- **Respect constraints they don't control.** An investor, a boss or a team decision may not be theirs to change. Help them with it: give them the evidence or the words to take back ("If the investor asks, the case is...").
- **Proportionate.** A small task gets a one-line thought at most. A big bet (pricing, a redesign, a new product) deserves a fuller challenge.
- **Once they've decided, commit.** If they've heard the challenge and still choose their way, build it well and don't re-argue it. Record it under "Decisions already made" in `DESIGN-CONTEXT.md`. Only reopen it if new evidence appears, and say what changed.
- **Keep the heavy reasoning out of the way.** Put the answer and the one thing worth reconsidering first. Comparison tables and full reasoning come after, for those who want them.

Wording that works:
- "Before I dive in, one thing worth checking..."
- "I've done it as asked. There's also a version I'd consider, because..."
- "This part is solid. The piece I'd push on is..."
- "Your call. Here's what I'd weigh."

Wording to avoid: "Actually...", "The real problem is...", "You're wrong about...", "Have you considered..." repeated five times, and framework jargon.

## 1. Challenge the problem

The problem you're handed is a hypothesis, not a fact. Before solving it, test it. Ask:

- **Is it the real problem or a symptom?** "Users don't finish onboarding" might really be "users don't see why the app is worth setting up".
- **Whose problem is it?** The user's, the business's, or one team's? A problem only the business has ("we need more sign-ups") needs a matching user reason, or the solution will push people.
- **What's the evidence?** Data, research, support tickets, or someone's opinion? Say how confident we are.
- **What if we did nothing?** If the answer is "not much", the effort may belong elsewhere.
- **Is the solution hiding inside the problem?** "Users need a filter bar" is a solution in disguise. Restate it without the solution.
- **Is the scope right?** Too narrow (one screen, when the flow is broken) or too broad (the whole product, when one step is the issue)?
- **Is there a bigger opportunity next to it?** Sometimes the handed problem is small and the adjacent one is where the value is.

Write the result as **"What you asked"** and **"What I think sits underneath"**: the problem as it was handed over, and the problem as you now understand it. If they differ in a way that changes the work, follow "How to challenge without overwhelming": say it briefly and kindly, and either ask one question or do the work as asked plus the alternative. If the original problem holds up, say so in one line and move on. Don't reframe to show off.

## 2. Frame the problems, for users and for the business

Name the problems from both sides.

**For users**
- The person's problem, not the feature request: *[Who] struggles to [do what] when [situation], because [cause].*
- Rank 2–5 problems; say which ones this work addresses.
- Root causes: ask "why?" until you reach something designable.

**For the business**
- What outcome does the business need here? Acquisition, activation, retention, conversion, revenue per user, cost to serve (support, operations), differentiation, brand, strategic fit, or risk and compliance.
- How is the business model affected (subscription, marketplace, ads, one-off purchase, B2B seats)?
- Which metric would move if this worked? Name one primary metric and any guardrail metric that must not get worse (for example churn, refunds, complaints, support volume).
- Read the business section of `DESIGN-CONTEXT.md`. If it's empty, make a reasonable assumption and mark it.

**Constraints versus assumptions**: separate real constraints (platform, deadline, legal, budget) from inherited assumptions ("it has to be a screen", "the user must confirm every field", "the paywall comes first"). Assumptions are what the bold ideas get to break.

**Success**: what would be observably true for the person, and which business metric would move?

## 3. Explore ideas

Generate **at least three structurally different ideas** for the top problem(s). Different means a different approach, not the same layout with other colours. Always include:

1. **The solid baseline**: the best version of the conventional approach. It's often right, and it's the benchmark.
2. **A different structure**: a genuinely different model for the flow, screen, interaction or service.
3. **A bold idea that breaks an assumption**: what if the assumption from step 2 weren't true?

If there's an existing design, or the brief describes a solution, treat it as one input, not the answer. At least one idea must depart from it.

Think from both sides while generating:
- **User side**: what would make this effortless, clear, even delightful for the person in their real situation?
- **Business side**: what would make this sustainable, cheaper to run, more valuable or more defensible? Ideas that change pricing, packaging, service or operations count too.
- **Both**: where does something the user wants also produce something the business needs? (A faster add-item flow means fuller wardrobes, better outfit suggestions and more retention.)

### Ways to think out of the box

Use two or three per task. They're prompts, not a checklist.

- **Remove it**: what if this screen, step or setting didn't exist? Can the system decide, default or infer instead?
- **Change the moment**: solve it earlier, later, or at a different time (before the problem happens, at the moment it matters, in a weekly batch).
- **Change the surface**: a notification, widget, watch, lock screen, email, voice, a physical object, a human in the loop.
- **Invert it**: instead of the user doing X for the system, the system does X for the user; instead of asking, suggest; instead of configuring, undo.
- **Push to the extreme**: what if there were 10× the items, zero time, one thumb, no screen, no connection?
- **Borrow from another domain**: how would a game, a hotel concierge, a kitchen, a transit map or a bank solve this?
- **Reframe the question** at a different altitude: "How might we make adding clothes faster?" versus "How might we never need to add clothes by hand?"
- **Change the business model or service**: could pricing, packaging, a partnership or an operational change remove the problem the UI is fighting?
- **Constraint flip**: what if it had to work with no text at all, or in 5 seconds, or for someone who has never used an app?

Stay honest: a bold idea has to address the problem and survive the real-life context. It's there to widen the space, and sometimes it wins.

## 4. Compare and find the intersection

Compare the ideas side by side on **user value** and **business value**, plus feasibility.

| Group | Criterion | Question |
|---|---|---|
| User | Solves the top user problem | How much of it does it remove? |
| User | Real-life fit and clarity | Works in the context brief; understood without help |
| User | Effort for the person | Taps, decisions, typing, memory |
| Business | Moves the primary metric | Which metric, how much, how soon? |
| Business | Cost and sustainability | Build cost, running cost, support load, operations |
| Business | Differentiation and brand | Makes the product distinctive or defensible? |
| Both | Risk and evidence | How sure are we? What's the cost if it's wrong? |
| Both | Ethics | Does it help the person, or win for the business at their expense? |

Rate simply (strong / okay / weak, or 1–3) with one line of reasoning where it isn't obvious. Then place each idea on two axes, **user value** and **business value**:

| | Low business value | High business value |
|---|---|---|
| **High user value** | *User bet*: people love it, no clear business case yet. Keep it, look for the business angle, or run it as a small bet. | **The intersection**: the target. Choose from here. |
| **Low user value** | Drop it. | *Business-only*: works for the business at users' expense (pressure, dark patterns, lock-in). Reject, or redesign until users benefit too. |

**Define the intersection in one sentence**: *"People get [user value], and the business gets [business outcome], because [mechanism]."* For example: "People add a whole wardrobe in one sitting without typing, and we get fuller wardrobes that make outfit suggestions good enough to keep them coming back, because batch capture removes the per-item effort."

Then:
- **Pick one** from the intersection and explain why in two or three sentences.
- **Borrow** the best parts of the runners-up.
- **Name the metrics on both sides**: the user outcome to watch and the business metric to watch, plus the guardrail.
- **Say what would change your mind**, and how to test the riskiest assumption quickly.
- If nothing lands in the intersection, say so. Don't dress up a business-only idea as user-friendly; propose what would move a user bet toward a business case instead.
- If two ideas are close and the person is available, show both and let them choose.

## Output format

Answer first, reasoning after. The person should get the recommendation and the one thing worth reconsidering in the first few lines, without reading the analysis.

```markdown
## In short
[2–4 sentences: what we're going with and why, in plain words. If the brief was
challenged: what you asked for, what I'd consider instead, and whether I've done both.]

**One thing worth checking**: [the single challenge that matters most, as a question, or "none"]

---
## How I got here
### The problem
**What you asked**: ...
**What I think sits underneath**: ... (or "holds up as asked")

### Problems
**Users**: 1. ... 2. ...
**Business**: outcome needed, primary metric, guardrail
**Assumptions worth questioning**: ...

### Ideas
A. [Name] — the solid baseline
B. [Name] — a different structure
C. [Name] — the bold one: breaks "[assumption]"
(each: a short paragraph, with what it does for users and for the business)

### Comparison
| | A | B | C |
|---|---|---|---|
| User: solves the top problem | | | |
| Business: moves [metric] | | | |
| ... | | | |
| **Where it lands** | intersection / user bet / business-only | | |

### Decision
**The overlap**: People get ..., and the business gets ..., because ...
Borrowing [detail] from [Y]. Watch: [user outcome], [business metric], guardrail [metric].
We'd reconsider if ... Test first: ...
```

For a small task, the "In short" block alone is often enough. Then the main deliverable follows.

## Traps

- **Accepting the brief as given**: solving a symptom, or a solution in disguise, very well.
- **Reframing for its own sake**: second-guessing a well-founded problem wastes the person's time. Challenge, then commit.
- **Overwhelming the person**: many challenges at once, a lecturing tone, or pages of analysis before the answer. One or two challenges, kindly put, answer first.
- **Holding the work hostage**: refusing to do what was asked until the person agrees with the reframe. Do it as asked and show the alternative, unless doing it would clearly harm users.
- **User-only or business-only thinking**: a delightful idea nobody can pay for, or a profitable one users resent. Look for the overlap.
- **Fake options**: three variants of the same idea, or strawmen built to lose. Each option should be one a reasonable designer might choose.
- **Novelty for its own sake**: a bold idea that ignores the context or the budgets.
- **Anchoring on the existing design**: improving what's there when the real fix is structural.
- **Analysis paralysis**: more than four or five options, or a comparison longer than the work. Decide and move.
- **Hiding the loop**: deciding silently. The person should be able to see and challenge the reasoning.
