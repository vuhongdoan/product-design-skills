# Native and web code output

Besides the HTML prototype, Figma screens and spec, design-ui can deliver the design as **production-ready UI code**: native iOS, native Android, cross-platform mobile, or web. The design process is the same; only the last step changes. Code output is the design made real, so everything the design decided (tokens, spacing, states, navigation, accessibility, motion) must survive into the code, not be approximated.

"Production-ready UI" means real components, design tokens, every key state, navigation that works, and full accessibility support. Data and backend are stubbed behind a clear seam (a view model, repository, hook or provider with sample data), so a developer can wire the real source without touching the UI.

## Choosing the output

Infer the output from context, and ask only when it's genuinely unclear:

1. **A repo or project files in context** → match them: language, framework, version, folder structure, state management, styling approach, existing components and tokens. Never introduce a second UI framework or styling system into a project that already has one.
2. **The person names a platform or framework** ("an iOS app", "in Compose", "our Next.js site") → use it.
3. **The platform is known but the framework isn't** ("a mobile app") → ask once, offering: SwiftUI (iOS), Jetpack Compose (Android), Flutter or React Native / Expo (both platforms). If the person isn't available, choose Flutter or React Native for "both platforms", SwiftUI for iOS-only and Compose for Android-only, and state the assumption.
4. **No code requested and no project** → the default deliverable is still the HTML prototype. Offer code as a next step in the handover.

When code is the deliverable, still build the brand kit and hierarchy plan first. For brand-facing or new work, a quick HTML prototype or direction board before the code is worth it, because changing direction is cheaper there.

## What every code output includes

