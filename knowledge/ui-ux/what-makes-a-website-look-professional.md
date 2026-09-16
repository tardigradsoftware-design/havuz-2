---
id: ui-ux-what-makes-a-website-look-professional
title: "What makes a website look professional"
domain: ui-ux
summary: >-
  The properties that read as professional — restraint, a real system, hierarchy, specific content, craft in the details — with the observable evidence for each and the reason it produces the impression it does.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [design-quality, professionalism, ui, ux, craft, typography, spacing, restraint, visual-design]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/ui-ux/what-makes-ai-websites-look-generic.md, knowledge/ui-ux/visual-hierarchy.md]
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Contrast, target size, reflow and reduced-motion compliance overlaps heavily with what reads as professional; the two judgments share mechanisms."
---
# What Makes a Website Look Professional

Professional is not a style. Minimal, dense, playful and corporate sites all read as professional, and
all of them can read as amateur. The impression comes from a set of properties that are observable,
checkable and independent of aesthetic preference.

## 1. Restraint

```text
FEWER HUES        one accent, used consistently for one meaning. A second accent needs a second
                  meaning. Most professional sites use two or three colours plus neutrals.
FEWER FONTS       one or two families, a small set of weights, sizes on a scale.
FEWER EFFECTS     one elevation system, one radius scale, one blur usage — or none.
NOTHING DECORATIVE WITHOUT A REASON  a gradient, a shadow or an animation that cannot be explained by
                  a state, a hierarchy or a transition is noise.

WHY IT READS AS PROFESSIONAL   Restraint signals that choices were made rather than accumulated. Every
                  additional effect is a claim that the designer could not decide.
```

## 2. A real system

```text
SPACING ON A SCALE        one token per relationship. The gap between a heading and its body, between
                          cards, between sections — each consistent everywhere, and the set of values
                          small (a 4 or 8 px base).
TYPE ON A MODULAR SCALE   sizes derived by ratio, not invented per element. Line height and letter
                          spacing adjusted per size, not left at default.
COLOUR AS ROLES, NOT VALUES background, surface, border, text-primary, text-secondary, accent,
                          success, warning, danger — each with one job, defined once.
ELEVATION AS MEANING      shadow indicates a layer relationship (floating above, detachable, modal),
                          not decoration.
COMPONENT REUSE           the same relationship rendered the same way everywhere. Two card styles for
                          the same content is a system failure visible to users who cannot name it.

WHY IT READS AS PROFESSIONAL   Consistency is the visible trace of a decision made once and applied
                          everywhere. Inconsistency is the visible trace of each element being designed
                          separately, which is what happens under time pressure or without a system.
```

## 3. Hierarchy

```text
ONE PRIMARY ELEMENT PER VIEW      the thing the user should do or see first, made unambiguous by size,
                                  weight, colour and position together — not by size alone.
WEIGHT UNEQUAL ON PURPOSE         headings, body, captions, meta at clearly different levels. Equal
                                  weight everywhere means nothing is emphasised.
RHYTHM THAT VARIES BY IMPORTANCE  section spacing larger than element spacing; a dense section and a
                                  spacious one in the same page, because they carry different weight.
SUBORDINATION                     secondary actions visually quieter: smaller, outlined, lower
                                  contrast. Two buttons competing at the same weight is an unresolved
                                  decision.

WHY IT READS AS PROFESSIONAL   Hierarchy is the designer telling the user what matters. Its absence
                               forces the user to work out the importance of everything, which reads as
                               "nobody decided".
```

## 4. Specific content

```text
REAL NUMBERS WITH DEFINITIONS   "Median response time 180 ms across 12M requests in March 2026" beats
                                "blazing fast". A metric with no denominator is decoration.
NAMED FEATURES, NOT BENEFIT STACKING  what the product does, concretely. "Automated invoice matching
                                against purchase orders" beats "streamline your workflow".
COPY WRITTEN FOR THE AUDIENCE   the vocabulary of the user, not of the category. Jargon used correctly
                                reads as expertise; jargon used generally reads as a template.
NO FILLER                       no "In today's fast-paced world", no "seamlessly", no "unleash", no
                                sentence that could appear on any competitor's site unchanged.
REAL NAMES AND REAL IMAGES      named customers with logos and quotes, product screenshots rather than
                                stock illustrations, photographs of the actual thing.

WHY IT READS AS PROFESSIONAL   Specificity is unfakeable. It requires knowing the product and the
                               customer, and a template cannot supply it.
```

