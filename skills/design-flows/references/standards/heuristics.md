# Established heuristics

Use these alongside the psychology lens and the four budgets. They're well known, which makes them a shared language with teams and stakeholders.

## Nielsen's 10 usability heuristics (paraphrased)

1. **Visibility of system status**: keep people informed about what's going on, promptly.
2. **Match with the real world**: use the user's language and familiar concepts, in a natural order.
3. **User control and freedom**: clear exits, undo and redo; no dead ends.
4. **Consistency and standards**: the same thing works and is named the same way everywhere; follow platform conventions.
5. **Error prevention**: design out mistakes, and confirm before destructive actions.
6. **Recognition rather than recall**: keep options and information visible instead of relying on memory.
7. **Flexibility and efficiency**: shortcuts for experts that don't get in the way of novices.
8. **Aesthetic and minimalist design**: every extra element competes with the relevant ones.
9. **Help users recognize, diagnose and recover from errors**: plain language, the precise problem, and a way forward.
10. **Help and documentation**: ideally not needed; when needed, searchable, task-focused and brief.

Severity scale for findings (from Nielsen): **0** not a problem, **1** cosmetic, **2** minor, **3** major (fix before release), **4** catastrophic (blocks the task).

## Accessibility baseline (WCAG 2.2 AA, summarized)

This is a design-level summary, not a compliance audit. For formal compliance, test with real assistive technology and the full specification.

- **Contrast**: body text at least 4.5:1; large text (about 24px, or 18.5px bold) and essential UI graphics at least 3:1.
- **Not colour alone**: pair colour with text, icon or pattern for status, errors and charts.
- **Target size**: at least 24×24 CSS px (WCAG 2.2 minimum); aim for 44×44 pt on iOS and 48×48 dp on Android.
- **Text resizing**: layout survives 200% text size without losing content or function.
- **Reflow**: content works at 320 CSS px wide without horizontal scrolling.
- **Keyboard and focus**: everything works by keyboard; focus is visible and never hidden behind sticky elements.
- **Labels and names**: every input has a visible label; every icon button has an accessible name.
- **Errors**: identify the field, describe the problem in text, suggest the fix.
- **Motion**: respect reduced motion; nothing flashes more than three times a second.
- **Time limits**: warn and allow extension.
- **Authentication**: don't require memorizing or transcribing codes when an alternative exists (paste, passkeys, password managers).
- **Consistent help**: help is in the same place across screens.

## Platform conventions (short)

- **iOS (HIG)**: tab bar for top-level sections (up to 5), navigation bar with back, sheets for focused sub-tasks, swipe-back gesture must work, Dynamic Type support.
- **Android (Material 3)**: navigation bar or rail, top app bar, system back must behave predictably, edge-to-edge layouts, respect font scale.
- **Web apps**: URLs reflect state, the back button works, links are links and buttons are buttons, forms work with autofill and password managers.
- **Marketing sites**: one idea per section, the first screen says what it is and who it's for, the primary call to action is consistent, pages load fast on mobile networks.
