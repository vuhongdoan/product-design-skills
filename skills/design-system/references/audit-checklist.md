# Design system audit checklist

Report each area as ✅ present and good, ⚠️ present but inconsistent or incomplete, ❌ missing. Always give evidence (counts, examples, file locations).

## Foundations
- [ ] Colour: number of distinct values in use; greys from one family; one primary action colour; semantic naming; light and dark modes
- [ ] Contrast: all text/background pairs meet AA
- [ ] Typography: number of distinct sizes and weights in use versus the scale; line heights; platform scaling support
- [ ] Spacing: values in use versus the scale; off-scale values
- [ ] Radius and elevation: encode hierarchy, not one value everywhere
- [ ] Iconography: one set, one stroke weight, labelled where ambiguous
- [ ] Motion: tokenized durations and easing; reduced-motion handling

## Tokens
- [ ] Components use tokens, not hard-coded values (count hard-coded instances)
- [ ] Three-layer structure (primitive → semantic → component)
- [ ] Consistent naming convention

## Components
- [ ] Inventory versus what real flows need (missing and unused)
- [ ] Duplicates (several button or card styles doing the same job)
- [ ] States complete for each component
- [ ] Accessibility: names, roles, focus, target sizes
- [ ] Usage docs with when-not-to-use and do/don't

## Patterns
- [ ] Empty, loading, error, success patterns provided
- [ ] Forms: labels, validation, errors
- [ ] Navigation patterns per platform

## Budgets at system level
- [ ] Hard to put two primary actions on one screen
- [ ] Accent and emphasis are scarce by design
- [ ] Motion is restrained by default
- [ ] Defaults are accessible

## Governance
- [ ] Owner, versioning, changelog
- [ ] How to propose a new component
- [ ] Design and code in sync (Code Connect, Storybook or equivalent)

## Output

```markdown
# Design system audit: [product]
## Summary (top 3 issues, overall health)
## Findings by area (status, evidence, impact)
## Consolidation plan (what merges into what, in order, what breaks)
## Quick wins
```
