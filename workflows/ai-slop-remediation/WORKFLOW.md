---
name: ai-slop-remediation
version: 1.0.0
description: >-
  Take an existing site that reads as AI-generated and make it read as designed — detect with
  evidence, group into root causes, delete before adding, rebuild the three systems, and re-measure
  until the S1 count is zero without flattening the site's character.
trigger: >-
  An existing website, landing page or application surface that stakeholders describe as "generic",
  "template-y" or "obviously AI-made"; or a pre-launch review that failed the slop gate in
  workflows/build-website stage 9.
not_for: >-
  Building a new site from scratch (use workflows/build-website, which prevents the slop rather
  than removing it); purely internal tooling where utility is the only requirement and the owner has
  said so; a deliberate brutalist or maximalist design — apply the craft checks but not the
  restraint checks; an accessibility or performance problem mislabelled as a design problem.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [ai-slop, remediation, design, frontend, quality, workflow]
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
estimated_duration: hours for a landing page; days for a multi-page product surface
stages:
  - id: 1
    name: Establish the target
    goal: Define what "designed" means for this specific product, audience and brand — otherwise remediation replaces one cliché with another.
    skill: visual-design-research
    inputs: [the site, the audience, the business goal, existing brand assets, 3-6 reference products at the target quality level]
    outputs: [Design Direction Brief with intended impression, position, adopted conventions, at most two differentiators, explicit rejections and anti-references]
    exit_gate: A written direction exists with explicit rejections, or the owner has accepted a conventional direction in writing and the remediation scope is limited to craft and consistency.
    max_loops: 2
    on_gate_failure: Escalate. Remediating without a target produces a different default, not a better design.
  - id: 2
    name: Capture at full coverage
    goal: Collect the evidence base — every template and state, at every required breakpoint, in both themes.
    skill: ai-slop-detection
    agent: website-quality-reviewer
    inputs: [the site, breakpoint list (360/768/1440 minimum), state list, theme list]
    outputs: [screenshot set, DOM captures, source access, computed-style extracts]
    exit_gate: Every template is captured in default, hover, focus, empty, loading, error and modal-open states, at every breakpoint, in both themes.
    on_gate_failure: Complete the capture. A review at 1440 px only will miss the majority of real defects.
  - id: 3
    name: Detect mechanically
    goal: Run the full slop catalogue against source and captures, producing symptoms with IDs, evidence and severity.
    skill: ai-slop-detection
    inputs: [captures, source, catalogue]
    outputs: [symptom table — catalogue ID, evidence at file:line or screenshot reference, severity S1/S2/S3]
    exit_gate: Every symptom carries a catalogue ID and concrete evidence, and the source has been grepped for the tell-tale tokens (backdrop-filter, gradient utilities, blur, indigo/purple ramps, pulse/bounce animations, filler adjectives, unsubstantiated metrics).
    max_loops: 2
    on_gate_failure: Remove symptoms that have no evidence. An unevidenced symptom is a taste judgement, and it discredits the rest of the report.
  - id: 4
    name: Measure the systems
    goal: Quantify the underlying disorder — spacing values, type sizes, hues, radii, shadows — so the fix targets the cause.
    skill: design-systems
    inputs: [computed-style extracts, source]
    outputs: [audit table of distinct values per property, count of off-scale values, near-duplicate component inventory]
    exit_gate: Distinct spacing values, font sizes, saturated hues, radii and shadow definitions are counted, and the count of values not drawn from a 4/8 px or modular scale is recorded.
    on_gate_failure: Extract from the rendered pages rather than the source; build-time values can be transformed before they reach the browser.
  - id: 5
    name: Group into root causes
    goal: Reduce the symptom list to at most five causes, so remediation changes systems rather than pixels.
    skill: ai-slop-detection
    inputs: [symptom table, audit table]
    outputs: [root-cause grouping with each symptom mapped to a cause]
    exit_gate: Every symptom maps to a cause, and there are five or fewer causes. Ungrouped symptoms mean the analysis is incomplete.
    max_loops: 2
    on_gate_failure: Re-read the symptoms. Typical causes are a missing spacing/type/colour system, decoration substituting for hierarchy, no content model, and no motion rationale.
  - id: 6
    name: Plan the remediation
    goal: Prioritise by blocking severity and recommend the smallest system change that removes the most symptoms.
    skill: ai-slop-detection
    inputs: [root-cause grouping, Design Direction Brief, effort constraints]
    outputs: [prioritised plan — CRITICAL/HIGH/MEDIUM/LOW, each with symptom IDs, the concrete change, effort and expected effect]
    exit_gate: The plan is ordered CRITICAL to LOW, every S1 symptom appears in CRITICAL or HIGH, and the first items are system changes (define the three scales) rather than per-element restyling.
    on_gate_failure: Re-order. Fixing twenty symptoms individually when one token file would fix eighteen is the most expensive possible path.
  - id: 7
    name: Delete
    goal: Remove before adding — deletion resolves more slop than any quantity of new styling.
    skill: frontend-implementation
    agent: frontend-engineer
    inputs: [remediation plan, source]
    outputs: [reduced source — gradients, blur layers, floating decoration, glow shadows, filler sections, fake metrics, placeholder copy, decorative controls, meaningless badges removed]
    exit_gate: Every decorative gradient, backdrop-blur layer beyond one, floating shape, glow shadow, unsubstantiated metric, filler adjective and unwired control identified in the plan is gone.
    max_loops: 2
    on_gate_failure: Re-check the plan; a symptom that survived deletion usually means its root cause is structural rather than decorative.
  - id: 8
    name: Establish the three systems
    goal: Define spacing, type and colour as role-named tokens with contrast-checked pairs, and bind components to them.
    skill: design-systems
    inputs: [Design Direction Brief, audit table, accessibility target]
    outputs: [token files, lint rules banning raw values, migrated components]
    exit_gate: A modular type scale and a 4/8 px spacing scale are defined, colour is expressed as roles with every text/surface pair contrast-checked at WCAG AA, and lint fails on any raw value in a component.
    max_loops: 2
    on_gate_failure: Fix the palette or the surfaces until contrast passes. Do not weaken the accessibility target to preserve a colour.
  - id: 9
    name: Rebuild hierarchy
    goal: Give each view exactly one primary element, distinguishable in at least three dimensions, and vary density deliberately between sections.
    skill: frontend-design
    inputs: [tokens, IA, content inventory with real strings]
    outputs: [recomposed views, with the primary element identified per view and per breakpoint]
    exit_gate: Each view has one primary element distinguishable in at least three of size, weight, colour, position, space, saturation or motion, and the squint/blur test identifies it at every breakpoint.
    max_loops: 3
    on_gate_failure: Remove competing elements rather than strengthening the primary one. If two elements compete, the user chooses neither.
  - id: 10
    name: Replace content
    goal: Put specific, true statements where filler was — this is the largest single contributor to "reads as generated".
    skill: documentation
    inputs: [product facts, real metrics with definitions, named customers or their absence, real screenshots or data]
    outputs: [rewritten copy, real or removed metrics, genuine imagery or none]
    exit_gate: No unsubstantiated metric remains, no filler adjective remains, every claim is specific and true, and stock imagery has been replaced with the actual product, real data or nothing.
    max_loops: 2
    on_gate_failure: Escalate to the owner for real facts. Inventing a plausible metric to replace a fake one is worse than removing it.
  - id: 11
    name: Add one deliberate detail
    goal: Restore character — remediation that only removes leaves a bland site, which is its own failure.
    skill: visual-design-research
    inputs: [Design Direction Brief, recomposed views]
    outputs: [at most two differentiators implemented, each documented with its purpose and risk]
    exit_gate: At least one deliberate, non-generic design decision is present and documented, and no more than two differentiators compete.
    on_gate_failure: Choose one. Zero differentiators is blandness; five is incoherence.
  - id: 12
    name: Motion rationalisation
    goal: Keep only motion that explains causality, continuity, feedback, hierarchy, state or relationship, with a complete reduced-motion path.
    skill: motion-design
    inputs: [existing animations, motion tokens]
    outputs: [motion specification per surviving animation, reduced-motion implementation, removed decorative animation]
    exit_gate: Every surviving animation names a purpose; load-time entrance animation without a cause is removed; durations follow the hierarchy; prefers-reduced-motion yields a complete experience; nothing flashes more than three times per second.
    on_gate_failure: Remove the animation. Decorative motion is never worth defending.
  - id: 13
    name: Verify no regression
    goal: Confirm the remediation did not break accessibility, responsiveness, performance or meaning.
    skill: accessibility-audit
    inputs: [remediated site, breakpoint list, WCAG target, performance budget]
    outputs: [contrast measurements at every breakpoint and theme, keyboard and screen-reader pass results, Core Web Vitals, responsive verification at 360 px]
    exit_gate: Contrast passes AA everywhere, every interactive element is keyboard operable with a visible focus indicator, nothing overflows at 360 px, tap targets are at least 24x24 CSS px, and Core Web Vitals are within budget with no new layout shift.
    max_loops: 2
    on_gate_failure: Fix the regression before re-measuring slop. A less generic site that is unusable is not an improvement.
  - id: 14
    name: Re-score and lock in
    goal: Measure the improvement and prevent decay.
    skill: ai-slop-detection
    agent: skill-curator
    inputs: [original and current symptom tables, remediated site]
    outputs: [slop score before and after, verdict, CI lint and visual-regression gates, design-token ownership, review date]
    exit_gate: S1 count is zero, the slop score has fallen by at least 70%, visual-regression and token-lint gates run in CI, and a re-review date is scheduled.
    max_loops: 3
    on_gate_failure: Return to stage 6 with the residual symptoms. If S1 symptoms remain, each needs a written justification accepted by the owner before ship.
