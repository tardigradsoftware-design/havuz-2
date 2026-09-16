---
id: detection-catalogue
title: "The full symptom catalogue: IDs, detection rules, severity and fix directions"
domain: ui-ux
summary: >-
  The complete AI-slop symptom catalogue with machine-checkable detection rules, severity ratings and fix directions, extracted from the skill so the skill body stays inside its context budget.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [reference, ui-ux]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [ai-slop-detection]
---

# The full symptom catalogue: IDs, detection rules, severity and fix directions

Reference material for [`ai-slop-detection`](../SKILL.md), extracted so the skill body stays
within its context budget. Load this file only when the step that needs it is reached.


Each symptom has an **ID**, a **detection rule** (something you can actually check), a
**severity**, and a **fix direction**. Severity: `S1` = instantly reads as AI-generated;
`S2` = reads as low-effort; `S3` = polish issue.

## Layout & composition

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| L1 | Hero-with-three-cards | H1 + subhead + two buttons, then a row of exactly 3 equal cards | S1 | Derive the layout from the content's real structure; vary card count and weight |
| L2 | Symmetry everywhere | Every section is centred, full-width, equal padding, equal height | S1 | Introduce asymmetry: 2/3–1/3 splits, offset grids, one anchored element |
| L3 | Feature grid monotony | ≥3 identical icon+title+paragraph blocks in a row, repeated per section | S1 | Differentiate by importance; lead feature gets more space, not the same space |
| L4 | No information hierarchy | All headings within 2 px of each other; nothing is clearly primary | S2 | Enforce a type scale with ≥1.5× ratio between adjacent steps |
| L5 | Section sameness | Every section has the same vertical rhythm and the same max-width | S2 | Vary density: tight data sections, generous narrative sections |
| L6 | Filler sections | "Trusted by", testimonials, or stats blocks with placeholder content | S1 | Remove or replace with real, specific evidence |

## Colour & surface

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| C1 | Decorative gradient | Gradient applied to a background, card, border or text with no semantic meaning | S1 | Remove; keep gradients only where they encode data or direction |
| C2 | Purple/indigo default | Primary hue in the 240–280° range with high saturation and no brand reason | S1 | Choose hue from brand or from the content's emotional register |
| C3 | Glassmorphism overload | `backdrop-filter: blur()` on ≥3 distinct surfaces | S1 | At most one translucent surface; prefer solid, layered elevation |
| C4 | Neon-on-dark cliché | Dark background + single saturated neon accent + glow shadows | S2 | Build a real dark palette: desaturated surfaces, ≥3 elevation levels |
| C5 | Too many accents | ≥4 saturated hues used at similar weight | S2 | One accent, one semantic set (success/warning/danger), everything else neutral |
| C6 | Border soup | Every element has a 1 px border of the same colour | S3 | Replace borders with spacing and background contrast where possible |
| C7 | Contrast fail on muted text | Body or secondary text below 4.5:1 (WCAG AA) | S1 | Raise contrast; check with a real contrast tool, not by eye |

## Typography

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| T1 | Default font stack | Inter / system-ui used with default weights and no optical sizing, everywhere | S2 | Pair a distinct display face with a text face, or use one family with deliberate weights |
| T2 | Scale by feel | Font sizes are arbitrary values (17 px, 19 px, 23 px) not from a scale | S2 | Adopt a modular scale and derive every size from it |
| T3 | Line length unbounded | Body text lines exceed ~85 characters at desktop widths | S2 | Constrain measure to 60–75 characters |
| T4 | Weight monotony | All text at one weight; hierarchy attempted with size alone | S3 | Use weight + colour + size together for hierarchy |
| T5 | Loose tracking on body | `letter-spacing` > 0 on body copy | S3 | Positive tracking belongs on small caps/labels, not paragraphs |

## Spacing & rhythm

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| SP1 | Off-system spacing | Padding/margin values not drawn from a 4 px or 8 px scale | S2 | Snap everything to the scale; add a lint rule |
| SP2 | Inconsistent gaps | Sibling components in one view use different gaps for the same relationship | S1 | One relationship = one token, everywhere |
| SP3 | Cramped or floaty | Cards with <12 px internal padding, or sections with >160 px of empty space | S3 | Set density per content type and hold it |

## Content & credibility

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| X1 | Fake metrics | "10,000+ teams", "99.9% uptime", "500% faster" with no source or definition | S1 | Remove, or make it real and verifiable with a footnote |
| X2 | Placeholder copy | "Lorem", "Your amazing product", "Seamlessly", "Unleash", "Elevate", "In today's fast-paced world" | S1 | Replace with specific, concrete claims about this product |
| X3 | Vague benefit stacking | Three adjectives where one measurable outcome belongs | S2 | One claim, one number, one proof |
| X4 | Duplicate iconography | The same icon set reused for unrelated concepts; ≥3 icons meaning "settings/gear" | S3 | Icon = concept, one-to-one |
| X5 | Meaningless badges | "NEW", "AI-powered", "Beta" badges on things that are none of those | S2 | Badges encode state; remove decorative ones |
| X6 | Stock-photo humans | Generic smiling-stock imagery in a B2B product context | S2 | Show the actual product, real data, or no imagery |

## Motion & interaction

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| M1 | Random animation | Elements animate on load with no relationship to user action or content | S1 | Animate state change and causality only |
| M2 | Uniform duration | Every transition uses the same 300 ms ease | S2 | Build a motion hierarchy: micro 120 ms, component 200 ms, page 320 ms |
| M3 | Floating decoration | Blurred orbs, floating shapes, drifting particles with no function | S1 | Remove; if depth is needed, use elevation and shadow |
| M4 | No reduced-motion | Animations run regardless of `prefers-reduced-motion` | S1 | Provide a reduced-motion path; this is also WCAG 2.3.3 |
| M5 | Animation over data | Charts animate on every re-render, obscuring the value change | S3 | Animate the transition, not the whole chart |

## Structural / code smell (visible in the UI)

| ID | Symptom | Detection rule | Sev | Fix direction |
|---|---|---|---|---|
| S1 | Component duplication | 5 near-identical card components instead of one with props | S2 | Extract; design systems beat copy-paste |
| S2 | Utility-class soup | Repeated 12-class strings for the same visual result | S3 | Extract a component or a `@apply`-free token class |
| S3 | Dead responsive rules | `md:` variants that produce the same result as base | S3 | Remove; test at real breakpoints |
| S4 | Fake interactivity | Buttons, tabs or inputs that are not wired and have no state | S1 | Wire them or remove them; never ship decorative controls |
