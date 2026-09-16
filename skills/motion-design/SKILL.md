---
name: motion-design
version: 1.0.0
description: >-
  Use animation to explain causality, state and spatial relationship — with a duration/easing system,
  a strict purpose test, and a complete reduced-motion path.
category: design
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [motion, animation, transitions, microinteraction, reduced-motion, ui]
applies_to: [web, saas, dashboard, marketing-site]
priority: 78
requires: [design-systems]
conflicts_with: []
estimated_tokens: 2539
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Motion system
    anchor: "#motion-system"
    purpose: implementation
  - heading: The purpose test
    anchor: "#the-purpose-test"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "WCAG 2.2 — 2.3.3 Animation from Interactions"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "MDN — prefers-reduced-motion"
    url: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
    type: official-docs
    organization: Mozilla
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [design-systems, frontend-design, frontend-implementation, accessibility-audit, ai-slop-detection]
related_repositories: [motiondivision/motion, react-spring/react-spring, pmndrs/zustand]
tests: 23
---

# Motion Design

## Purpose

Make change **legible**. Motion exists to answer three questions a static frame cannot:
where did this come from, what just happened, and what is related to what. Everything else
is decoration, and decoration that moves is the most recognisable signature of generated UI.

## When to Use

```text
□ Any state change the user triggers and must understand (open/close, add/remove, select)
□ Spatial relationships: an element moving between containers, expanding from its origin
□ Feedback that a system acknowledged an action (press, submit, success, failure)
□ Directing attention to the one thing that changed
□ Continuity across navigation, so context is not lost
```

## When NOT to Use

```text
✗ To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slop-detection)
✗ On data that updates continuously (dashboards, logs, tickers) — motion obscures the value
✗ Entrance animations on content the user came to read
✗ Anything that delays an interaction's result
✗ Where the user has asked for reduced motion — provide the non-motion equivalent
```

## Motion system

Define these as tokens in the design system, not as values in components.

```text
DURATION      a hierarchy, not one number:
                instant    ~80–120 ms   hover, active, focus, toggle, tiny state
                fast       ~150–200 ms  menu, tooltip, dropdown, small element move
                normal     ~220–300 ms  modal, drawer, card expand, tab switch
                slow       ~350–500 ms  page-level transition, large spatial rearrangement
              Rules: exits are ~30% faster than entrances (nothing should feel laggy leaving);
              larger distance/mass → longer duration; nothing over ~500 ms unless it is a
              deliberate narrative sequence with a way to skip it.

EASING        asymmetric by intent:
                enter / decelerate  fast start, soft landing — the element arrives
                exit / accelerate   slow start, fast finish — the element leaves
                standard            for movement within the same context
                spring              for direct manipulation and physical continuity, damped
              Never linear for UI elements — linear reads as mechanical and unfinished.
              Never the default `ease` everywhere — it encodes no intent.

PROPERTY      animate only compositor-friendly properties: transform and opacity.
              Animating width/height/top/left/margin/box-shadow triggers layout and paint on
              every frame. If you must animate a shadow, cross-fade two pre-rendered layers.

CHOREOGRAPHY  related elements move in sequence with a small stagger (~30–60 ms), in the
              direction of reading, origin-first. Unrelated elements do not animate together.
              One element is the subject; the rest are support.

SCOPE         one primary motion per view. Competing animations cancel each other's meaning.

PERFORMANCE   respect the frame budget: 60 fps means ~16.7 ms per frame; target 8.3 ms of work.
              No jank on mid-range mobile — test there, not on a workstation.
              Use will-change sparingly and remove it; promote layers deliberately, not globally.
```

## The purpose test

Before adding any animation, name the purpose. If none of these is the answer, do not add it.

```text
CAUSALITY      "This appeared because you did that." — links action to result
CONTINUITY     "This is the same object, now here." — preserves identity across a change
               (shared-element transitions, expand-from-origin, collapse-to-origin)
FEEDBACK       "The system received and completed your action." — press, pending, success, error
HIERARCHY      "This is what changed and matters now." — directs attention to one thing
STATE          "This is now selected/open/disabled/loading." — makes a state visible over time
RELATIONSHIP   "These belong together; those do not." — grouping and spatial structure
ORIENTATION    "You moved from here to there." — navigation and zoom context
```

Rules that follow:

```text
1. Motion is triggered by a cause — user action, data arrival, or state change. Never by
   the mere existence of the element.
2. Interruptible: a second interaction during an animation must retarget, not queue.
3. Skippable: no animation may delay the availability of content or a control.
4. Reversible: exit motion mirrors entrance (faster), so the model of the interface is consistent.
5. Consistent: the same kind of change uses the same motion everywhere. Two different
   animations for "close a panel" is a defect.
6. Reduced motion is a first-class path, not an afterthought: honour
   `prefers-reduced-motion` by removing non-essential motion and replacing essential
   motion with an instant state change or a cross-fade. The experience must remain
   complete and understandable — never merely frozen mid-state. (WCAG 2.2 §2.3.3.)
7. No flashing more than three times per second (WCAG 2.3.1) — this is a seizure risk,
   not a taste matter.
8. Auto-playing motion longer than ~5 s must have a visible pause/stop control (WCAG 2.2.2).
```

## Implementation notes

```text
CSS first      Transitions and keyframes for anything the compositor can own. Reach for a
               JS animation library only when you need physics, gestures, shared-element
               choreography across routes, or interruption semantics.
Declare states Animate between explicit states, not by imperatively poking styles.
               A state machine (idle → pressed → loading → success → idle) prevents the
               impossible transitions that cause visual bugs.
Reserve space  Motion must not cause layout shift for other content (CLS).
Test           at 60 fps on a throttled mid-range device; with reduced motion on;
               at every breakpoint; interrupted mid-animation; and with the data slow.
Document       every motion in the design system: purpose, trigger, duration token,
               easing token, reduced-motion behaviour.
```

## Failure Modes

```text
DECORATIVE MOTION     Animation with no cause — the strongest AI-slop signal (M1, M3).
UNIFORM 300ms EASE    Every transition identical; no hierarchy, no intent (M2).
LINEAR UI MOTION      Mechanical, unfinished feel.
LAYOUT-PROPERTY ANIMATION  Animating height/top/box-shadow; dropped frames under load.
NON-INTERRUPTIBLE     Queued animations that ignore the user's second click.
BLOCKING ENTRANCE     Content unavailable until the animation completes.
MISSING REDUCED PATH  Motion runs regardless of user preference — an accessibility failure.
INCONSISTENT SEMANTICS Two different animations for the same kind of change.
FLASHING / AUTOPLAY   Seizure risk and no pause control.
DATA-CHART ANIMATION  Re-animating the whole chart on every update, hiding the actual change.
MOTION AS MASK        Animating to distract from a slow operation instead of fixing the slowness.
```

## Quality Checklist

```text
□ Duration, easing and property tokens defined in the design system; components use only tokens
□ Every animation names a purpose from the purpose test; decorative motion removed
□ Duration hierarchy applied: instant/fast/normal/slow, exits ~30% faster than entrances
□ Non-linear, intent-matched easing; no `linear` and no default `ease` everywhere
□ Only transform/opacity animated (or a justified, measured exception)
□ One primary motion per view; related elements staggered in reading order
□ Motions are interruptible, skippable, reversible and semantically consistent
□ `prefers-reduced-motion` path complete: experience still understandable, never frozen mid-state
□ No flashing >3×/s; auto-playing motion >5 s has a pause control
□ No layout shift caused by motion; no content blocked by it
□ Verified at 60 fps on a throttled mid-range device and at every breakpoint
□ Each motion documented with purpose, trigger, tokens and reduced-motion behaviour
```

## Anti-Patterns

```text
✗ Entrance animations on every card, staggered, on page load, for no reason
✗ A logo that animates on load
✗ Floating blurred orbs drifting in the background
✗ `transition: all 300ms ease` applied globally
✗ Animating `height: auto` with a JS-driven maxHeight hack and jank
✗ A spinner that delays content the server already returned
✗ Ignoring `prefers-reduced-motion` because "it looks worse"
✗ A chart that re-animates every bar when one value changes
```

## References

- [`design-systems`](../design-systems/SKILL.md) · [`frontend-design`](../frontend-design/SKILL.md)
- [`ai-slop-detection`](../ai-slop-detection/SKILL.md) — motion symptoms M1–M5
- [`accessibility-audit`](../accessibility-audit/SKILL.md) · [`patterns/animation/`](../../patterns/animation/)
- [`knowledge/motion/`](../../knowledge/motion/)
- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> · `prefers-reduced-motion` — <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion>

## Related Skills

`design-systems` · `frontend-design` · `frontend-implementation` · `accessibility-audit` ·
`ai-slop-detection` · `performance-audit`

## Evaluation Criteria

```text
1. Purpose coverage: 100% of animations have a documented purpose from the test; 0 decorative.
2. System compliance: 0 hard-coded durations/easings in components.
3. Accessibility: reduced-motion path complete; no flashing; pause controls present.
4. Performance: 60 fps on a throttled mid-range device; 0 layout-property animations.
5. Consistency: the same change type uses the same motion across the product.
6. Latency neutrality: no interaction's result is delayed by motion.
```

Test cases in [`tests/`](tests/).