- **Tokens first.** One token file per project for colour (with light and dark), type scale, spacing scale (the product's, or the default 4 pt scale from `standards/whitespace.md`), radius, elevation and motion durations. Components read tokens; no raw hex values, font sizes or spacing numbers in views.
- **Components, then screens.** Reusable components for anything used twice (buttons, fields, list rows, cards, empty states). Screens compose them.
- **Every key state**: default, loading, empty, error, success, plus partial and offline where relevant. Each state is reachable through previews or sample data.
- **Navigation that works**: the app's real navigation structure (tab bar, stacks, sheets, routes), with back behaviour and the selected tab shown, as planned in the hierarchy step.
- **Accessibility built in**, using the platform's own APIs (see each section), checked against `standards/accessibility.md`.
- **White space from the spacing tokens only**, with the default minimums from `standards/whitespace.md`. Spacing adapts to screen size and text size without breaking.
- **Motion** limited to jobs from the motion budget, respecting the platform's reduce-motion setting.
- **Real copy** from the design, not placeholders, ready for localisation (strings in the platform's string resources where the project does this).
- **Previews**: per-screen previews of each state, in light and dark, and at the largest text size.
- **A short README**: how to run it, where tokens live, which seam to replace with real data, and any deliberate deviations from the design.

## SwiftUI (iOS)

- Swift with SwiftUI, targeting a current iOS version unless the project says otherwise. Use `NavigationStack`, `TabView` and `.sheet` for structure.
- Tokens in a `DesignTokens` (or `Theme`) namespace: `Color` assets or extensions with light and dark variants, a type scale built on `Font.TextStyle` so Dynamic Type works (custom fonts via `.custom(_:size:relativeTo:)`), and spacing constants (`Spacing.s4 = 16` and so on).
- Data through `@Observable` view models with sample data; views stay free of logic.
- Accessibility: `accessibilityLabel` on icon-only controls, `accessibilityHint` only when needed, grouped elements via `accessibilityElement(children:)`, headers marked with `.isHeader`, tap targets of at least 44×44 pt, layouts that hold at the accessibility text sizes (switch stacks to vertical with `ViewThatFits` or `dynamicTypeSize` checks), and `accessibilityReduceMotion` respected.
- `#Preview` blocks for each state, light and dark, and `.dynamicTypeSize(.accessibility3)`.

## Jetpack Compose (Android)

- Kotlin with Jetpack Compose and Material 3, unless the project uses something else. Navigation Compose for structure; `Scaffold` with the top app bar and navigation bar; edge-to-edge with window insets handled.
- Tokens in a custom `MaterialTheme` setup: `ColorScheme` for light and dark (dynamic colour only if the brand allows it), `Typography` in `sp`, and a spacing object exposed through a `CompositionLocal` (`LocalSpacing.current.s4`).
- State through a `ViewModel` exposing `StateFlow` UI state with sample data; composables are stateless where possible.
- Accessibility: `contentDescription` on meaningful images and icon buttons (`null` for decorative ones), `Modifier.semantics` for headings, state descriptions and merged elements, touch targets at least 48×48 dp, text in `sp` so font scaling works, and layouts that hold at 200% font scale.
- `@Preview` for each state, light and dark, and `fontScale = 2f`.

## Flutter

- Dart with Flutter, current stable. `MaterialApp` or `CupertinoApp` as the brand needs, with routing via the project's choice (default `go_router`).
- Tokens in `ThemeData` plus a `ThemeExtension` for brand colours and spacing (`context.spacing.s4`); text styles in the theme's `TextTheme`.
- State through the project's approach (default Riverpod) with sample data behind a repository.
- Accessibility: `Semantics` widgets for labels, headers and grouping, `tooltip` on icon buttons, minimum tap targets of 48×48, layouts that hold under `MediaQuery.textScaler` at 2.0, and `MediaQuery.disableAnimations` respected.
- Respect each platform's conventions where they differ (back behaviour, navigation patterns, scroll physics), rather than shipping one platform's look on the other.

## React Native / Expo

- TypeScript with Expo, unless the project is bare React Native. Expo Router or React Navigation per the project.
- Tokens in a `theme.ts` (colours for light and dark via `useColorScheme`, type scale, spacing scale, radius), consumed through a small hook; `StyleSheet.create` or the project's styling library.
- State through hooks with sample data behind a data module or query layer.
- Accessibility: `accessibilityLabel`, `accessibilityRole` and `accessibilityState` on interactive elements, `accessibilityRole="header"` for headings, `hitSlop` or sizing to reach 44×44 / 48×48, `allowFontScaling` left on and layouts that hold at large font scales, and `AccessibilityInfo.isReduceMotionEnabled` respected.
- Platform conventions where they differ (back gesture and button, sheets, haptics), using `Platform.select` sparingly.

## Web

- **Match the project**: its framework (React, Next.js, Vue, Svelte, Astro…), language, styling approach (CSS Modules, Tailwind, CSS-in-JS, plain CSS), component library and folder structure. Map the design's tokens onto the project's existing token system or Tailwind config rather than creating a parallel one.
- **No project**: React with TypeScript, styled with CSS custom properties for tokens (plain CSS or CSS Modules), and Vite as the build tool.
- Semantic HTML first: landmarks, one `h1`, ordered headings, real buttons and links, labelled inputs. ARIA only where native elements can't express the pattern.
- Responsive from 320 px up, with fluid type and section spacing via `clamp()`, and container queries where components move between contexts.
- Accessibility: visible focus, logical tab order, focus management for dialogs and route changes, `prefers-reduced-motion` and `prefers-color-scheme` respected, and layouts that hold at 200% zoom and with WCAG text-spacing overrides.
- Performance on a mobile network: optimised images with dimensions set, fonts with `font-display: swap`, no heavy dependency for a small effect.

## Checking code output

Before handing over:
- Run it, or at least build it, if the environment allows. Fix compile errors and warnings.
- Look at it: screenshots or previews at small and large screen sizes, light and dark, and the largest text size.
- Run the step 7 critique (including the white-space and accessibility checks) on the rendered result, not on the code.
- Search the code for raw colour values, font sizes and spacing numbers outside the token files, and replace them.
- Confirm every state and navigation path from the hierarchy plan is reachable.