## 5. Craft in the details

```text
ALIGNMENT AND OPTICAL BALANCE   edges aligned to a grid; optical centring where geometric centring
                                looks wrong (a play triangle, a rounded icon).
TEXT MEASURES                 line length 45-75 characters; orphan and widow control; no single word
                                on the last line of a paragraph in a prominent position.
EMPTY, LOADING AND ERROR STATES designed, not defaulted. The empty state explains what will appear and
                                how; the error state says what went wrong and what to do.
FORM CRAFT                    visible labels (not placeholder-only), inline validation on blur, the
                              error message next to the field and associated programmatically, the
                              submit button disabled only when submitting.
RESPONSIVE INTENT             breakpoints chosen from where the content breaks, not from a device list.
                              Nothing overflows, nothing overlaps, no horizontal scroll at 320 px.
MOTION WITH A PURPOSE         duration and easing consistent; motion explains a state change or a
                              spatial relationship; reduced-motion honoured.
MICRO-INTERACTION FEEDBACK    every action produces a visible response within ~100 ms — a state change,
                              a spinner, a pressed state. Silence reads as broken.
TYPOGRAPHIC DETAIL            real quotation marks, en dashes for ranges, no double spaces after
                              periods, consistent capitalisation in headings, tabular figures for numbers
                              in tables.
PERFORMANCE AS CRAFT          fast TTFB, no layout shift, images sized and in a modern format. A slow
                              site reads as unmaintained regardless of how it looks.

WHY IT READS AS PROFESSIONAL   These are the things nobody notices when present and everybody notices
                               when absent. They are also the things a template does not include,
                               because they require attention to the actual content.
```

## 6. Trust signals that are not decoration

```text
□ a real company address, registration number or legal entity where the jurisdiction requires it
□ a privacy policy and terms that describe THIS product's actual data handling
□ a working contact path — an address that receives mail, or a form that reaches a human
□ security claims that are verifiable: a named certification, a disclosure policy, a status page
□ a changelog, documentation or release history that shows ongoing work
□ pricing that is complete — no "contact us" for a price that could be published
□ no badge that encodes nothing ("AI-powered", "Enterprise-ready" with no supporting statement)

A trust signal that cannot be verified is worse than none, because it invites the check.
```

## The one-paragraph summary

A professional website is one where **every visible property has a reason**, the reasons are
consistent across the page, the content is specific to this product and this audience, and the states
nobody photographs — empty, loading, error, 320 px wide, keyboard-only, reduced-motion — were designed
rather than left to defaults. Generic output fails this test not because it looks a particular way, but
because its properties have no reasons: they are the most probable values, not the derived ones.

## How to check

```text
1. SCREENSHOT THE PAGE AND SQUINT.  What is the one thing that stands out? If the answer is "nothing"
   or "everything", hierarchy is missing.
2. LIST EVERY COLOUR, FONT SIZE AND SPACING VALUE IN USE.  Count them. A professional page has a short
   list; a generated one has a long one.
3. READ THE COPY ALOUD, REMOVING THE PRODUCT NAME.  If it could belong to a competitor unchanged, it is
   filler.
4. CHECK THE STATES.  Empty, loading, error, mobile, keyboard-only, 400% zoom, reduced motion.
5. ASK WHY FOR FIVE VISUAL PROPERTIES.  "Why this gradient", "why this shadow", "why this animation".
   An answer that is not about content, hierarchy or state is a decoration.
6. COMPARE AGAINST THE GENERIC SIGNATURES.  See what-makes-ai-websites-look-generic.md.
```

## References

- [`what-makes-ai-websites-look-generic.md`](what-makes-ai-websites-look-generic.md) — the negative counterpart
- [`ai-slop-signature-catalogue.md`](ai-slop-signature-catalogue.md) · [`visual-hierarchy.md`](visual-hierarchy.md)
- [`../accessibility/wcag-practical-checklist.md`](../accessibility/wcag-practical-checklist.md) · [`../performance/frontend-budgets.md`](../performance/frontend-budgets.md)
- [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md) · [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md) · [`skills/visual-design-research/SKILL.md`](../../skills/visual-design-research/SKILL.md)
- [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md) · [`workflows/ai-slop-remediation/WORKFLOW.md`](../../workflows/ai-slop-remediation/WORKFLOW.md)
- [`prompts/ui-ux/design-direction-brief.md`](../../prompts/ui-ux/design-direction-brief.md)
