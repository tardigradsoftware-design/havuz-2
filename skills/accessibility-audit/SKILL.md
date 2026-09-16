---
name: accessibility-audit
version: 1.0.0
description: >-
  Audit an interface against WCAG with real assistive-technology testing — automated scans find
  roughly a third of issues; keyboard, screen-reader and cognitive passes find the rest.
category: design
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [accessibility, a11y, wcag, audit, inclusive-design, frontend]
applies_to: [web, saas, dashboard, marketing-site]
priority: 86
requires: []
conflicts_with: []
estimated_tokens: 2779
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Audit passes
    anchor: "#audit-passes"
    purpose: implementation
  - heading: Reporting
    anchor: "#reporting"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    published: 2023-10-05
    license: W3C Document License
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "Understanding WCAG 2.2"
    url: https://www.w3.org/WAI/WCAG22/Understanding/
    type: official-docs
    organization: W3C WAI
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "axe-core"
    url: https://github.com/dequelabs/axe-core
    type: github-repository
    organization: Deque Systems
    license: MPL-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [frontend-design, design-systems, code-review, browser-testing, seo-audit]
related_repositories: [dequelabs/axe-core, Siteimprove/alfa, microsoft/playwright, a11yproject/a11yproject.com]
tests: 20
---

# Accessibility Audit

## Purpose

Establish, with evidence, whether people using assistive technology can complete the
actual tasks on a page — and produce a remediation list ordered by the barrier's severity,
not by how easy it is to fix.

**Automated tooling detects roughly 30–50% of WCAG issues** (a widely cited practitioner
range; treat the exact figure as approximate). It finds missing attributes and contrast
failures. It cannot find a broken focus order, an unlabelled control that has an
`aria-label` of "button", a modal that traps the wrong element, or a flow that is
impossible without a mouse. Manual passes are the audit; the scanner is a pre-filter.

## When to Use

```text
□ Before launching or redesigning any public-facing interface
□ Per release for products under accessibility obligations (public sector, EU EAA, ADA-exposed)
□ After adding a complex interactive component (data grid, editor, map, drag-and-drop, chart)
□ When a user reports a barrier — audit the whole flow, not just the report
```

## When NOT to Use

```text
✗ As the only accessibility activity — designing accessibly beats auditing later
✗ On a prototype with no users (but keep the token-level decisions correct anyway)
✗ To produce a compliance badge without testing real tasks
```

## Inputs

```text
target            URL(s) or component(s), the exact build/ref
target level      WCAG 2.2 A | AA | AAA (AA is the usual contractual level)
critical tasks    the 5–10 journeys that must work (login, search, checkout, submit, …)
user context      known assistive technology in your audience; devices; connection
```

## Audit passes

Run all seven. Each finds a distinct class of failure.

### 1. Automated scan (pre-filter)
```text
axe-core (or Siteimprove alfa) on every template and every state:
default, hover, focus, error, empty, loading, expanded, modal-open, dark mode
```
Record violations with rule IDs. **A clean scan is not a pass** — it is the start.

### 2. Keyboard pass
```text
□ Tab reaches every interactive element; Shift+Tab reverses exactly
□ Focus order matches visual and DOM order (no jumping backwards across the page)
□ Focus is always visible, on every surface including dark and image backgrounds
□ Nothing is keyboard-trapped except a modal that has an explicit escape
□ All functionality operable without a mouse: menus, sliders, drag-and-drop (needs an
  alternative), carousels, map interactions, canvas, custom widgets
□ Escape closes overlays; focus returns to the trigger
□ Skip link present, first in the tab order, and it works
□ Shortcuts do not conflict with screen-reader or browser keys; remappable or disableable
   (WCAG 2.1.4)
□ No keyboard-only timing requirement
```

### 3. Screen-reader pass
Test with at least one real combination, not a simulator:
```text
NVDA + Firefox (Windows) · VoiceOver + Safari (macOS/iOS) · TalkBack + Chrome (Android)
□ Every meaningful element has an accessible name AND role that match its appearance/function
□ Reading order is logical; landmark regions present (banner, nav, main, search, contentinfo)
□ Headings form a real outline: one h1, no skipped levels, no headings used for styling
□ Dynamic changes are announced: form errors, toasts, loading completion, filter results
   (aria-live with the right politeness — and never on a container that updates constantly)
□ Images: alt text that conveys the same information; decorative images alt="" ;
   charts need a text alternative carrying the insight, not "chart of sales"
□ Tables: header cells associated; complex tables scoped correctly
□ Custom widgets: correct ARIA roles, states and properties — and prefer a native element
   or an existing accessible primitive over building one
□ Labels are programmatic (<label for>, aria-labelledby), not placeholder text
□ Error messages are associated with the field and announced
```

### 4. Vision pass
```text
□ Contrast: normal text ≥ 4.5:1, large text (≥18.66px bold or ≥24px) ≥ 3:1,
  non-text UI components and graphical objects ≥ 3:1 — measured with a tool
□ Text on images/gradients passes at every breakpoint and in both themes
□ Zoom to 200% and 400%: no loss of content or functionality; no two-dimensional scrolling
   at 320 CSS px wide (WCAG 1.4.10)
□ Text resized to 200% does not clip, overlap or truncate
□ Colour is never the only channel: status, chart series, required fields, selected states
  all have a non-colour indicator
□ Works with forced-colors / high-contrast mode; no reliance on custom colours for meaning
□ Motion: `prefers-reduced-motion` honoured; no auto-playing motion > 5 s without a pause;
  nothing flashes more than 3× per second (WCAG 2.3.1)
□ Focus indicators survive custom themes
```

