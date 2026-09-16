---
name: build-website
version: 1.0.0
description: >-
  End-to-end production of a website that looks designed rather than generated — research the
  direction, design the system, implement it, then pass the accessibility, slop and performance
  gates before anything is called finished.
trigger: >-
  A request to build, redesign or substantially extend a website, landing page, marketing site,
  dashboard or web application, where the visual result will be seen by users.
not_for: >-
  Backend-only work; a pure content edit; extending an existing surface inside an established
  design system (use the system, do not re-derive it); internal tooling where utility is the only
  requirement and the requester has said so.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [website, frontend, design, build, workflow, quality-gate, ai-slop]
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
estimated_duration: hours to days depending on scope; the gates are not optional at any scale
stages:
  - id: 1
    name: Brief and content inventory
    goal: Establish the audience, the single most important action, the real content with its variance, and the constraints.
    skill: project-planning
    inputs: [requester brief, brand assets, existing content, technical constraints]
    outputs: [brief, critical tasks, content inventory with variance, constraint list]
    exit_gate: Real content exists for every section, including shortest and longest plausible strings, and empty/one/many/error data states. Placeholder copy is not accepted.
    on_gate_failure: Request the content or write it and get sign-off. Designing against lorem ipsum produces layouts that break on first contact with truth.
  - id: 2
    name: Visual design research
    goal: Build a written, defensible visual direction from real references instead of reaching for the default generated aesthetic.
    skill: visual-design-research
    inputs: [brief, audience, 3-6 competitors, differentiator]
    outputs: [Design Direction Brief — intended impression, position, aesthetic, adopted conventions, at most two differentiators, explicit rejections, anti-references]
    exit_gate: 15-30 references across four pools including anti-references, 5-8 fully decomposed with "why it works", and the brief states explicit rejections.
    max_loops: 2
    on_gate_failure: Escalate to the requester for references or for acceptance of a conventional direction, recorded as unresearched.
  - id: 3
    name: Information architecture
    goal: Decide structure and priority before any pixels — what the user does here, what must be true to succeed, and in what order.
    skill: frontend-design
    inputs: [brief, critical tasks, content inventory]
    outputs: [per-view priority outline, navigation model, reading and action order, page inventory]
    exit_gate: Every view has exactly one primary element identified, and content that serves no task has been removed rather than placed.
    on_gate_failure: Re-derive from the task list; a layout with no task behind it is decoration.
  - id: 4
    name: Design system and tokens
    goal: Define the three systems that remove most slop before any component is drawn — spacing scale, type scale, colour roles.
    skill: design-systems
    inputs: [Design Direction Brief, IA, brand constraints, accessibility level]
    outputs: [token definitions — spacing, type, colour roles with contrast-checked pairs, radius, elevation, motion durations and easings]
    exit_gate: Every semantic colour token has a contrast-checked partner at WCAG AA, and every token is named by role rather than by appearance.
    max_loops: 2
    on_gate_failure: Fix the palette or the surfaces until contrast passes; never ship a token set that fails AA.
  - id: 5
    name: Composition and craft
    goal: Design the views with deliberate hierarchy, asymmetry, density variation and craft details, plus one signature element specific to this product.
    skill: frontend-design
    inputs: [IA, tokens, content inventory, Design Direction Brief]
    outputs: [compositions for every view and state, at every required breakpoint, in both themes]
    exit_gate: Each view's primary element is distinguishable in at least three dimensions, and the squint/blur test identifies it at every breakpoint.
    max_loops: 3
    on_gate_failure: Reduce competing elements. If two elements compete, the user chooses neither.
  - id: 6
    name: Motion design
    goal: Add animation only where it explains causality, continuity, feedback, hierarchy, state or relationship — with a complete reduced-motion path.
    skill: motion-design
    inputs: [compositions, motion tokens]
    outputs: [motion specification per interaction — purpose, trigger, duration token, easing token, reduced-motion behaviour]
    exit_gate: Every animation names a purpose from the purpose test; nothing flashes more than three times per second; prefers-reduced-motion yields a complete, understandable experience.
    on_gate_failure: Remove the animation. Decorative motion is the strongest AI-slop signal and it is never worth defending.
  - id: 7
    name: Implementation
    goal: Build the design in code with token-only styling, accessible primitives, every state implemented, and generated types at the data boundary.
    skill: frontend-implementation
    agent: frontend-engineer
    inputs: [tokens, compositions, motion spec, content model, API contract]
    outputs: [components, routes with recorded rendering strategy, data layer, component tests]
    exit_gate: Zero raw colour, spacing or type values in component code, and every data-bound component implements empty, loading, error, partial and success states.
    max_loops: 3
    on_gate_failure: Return to stage 4 or 5 — a hard-coded value usually means the token set is missing something the design needs.
  - id: 8
    name: Accessibility gate
    goal: Prove a user with assistive technology can complete every critical task.
    skill: accessibility-audit
    inputs: [implementation, critical tasks, target WCAG level, device matrix]
    outputs: [findings per criterion with barrier, evidence, remediation, priority; conformance statement]
    exit_gate: All seven audit passes run at every breakpoint and theme; every critical task is completable by keyboard and by screen reader; no P1 barriers remain.
    max_loops: 3
    on_gate_failure: Fix and re-audit. An automated scan alone is not a pass — it detects roughly a third of issues.
  - id: 9
    name: AI-slop gate
    goal: Detect and remove the signatures of generated design, with evidence per symptom and remediation aimed at root causes.
    skill: ai-slop-detection
    agent: website-quality-reviewer
    inputs: [implementation, Design Direction Brief, breakpoints]
    outputs: [symptom table with IDs and evidence, root-cause grouping, prioritised remediation, slop score before and after]
    exit_gate: S1 symptom count is zero, or each remaining S1 has a written justification accepted by the requester, and at least one deliberate non-generic design decision is documented.
    max_loops: 3
    on_gate_failure: Delete before adding — removal fixes more slop than any amount of new styling. Do not replace one cliché with another.
  - id: 10
    name: Performance and SEO gate
    goal: Meet the agreed Core Web Vitals budget on the target device profile, and confirm the pages that should be found can be crawled, rendered and indexed.
    skill: performance-audit
    agent: performance-engineer
    inputs: [implementation, budgets, target population, critical pages]
    outputs: [baseline and after measurements by segment, ranked profile, remediation, CI budget gates, SEO findings]
    exit_gate: Core Web Vitals within budget at field p75 for the target profile, no regression in error rate or correctness, and every indexable page has its primary content in the served HTML or verified as rendered.
    max_loops: 2
    on_gate_failure: Remove work before adding infrastructure — deletion, caching, code-splitting and image optimisation precede any scaling decision.
  - id: 11
    name: Usability review
    goal: Walk every critical task cold, in success and failure states, on the audience's device profile.
    skill: frontend-design
    agent: ux-reviewer
    inputs: [implementation, critical tasks, audience, content model]
    outputs: [task walkthroughs, barrier report with severity and smallest fix, IA review, verdict]
    exit_gate: Every critical task is completable by a first-time user with no P1 barriers, in both success and failure states.
    max_loops: 2
    on_gate_failure: Fix the barrier with the smallest effective change; preferences are recorded separately and do not block.
  - id: 12
    name: Browser verification and ship
    goal: Verify in real browsers at real breakpoints with real content, then release through a reversible, observable deploy.
    skill: browser-testing
    agent: qa-engineer
    inputs: [implementation, journey list, device and browser matrix]
    outputs: [browser test results, cross-browser matrix, verification report, deploy record]
    exit_gate: Critical journeys pass in the target browser matrix at every breakpoint with real content, both themes, reduced motion on and off, and the deploy has a verified instant rollback path.
    max_loops: 2
    on_gate_failure: Fix and re-verify; do not ship on a desktop-only pass or a retry that happened to go green.
