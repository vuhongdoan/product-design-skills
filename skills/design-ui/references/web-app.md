# Web apps

Web apps are used for longer, more focused sessions, often by the same people every day. Speed, density and predictability matter more than first impressions.

## Structure

- Navigation shows where you are and what's available. Current location is always visible.
- URLs reflect state (filters, tabs, selected items) so people can share, bookmark and use the back button.
- One primary action per view. Bulk and secondary actions appear when relevant (on selection, in a menu).
- Density is fine when it serves repeated work. Density is not the same as clutter, and dense is not cramped: tight inside groups, clear gaps between groups, minimums from `standards/whitespace.md` still hold.

## Tables and lists

- Right-align numbers and use tabular figures. Left-align text.
- Sticky headers for long tables; sensible default sort; visible sort state.
- Empty, loading, filtered-to-nothing and error states for every list.
- Row actions visible on focus as well as hover (keyboard users).

## Forms

- Labels above fields, always visible. Placeholder text is not a label.
- Validate on blur or submit, not on every keystroke. Keep the user's input on error.
- Group related fields; ask only what's needed now.
- Support autofill and password managers; the right input types.
- Primary button says what happens; destructive actions confirm or offer undo.

## Dashboards

- Start from the questions the viewer needs answered, then pick the numbers. One dashboard, one purpose.
- Lead with the few numbers that drive decisions; details on demand.
- Every number has context: compared to what, over what period, good or bad.
- Avoid a wall of equal-weight cards.

## Keyboard and efficiency

- Everything works by keyboard; visible focus.
- Shortcuts and a command palette for frequent actions, without getting in novices' way.
- Remember the user's last choices (view, filter, sort).

## Responsive behaviour

- Decide what matters at each width, don't just stack everything.
- Test at 320 px wide and at 200% zoom.

## Web app anti-patterns

- Modal for every action
- Sidebar navigation with twenty equal items
- Spinners replacing the whole page for partial loads
- Hover-only controls
- Settings pages that are a flat list of every toggle
