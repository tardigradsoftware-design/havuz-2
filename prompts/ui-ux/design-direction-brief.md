---
id: prompt-design-direction-brief
name: Design direction brief
task: Turn a product and an audience into a specific, testable design direction — a stated intent, a token set, a hierarchy decision and explicit exclusions — so that implementation is a series of derivations rather than a sequence of defaults.
use_case: 'Before any visual implementation begins: a new site or product surface, a redesign, or a build that must not look generated. The brief is the input to design-systems, frontend-design and ai-slop-detection work, and the reference those skills are checked against afterwards.'
category: ui-ux
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
tags:
- design
- ui
- ux
- design-direction
- brief
- tokens
- hierarchy
- anti-slop
- prompts
updated: '2026-09-15'
verified_at: '2026-09-15'
expires_at: '2027-03-15'
model_sensitivity: portable
techniques:
- role-priming
- constraint-list
- negative-example
- structured-output
- rubric-scoring
variables:
- name: product
  required: true
  description: What the product is and does, concretely.
- name: audience
  required: true
  description: Who uses it, in what context, at what frequency, with what expertise.
- name: primary_action
  required: true
  description: The one thing a user must be able to do. Everything else is subordinate.
- name: constraint
  required: false
  description: Existing brand, components, technical stack, accessibility or regulatory requirement.
- name: references
  required: false
  description: Products or sites already admired, and specifically what about them.
- name: anti_references
  required: false
  description: Things this must not resemble, and why.
required_context:
- The product and what it does concretely
- The audience, usage frequency and device context
- The one thing a user must be able to do
- Existing brand, component or accessibility constraints
- WCAG 2.2 AA as the compliance floor
prompt: "You are a design director writing a direction brief for an implementation team. Your brief will be\nused to build the interface and to judge the result. Every decision must be derivable by someone who\nwas not in the conversation: if a value is not stated, it will be invented, and invented values are\nwhat make an interface look generated.\n\nPRODUCT\n  {product}\n\nAUDIENCE AND CONTEXT\n  {audience}\n\nTHE ONE THING A USER MUST BE ABLE TO DO\n  {primary_action}\n\nCONSTRAINTS\n  {constraint}\n\nREFERENCES — and what specifically about each\n  {references}\n\nANTI-REFERENCES — what this must not resemble, and why\n  {anti_references}\n\n──────────────────────────────────────────────────────────────\nPRODUCE THE BRIEF IN THESE EIGHT SECTIONS\n──────────────────────────────────────────────────────────────\n\n1. INTENT\n   One or two sentences: what this interface is for, who it is for, and what it should feel like to\n   use. Not adjectives — a statement an implementer could argue with. Then three adjectives that\n   follow FROM it, each with the reason it follows.\n   Reject any adjective that could describe a competitor's product unchanged.\n\n2. AUDIENCE AND USAGE CONTEXT\n   Frequency of use (first visit vs daily), expertise level, device and environment, tolerance for\n   density, and what the user is trying to get out of the session. State which of these dominates the\n   visual decisions and why. A first-visit marketing page and a daily-use internal tool have opposite\n   correct answers on density, motion and hierarchy.\n\n3. THE HIERARCHY DECISION\n   For each primary view, name the ONE element that matters most and state how it is made primary —\n   which of size, weight, contrast, colour, position, space and isolation are moved, and in which\n   direction. Then name what is deliberately subordinate and how it is quieted.\n   A view with two primaries is an undecided view; pick one.\n   State the reading order and confirm it matches the DOM order.\n\n4. THE TOKEN SET\n   The complete set, with values. Anything absent will be invented per component.\n     SPACING      a base unit (4 or 8 px) and the named steps. Then the mapping: one token per\n                  RELATIONSHIP — heading-to-body, element-to-sibling, card-internal-padding,\n                  card-to-card, section-to-section. The intra-group gap must be visibly smaller than\n                  the inter-group gap (a ratio of at least 2:1).\n     TYPE         families (one or two), the modular scale with its ratio, and per size: weight, line\n                  height, letter spacing. Include the meta/caption level.\n     COLOUR       as ROLES, not raw values: background, surface, surface-raised, border, text-primary,\n                  text-secondary, text-disabled, accent, accent-hover, success, warning, danger, focus.\n                  One accent, one meaning. A second accent needs a second meaning.\n                  Every pairing stated with its contrast ratio: text at ≥4.5:1 (≥3:1 large text),\n                  non-text UI boundaries and graphical objects at ≥3:1.\n     RADIUS       a scale of three or four values with what each is for. Not one value applied\n                  everywhere.\n     ELEVATION    what shadow MEANS here — a layer relationship, a detachable surface, a modal — and\n                  the values for each level. If elevation has no meaning, say so and use borders.\n     MOTION       durations (fast/base/slow), easing, what motion is FOR (explaining a state change or\n                  a spatial relationship), and the reduced-motion behaviour. Motion that decorates is\n                  excluded in section 7.\n\n5. TYPOGRAPHY IN USE\n   Maximum line length in characters, how orphan and widow control is handled, tabular figures for\n   numbers in tables, the capitalisation rule for headings, and the punctuation conventions (real\n   quotation marks, en dashes for ranges). These are the details that separate a built design from a\n   styled one.\n\n6. LAYOUT AND RHYTHM\n   The grid, the column count and gutter, the container\
  \ max-width, and how sections differ in rhythm.\n   Sections should NOT all have the same shape and the same spacing: state which sections are dense\n   and which are spacious, and what the difference communicates. Name the breakpoints and state that\n   they are chosen from where the content breaks, not from a device list.\n\n7. WHAT THIS DESIGN IS NOT — REQUIRED, AND THE MOST IMPORTANT SECTION\n   Name the specific signatures being excluded, so the defaults are ruled out rather than left\n   available:\n     - the default hue ramp and any decorative gradient\n     - glassmorphism and backdrop blur beyond one deliberate use\n     - glow shadows, floating orbs, and neon-on-dark as a palette strategy\n     - hero-plus-three-equal-cards, and any layout derived from a template slot count\n     - animation on load, animation without a cause, and any animation with no reduced-motion path\n     - filler copy: \"seamlessly\", \"unleash\", \"elevate\", \"in today's fast-paced world\"\n     - metrics without a definition and a source; badges that encode no state\n     - stock-photo humans; icon sets mixed from different families\n     - a single font family at default weights with sizes not on a scale\n     - anything present because it looked good rather than because it serves the content\n   For each exclusion, one line on what is done INSTEAD. An exclusion without a replacement will be\n   filled by the default.\n   If you cannot write this section specifically, the brief is not finished.\n\n8. ACCEPTANCE CRITERIA — each one checkable by looking at the built page\n   □ the intent sentence could not describe a competitor's product unchanged\n   □ every view has exactly one primary element, identifiable in under two seconds\n   □ the spacing values in use are exactly the tokens defined, with no invented intermediate\n   □ the type sizes in use are exactly the scale defined\n   □ the colour count is the defined set, and each hue has one meaning\n   □ every text and non-text contrast pairing meets its stated ratio\n   □ no element from the section 7 exclusion list is present\n   □ reading order matches DOM order; the page is fully operable by keyboard\n   □ target size ≥24×24 CSS px; content reflows at 320 px with no horizontal scroll\n   □ text resizes to 200% without loss; text-spacing overrides do not clip\n   □ every animation has a cause and a reduced-motion path\n   □ every number on the page has a definition and a source, or is removed\n   □ the copy could not be pasted onto a competitor's site unchanged\n   □ a screenshot of one section cannot be confused with a section from another page of the product\n\nDo not produce any visual implementation, component code or copy for the page. Produce the brief only.\nWhere you must choose and the inputs do not determine the answer, state the choice, state that it was\nunderspecified, and say what input would have determined it."
