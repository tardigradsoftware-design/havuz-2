---
name: ai-slop-detection
version: 1.0.0
description: >-
  Detect, explain, fix and re-review the visual and structural signatures of AI-generated
  interfaces: generic layouts, decorative gradients, glassmorphism overload, fake metrics,
  inconsistent spacing, default typography and motion without purpose.
category: design
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [ai-slop, design, frontend, ui, ux, review, quality, visual-design]
applies_to: [web, marketing-site, saas, dashboard, landing-page]
priority: 90
requires: [visual-design-research, design-systems]
conflicts_with: []
estimated_tokens: 2513
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Detection catalogue
    anchor: "#detection-catalogue"
    purpose: implementation
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Failure Modes
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: Anti-Patterns
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: Evaluation Criteria
    anchor: "#evaluation-criteria"
    purpose: validation
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Apple Human Interface Guidelines"
    url: https://developer.apple.com/design/human-interface-guidelines/
    type: official-docs
    organization: Apple
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Reference for restraint, hierarchy and motion purpose. Not fetched in this run; verify before quoting specifics."
  - title: "Material Design — foundations"
    url: https://m3.material.io/foundations
    type: official-docs
    organization: Google
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Contrast and non-text-contrast thresholds used by the colour-discipline checks."
related_skills: [visual-design-research, design-systems, frontend-design, accessibility-audit, motion-design]
related_repositories: [shadcn-ui/ui, radix-ui/primitives, tailwindlabs/tailwindcss, GoogleChrome/lighthouse]
tests: 6
---

# AI-Slop Detection

## Purpose

Give an agent a **falsifiable vocabulary** for "this looks AI-generated", and a
mechanical path from detection to fix.

"Slop" is not a taste judgement. It is a set of measurable symptoms that appear when
an interface is generated without a design system: the model reaches for the most
probable visual tokens in its training distribution, and the most probable tokens are
the ones everyone else's model also reached for. The result is technically valid,
accessibility-passing, and instantly recognisable as machine-made.

This skill exists because the cheapest fix is *before* the design is built, and the
second cheapest is a structured audit immediately after.

## When to Use

```text
□ Reviewing any AI-generated landing page, dashboard, marketing site or app UI
□ Before shipping a design that was produced without a human designer
□ When a stakeholder says "it looks generic" and nobody can say why
□ As a gate in workflows/build-website before the visual sign-off step
□ When auditing an existing product for design-system drift
```

## When NOT to Use

```text
✗ Internal tools where utility is the only requirement — say so and move on
✗ Deliberately brutalist, maximalist or expressive designs: apply the craft checks
  (contrast, spacing consistency, hierarchy) but not the "restraint" checks
✗ As a substitute for accessibility-audit — this skill catches visual smell, not WCAG failures
✗ On a design system's own primitives: judge the composition, not the component library
```

## Inputs

```text
target        URL, screenshot set, or component source
intended_audience   who is this for, and what job are they doing
brand_constraints   existing palette, type, logo, tone (or "none")
reference_set       2-4 products whose quality level is the target (see visual-design-research)
breakpoints         the widths that must be reviewed (minimum: 360, 768, 1440)
```

## Required Context

```text
knowledge/ui-ux/what-makes-a-website-look-professional.md
knowledge/ui-ux/ai-slop-signature-catalogue.md
skills/design-systems/SKILL.md          (spacing, type and colour systems)
skills/motion-design/SKILL.md           (motion hierarchy and reduced-motion)
```

## Detection catalogue

Each symptom has an **ID**, a **detection rule** (something you can actually check), a
**severity**, and a **fix direction**. Severity: `S1` = instantly reads as AI-generated;
`S2` = reads as low-effort; `S3` = polish issue.

### Layout & composition

The full detail — every entry with its detection rule, severity and fix direction — lives in [`references/detection-catalogue.md`](references/detection-catalogue.md). Load it when this step is reached rather than keeping it in context for the whole run.

## Workflow

```text
DETECT → EXPLAIN → RECOMMEND → REWRITE → REVIEW
```

### 1. DETECT

Capture the target at every required breakpoint. Run the catalogue mechanically:

```text
□ Grep the source for the tell-tale tokens:
    backdrop-filter, bg-gradient-, linear-gradient, blur-, shadow-[0_0_...,
    animate-pulse, animate-bounce, from-indigo-, via-purple-, to-pink-,
    "Seamlessly", "Unleash", "Elevate", "10,000+", "AI-powered"
□ Measure: extract every distinct spacing value; count how many are not on a 4/8 px scale
□ Measure: extract every distinct font-size; check against a modular scale
□ Count: distinct saturated hues used at >10% of surface area
□ Screenshot diff: are ≥3 sections structurally identical?
□ Interaction pass: click everything; note decorative controls (S4)
```

Output a **symptom table**: `ID | evidence (file:line or screenshot) | severity`.

**Exit gate:** every symptom has concrete evidence attached. "Feels generic" is not evidence.

### 2. EXPLAIN

For each symptom, state *why it reads as machine-made* in one sentence, referencing the
underlying cause (probable-token default, missing design system, no content model).
Group symptoms by root cause — usually 3–5 causes explain 20 symptoms.

```text
Root cause A: no spacing system        → SP1, SP2, SP3, L5
Root cause B: decoration substituting for hierarchy → C1, C3, M1, M3
Root cause C: no content model         → X1, X2, X3, L6
```

