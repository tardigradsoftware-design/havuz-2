---
id: ui-ux-ai-slop-signature-catalogue
title: "The AI-slop signature catalogue: what makes an interface read as machine-generated"
domain: ui-ux
summary: >-
  The measurable symptoms that make an interface read as AI-generated, grouped by root cause, with
  the underlying mechanism for each. Companion reference to skills/ai-slop-detection — this file
  explains why the signatures exist, the skill defines how to detect and fix them.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [ai-slop, design, ui, ux, visual-design, generated-content, craft]
applies_to: [web, marketing-site, saas, dashboard, landing-page]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
sections:
  - heading: Why slop looks the way it does
    anchor: "#why-slop-looks-the-way-it-does"
    purpose: overview
  - heading: The five root causes
    anchor: "#the-five-root-causes"
    purpose: decision
  - heading: Signature groups
    anchor: "#signature-groups"
    purpose: implementation
  - heading: The tell-tale token list
    anchor: "#the-tell-tale-token-list"
    purpose: implementation
  - heading: What slop is not
    anchor: "#what-slop-is-not"
    purpose: pitfalls
estimated_tokens: 2351
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [ai-slop-detection, frontend-design, design-systems, visual-design-research, motion-design]
related:
  - knowledge/ui-ux/what-makes-ai-websites-look-generic.md
  - knowledge/ui-ux/what-makes-a-website-look-professional.md
  - knowledge/ui-ux/visual-hierarchy.md
  - skills/ai-slop-detection/references/detection-catalogue.md
  - workflows/ai-slop-remediation/WORKFLOW.md
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The contrast, animation and reduced-motion thresholds several signatures violate."
  - title: "Material Design 3 — foundations"
    url: https://m3.material.io/foundations
    type: official-docs
    organization: Google
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A worked example of the elevation, colour-role and type-scale systems whose absence produces most signatures."
---

# The AI-Slop Signature Catalogue

## Why slop looks the way it does

Slop is not a taste failure. It is the predictable output of a generator that selects the most
probable continuation, applied to a task whose correct answer is *specific*.

A model asked for "a SaaS landing page" produces the highest-probability arrangement of landing-page
features in its training distribution: hero with a gradient, three equal feature cards, a logo
strip, a testimonial row, a pricing table, a footer CTA. Each element is individually reasonable.
The composition is what every other generator produced from the same distribution — which is
precisely why a human recognises it instantly and cannot say why.

Three properties make it detectable:

```text
PROBABLE, NOT DERIVED    Every choice is the mode of a distribution rather than a consequence of
                         the content, the audience or the task. Nothing is load-bearing.
UNIFORM, NOT HIERARCHICAL Weight is distributed evenly because a generator has no reason to
                         privilege one element. Real design is deliberately unequal.
DECORATIVE, NOT FUNCTIONAL Gradient, blur, glow and motion are added where a decision was needed,
                         because decoration is the cheapest thing to emit.
```

## The five root causes

Almost every signature traces to one of five missing inputs. This is why remediation works better
on causes than on symptoms — three system files remove twenty symptoms.

```text
1. NO DESIGN SYSTEM      Nothing defined spacing, type or colour, so each component invented its
                         own values. Signatures: off-scale spacing, arbitrary font sizes, too many
                         hues, inconsistent gaps between siblings.

2. NO CONTENT MODEL      The layout was designed before the content was known, so it was designed
                         against placeholders. Signatures: filler copy, unsubstantiated metrics,
                         sections that exist to fill space, layouts that break on real string
                         lengths, three cards because the template had three slots.

3. NO HIERARCHY DECISION  Nobody chose what matters most, so nothing was subordinated.
                         Signatures: equal-weight headings, competing CTAs, uniform section rhythm,
                         symmetry everywhere, no primary element per view.

4. DECORATION AS PROXY    Where a design decision was needed, visual effect was supplied instead.
                         Signatures: gradients on surfaces with no semantic meaning, backdrop blur
                         on three or more layers, floating orbs, glow shadows, entrance animation
                         on load, neon-on-dark as an entire palette strategy.

5. NO REFERENCE RESEARCH  Nothing was looked at before drawing, so the default was drawn.
                         Signatures: an aesthetic that matches no stated intent, icon sets mixed
                         from different families, a look that could belong to any product in the
                         category and does not belong to this one.
```

## Signature groups

The full detection rules, severities and fix directions live in
[`skills/ai-slop-detection/references/detection-catalogue.md`](../../skills/ai-slop-detection/references/detection-catalogue.md).
This is the explanatory view — the mechanism behind each group.