### 5. Motor & dexterity pass
```text
□ Target size ≥ 24×24 CSS px (WCAG 2.2 AA 2.5.8), spacing sufficient to avoid mis-hits
□ No hover-only interactions; no timing-critical interactions without adjustment
□ Everything reachable in one gesture or with switch/voice control
□ Drag-and-drop has a non-drag alternative (WCAG 2.5.7)
□ Form completion tolerates error: validation before submit, clear recovery, no data loss
  on timeout (or the timeout is adjustable/extendable)
```

### 6. Cognitive & language pass
```text
□ `lang` correct on <html> and on any foreign-language span
□ Plain language; consistent navigation and naming across pages (WCAG 2.4.x, 3.2.x)
□ Error messages say what went wrong, where, and how to fix it — in words, not codes
□ No context-changing behaviour on focus or input (WCAG 3.2.1/3.2.2)
□ Content is understandable without relying on sensory characteristics ("click the green button")
□ Reading-order independence: meaning survives when styles are removed
```

### 7. Structure & semantics pass
```text
□ Valid HTML; correct elements (button vs div, a vs onclick, table vs grid-of-divs)
□ Landmarks unique and labelled when repeated
□ Forms: fieldsets/legends for grouped controls, autocomplete attributes for personal data
□ PDFs, documents and media: tagged, captioned, transcribed; video has captions and
   audio description where needed
□ Third-party embeds (chat, payment, video, ads) audited too — they are your responsibility
```

## Reporting

Per finding:

```markdown
### [WCAG <criterion id> — <level>] <plain-language title>
- Barrier: <what the user cannot do, in user terms>
- Affected: <page/component/state, with URL and selector or file:line>
- Detected by: <automated rule id | keyboard pass | NVDA+Firefox | measured contrast>
- Evidence: <screenshot / recording / measured value / read-aloud text>
- Remediation: <the specific fix, with a code sketch>
- Effort: <S/M/L>
- Priority: <P1 blocks a critical task | P2 significant barrier | P3 minor | P4 enhancement>
```

Priority is set by **barrier severity on a critical task**, never by fix effort. Summary
table:

```text
| criterion | level | findings | P1 | P2 | P3 | status |
Conformance statement: <meets A / partially meets AA / does not meet AA> with the
specific failures listed — never an unqualified "compliant".
```

## Failure Modes

```text
SCANNER-ONLY AUDIT       Reporting axe results as an accessibility audit.
OVERLAY WIDGETS          Installing an "accessibility overlay" instead of fixing the code.
                         Overlays frequently conflict with users' own AT and do not achieve
                         conformance; treat as a red flag, not a remediation.
ARIA OVER NATIVE         Adding ARIA to fix semantics that a native element would provide.
                         First rule of ARIA: don't.
ALT TEXT THEATRE         alt="image" on a chart carrying the only copy of a number.
FOCUS INVISIBLE          Focus ring removed for aesthetics and never replaced.
LIVE-REGION SPAM         aria-live on a frequently-updating container.
CHECKLIST WITHOUT TASKS  Auditing criteria but never attempting the user's actual journey.
ONE AT ONLY              Testing VoiceOver on macOS and assuming Android is fine.
```

## Quality Checklist

```text
□ Target level and critical tasks agreed before auditing
□ All seven passes run on every template and state, both themes
□ Automated scan run on states, not just the default render
□ Keyboard: order, visibility, traps, skip link, full operability verified
□ Screen reader tested with a real AT/browser combination, reading order and announcements checked
□ Contrast measured with a tool; 200%/400% zoom and 320 px width verified
□ Colour-independence, motion, target size and drag alternatives verified
□ Cognitive pass: language, consistency, error recovery, no context change on input
□ Semantics pass: valid HTML, landmarks, forms, media, third-party embeds
□ Every finding has criterion, barrier, evidence, remediation, effort, priority
□ Priorities set by barrier severity, not effort
□ Conformance statement qualified and specific
□ Regression checks added to CI (axe on states + a11y unit tests on new components)
```

## Anti-Patterns

```text
✗ "We ran Lighthouse and got 100"
✗ `aria-label="button"` on an unlabelled icon control
✗ A `<div onclick>` styled to look like a button
✗ Placeholder text as the only label
✗ Removing the focus outline with `outline: none` and nothing in its place
✗ An accessibility overlay script presented as compliance
✗ alt="" on an image that contains the only copy of a price
✗ Testing only the marketing page and not the checkout
```

## References

- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> (verified 2026-09-15)
- Understanding WCAG 2.2 — <https://www.w3.org/WAI/WCAG22/Understanding/>
- WAI-ARIA Authoring Practices — <https://www.w3.org/WAI/ARIA/apg/>
- axe-core — <https://github.com/dequelabs/axe-core> (MPL-2.0)
- [`knowledge/accessibility/`](../../knowledge/accessibility/) · [`patterns/ui/`](../../patterns/ui/)
- [`frontend-design`](../frontend-design/SKILL.md) · [`design-systems`](../design-systems/SKILL.md)
- [`browser-testing`](../browser-testing/SKILL.md) — how to automate these passes

## Related Skills

`frontend-design` · `design-systems` · `code-review` · `browser-testing` · `seo-audit`

## Evaluation Criteria

```text
1. Task completion: a screen-reader user can complete every critical task (target 100%).
2. Detection coverage: fraction of expert-identified barriers the audit found (target ≥ 0.85).
3. False-positive rate: findings confirmed invalid by a human reviewer (target < 0.1).
4. Remediation durability: fixed barriers do not regress (CI checks exist for each).
5. Conformance accuracy: the stated conformance level matches an independent assessment.
```

Test cases in [`tests/`](tests/).
