# Mobile apps

Phones are used in the least controlled conditions: moving, one-handed, in bright light, interrupted, on bad networks. Design for that first.

## Reach and touch

- Put frequent actions in the **bottom half** of the screen, within thumb reach. Top corners are hardest to reach on large phones.
- Primary actions go in a bottom bar, bottom sheet or a large button near the bottom, not a small top-right link.
- Targets at least 44×44 pt (iOS) or 48×48 dp (Android), with space between them.
- Destructive actions are never next to frequent ones.
- Support the platform's gestures (swipe back on iOS, system back on Android) and don't hijack them.

## Glanceability

- The most important information is readable in one glance, in a second or two.
- Large, high-contrast text for key numbers and status. Test in bright light.
- Short labels. If a label needs to wrap, reword it.
- Page margins of 16–24 pt and clear space between sections. Small screens tempt cramming; cut content, not space (see `standards/whitespace.md`).

## Interruption and resume

- Save progress continuously. Coming back after a phone call should land exactly where they left.
- Drafts are never lost when the app is backgrounded or killed.
- Long tasks can be split across sessions.

## Networks

- Show cached content immediately, then refresh.
- Optimistic updates for low-risk actions, with a clear rollback on failure.
- Say plainly what's offline and what will sync.

## Platform conventions

- **iOS**: tab bar (up to 5), navigation bar with back, large titles where appropriate, sheets for focused tasks, SF Symbols style iconography, Dynamic Type.
- **Android**: navigation bar, top app bar, predictable system back, Material components, font scaling, edge-to-edge layouts.
- Cross-platform apps: share structure and content, respect each platform's navigation and controls. Don't ship iOS controls on Android or the other way round.
- When the person asks for a native result (native-faithful prototype, SwiftUI or Jetpack Compose code), follow `native.md`.

## Permissions and notifications

- Ask for a permission at the moment it's needed, after explaining the benefit in-context.
- Notifications must be useful to the person, not to the metric. Let people control frequency and type.

## Motion on mobile

- System-like transitions (push, sheet, fade) that explain where things came from and went.
- Haptics for confirmation of important actions, used sparingly.
- Respect reduced motion and low-power modes.

## Mobile anti-patterns

- Hamburger menu hiding the main sections
- Onboarding carousels before any value
- Permission prompts on launch
- Tiny text links as primary actions
- Modals stacked on modals
- Forms without the right keyboard type, autofill or paste support