quality_gates:
  - A Design Direction Brief with explicit rejections exists before remediation begins.
  - Captures cover every template, state, breakpoint and theme.
  - 100% of symptoms carry a catalogue ID and concrete evidence.
  - Symptoms grouped into five or fewer root causes.
  - Deletion precedes addition.
  - Spacing, type and colour-role tokens defined, contrast-checked at AA, and lint-enforced.
  - Zero raw visual values remain in component code.
  - Each view has exactly one primary element, distinguishable in at least three dimensions.
  - No unsubstantiated metric or filler adjective remains; every claim is specific and true.
  - At least one deliberate non-generic design decision documented; no more than two differentiators.
  - Every surviving animation names a purpose; reduced-motion path complete.
  - Accessibility, responsiveness and performance verified after remediation, not only before.
  - S1 count is zero and slop score reduced by at least 70%, or residuals are justified in writing.
  - CI gates prevent decay; re-review scheduled.
artifacts:
  - Design Direction Brief
  - capture set across states, breakpoints and themes
  - symptom table with IDs, evidence and severity
  - value audit table
  - root-cause grouping
  - prioritised remediation plan
  - token files and lint rules
  - recomposed views with identified primary elements
  - rewritten copy and content decisions
  - motion specification
  - post-remediation accessibility, responsive and performance verification
  - before/after slop score, verdict and CI gates
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: Google Chrome team
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Thresholds change; verify current values before quoting numbers."
related: [skills/ai-slop-detection/SKILL.md, workflows/build-website/WORKFLOW.md, agents/website-quality-reviewer/AGENT.md, knowledge/ui-ux/]
---

