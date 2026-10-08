---
name: "design-ux-writing"
description: Write and review the words in a product, such as microcopy, button and link labels, headings, error messages, notifications, empty states, onboarding copy and tone of voice. Based on NN/g's UX writing guidance (scanning behaviour, plain language, tone, structure, short copy, error recovery). Use this skill whenever someone asks to write, rewrite, review or fix product text, button labels, error messages, empty states, notifications, onboarding copy, tone of voice or a content style, or says the words "feel off", "are unclear", or "don't match the brand". The design-lead routes here when the copy is the main job; design-ui uses it for the copy in every screen it builds.
---

# Design UX writing

UX writing is design with words. Every label, heading and message either helps a person do the next thing in their real situation, or it gets in the way. Write for the person's context and goal first, and for the brand second.

Source: NN/g's UX writing study guide (https://www.nngroup.com/articles/ux-writing-study-guide/). That guide links to detailed articles that aren't covered here. Where this skill gives examples or checklists, they are illustrative and labelled as such.

## Before writing: the brief

Answer these before drafting any copy:

1. **Who reads it**, and what they already know.
2. **Why they need it** right now: what they're trying to do.
3. **What they need to understand** to do it.
4. **What they do next**, and what happens if they don't.
5. **How they should feel afterwards**, and how they probably feel now (confused, stressed, excited, bored).
6. **Which tone fits this moment** (see Tone of voice).

If the brief is missing, ask once, in one message. If the person isn't available, write the copy and list the assumptions next to it.

## How people read the screen

- **Assume scanning.** Most people skim. The first words of headings, labels and links carry the most weight, so front-load the keyword.
- **Expect satisficing.** People take the first option that looks good enough. Make the right choice recognisable at a glance rather than hoping they read all the options.
- **Read closely only when something is at stake or unclear**: payments, deletion, consent, errors, and anything irreversible. Give those moments full sentences and clear consequences.
- **Test the scan.** Could someone who reads only the bold words and button labels still understand the screen and act correctly?

## Plain language

- Copy should be understood on the first reading, including by experts. Clear for a newcomer is clear for everyone.
- Cut vague and empty words. Example: "Manage your preferences" becomes "Choose which emails you get".
- Be brief, but not so brief that the meaning is lost.
- Test legibility and comprehension: read it aloud, or ask someone to explain back what the button will do.

## Tone of voice

Calibrate tone deliberately on four dimensions: **humour, formality, respectfulness and enthusiasm**. Decide each level for the specific moment, not once for the whole product.

- **Start from feeling.** Decide how the reader feels now and how they should feel after the screen. Research on how people actually read and feel is better than guessing.
- **Serious moments** (failed payments, lost data, health or safety, account lockouts): drop humour and enthusiasm. Keep respect and be direct.
- **Celebrations and onboarding**: enthusiasm can carry, as long as it stays clear.
- **Consistency across channels**: tone reflects the brand, so the app, emails, notifications and help pages should sound like the same company.
- **Assistant and AI chat copy**: match tone to context in the same way. A cheerful reply to a stressed question reads as careless.

## Jargon

The test is the audience's everyday vocabulary, not whether a word is technical. A term that the audience uses in their daily work isn't jargon for them. Experts can handle precise technical language, but it should still be clear and easy to scan.

## Structure

- **Most important information first** (inverted pyramid): the outcome or the decision, then the detail.
- **Plan with a content frame** before writing: list the sections, the purpose of each and the order. Write to the frame.
- **Chunk the text.** Short paragraphs, meaningful groups, clear breaks.
- **Use bullet lists sparingly**, for three or more genuinely parallel items that someone will scan.
- **Write numbers as numerals** on screen. Use unambiguous dates (for example "8 October 2026", not "10/8").
- **Progressive disclosure**: show the essentials first and reveal detail when the person asks for it.
- **Accordions** hide content. Avoid them for complex desktop content, where people need to compare. Use them where a long list of short items benefits from collapsing on a small screen.
- **Anchor links** help people jump to a section on long pages.

## Short copy

### Headings

- Lead with the keyword. "Delivery address" beats "Where should we send it?" when the person is scanning a form.
- Be specific. Headings are a first impression and a scanning aid at once.
- Passive voice is acceptable in a heading when it puts the key word first.

### Links

Good link text is **specific, sincere, substantial and succinct** (the "4 Ss" in the NN/g guidance).

- Avoid generic labels such as "Learn more" or "Get started" on their own.
- Treat a link as a promise. The page it leads to must deliver what the text says.
- People judge a link by the text around it, so make the link match the sentence it sits in.

Example: "Read our returns policy" beats "Click here".

### Buttons and command labels

- **Say what happens after the action.** "Save address" beats "Submit". "Delete 3 photos" beats "Delete".
- **Support the choice.** For destructive or costly actions, the label and the surrounding text should make the consequence clear before the person taps.
- **Keep labels short and consistent.** The same action should use the same words everywhere in the product.

### Tooltips

Use tooltips for short clarifications only. Don't hide anything a person needs to finish the task inside a tooltip, because many people never see it.

## Messages

### Notifications (orders, account activity, reminders)

Make them clear and timely. Say what happened, and the one thing the person might need to do next. Don't make them guess which account or order is affected.

### Error messages

An error message should help people recover. It should explain what went wrong and how to fix it.

- **Say what's wrong, in plain words.** Name the field or the action, not the system.
- **Say how to fix it.** Give the expected format, or the next step.
- **Keep what the person entered** wherever possible, so they don't retype it.
- **Don't blame or joke.** No apologies stacked on top of the instruction, and no humour at the person's expense.
- **Place the message where the eye is**: next to the field or at the top of the form, and don't rely on colour alone.

Example:
- Weak: "Invalid input."
- Better: "Enter a postcode with 5 digits, like 12345."

## Gaps in the source

- The NN/g guide gives no empty-state rules. Use the house rule: say what will appear here, and offer one action to fill it.
- The detailed button, CTA and error-message rules sit in the linked NN/g articles, which this skill doesn't include. Ask for them if you want the full detail applied.

## Review checklist

When reviewing copy, check:

- [ ] Can the screen be understood by reading only the headings, labels and bold words?
- [ ] Does every button and link say what will happen?
- [ ] Is there any generic label ("Learn more", "Click here", "Submit", "OK") left?
- [ ] Do errors say what went wrong and how to fix it, and keep what the person entered?
- [ ] Does the tone match the moment: serious when stakes are high, warm when it's safe?
- [ ] Is any jargon checked against the audience's everyday words?
- [ ] Is the most important information first?
- [ ] Are numbers and dates unambiguous?
- [ ] Do the same terms mean the same thing on every screen?
- [ ] Is each notification clear about what happened and what to do next?

## House style

These rules come from the design skills' copy rules, and they apply everywhere:

- Sentence case, plain verbs, active voice.
- A call to action says what happens ("Check my address").
- Confirmations echo the action in the person's words.
- Errors state the problem and the fix, without apology or jokes.
- Empty states invite one action.
- Voice has personality only when the brand does, and a clear line beats a clever one.

## Output

- **Rewrite**: give the new copy, then one short reason per change.
- **Review**: rank the issues by harm to the person (blocking first, then confusing, then polish). For each, give the screen, the problem and a fixed version.
- **New copy**: group it by screen, and name the screen and state for each line, so it can be dropped in place.

## How this connects to the other design skills

- **design-lead** routes here when the copy is the main job, and asks for the brief before drafting.
- **design-ui** uses this skill for the copy in every screen it builds, and sends copy-heavy flows here first.
- **design-review** checks copy against the review checklist above.
