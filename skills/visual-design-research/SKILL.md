---
name: visual-design-research
version: 1.0.0
description: >-
  Build an evidence-based visual direction before designing: collect references, decompose them
  into transferable principles, define the target aesthetic in writing, and derive a system from it.
category: design
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [design-research, references, aesthetics, moodboard, visual-direction, ui]
applies_to: [web, marketing-site, saas, dashboard, landing-page, brand]
priority: 86
requires: []
conflicts_with: []
estimated_tokens: 2513
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Decomposition template
    anchor: "#decomposition-template"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Awwwards"
    url: https://www.awwwards.com/
    type: gallery
    organization: Awwwards
    confidence: medium
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Reference pool. Award sites skew toward expressive work; filter by product type."
  - title: "Godly"
    url: https://godly.website/
    type: gallery
    confidence: medium
    claim_type: recommendation
    verified_at: 2026-09-15
related_skills: [frontend-design, design-systems, ai-slop-detection, competitive-analysis]
related_repositories: [nextlevelbuilder/ui-ux-pro-max-skill, Leonxlnx/taste-skill, blader/humanizer]
tests: 6
---

# Visual Design Research

## Purpose

Replace "make it look good" with a **written, defensible visual direction** derived from
real references. Design quality is mostly a research problem: agents produce generic
output because they skip the step where a human designer would look at twenty things
before drawing one.

Output: a *Design Direction Brief* — references, extracted principles, an explicit
aesthetic statement, and the constraints that follow from it.

## When to Use

```text
□ Starting any visual design without an established system
□ A redesign where "modernise" is the only instruction
□ Choosing between several plausible aesthetics
□ Before frontend-design's SYSTEM stage, to decide what the system should express
□ When a stakeholder cannot articulate what they want but can point at what they like
```

## When NOT to Use

```text
✗ A brand book already exists — read it, do not research around it
✗ Extending an existing product surface: research the product, not the internet
✗ Purely functional internal tooling
✗ When the deadline allows no research: say so, pick the safest conventional direction,
  and record that it was unresearched
```

## Inputs

```text
product          what it is, who uses it, in what emotional register (trust? delight? speed? calm?)
audience         technical level, expectations, device context
competitors      3–6 direct competitors (what the category looks like — and what to avoid)
constraints      brand assets, accessibility level, framework, performance budget
differentiator   the one thing this product does that the category does not
```

## Workflow

```text
FRAME → COLLECT → DECOMPOSE → CLUSTER → POSITION → STATE → DERIVE → VALIDATE
```

### 1. FRAME
Write the intended impression in three adjectives and one sentence, before looking at
anything. This is the filter, not the conclusion — but without it you will collect
randomly.

```text
Example: "precise, quiet, engineered. A tool that feels like it was made by people who
care about measurement, not marketing."
```

### 2. COLLECT
Gather 15–30 references across **four pools**, not one:

```text
in-category       direct competitors and adjacent products (what "normal" looks like)
out-of-category   products from other domains that share the intended register
                  (instrument panels, scientific software, print, industrial design,
                   architecture, typography specimens)
aspirational      award galleries and known-excellent work — filtered by product type,
                  because an award-winning agency site is a bad reference for a data tool
anti-references   3–5 things that represent what you must NOT look like (including
                  the AI-slop signatures in ai-slop-detection)
```

Capture each reference with: URL or image, product type, why it was collected (one line).

**Budget:** 15–30 references, 4 pools. Fewer than 10 and you are decorating an opinion;
more than 40 and you will not decompose them properly.