expected_output: 'An eight-section design brief: intent derived from the product and audience; usage context with the dominating factor named; the hierarchy decision naming exactly one primary element per view and how it is made primary; a complete token set covering spacing with a relationship mapping, a modular type scale, colour as roles with contrast ratios, radius and elevation with meaning; typographic conventions; layout and rhythm with content-derived breakpoints; a specific exclusion list naming the generic signatures ruled out and what replaces each; and acceptance criteria that are each checkable by looking at the built page. No visual implementation or component code.'
output_format: markdown
cacheable_prefix: false
estimated_tokens: 1219
evaluation:
  method: 'Feed the produced brief to an implementation pass, then audit the result with the ai-slop-detection skill and the WCAG checklist. Score: the intent sentence could not describe a competitor unchanged; every view has exactly one identifiable primary element; spacing and type values in use are exactly the defined tokens; no excluded signature appears; every acceptance criterion is objectively checkable; contrast pairings meet their stated ratios.'
  runs: 0
  pass_rate: null
failure_modes:
- 'An adjective brief: ''modern, clean, minimal, professional'' with no decision an implementer can derive from.'
- A token set with a gap, so each component invents its own value — which is the root cause of most generic output.
- No exclusions, so the defaults are not ruled out and will appear.
- A hierarchy that names two primaries, leaving the competition unresolved in the implementation.
- References given without a stated purpose, so they are copied rather than analysed.
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills:
- frontend-design
- design-systems
- visual-design-research
- ai-slop-detection
- motion-design
- accessibility-audit
related:
- knowledge/ui-ux/what-makes-a-website-look-professional.md
- knowledge/ui-ux/what-makes-ai-websites-look-generic.md
- knowledge/ui-ux/visual-hierarchy.md
- knowledge/ui-ux/ai-slop-signature-catalogue.md
- workflows/build-website/WORKFLOW.md
- workflows/ai-slop-remediation/WORKFLOW.md
sources:
- title: WCAG 2.2
  url: https://www.w3.org/TR/WCAG22/
  type: specification
  organization: W3C
  claim_type: fact
  confidence: very-high
  verified_at: '2026-09-15'
  note: 'The contrast, target-size, reflow and reduced-motion requirements that bound the token set: a colour or type decision that fails WCAG is not a valid design direction, and the brief requires the tokens to be stated at compliant values from the start.'