**Exit gate:** every symptom maps to a root cause. Ungrouped symptoms mean the analysis is incomplete.

### 3. RECOMMEND

Produce a prioritised remediation plan:

```markdown
### CRITICAL (blocks ship)          — S1 symptoms, credibility and accessibility damage
### HIGH (ship-blocker for B2B)     — S1/S2 that break hierarchy or consistency
### MEDIUM                          — S2 polish
### LOW                             — S3
```

Each item: symptom ID → concrete change → estimated effort → expected effect.
Recommend the **smallest system change that removes the most symptoms** (usually:
define a spacing scale, a type scale, and a colour role set — three files).

### 4. REWRITE

Apply the plan. Order matters:

```text
1. Remove before you add. Deletion fixes more slop than any amount of new styling.
2. Establish the three systems: spacing scale, type scale, colour roles.
3. Enforce one relationship = one token.
4. Rebuild hierarchy: one primary element per view, then everything else subordinate.
5. Replace filler copy with specific, true statements.
6. Add motion only where it explains a state change; add prefers-reduced-motion.
7. Only then consider distinctive details (a real illustration, a data-driven visual,
   one signature interaction).
```

### 5. REVIEW

Re-run DETECT. Score:

```text
SLOP SCORE = (S1 × 3) + (S2 × 2) + (S3 × 1)
```

Report before/after. Also verify the fixes did not break:

```text
□ contrast still passes (WCAG AA) at all three breakpoints
□ layout still works at 360 px
□ nothing new became decorative-only
□ reduced-motion path still complete
□ design tokens actually used (no hard-coded values reintroduced)
```

**Exit gate:** S1 count is 0, or each remaining S1 has a written, accepted justification.

## Failure Modes

```text
TASTE-WASHING        Declaring something slop without evidence. Fix: symptom ID + file:line.
STYLE CONFORMISM     "Fixing" slop by applying a different cliché (e.g. brutalist-by-default).
                     Fix: derive choices from brand and content, not from a trending aesthetic.
OVER-CORRECTION      Stripping all character until the design is bland.
                     Fix: the goal is deliberate, not minimal. Keep one signature element.
TOKEN THEATRE        Creating design tokens nobody uses. Fix: grep for hard-coded values after.
SCREENSHOT-ONLY      Reviewing at 1440 px and missing 360 px. Fix: all required breakpoints.
FIXING SYMPTOMS      Re-colouring a gradient instead of asking why it exists. Fix: root-cause grouping.
```

## Quality Checklist

```text
□ Every symptom has an ID, evidence and severity
□ Symptoms grouped into ≤5 root causes
□ Remediation ordered CRITICAL → LOW with effort estimates
□ Deletion attempted before addition
□ Spacing scale, type scale and colour roles defined as tokens
□ One primary element per view; hierarchy enforced by size + weight + colour
□ All filler copy replaced with specific, verifiable statements
□ No decorative gradients, blur layers, floating shapes or glow shadows
□ Motion has a hierarchy and a prefers-reduced-motion path
□ Contrast verified with a tool at every breakpoint
□ Slop score before/after recorded; S1 count is 0
□ At least one deliberate, non-generic design decision is documented
```

## Examples

- [`examples/before-after-dashboard.md`](examples/before-after-dashboard.md) — an SaaS
  dashboard reduced from slop score 34 to 4 by deleting, not adding.
- [`examples/landing-page-rewrite.md`](examples/landing-page-rewrite.md)

## Anti-Patterns

```text
✗ Adding a gradient to "make it less flat"
✗ Adding a blurred orb behind the hero for "depth"
✗ Three equal feature cards because the content has three items
✗ Inter at 400/600 with 16/24/48 px because that is what the template shipped
✗ "AI-powered" badge on a form
✗ Animating the logo on page load
✗ Dark mode as a single neon accent on #0a0a0a with glow shadows
✗ Shipping decorative buttons to fill a layout gap
```

## References

- [`knowledge/ui-ux/ai-slop-signature-catalogue.md`](../../knowledge/ui-ux/ai-slop-signature-catalogue.md)
- [`knowledge/ui-ux/what-makes-a-website-look-professional.md`](../../knowledge/ui-ux/what-makes-a-website-look-professional.md)
- [`knowledge/ui-ux/what-makes-ai-websites-look-generic.md`](../../knowledge/ui-ux/what-makes-ai-websites-look-generic.md)
- [`skills/visual-design-research/SKILL.md`](../visual-design-research/SKILL.md)
- [`skills/design-systems/SKILL.md`](../design-systems/SKILL.md)
- [`agents/website-quality-reviewer/AGENT.md`](../../agents/website-quality-reviewer/AGENT.md)
- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> (verified 2026-09-15)

## Related Skills

`visual-design-research` · `design-systems` · `frontend-design` · `accessibility-audit` ·
`motion-design` · `code-review`

## Evaluation Criteria

```text
1. Detection recall: of the slop symptoms a human designer identifies, what fraction does
   the agent find? Target ≥ 0.8 on S1 symptoms.
2. Evidence precision: every reported symptom has a verifiable location. Target 1.0 —
   a symptom without evidence is a false positive by definition.
3. Fix effectiveness: slop score reduction after REWRITE. Target ≥ 70%.
4. No regression: contrast, responsive and reduced-motion checks still pass. Target 1.0.
5. Character preserved: a human reviewer confirms the result is deliberate rather than bland.
```

Test cases in [`tests/`](tests/).
