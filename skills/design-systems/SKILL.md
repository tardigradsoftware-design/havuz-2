---
name: design-systems
version: 1.0.0
description: >-
  Build and maintain a real design system — tokens, components, composition rules, documentation and
  governance — so visual consistency is enforced by structure rather than by review.
category: design
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [design-systems, tokens, components, consistency, governance, frontend]
applies_to: [web, saas, dashboard, design-system]
priority: 84
requires: [frontend-design]
conflicts_with: []
estimated_tokens: 2543
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Token architecture
    anchor: "#token-architecture"
    purpose: implementation
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "W3C Design Tokens Community Group — format module"
    url: https://tr.designtokens.org/format/
    type: specification
    organization: W3C
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Draft community-group specification for an interoperable token interchange format. Draft status: verify before depending on details."
  - title: "Material Design 3"
    url: https://m3.material.io/
    type: official-docs
    organization: Google
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
  - title: "Radix UI Primitives"
    url: https://github.com/radix-ui/primitives
    type: github-repository
    license: MIT
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [frontend-design, frontend-implementation, ai-slop-detection, accessibility-audit, motion-design]
related_repositories: [shadcn-ui/ui, radix-ui/primitives, tailwindlabs/tailwindcss, salesforce-ux/design-system, primer/react]
tests: 6
---

# Design Systems

## Purpose

Move consistency from a review activity to a structural property. A design system is not
a component library; it is the **decision layer** (tokens) plus the **implementation layer**
(components) plus the **rules** for how they compose, plus the governance that keeps them
from rotting.

The test of a real system: a new engineer can build a new screen that looks like it belongs,
without asking a designer.

## When to Use

```text
□ Two or more surfaces share visual language
□ The same visual bug keeps recurring in different places
□ A team is growing past the point where taste can be transmitted by conversation
□ Before a redesign, so the redesign is applied once rather than per-page
□ When hard-coded values have made theming or dark mode impractical
```

## When NOT to Use

```text
✗ A single page, a prototype, a one-off landing site — use tokens lightly, skip governance
✗ Before any design exists: a system codifies decisions, it does not make them
✗ As a substitute for shipping: an unpublished component nobody uses is worse than none
```

## Token architecture

Three tiers. Skipping the middle tier is the most common failure — it produces tokens
named after values (`blue-500`) used directly in components, which cannot be themed.

```text
TIER 1 — PRIMITIVE / GLOBAL      the palette and the scales, named by what they ARE
  color.gray.50 … color.gray.950
  color.brand.100 … color.brand.900
  space.0 … space.24              (4 or 8 px base)
  font.size.100 … font.size.900
  font.family.display / .text / .mono
  radius.none / .sm / .md / .lg / .full
  shadow.1 / .2 / .3
  duration.instant / .fast / .normal / .slow
  easing.standard / .enter / .exit

TIER 2 — SEMANTIC / ALIAS        named by what they MEAN; components use only this tier
  surface.background / .default / .raised / .sunken / .overlay
  border.default / .strong / .subtle / .focus
  text.primary / .secondary / .tertiary / .disabled / .inverse / .link
  action.primary.bg / .fg / .hover / .active / .disabled
  action.secondary.* / .danger.* / .ghost.*
  status.success.* / .warning.* / .danger.* / .info.*
  elevation.0 / .1 / .2 / .3

TIER 3 — COMPONENT-SPECIFIC      only where a component genuinely needs its own knob
  button.padding.x / .height.sm / .radius
  card.padding / .border
  table.row.height / .header.bg
```

Rules:

```text
1. Components reference tier 2 or 3 — never tier 1. (Tier-1 use in a component is a lint error.)
2. Every semantic token has a contrast-checked partner: text.primary on surface.default ≥ 4.5:1.
3. Dark mode is a second tier-2 mapping over the same tier-1 primitives — not a filter,
   not an inversion, and not a duplicate component set.
4. Token names describe role, not appearance: `border.subtle`, never `border-gray-200`.
5. Every token has one owner and one definition site. Two definitions of the same token is a bug.
6. Interchange format: W3C Design Tokens JSON where tooling supports it
   (draft spec — verify current status before depending on details).
```

## Workflow

```text
AUDIT → SYSTEMATISE → COMPONENTS → COMPOSE → DOCUMENT → ENFORCE → GOVERN
```

### 1. AUDIT
Extract every distinct value currently in use. Count them.

```text
□ distinct font sizes   □ distinct spacings   □ distinct colours
□ distinct radii        □ distinct shadows    □ distinct z-index values
□ near-duplicate components (same purpose, different implementation)
```

The audit table is the argument for the system: "we use 41 greys and 19 font sizes" is
more persuasive than "we need consistency".

### 2. SYSTEMATISE
Collapse the audit into the three tiers. Merge values within a just-noticeable difference
into one token. Record every merge as a mapping so existing code can be migrated mechanically:

```text
old value → token            (a codemod target list)
```

### 3. COMPONENTS
Build on unstyled, accessible primitives rather than from scratch — behaviour, focus
management and ARIA are solved problems (Radix, Headless UI, React Aria, Ark).

Per component, define and document:

```text
variants        the closed set (e.g. primary | secondary | ghost | danger)
sizes           the closed set (sm | md | lg) — not arbitrary props
states          default, hover, active, focus-visible, disabled, loading, error, selected
slots           what content can go where
composition     what it may contain and what it may never contain
a11y contract    role, keyboard interactions, announcements
do / don't       two concrete examples each
```

**Closed sets matter.** A component that accepts `style` or arbitrary padding will be
used inconsistently, and the system will lose.

### 4. COMPOSE
Document layout primitives separately from components: `Stack`, `Inline`, `Grid`, `Box`,
`Container`, `Section`, `Card`, `PageHeader`. Most inconsistency lives in layout, not in
components. Layout primitives take spacing tokens only.

### 5. DOCUMENT
Every token and component gets: what it is, when to use it, when not to, code, rendered
example, a11y notes, changelog. Documentation lives with the code and is published from it.

### 6. ENFORCE
Unenforced systems decay in one release cycle.

```text
□ lint/stylelint rules banning raw hex, px spacing and tier-1 tokens in components
□ CI check that every semantic token resolves in every theme
□ CI contrast check for every documented text/surface token pair
□ visual regression tests (Playwright + snapshots, or Chromatic/Percy)
□ codemod available for each token rename; deprecation warnings before removal
□ a "no new primitive" rule: additions require a proposal
```

### 7. GOVERN

```text
contribution    how anyone proposes a token/component (issue template → RFC → PR)
ownership       a named owner per component, and one system owner
versioning      SemVer on the system package; breaking token changes are major
deprecation     announce → warn for one minor → remove in the next major
adoption metric % of screens built from system components; tracked, published
release notes   every release lists added/deprecated/removed tokens
```

## Failure Modes

```text
TWO-TIER COLLAPSE     Skipping semantic tokens; components bind to palette values.
                      Fix: lint against tier-1 usage in components.
TOKEN PROLIFERATION   A token per screen. Fix: additions need a proposal and a reuse check.
UNENFORCED SYSTEM     Tokens exist; hard-coded values keep arriving. Fix: CI + lint.
ZOMBIE LIBRARY        Beautiful components nobody uses. Fix: adoption metric, and build
                      the system from real screens rather than in isolation.
VERSIONING BY VIBES   Renaming tokens without deprecation breaks every consumer.
DARK MODE AS INVERSION Filter-based dark mode with broken contrast and elevation.
OVER-ABSTRACTION      Configurable components with 40 props. Fix: closed variant sets.
DOCUMENTATION DRIFT   Docs describe a version that no longer exists. Fix: publish from code.
```

## Quality Checklist

```text
□ Audit completed with counts; the case for the system is quantified
□ Three token tiers defined; components reference only tier 2/3
□ Every semantic token has a contrast-checked partner in every theme
□ Dark mode implemented as a second semantic mapping
□ Components built on accessible unstyled primitives; closed variant/size sets
□ All states implemented: hover, active, focus-visible, disabled, loading, error, selected
□ Layout primitives documented separately from components
□ Do/don't examples for every component
□ Lint + CI enforcement live (no raw values, tokens resolve, contrast passes)
□ Visual regression tests running on every component
□ Codemod + deprecation path defined for renames
□ Named owner per component; contribution and versioning policy written
□ Adoption metric tracked and published
```

## Anti-Patterns

```text
✗ `--blue-500` used in a component instead of `--action-primary-bg`
✗ A `<Button variant="custom" style={{...}} />` escape hatch
✗ Building the system for six months before shipping a single screen with it
✗ Two "Button" components in the same codebase
✗ Renaming a token in the same commit that removes the old one
✗ Documenting components with screenshots of a design file that has since changed
✗ Dark mode via `filter: invert(1)`
```

## References

- [`frontend-design`](../frontend-design/SKILL.md) · [`frontend-implementation`](../frontend-implementation/SKILL.md)
- [`ai-slop-detection`](../ai-slop-detection/SKILL.md) — the enforcement target
- [`accessibility-audit`](../accessibility-audit/SKILL.md) · [`motion-design`](../motion-design/SKILL.md)
- [`patterns/frontend/`](../../patterns/frontend/) · [`patterns/ui/`](../../patterns/ui/)
- W3C Design Tokens format (draft) — <https://tr.designtokens.org/format/>
- Material Design 3 — <https://m3.material.io/> · Radix Primitives — <https://github.com/radix-ui/primitives>
- Reference systems in [`indexes/best-of.md`](../../indexes/best-of.md): shadcn-ui/ui, primer/react, salesforce-ux/design-system

## Related Skills

`frontend-design` · `frontend-implementation` · `ai-slop-detection` · `accessibility-audit` ·
`motion-design` · `refactoring`

## Evaluation Criteria

```text
1. Token compliance: 0 raw colour/spacing/type values in component code.
2. Contrast coverage: 100% of documented text/surface pairs pass AA in every theme.
3. Adoption: % of screens composed from system components (target ≥ 80% within 2 quarters).
4. Consistency: distinct visual values per property decrease monotonically over releases.
5. Onboarding: a new contributor builds a compliant screen without designer intervention.
6. Change cost: a global retheme lands in ≤1 day of work.
```

Test cases in [`tests/`](tests/).