- title: Material Design 3 — foundations
  url: https://m3.material.io/foundations
  type: official-docs
  organization: Google
  claim_type: recommendation
  confidence: high
  verified_at: '2026-09-15'
  note: 'A worked example of the token structure this brief requires: colour roles rather than raw values, a type scale, an elevation system with meaning, and spacing tied to a base unit.'
---

# Design Direction Brief

## When to use this

Before visual implementation, and before any component library theme is touched. The output is the
reference that `design-systems`, `frontend-design` and `ai-slop-detection` are checked against. Without
it, every visual decision is made at the point of use, which is how a page ends up with eleven spacing
values and no hierarchy.

## The prompt


## Why it is shaped this way

```text
DECISIONS BEFORE AESTHETICS     Sections 1-3 decide what matters; sections 4-6 specify it. Reversing
                                the order produces a pretty brief that an implementer cannot build from.
TOKENS AS THE UNIT              A token set with a gap is an instruction to invent a value, and
                                invented values are the mechanism behind most generic output. One token
                                per RELATIONSHIP, not per element, is what makes spacing consistent.
ONE PRIMARY PER VIEW            Hierarchy is a decision, and an undecided hierarchy is rendered as
                                competing elements. Forcing the choice is the point of section 3.
A REQUIRED EXCLUSION LIST       Defaults are not absent; they are available. Ruling them out by name is
                                the only way they do not appear. An exclusion without a replacement gets
                                refilled by the default, which is why each needs one.
CONTRAST IN THE TOKEN SET       Accessibility is not a later audit step here; the tokens are stated at
                                compliant values so the design cannot be built non-compliant and then
                                fixed.
CHECKABLE ACCEPTANCE CRITERIA   "Looks professional" cannot be verified. Each criterion is answerable
                                by looking at the page, which is what makes the brief usable as a review
                                instrument later.
UNDERSPECIFICATION IS DECLARED  A model that must choose will choose silently otherwise. Requiring it to
                                flag the gap turns a hidden default into a visible open question.
NO IMPLEMENTATION IN THE OUTPUT Keeping the brief separate from the build prevents the brief from being
                                reverse-engineered to justify what was already produced.
```

## What a bad brief looks like

```text
✗ "Modern, clean, minimal, professional, with a premium feel."   Adjectives with no derivation and no
  exclusion. Any product could claim them.
✗ A token set with spacing values but no relationship mapping.   The implementer must still decide which
  value applies where, and will decide differently in each component.
✗ Colour given as hex values with no roles.   Nothing prevents the accent being used decoratively.
✗ No section 7, or a section 7 that says "nothing generic".   The defaults remain available.
✗ Two primary CTAs named as equally important.   The hierarchy decision was not made.
✗ Acceptance criteria that require judgement rather than observation.   They cannot be checked, so they
  will not be.
✗ References listed without what to take from them.   They will be copied rather than analysed.
```

## References

- [`knowledge/ui-ux/what-makes-a-website-look-professional.md`](../../knowledge/ui-ux/what-makes-a-website-look-professional.md) — the properties section 8 checks
- [`knowledge/ui-ux/what-makes-ai-websites-look-generic.md`](../../knowledge/ui-ux/what-makes-ai-websites-look-generic.md) — the mechanism section 7 excludes
- [`knowledge/ui-ux/visual-hierarchy.md`](../../knowledge/ui-ux/visual-hierarchy.md) — the channels section 3 uses
- [`knowledge/ui-ux/ai-slop-signature-catalogue.md`](../../knowledge/ui-ux/ai-slop-signature-catalogue.md) · [`knowledge/accessibility/wcag-practical-checklist.md`](../../knowledge/accessibility/wcag-practical-checklist.md)
- [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md) · [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md) · [`skills/visual-design-research/SKILL.md`](../../skills/visual-design-research/SKILL.md) · [`skills/motion-design/SKILL.md`](../../skills/motion-design/SKILL.md)
- [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md) · [`workflows/ai-slop-remediation/WORKFLOW.md`](../../workflows/ai-slop-remediation/WORKFLOW.md) · [`agents/ux-reviewer/AGENT.md`](../../agents/ux-reviewer/AGENT.md)
- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> · Material Design 3 foundations — <https://m3.material.io/foundations>
