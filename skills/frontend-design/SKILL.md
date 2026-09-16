---
name: frontend-design
version: 1.0.0
description: >-
  Turn a product brief into a deliberate, non-generic interface: information architecture first,
  then a real design system, then composition, then craft details — with the AI-slop gate applied
  before anything ships.
category: design
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [frontend, design, ui, ux, layout, typography, colour, composition]
applies_to: [web, marketing-site, saas, dashboard, landing-page]
priority: 93
requires: [visual-design-research, design-systems, ai-slop-detection]
conflicts_with: []
estimated_tokens: 2630
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: The hierarchy rule
    anchor: "#the-hierarchy-rule"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: Anti-Patterns
    anchor: "#anti-patterns"
    purpose: pitfalls
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "Material Design 3 foundations"
    url: https://m3.material.io/foundations
    type: official-docs
    organization: Google
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
related_skills: [visual-design-research, design-systems, ai-slop-detection, motion-design, accessibility-audit, frontend-implementation]
related_repositories: [shadcn-ui/ui, radix-ui/primitives, tailwindlabs/tailwindcss, nextlevelbuilder/ui-ux-pro-max-skill]
tests: 22
---

# Frontend Design

## Purpose

Produce an interface that looks **designed** rather than **generated**. The difference is
not decoration; it is that every visual property traces to a decision about the content
and the user's task.

The failure this skill prevents: an agent asked to "build a landing page" emits the
highest-probability layout in its training distribution — hero, three cards, gradient,
testimonial strip — which is correct HTML, accessible, and completely indistinguishable
from ten thousand other pages.

## When to Use

```text
□ Designing any new page, screen or component set
□ Redesigning an existing surface
□ Choosing layout, type, colour and spacing before implementation
□ Reviewing a design for deliberate-ness (pairs with ai-slop-detection)
```

## When NOT to Use

```text
✗ Implementing an already-approved design — use frontend-implementation
✗ Data-dense internal tooling where the answer is "use the component library defaults"
✗ Anything where the visual system already exists and is documented — extend it, don't redesign it
```

## Inputs

```text
brief            the product, the user, the job to be done, the single most important action
content          the real content, not placeholders — design to actual copy lengths
constraints      brand, existing system, framework, budget, deadline
reference_set    2-4 products at the target quality level (from visual-design-research)
platform         devices, browsers, input methods (touch vs pointer changes everything)
```

**No real content, no design.** Designing against "Lorem ipsum" produces layouts that
break on first contact with truth.

## Workflow

```text
CONTENT → IA → HIERARCHY → SYSTEM → COMPOSITION → CRAFT → MOTION → SLOP GATE → VERIFY
```

### 1. CONTENT — inventory what actually exists

```text
For each view: what data, in what quantity, at what variance?
  • shortest plausible headline / longest plausible headline
  • empty state / one item / one hundred items / ten thousand items
  • missing field / error state / loading state / partial failure
```

Design for the variance, not the median. This single step removes most "it broke with
real data" failures.

### 2. IA — structure before pixels

```text
□ What is the user trying to do here? (one sentence, one verb)
□ What must be true for them to succeed? (information, controls, feedback)
□ What is the reading/action order?
□ What can be removed entirely?
□ How does this view connect to the next one?
```

Deliverable: a text outline of the view in priority order. Not boxes — priorities.

### 3. HIERARCHY — one primary thing per view