# Workflow: AI-Slop Remediation

```text
1 TARGET → 2 CAPTURE → 3 DETECT → 4 MEASURE → 5 ROOT-CAUSE → 6 PLAN → 7 DELETE
  → 8 SYSTEMS → 9 HIERARCHY → 10 CONTENT → 11 CHARACTER → 12 MOTION → 13 NO-REGRESSION → 14 RE-SCORE
```

## The three ideas that make this work

```text
DELETION BEFORE ADDITION (stage 7).  Most slop is present because something was added —
    a gradient, a blur, an orb, a badge, a testimonial strip. Removing it costs nothing and
    fixes more than any quantity of new styling. Addition comes only at stage 11, and only once.

SYSTEMS BEFORE PIXELS (stages 5, 6, 8).  Twenty symptoms usually trace to three missing scales.
    Defining spacing, type and colour roles in one commit resolves more symptoms than twenty
    individual edits, and it prevents the twentieth from returning.

TARGET BEFORE FIX (stage 1).  Without a written direction containing explicit rejections, the
    remediation converges on a different cliché. Fixing "generic purple gradient" into "generic
    brutalist mono" is not progress.
```

## The failure this workflow must also avoid

**Over-correction.** A site stripped of every deviation is bland, and blandness is its own
recognition signature. Stage 11 exists for this reason: exactly one or two deliberate
differentiators, documented, with their risk stated. The goal is *deliberate*, not *minimal*.

## Scaling

```text
SINGLE LANDING PAGE    1 (abbreviated), 2, 3, 5, 6, 7, 8 (minimal scales), 9, 10, 13, 14
MULTI-PAGE SITE        all stages
PRODUCT / DASHBOARD    all stages, with stage 8 expanded into a real design system and
                       stage 13 expanded into a journey-level accessibility pass
PRE-LAUNCH GATE ONLY   stages 2, 3, 5, 6, 14 — detect and score, hand the plan to build-website
```

## References

- [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md) — the full catalogue with IDs, detection rules and fix directions
- [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md) · [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md)
- [`skills/visual-design-research/SKILL.md`](../../skills/visual-design-research/SKILL.md) · [`skills/motion-design/SKILL.md`](../../skills/motion-design/SKILL.md)
- [`skills/accessibility-audit/SKILL.md`](../../skills/accessibility-audit/SKILL.md)
- [`agents/website-quality-reviewer/AGENT.md`](../../agents/website-quality-reviewer/AGENT.md)
- [`workflows/build-website/WORKFLOW.md`](../build-website/WORKFLOW.md) — prevention is cheaper than remediation
- [`knowledge/ui-ux/`](../../knowledge/ui-ux/) · [`anti-patterns/frontend/`](../../anti-patterns/frontend/)