```text
LAYOUT & COMPOSITION (root causes 2, 3)
  Hero-plus-three-cards, symmetry everywhere, feature-grid monotony, section sameness, filler
  sections. Mechanism: the layout was derived from a template slot count rather than from the
  content's real structure, so every section has the same shape and the same weight.

COLOUR & SURFACE (root causes 1, 4)
  Decorative gradients, the purple/indigo default, glassmorphism overload, neon-on-dark, too many
  accents, border soup. Mechanism: with no colour-role system, hue is chosen for effect; with no
  elevation system, depth is faked with blur and glow instead of shadow and surface tone.

TYPOGRAPHY (root causes 1, 3)
  A single default family at default weights, font sizes not on a scale, unbounded line length,
  hierarchy attempted by size alone. Mechanism: no modular scale means every size is invented at
  the point of use, so sizes cluster arbitrarily and hierarchy collapses to one dimension.

SPACING & RHYTHM (root cause 1)
  Off-system spacing, inconsistent gaps for the same relationship, cramped or floaty density.
  Mechanism: spacing chosen per element instead of per relationship. The diagnostic is precise —
  one relationship must have exactly one token, everywhere.

CONTENT & CREDIBILITY (root cause 2)
  Unsubstantiated metrics, filler adjectives, vague benefit stacking, duplicate iconography,
  meaningless badges, stock-photo humans. Mechanism: copy written to fill a slot rather than to
  state something true about this product. This group does the most damage, because it is the one
  a reader consciously notices.

MOTION & INTERACTION (root cause 4)
  Animation without a cause, uniform duration, floating decoration, no reduced-motion path,
  animation obscuring data changes. Mechanism: motion added as effect rather than as explanation
  of a state change, so it has no hierarchy and no trigger discipline.

STRUCTURE VISIBLE IN THE UI (root cause 1)
  Near-duplicate components, utility-class soup, dead responsive rules, decorative controls with
  no state. Mechanism: without a system, each occurrence is re-implemented; the repetition shows
  up as inconsistency the user can see but cannot name.
```

## The tell-tale token list

Signatures are grep-able, which is what makes detection mechanical rather than aesthetic:

```text
backdrop-filter / backdrop-blur        blur layers beyond one
bg-gradient- / linear-gradient(        decorative gradients
from-indigo- via-purple- to-pink-      the default hue ramp
shadow-[0_0_…  /  drop-shadow          glow shadows
animate-pulse / animate-bounce         animation without a cause
rounded-2xl on everything              radius used as a style rather than a scale
17px, 19px, 23px                       font sizes off any scale
13px, 17px, 26px padding               spacing off a 4/8 px scale
"Seamlessly" "Unleash" "Elevate"       filler adjectives
"In today's fast-paced world"          filler openings
"10,000+ teams" "99.9%" "500% faster"  metrics with no definition or source
"AI-powered" badge                     a badge encoding no state
```

A grep hit is a lead, not a verdict — each requires the evidence step in the skill. But a page
with zero hits and a page with twelve do not have the same probability of being deliberate.

## What slop is not

The catalogue is often misapplied, and the misapplications matter because they push designs toward
a different cliché rather than toward quality.

```text
NOT MINIMALISM       A restrained, sparse design with a real system is the opposite of slop.
                     Slop is undeliberate, not decorated — removing decoration from an
                     undeliberate design produces a bland one, which is its own signature.
NOT A SPECIFIC STYLE Dark mode is not slop. Gradients are not slop. Blur is not slop. Each
                     becomes a signature when applied as a default rather than as a decision.
NOT DENSE OR PLAIN   A dense internal tool with consistent tokens and clear hierarchy is
                     well designed. Judge deliberateness, not density.
NOT THE LIBRARY      Using a component library is not slop. Using its default theme untouched,
                     with no tokens of your own, is.
NOT NEWNESS          An unfamiliar layout is not automatically a deviation worth keeping, and a
                     conventional one is not automatically slop. Conventions that serve usability
                     should be kept; only the ones serving sameness should be broken.
```

The test that separates deliberate from generated: **can the designer say why each property has
the value it has, in terms of the content and the task?** If every answer is "it looked good",
the design is a sample from a distribution, and it will look like every other sample.

## References

- [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md) — the workflow and reporting format
- [`skills/ai-slop-detection/references/detection-catalogue.md`](../../skills/ai-slop-detection/references/detection-catalogue.md) — full rules, severities and fixes
- [`knowledge/ui-ux/what-makes-ai-websites-look-generic.md`](what-makes-ai-websites-look-generic.md)
- [`knowledge/ui-ux/what-makes-a-website-look-professional.md`](what-makes-a-website-look-professional.md)
- [`knowledge/ui-ux/visual-hierarchy.md`](visual-hierarchy.md)
- [`workflows/ai-slop-remediation/WORKFLOW.md`](../../workflows/ai-slop-remediation/WORKFLOW.md)
- [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
