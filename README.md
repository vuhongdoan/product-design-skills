# Product design skills

**Make your agents work like thoughtful product designers.**

Ask AI for a screen and you'll get one fast, but nobody asked if it was the right one, who it's for, or what happens when things go wrong. That's the work a thoughtful product designer does. This skill set carries it: it challenges the brief, plans every state, and hands the big decisions back to you.

Works with **Claude**, **Codex** and **Cursor**.

## How it works

You prompt your agent the way you normally would: "Build a medication reminder app", "Redesign our home screen". The `design-lead` skill takes it from there, and hands each stage to a specialist:

| Stage | Skill | What it does |
|---|---|---|
| 1 | [`design-lead`](skills/design-lead/) | Questions the brief, compares approaches, plans the work |
| 2 | [`design-discovery`](skills/design-discovery/) | Swaps guesses for evidence |
| 3 | [`design-flows`](skills/design-flows/) | Maps the steps, every state and the edge cases |
| 4 | [`design-exploration`](skills/design-exploration/) | Finds visual directions, then stops so you can choose |
| 5 | [`design-ui`](skills/design-ui/) | Builds the chosen direction into real screens |
| 6 | [`design-ux-writing`](skills/design-ux-writing/) | Writes the words: buttons, errors, empty states |
| 7 | [`design-system`](skills/design-system/) | Turns it into tokens and components |
| 8 | [`design-review`](skills/design-review/) | Checks it against the bar, then fixes it |

Two moments where the skills stop and wait for you, on purpose:

- **The lead asks before it builds.** It answers first, proposes its best guesses about who and what it's for, and raises the one thing worth checking.
- **Exploration ends with your choice.** It shows two or three genuinely different directions, and nothing gets built until you pick one.

Every skill holds its work to the same short standards (real life, clarity, attention, motion and character), so the work holds together from the first question to the final review. Each folder in `skills/` is a self-contained skill: a `SKILL.md` plus its references.

## Install

### With [skills.sh](https://skills.sh)

Install all eight for Claude Code:

```bash
npx skills add vuhongdoan/product-design-skills --skill '*' -a claude-code -g
```

For Codex or Cursor, swap the agent, or name several:

```bash
npx skills add vuhongdoan/product-design-skills --skill '*' -a codex -g
npx skills add vuhongdoan/product-design-skills --skill '*' -a cursor -g
npx skills add vuhongdoan/product-design-skills --skill '*' -a claude-code -a codex -a cursor -g
```

Install specific skills only:

```bash
npx skills add vuhongdoan/product-design-skills --skill design-lead --skill design-ui
```

Other useful commands:

```bash
npx skills add vuhongdoan/product-design-skills --list   # list available skills
npx skills update                                        # update installed skills
npx skills remove design-ui                              # remove a skill
```

Drop `-g` to install into the current project instead of for your user.

### Manually (Claude Code)

```bash
git clone https://github.com/vuhongdoan/product-design-skills.git
cp -R product-design-skills/skills/* ~/.claude/skills/
```

## Why these exist

Made for my own work first. Shaped by everyone who's tried it since.

It started as a way to work faster with AI. Now friends test it with me, and every round of feedback goes back into the skills. If something feels off or is missing, [open an issue](https://github.com/vuhongdoan/product-design-skills/issues).

— [Hong Doan](https://vuhongdoan.com)