See [The hierarchy rule](#the-hierarchy-rule).

### 4. SYSTEM — tokens before components

Define, in this order, as actual values in a file:

```text
spacing     4 or 8 px base; the scale (0,1,2,3,4,6,8,12,16,24,32,48,64,96)
type        modular scale (1.2–1.333 for dense UI, 1.25–1.5 for editorial),
            sizes derived from it, line-heights paired to size, measure capped 60–75ch
colour      roles, not hues: background / surface / surface-raised / border /
            text-primary / text-secondary / text-disabled / accent / accent-hover /
            focus-ring / success / warning / danger — each with a contrast-checked pair
radius      one scale (e.g. 0, 4, 8, 12, 9999), applied by component class
elevation   shadow scale with ≥3 levels, plus a border strategy for dark mode
```

Rules: **every visual property comes from a token**; no magic numbers in components.

### 5. COMPOSITION — layout with intent

```text
□ Break symmetry deliberately: asymmetric grids, 2/3–1/3, offset anchors
□ Vary density between sections — narrative sections breathe, data sections compress
□ Give the most important element the most space AND the strongest contrast AND the
  largest type — all three, never one
□ Align to a real grid; make the grid visible in the code (CSS grid template, not margins)
□ Design the negative space as an element, not as leftover
□ At every breakpoint, re-decide the hierarchy — do not just stack the desktop order
```

### 6. CRAFT — the details that read as human

```text
□ Optical alignment over mathematical alignment (icons, caps, round shapes)
□ Consistent icon stroke weight and corner radius across the whole set
□ Type details: real hanging punctuation where editorial, tabular numbers in tables,
  proper minus signs, no double spaces, correct dashes and quotes
□ Colour details: shadows tinted with the surface hue, not pure black; borders darker
  in light mode and lighter in dark mode
□ Focus states designed, not defaulted
□ Empty states with a reason and a next action
□ Loading states that reserve space (no layout shift)
□ One signature element: something specific to THIS product (a data-driven visual,
  a real illustration, one distinctive interaction) — deliberately, not decoratively
```

### 7. MOTION

Apply [`motion-design`](../motion-design/SKILL.md): motion explains causality and state
change. Hierarchy of durations, `prefers-reduced-motion` path, no animation without a reason.

### 8. SLOP GATE

Run [`ai-slop-detection`](../ai-slop-detection/SKILL.md) DETECT on your own design.
**S1 count must be 0.** This is a blocking gate, not a review.

### 9. VERIFY

```text
□ Contrast: all text ≥ 4.5:1 (AA), large text ≥ 3:1, non-text UI ≥ 3:1 — measured, not eyeballed
□ Keyboard: every interactive element reachable and operable; focus order matches visual order
□ 360 px: nothing overflows, nothing becomes unreachable, tap targets ≥ 44×44 CSS px
□ 1440 px: measure stays ≤ 85ch, no orphaned columns
□ Real content: longest plausible strings, empty state, error state, 1000-row table
□ Reduced motion: usable and complete without animation
□ Dark mode: not inverted light mode — separate elevation and border strategy
□ No layout shift (CLS) from images, fonts or late data
```

## The hierarchy rule

For any view, exactly one element is primary. Everything else is subordinate, and the
subordination must be visible in **at least three** of:

```text
size        primary is largest by ≥1.5× the next step on the scale
weight      primary is heavier
colour      primary has the highest contrast against its surface
position    primary is first in the reading order for the locale
space       primary has more surrounding whitespace
saturation  primary may be the only saturated element
motion      primary may be the only thing that animates (sparingly)
```

If two elements compete, the user chooses neither. If nothing is primary, the user leaves.

Test: squint at the design (or blur the screenshot by 8 px). The primary element should
still be obvious. If it is not, hierarchy is broken — and no amount of detail will fix it.

## Failure Modes

```text
PLACEHOLDER DESIGN   Designing against fake copy; breaks on real content.
EQUAL-WEIGHT LAYOUT  Three things all trying to be primary.
DECORATION AS FIX    Adding gradients/blur/glow to solve a flat composition.
TOKEN THEATRY        Defining tokens and then hard-coding values in components.
DESKTOP-ONLY ORDER   Stacking the desktop hierarchy at 360 px.
DEFAULT FOCUS        Leaving the browser's focus ring on a custom dark surface.
SYSTEM-SWITCHING     Using one spacing scale on the left of the page and another on the right.
BLAND OVER-CORRECTION Removing all character after slop detection, leaving nothing memorable.
```

## Quality Checklist

```text
□ Real content inventory with variance (empty/one/many/error)
□ IA written as a priority list before any layout
□ Exactly one primary element per view, distinguishable in ≥3 dimensions
□ Spacing, type, colour, radius and elevation defined as tokens; components use only tokens
□ Composition breaks symmetry deliberately; density varies by section
□ Craft details applied (optical alignment, tabular numbers, tinted shadows, focus states)
□ One signature element specific to this product
□ Motion has a purpose and a reduced-motion path
□ Slop gate passed: 0 S1 symptoms
□ Contrast measured at all breakpoints; keyboard operable
□ Verified at 360 px, 768 px, 1440 px with real content and all states
□ Dark mode designed separately, not inverted
```

## Anti-Patterns

```text
✗ Hero + three equal cards + testimonial strip as the default answer to "landing page"
✗ Gradient text on a headline
✗ A blurred orb behind the hero
✗ 4 px here, 18 px there, 22 px somewhere else
✗ Six font sizes none of which come from a scale
✗ Four saturated accent colours
✗ `backdrop-blur` on the navbar, the cards and the modal
✗ Icons from two different sets with different stroke weights
✗ A "Trusted by 10,000+ teams" strip with no named teams
✗ Animating the hero on load for no reason
✗ Designing the happy path only
```

## References

- [`visual-design-research`](../visual-design-research/SKILL.md) · [`design-systems`](../design-systems/SKILL.md)
- [`ai-slop-detection`](../ai-slop-detection/SKILL.md) · [`motion-design`](../motion-design/SKILL.md)
- [`knowledge/ui-ux/what-makes-a-website-look-professional.md`](../../knowledge/ui-ux/what-makes-a-website-look-professional.md)
- [`knowledge/ui-ux/visual-hierarchy.md`](../../knowledge/ui-ux/visual-hierarchy.md)
- [`patterns/ui/`](../../patterns/ui/)
- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> (verified 2026-09-15)

## Related Skills

`visual-design-research` · `design-systems` · `ai-slop-detection` · `motion-design` ·
`accessibility-audit` · `frontend-implementation` · `data-visualization`

## Evaluation Criteria

```text
1. Slop gate: 0 S1 symptoms in the final design.
2. Hierarchy test: a reviewer identifies the primary element of each view without prompting.
3. Token compliance: 0 hard-coded spacing/colour/type values in components.
4. Accessibility: WCAG AA contrast + keyboard operability verified at all breakpoints.
5. Content robustness: design survives empty/one/many/error states without breaking.
6. Distinctiveness: a reviewer shown the design and 5 references cannot mistake it for
   a default template.
```

Test cases in [`tests/`](tests/).
