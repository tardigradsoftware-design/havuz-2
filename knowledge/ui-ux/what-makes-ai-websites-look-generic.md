---
id: ui-ux-what-makes-ai-websites-look-generic
title: "What makes an AI-built website look generic"
domain: ui-ux
summary: >-
  The mechanism behind generic AI output — probable rather than derived choices — the six observable signature families, the tell-tale token list that makes detection mechanical, and what generic is NOT, so remediation does not produce a different cliché.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [ai-slop, generic-design, ui, ux, visual-design, generated-content, signatures, craft]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/ui-ux/ai-slop-signature-catalogue.md, knowledge/ui-ux/what-makes-a-website-look-professional.md]
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Several signatures are simultaneously accessibility failures — animation without a reduced-motion path, contrast below threshold, colour as the only channel — which makes the WCAG criteria a mechanical detector for part of the catalogue."
---
# What Makes an AI-Built Website Look Generic

## The mechanism

Generic output is not a taste failure. It is the predictable product of a generator that selects the
most probable continuation, applied to a task whose correct answer is *specific*.

Asked for "a SaaS landing page", a model produces the highest-probability arrangement of
landing-page features in its training distribution: gradient hero, three equal feature cards, a logo
strip, a testimonial row, a pricing table, a footer CTA. Each element is individually reasonable.
The composition is what every other generator produced from the same distribution — which is why a
human recognises it instantly and cannot say why.

```text
PROBABLE, NOT DERIVED      Every choice is the mode of a distribution rather than a consequence of
                           the content, the audience or the task. Nothing is load-bearing.
UNIFORM, NOT HIERARCHICAL  Weight is spread evenly because a generator has no reason to privilege one
                           element. Real design is deliberately unequal.
DECORATIVE, NOT FUNCTIONAL Gradient, blur, glow and motion are added where a decision was needed,
                           because decoration is the cheapest thing to emit.
```

## The five missing inputs

Almost every signature traces to one of these. This is why remediation works on causes rather than
symptoms — three system files remove twenty symptoms.

```text
1. NO DESIGN SYSTEM     Nothing defined spacing, type or colour, so each component invented its own
                        values. → off-scale spacing, arbitrary font sizes, too many hues, inconsistent
                        gaps between siblings.
2. NO CONTENT MODEL     The layout was designed against placeholders because the content was not yet
                        known. → filler copy, unsubstantiated metrics, sections that exist to fill
                        space, layouts that break on real string lengths, three cards because the
                        template had three slots.
3. NO HIERARCHY DECISION Nobody chose what matters most, so nothing was subordinated. → equal-weight
                        headings, competing CTAs, uniform section rhythm, symmetry everywhere, no
                        primary element per view.
4. DECORATION AS PROXY   Where a decision was needed, visual effect was supplied instead. → gradients
                        on surfaces with no semantic meaning, blur on three or more layers, floating
                        orbs, glow shadows, entrance animation on load, neon-on-dark as an entire
                        palette strategy.
5. NO REFERENCE RESEARCH Nothing was looked at before drawing, so the default was drawn. → an
                        aesthetic matching no stated intent, icon sets mixed from different families,
                        a look that could belong to any product in the category and does not belong to
                        this one.
```

## The six signature families

Full detection rules, severities and fixes:
[`ai-slop-signature-catalogue.md`](ai-slop-signature-catalogue.md) and
[`skills/ai-slop-detection/references/detection-catalogue.md`](../../skills/ai-slop-detection/references/detection-catalogue.md).

```text
LAYOUT & COMPOSITION   hero-plus-three-cards, symmetry everywhere, feature-grid monotony, section
                       sameness, filler sections. The layout came from a template slot count, not from
                       the content's real structure — so every section has the same shape and weight.
COLOUR & SURFACE       decorative gradients, the purple/indigo default, glassmorphism overload,
                       neon-on-dark, too many accents, border soup. With no colour-role system hue is
                       chosen for effect; with no elevation system depth is faked with blur and glow.
TYPOGRAPHY             one default family at default weights, sizes not on a scale, unbounded line
                       length, hierarchy attempted by size alone. No modular scale means every size is
                       invented at the point of use.
SPACING & RHYTHM       off-system spacing, inconsistent gaps for the same relationship, cramped or
                       floaty density. Spacing chosen per element instead of per relationship. The
                       diagnostic is precise: one relationship must have exactly one token, everywhere.
CONTENT & CREDIBILITY  unsubstantiated metrics, filler adjectives, vague benefit stacking, duplicated
                       iconography, meaningless badges, stock-photo humans. Copy written to fill a slot
                       rather than to state something true. The group a reader consciously notices, and
                       the one that does the most damage.
MOTION & INTERACTION   animation without a cause, uniform duration, floating decoration, no
                       reduced-motion path, motion obscuring data changes. Motion added as effect
                       rather than as explanation of a state change.
```

## The tell-tale token list

Signatures are grep-able, which makes detection mechanical rather than aesthetic:

```text
backdrop-filter / backdrop-blur         blur layers beyond one
bg-gradient- / linear-gradient(         decorative gradients
from-indigo- via-purple- to-pink-       the default hue ramp
shadow-[0_0_…  /  drop-shadow           glow shadows
animate-pulse / animate-bounce          animation without a cause
rounded-2xl applied everywhere          radius as a style rather than a scale
17px, 19px, 23px                        font sizes off any scale
13px, 17px, 26px padding                spacing off a 4/8 px scale
"Seamlessly" "Unleash" "Elevate"        filler adjectives
"In today's fast-paced world"           filler openings
"10,000+ teams" "99.9%" "500% faster"   metrics with no definition or source
"AI-powered" badge                      a badge encoding no state
```

A grep hit is a lead, not a verdict — each requires an evidence step. But a page with zero hits and a
page with twelve do not carry the same probability of being deliberate.

## What generic is NOT

Misapplication matters, because it pushes a design toward a different cliché rather than toward quality.

```text
NOT MINIMALISM      A restrained, sparse design with a real system is the opposite of generic. Slop is
                    undeliberate, not decorated — removing decoration from an undeliberate design
                    produces a bland one, which is its own signature.
NOT A STYLE         Dark mode is not generic. Gradients are not generic. Blur is not generic. Each
                    becomes a signature when applied as a default rather than as a decision.
NOT DENSE OR PLAIN  A dense internal tool with consistent tokens and clear hierarchy is well designed.
                    Judge deliberateness, not density.
NOT THE LIBRARY     Using a component library is not generic. Using its default theme untouched, with
                    no tokens of your own, is.
NOT NEWNESS         An unfamiliar layout is not automatically worth keeping and a conventional one is
                    not automatically generic. Keep conventions that serve usability; break only the
                    ones serving sameness.
```

The test that separates deliberate from generated: **can the designer say why each property has the
value it does, in terms of the content and the task?** If every answer is "it looked good", the design
is a sample from a distribution and will look like every other sample.

## References

- [`ai-slop-signature-catalogue.md`](ai-slop-signature-catalogue.md) — the mechanism and grouping in full
- [`what-makes-a-website-look-professional.md`](what-makes-a-website-look-professional.md) — the positive counterpart
- [`visual-hierarchy.md`](visual-hierarchy.md) — the hierarchy dimension
- [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md) · [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md)
- [`workflows/ai-slop-remediation/WORKFLOW.md`](../../workflows/ai-slop-remediation/WORKFLOW.md) · [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
