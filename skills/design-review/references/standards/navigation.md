# Navigation: how people move through the product

A screen or flow is never used alone. People arrive from somewhere (a tab, a notification, a link, a widget, a search), move between features, get interrupted, and come back. Designs that look right in isolation often fail here: the feature is impossible to find, the back button goes somewhere odd, a notification opens the wrong screen, or the person ends up in a dead end. Every skill in this set checks its work against the whole product's navigation.

## Contents
- The questions every design answers
- Navigation models
- The navigation budget
- Entry points
- Moving on and coming back
- Wayfinding
- Discoverability
- Platform conventions
- The app map deliverable
- Navigation anti-patterns

## The questions every design answers

For any screen, flow or feature, answer these before calling it done:

1. **Where does it live?** Which part of the product owns it: a tab, a section, a detail view, a sheet, settings?
2. **How do people get here?** All the entry points, not just the obvious one (see below).
3. **Where do they go next?** The natural next step, and how they get back to where they were.
4. **What does back do?** At every step, including after a deep link or a notification.
5. **What's kept?** Scroll position, filters, drafts, selected tab, when they leave and return.
6. **How would they find it again tomorrow** without remembering the path?
7. **What does this change elsewhere?** New tabs, badges, home cards or menu items affect every other feature's attention and findability.

## Navigation models

Choose the model from how people use the product, not from habit.

| Model | Good for | Watch out for |
|---|---|---|
| **Tab bar / bottom navigation** (mobile) | 3–5 top-level areas people switch between often | Tabs for rarely used things; more than 5; tabs that are actions |
| **Navigation rail / sidebar** (tablet, web apps) | Tools with several work areas; power users | 20 equal items; nesting three levels deep |
| **Hub and spoke** (a home that leads to tasks) | Products with one main dashboard or a daily routine | Home turning into a dumping ground for every team's module |
| **Stack / drill-down** (list → detail → sub-detail) | Browsing collections, hierarchical content | Depth beyond three levels; losing the list position on return |
| **Sheets and modals** | Focused, self-contained tasks (compose, confirm, pick) | Stacked modals; long flows inside a sheet; modals for things that deserve a page |
| **Command palette / search-first** | Large products, expert users, many objects | Being the only way to find things |
| **Linear wizard** | One-off setup, checkout | Using it for things people revisit and edit |

Most products combine two or three. Name the combination explicitly.

## The navigation budget

Defaults, not laws. Exceed them only with a reason.

- **Frequent tasks within one or two taps** from where people usually are. Measure frequency, don't guess: daily tasks near the surface, monthly ones can live deeper.
- **Three levels of depth at most** for anything people use regularly.
- **One modal layer at a time.** A modal that opens a modal is a sign the task needs its own screen.
- **3–5 top-level destinations** on mobile, consistent across every screen they appear on.
- **One way that's primary**, plus shortcuts. Multiple equal routes to the same place confuse people about where it "lives".
- **Every screen has a way out**, and none traps the person without an obvious back or close.

## Entry points

Design every way people arrive, not just the tab:

- Top-level navigation (tab, sidebar, menu)
- Home or dashboard cards
- Search results
- Push notifications, email and SMS links
- Deep links and shared links (from friends, social, marketing)
- Widgets, lock-screen and watch surfaces, app shortcuts, share sheets
- Onboarding and empty states pointing to it
- Other features linking in (cross-links, "see also", related items)
- Returning after interruption or relaunch (restoring where they were)

For each entry point, define: **where exactly they land** (the specific item, not a generic list), **what context they need** on arrival (they may not know where they are), and **what back does** from there (usually to the logical parent, not out of the app).

## Moving on and coming back

- **Next step**: after finishing a task, what's the natural next move? Offer it, plus a clear way back.
- **Back is predictable**: it returns to the previous logical place, with its state intact. Swipe-back (iOS) and system back (Android) must behave the same as the on-screen back.
- **Cross-feature movement**: when one feature links to another (outfit → item → outfits with this item), make the path reversible and don't create loops that bury the person.
- **State is kept**: returning to a list keeps the scroll position and filters; switching tabs keeps each tab's stack; drafts survive leaving.
- **Interruption and relaunch**: after a call or an app kill, return to the same place, or say clearly where they are.
- **Exits**: a good place to stop (peak-end), and a way to leave long flows without losing work.

## Wayfinding

At any moment people should be able to answer: *Where am I? How did I get here? Where can I go?*

- A clear title for every screen, in the user's words.
- The active tab or section is visibly selected.
- Breadcrumbs or a parent label in deep web hierarchies.
- Consistent placement of navigation chrome across screens.
- Transitions that show spatial relationships (pushing forward, sheets coming up from below) and match platform expectations.
- The same thing is called the same name in the navigation, the screen title and the buttons that lead to it.

## Discoverability

A feature people can't find doesn't exist.

- Put it where people would look for it, based on their mental model, not the org chart. Test with tree testing or first-click tests when unsure.
- Surface new or rarely used features at the moment they're relevant (contextual entry points), not with a tour on day one.
- Search should find features and settings, not just content.
- Don't hide primary features behind gestures, long-presses or unlabeled icons alone.

## Platform conventions

- **iOS**: tab bar for top-level areas; navigation stack with a back button labeled with the previous screen; swipe-back from the edge; sheets for focused tasks; tabs keep their own stacks.
- **Android**: navigation bar or rail; top app bar; system back and predictive back gestures; back from a deep link goes to the app's logical parent.
- **Web apps**: URLs for every meaningful state so back, refresh, bookmarks and sharing work; links are links, buttons are buttons; open-in-new-tab works for navigation.
- **Marketing sites**: a simple top navigation, the primary call to action always reachable, anchors for long pages, and a footer for the rest.

## The app map deliverable

When work adds or changes navigation (a new feature, a redesign, a new section), deliver an **app map**: a simple diagram of the product's top-level structure, showing
- where the new work sits,
- its entry points (marked by type: tab, notification, deep link, widget, cross-link),
- where people go next and back,
- anything that moved or changed.

Keep it to one screen. It can be a section of the flow visual (`design-flows` renders it with its script) or a small diagram in the doc.

## Navigation anti-patterns

- A new tab for every new feature
- Hamburger menus hiding primary areas on mobile
- Notifications and deep links that open a generic home instead of the item
- Back that exits the app, resets a form, or jumps to an unexpected place
- Losing scroll position or filters when returning to a list
- Modals stacked on modals; long flows trapped inside a sheet
- The same destination reachable through five different equal paths
- Dead ends: success screens and empty states with nowhere to go
- Feature names that differ between the menu, the title and the button
- Home screens that grow a card for every team's feature