quality_gates:
  - Real content exists before design begins; no placeholder copy reaches stage 5.
  - A Design Direction Brief with explicit rejections exists before composition.
  - Spacing, type and colour-role tokens are defined and used exclusively by components.
  - Every semantic colour pair passes WCAG AA contrast, measured with a tool.
  - Every animation names a purpose and has a complete prefers-reduced-motion path.
  - Zero raw visual values in component code.
  - Every data-bound component implements empty, loading, error, partial and success states.
  - All seven accessibility passes run; every critical task keyboard and screen-reader operable.
  - AI-slop S1 count is zero, or each is justified in writing and accepted.
  - Core Web Vitals within budget at field p75 for the target device profile.
  - Every critical task walked cold in success and failure states with no P1 barrier.
  - Verified in the real browser matrix, at 360/768/1440 px, in both themes.
  - Indexable pages have their primary content in the served HTML or verified as rendered.
  - The deploy has a rehearsed instant rollback and observability wired from the first request.
artifacts:
  - brief and content inventory
  - Design Direction Brief
  - information architecture and page inventory
  - token definitions
  - compositions for every view, state, breakpoint and theme
  - motion specification
  - implementation with component and browser tests
  - accessibility findings and conformance statement
  - slop symptom table, root causes, remediation and before/after score
  - performance baseline, profile and after-measurement
  - usability walkthroughs and barrier report
  - browser verification matrix and deploy record
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
related: [skills/frontend-design/SKILL.md, skills/ai-slop-detection/SKILL.md, workflows/ai-slop-remediation/WORKFLOW.md, agents/website-quality-reviewer/AGENT.md]
---