### 3. DECOMPOSE
For the 5–8 strongest references, fill the [decomposition template](#decomposition-template).
Decomposition is the whole skill — a moodboard without decomposition transfers nothing.

### 4. CLUSTER
Group the extracted decisions. Patterns that recur across ≥3 references are *category
conventions* (safe, expected, unremarkable). Patterns that appear once, in a reference
you rated highly, are *candidate differentiators* (risky, memorable).

```text
convention    → adopt the ones that serve usability; you may break the ones that only serve sameness
differentiator → choose at most TWO; more than two becomes incoherent
```

### 5. POSITION
Plot the category on two axes that matter to your product (e.g. *dense ↔ spacious*,
*expressive ↔ restrained*, *warm ↔ clinical*, *playful ↔ serious*). Place your
competitors, then place yourself deliberately — not in the biggest gap (gaps are often
empty for reasons), but in a defensible position consistent with step 1.

### 6. STATE
Write the Design Direction Brief:

```markdown
## Design Direction — <product>
Intended impression: <3 adjectives + 1 sentence>
Position: <axis coordinates and why>
Aesthetic: <named, described in prose — e.g. "instrument panel: dense, monospaced
            numerals, hairline rules, single amber accent, no shadows">
Adopted conventions: <list, each with the usability reason>
Chosen differentiators (max 2): <each with the risk and the reason it is worth it>
Explicitly rejected: <list, each with the reason — this is what prevents drift>
Anti-references: <what we must not look like>
Constraints that follow: <type families, palette size, density, motion character,
                          imagery policy, illustration policy>
```

### 7. DERIVE
Hand the brief to [`frontend-design`](../frontend-design/SKILL.md) step 4 (SYSTEM). Every
token must be traceable to a line in the brief. If a token cannot be traced, either the
brief is incomplete or the token is arbitrary.

### 8. VALIDATE

```text
□ Does the direction survive contact with the real content? (test with the worst-case strings)
□ Is it distinguishable from the 3 closest competitors at a glance / 8 px blur?
□ Is it defensible to the audience, not just to the designer?
□ Is it implementable within the performance and accessibility budget?
□ Does it pass the slop gate on paper (no gradient/blur/neon defaults)?
□ Can someone else rebuild the same direction from the brief alone?
```

## Decomposition template

```markdown
### Reference: <name> — <url> — <product type>
Rated: <1-5 for relevance to our brief>

Layout        grid, column count, max width, section rhythm, symmetry/asymmetry
Density       items per viewport, padding scale, whitespace ratio
Type          families, display vs text, scale ratio, weights used, tracking, measure
Colour        hue strategy, saturation level, neutral temperature, accent count,
              background/surface/contrast relationships
Surfaces      flat vs elevated; border vs shadow; translucency; corner radius
Imagery       photography / illustration / none / data-as-imagery; treatment
Iconography   style, stroke weight, filled vs outline, size relationship to type
Motion        character (snappy / eased / springy), durations, what moves and why
Micro-details the 3 things that make it feel made by a human
Why it works  the underlying principle, stated transferably
What to steal the specific decision we will adopt
What to avoid the part that would not survive our content/audience
```

**The critical field is "Why it works".** A reference you can only describe is a
reference you cannot use.

## Failure Modes

```text
MOODBOARD WITHOUT ANALYSIS   Pretty pictures, zero extracted decisions.
SINGLE-POOL RESEARCH         Only looking at competitors → you will look like a competitor.
AWWARD-WASHING               Copying expressive agency sites into a data-dense tool.
DIFFERENTIATOR MAXIMALISM    Five deliberate deviations → incoherence, not character.
GAP CHASING                  Choosing a position because it is empty, not because it fits.
COPYING SURFACE              Replicating a specific visual without its underlying system.
BRIEF DRIFT                  Designing tokens that the brief does not support.
NO ANTI-REFERENCES           Nothing to steer away from, so defaults creep back in.
```

## Quality Checklist

```text
□ Intended impression written before collecting
□ 15–30 references across 4 pools including 3–5 anti-references
□ 5–8 strongest references fully decomposed with "why it works"
□ Conventions vs differentiators separated by recurrence
□ Position stated on two meaningful axes, with competitors placed
□ Design Direction Brief complete, including explicit rejections
□ At most 2 differentiators chosen, each with a stated risk
□ Every derived token traceable to a line in the brief
□ Direction validated against real content and the slop gate
□ A third party could rebuild the direction from the brief alone
```

## Anti-Patterns

```text
✗ "Let's do a dark, minimal, modern look" with no references and no reasoning
✗ A moodboard of 40 screenshots and no written analysis
✗ Choosing an aesthetic because a competitor does not have it
✗ Naming an aesthetic ("brutalist", "glassmorphism") instead of describing decisions
✗ Copying a reference's colour palette while ignoring its density and type decisions
✗ Skipping anti-references, then shipping a gradient hero
```

## References

- [`frontend-design`](../frontend-design/SKILL.md) · [`design-systems`](../design-systems/SKILL.md)
- [`ai-slop-detection`](../ai-slop-detection/SKILL.md) — the anti-reference catalogue
- [`knowledge/ui-ux/`](../../knowledge/ui-ux/)
- [`prompts/ui-ux/design-direction-brief.md`](../../prompts/ui-ux/)
- Reference pools: Awwwards, Godly, Dribbble/Behance (filter hard — high volume, low signal),
  plus primary sources: museum/open-access image libraries, type foundries, industrial design archives

## Related Skills

`frontend-design` · `design-systems` · `ai-slop-detection` · `competitive-analysis` ·
`web-research`

## Evaluation Criteria

```text
1. Decomposition completeness: every selected reference has "why it works" and "what to steal".
2. Brief reproducibility: a second agent given the brief produces a recognisably similar system.
3. Distinctiveness: ≥1 of 2 chosen differentiators is visibly present in the result.
4. Convention retention: no usability-serving convention was broken without a stated reason.
5. Traceability: 100% of design tokens trace to a brief line.
```

Test cases in [`tests/`](tests/).
