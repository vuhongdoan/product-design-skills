# States and edge cases

Design every state below for each screen, or mark it N/A on purpose. Most "finished" designs cover only the default state.

## Core states

| State | What to design | Common mistake |
|---|---|---|
| **Default** | Typical content, realistic data | Ideal data only (short names, round numbers) |
| **Empty (first use)** | Explain what goes here and give one action to start | A blank screen or "No items" with nothing to do |
| **Empty (cleared / no results)** | Say why it's empty and offer a way forward (clear filters, broaden search) | Same message as first use |
| **Loading** | Layout-shaped placeholder; for long waits, say what's happening | Spinner forever; layout jumps when content arrives |
| **Partial** | Some content loaded, some failed or pending | All-or-nothing |
| **Error** | What went wrong in plain words, what to do, keep user input | "Something went wrong", losing typed data |
| **Offline** | What still works, what's saved, what will sync | Silent failure |
| **No permission** | Why it's needed, what they lose without it, how to enable later | Asking on launch with no context |
| **Success** | Confirm specifically what happened, offer the next step | Vague toast, or no confirmation at all |
| **Disabled** | Why it's disabled and how to enable it | Grey button with no explanation |

## Edge cases checklist

**Content**
- Very long names, titles, translations (German, Finnish can be 30–40% longer)
- Zero, one, and very many items (1,000+)
- Missing images, odd aspect ratios, dark photos
- Unusual but valid input: emoji, accents, right-to-left text

**Time and interruption**
- Leaves mid-flow and returns later (minutes, days)
- Session expires mid-task
- App killed in the background
- Two devices at once

**Network and device**
- Slow network, flaky network, no network
- Small old phone, tablet, large desktop
- Large text size, screen reader, keyboard-only
- Low battery or power-saving mode (reduced animation)

**People**
- First-time user versus expert
- Made a mistake and wants to undo
- Changes their mind halfway
- Shared device or account

**Business rules**
- Limits reached (storage, plan, quota)
- Item deleted by someone else
- Price or availability changed between steps

## Writing state copy

- Errors: say what happened, why if useful, and how to fix it. "Photo too large. Choose one under 10 MB." Not "Oops!".
- Empty states: an invitation to act. "Add your first item to start planning outfits." Plus one button.
- Success: name the result with the same verb as the action. Button "Save outfit" → confirmation "Outfit saved".
- No exclamation marks by default. Calm and specific.