# Workflow: Build Website

Twelve stages in a deliberate order: **research → structure → system → composition → motion →
implementation → four gates → ship.** The four gates (accessibility, slop, performance, usability)
are not review steps at the end; they are conditions of calling the work finished.

```text
1 BRIEF+CONTENT → 2 DESIGN RESEARCH → 3 IA → 4 TOKENS → 5 COMPOSITION → 6 MOTION
  → 7 IMPLEMENT → 8 A11Y GATE → 9 SLOP GATE → 10 PERF+SEO GATE → 11 UX REVIEW → 12 VERIFY+SHIP
```

## The two decisions that determine the outcome

```text
STAGE 1 — REAL CONTENT.   Designing against placeholder copy is why generated sites break with
                          real data: the longest headline, the empty table, the error state and
                          the 1,000-row list were never in the picture.
STAGE 2 — WRITTEN DIRECTION. Without a Design Direction Brief containing explicit rejections,
                          stage 5 defaults to the highest-probability layout in the model's
                          training distribution. That is the slop, and stage 9 will spend its
                          whole budget removing it.
```

Every later gate is cheaper when these two stages were done properly.

## Scaling the workflow

```text
SINGLE LANDING PAGE    1, 2 (abbreviated — 10 references, one anti-reference set), 3, 4 (minimal
                       scale), 5, 7, 8 (passes 1-3), 9, 12
FULL MARKETING SITE    all stages
PRODUCT / DASHBOARD    all stages, with stage 4 expanded into a real design system and stage 12
                       expanded into a journey suite
REDESIGN               start at stage 1 with a content and IA audit of the existing site; carry
                       the existing brand constraints into stage 2
REMEDIATION ONLY       use workflows/ai-slop-remediation instead — it starts from an existing site
```

## Failure modes specific to this workflow

```text
SKIPPING TO STAGE 7     "Just build it and we'll design as we go." The result is the default
                        layout, and stages 8-11 then produce a long list of expensive fixes.
GATE DEFERRAL           Passing a gate conditionally with a promise to fix later. The promise
                        does not survive the release.
TOKEN THEATRE           Tokens defined at stage 4 and hard-coded values arriving at stage 7.
                        Lint from the first component, not at the end.
SLOP FIX BY RESTYLING   Re-colouring the gradient instead of asking why it exists. Root causes
                        first; deletion before addition.
OVER-CORRECTION         Stripping all character to pass the slop gate. The goal is deliberate,
                        not minimal — one signature element must survive.
DESERTED BRIEF          Stage 5 drifts from the Design Direction Brief with no amendment.
                        Trace every token to a line in the brief.
```

## References

- [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md)
- [`skills/visual-design-research/SKILL.md`](../../skills/visual-design-research/SKILL.md) · [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md)
- [`skills/frontend-implementation/SKILL.md`](../../skills/frontend-implementation/SKILL.md) · [`skills/accessibility-audit/SKILL.md`](../../skills/accessibility-audit/SKILL.md)
- [`skills/motion-design/SKILL.md`](../../skills/motion-design/SKILL.md) · [`skills/performance-audit/SKILL.md`](../../skills/performance-audit/SKILL.md)
- [`workflows/ai-slop-remediation/WORKFLOW.md`](../ai-slop-remediation/WORKFLOW.md)
- [`agents/frontend-engineer/AGENT.md`](../../agents/frontend-engineer/AGENT.md) · [`agents/website-quality-reviewer/AGENT.md`](../../agents/website-quality-reviewer/AGENT.md)
- [`knowledge/ui-ux/`](../../knowledge/ui-ux/) · [`patterns/ui/`](../../patterns/ui/)
