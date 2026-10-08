# Native app results (iOS and Android)

Use this file only when the person asks for a native result: "native app", "SwiftUI", "Jetpack Compose", "make it feel like a real iPhone/Android app", "something my developer can build from", and similar. Otherwise mention in the handover that native output is available, in one line, and stop there.

Two native results are possible. When asked for "native", produce both unless the person names one:

1. **Native-faithful HTML prototype**: the same clickable prototype, rendered with real iOS and Android chrome, type, sizes and behaviour, so testers feel the actual platform.
2. **Native code**: SwiftUI (iOS) and Jetpack Compose (Android) screens that implement the chosen design, with the brand kit as native tokens.

Both follow everything else in this skill: the concept, the brand kit, the white space standard, accessibility and every key state. Read `mobile.md` first; it covers reach, glanceability and platform conventions.

## 1. Native-faithful HTML prototype

Build one file with a platform switch (iOS / Android) in the prototype chrome, clearly marked as not part of the product.

- **Frame**: iPhone at 393×852 pt and Android at 412×915 dp, with the status bar, safe areas and the iOS home indicator (34 pt) or Android gesture bar. Content never sits under them.
- **Type**: `-apple-system, "SF Pro Text"` on iOS and `Roboto` (or `"Google Sans"` where appropriate) on Android for system UI. Brand type stays for brand moments: headlines, hero numbers, the signature element. Body and controls use the system face unless the brand kit says otherwise.
- **Chrome per platform**:
  - iOS: navigation bar 44 pt, with large title (scrolling to a small title); back button showing the parent's name; tab bar 49 pt plus the home indicator; sheets with a grabber and detents; segmented controls, toggles and action sheets in iOS style.
  - Android (Material 3): top app bar 64 dp; navigation bar 80 dp; FAB where a single primary action fits; bottom sheets, filled and tonal buttons, switches, snackbars in Material style; system back returns predictably.
- **Behaviour**: push and pop transitions, sheets that slide up, a tab switch without animation, a pressed state on every control. Respect `prefers-reduced-motion`.
- **Spacing**: page margins of 16–20 pt on iOS and 16 dp on Android (24 dp on wider screens), all other values from the spacing scale.
- Keep it honest: it's a prototype that *looks* native. Say so in the handover.

## 2. Native code: SwiftUI and Jetpack Compose

### Scope
Build the screens of the chosen design, the navigation between them and every key state (default, empty, loading, error, success). Not networking, persistence or business logic: use sample data and closures/lambdas for actions, and say what's stubbed.

### Structure
Deliver one folder per platform:

```
ios/
  DesignTokens.swift      // Color, Typography, Spacing, Radius
  Components/             // buttons, cards, rows built from tokens
  Screens/                // one file per screen, with previews for each state
  SampleData.swift
android/
  ui/theme/Tokens.kt      // Color, Type, Spacing, Shape
  ui/components/
  ui/screens/             // one file per screen, with @Preview for each state
  SampleData.kt
README.md                 // how to drop the files into a project, what's stubbed
```

### Tokens
Translate the brand kit, including the spacing scale, into native tokens so values never appear as raw numbers in screens.

```swift
enum Spacing {
    static let s1: CGFloat = 4,  s2: CGFloat = 8,  s3: CGFloat = 12, s4: CGFloat = 16
    static let s5: CGFloat = 24, s6: CGFloat = 32, s7: CGFloat = 48, s8: CGFloat = 64
    static let s9: CGFloat = 96, s10: CGFloat = 128
    static let pageMargin = s4   // 16–20 pt; use 20 when the design needs more room
}
```

```kotlin
object Spacing {
    val s1 = 4.dp;  val s2 = 8.dp;  val s3 = 12.dp; val s4 = 16.dp
    val s5 = 24.dp; val s6 = 32.dp; val s7 = 48.dp; val s8 = 64.dp
    val s9 = 96.dp; val s10 = 128.dp
    val pageMargin = s4          // 24.dp on medium and expanded width classes
}
```

Colours as asset-catalog colours or `Color` extensions with light and dark values (iOS) and a Material 3 `ColorScheme` for light and dark (Android). Type styles map to Dynamic Type text styles (iOS) and a Material `Typography` in `sp` (Android) so they scale with the user's setting.

### White space in native code
The white space standard applies unchanged:
- `VStack(spacing:)`, `.padding()`, `Arrangement.spacedBy()` and `Modifier.padding()` take spacing tokens only.
- Inner space smaller than outer space: tight spacing inside a row or card, larger spacing between sections.
- Don't rely on default `List`/`Form` or `LazyColumn` padding when it fights the design; set it with tokens.
- Respect safe areas and window insets (`safeAreaInset`, `WindowInsets`), and keep extra room around the primary action.
- Layouts grow with text: no fixed heights on text containers.

### Navigation
- iOS: `NavigationStack` for hierarchy, `TabView` for top-level sections, `.sheet` with detents for focused tasks.
- Android: `Scaffold` with `NavigationBar` and `TopAppBar`, Navigation Compose for destinations, `ModalBottomSheet` for focused tasks, predictable system back.
- The navigation context from the hierarchy plan (where each screen sits, how people arrive) maps directly onto these.

### Accessibility
- iOS: Dynamic Type through text styles, `.accessibilityLabel` on icon-only buttons, `.accessibilityElement(children: .combine)` for rows, 44×44 pt targets, honour `accessibilityReduceMotion`, test with VoiceOver.
- Android: `sp` type that scales, `contentDescription` on icons (null for decorative), `Modifier.semantics` and `mergeDescendants` for rows, 48×48 dp targets, honour the system animation scale, test with TalkBack.
- States carry more than colour: icons and text for error, success and selection.

### Previews and verification
- A SwiftUI `#Preview` and a Compose `@Preview` for each key state, in light and dark, and at the largest text size.
- If a Swift or Kotlin toolchain is available, compile the code. If not, say plainly that it wasn't compiled, and keep the code conservative (standard APIs only, iOS 17+ and Compose Material 3) so it's likely to build first time.
- Code is a handoff for a developer to integrate, not a finished app. Say so in the README.

## Handover additions
Add to the handover: which native results were made, platform versions targeted, what's stubbed, whether the code was compiled, and any place where the two platforms deliberately differ.
