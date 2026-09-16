---
id: accessibility-wcag-practical-checklist
title: "WCAG in practice: the checks that catch real failures"
domain: accessibility
summary: >-
  A working checklist derived from WCAG 2.2 AA, organised by what an automated tool can and cannot detect, with the specific failure patterns that pass automated audits and still exclude users.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [accessibility, wcag, a11y, aria, contrast, keyboard, screen-reader, automated-testing]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [skills/accessibility-audit, knowledge/ui-ux/visual-hierarchy.md]
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The normative success criteria this checklist operationalises. Level AA is the contractual baseline in most jurisdictions."
---
# WCAG in Practice

## The framing

Automated tools detect roughly 30–40% of WCAG failures — the mechanically checkable ones. The
remainder require judgement about meaning, order and behaviour. A clean automated audit is therefore
not evidence of accessibility; it is evidence that the cheap failures were fixed.

```text
AUTOMATED      contrast ratios · missing alt attributes · missing form labels · missing document
               language · empty headings and buttons · duplicate IDs · invalid ARIA attribute
               values · missing skip link targets
MANUAL         reading order · focus order and visibility · keyboard operability of custom widgets ·
               whether alt text conveys the same information · whether labels describe the action ·
               screen-reader announcement of dynamic changes · whether the experience makes sense
```

## Checklist, in the order failures actually occur

### 1. Keyboard (SC 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11)

```text
□ Every interactive element is reachable with Tab, in an order that matches the visual reading order
□ Tab never traps: from every element, focus can leave without a mouse
□ A visible focus indicator is present on every element. outline: none without a replacement is the
  single most common deliberate accessibility regression in modern CSS.
□ Custom widgets (dropdown, modal, tabs, date picker, combobox) implement the expected key handling:
  Escape closes, arrows move within a widget, Enter/Space activates
□ A skip-to-content link is the first focusable element
□ Focus is managed on route change and on modal open/close — it moves to the new context and returns
  to the trigger on close
□ No keyboard shortcut is bound to a single printable character without a way to remap or disable it
```

### 2. Semantics and names (SC 1.3.1, 4.1.2, 2.4.4, 2.4.6, 3.3.2)

```text
□ Elements are the right HTML element before any ARIA is added. A <button> beats a <div role=button>
  on every axis: it is focusable, it has an implicit role, and it responds to Space and Enter.
□ The first rule of ARIA: do not use ARIA if a native element or attribute exists.
□ Every interactive element has an accessible name, computed from text content, aria-label,
  aria-labelledby or an associated <label> — in that precedence order.
□ Icon-only buttons have an accessible name that states the ACTION ("Delete draft"), not the icon
  ("Trash can") and not the element type ("Button").
□ Heading levels are nested without skipping; the heading text describes the section that follows it
□ Every form control has a visible label. Placeholder text is not a label — it disappears on input
  and is not reliably announced.
□ Error messages are programmatically associated (aria-describedby) and announced, not merely shown
  in red next to the field
□ Landmarks are used correctly: one main, banner/contentinfo as appropriate, nav for navigation
  regions. Landmark soup is as unhelpful as none.
```

### 3. Images and media (SC 1.1.1, 1.2.1–1.2.5)

```text
□ Informative images: alt text that conveys the same information the image carries. "Chart showing
  revenue rising from $1.2M to $3.4M across four quarters" — not "chart.png", not "revenue".
□ Decorative images: alt="" (empty, present) so assistive technology skips them. Omitting the
  attribute makes some screen readers read the filename.
□ Images of text: avoided. Where unavoidable, the alt contains the full text.
□ Complex graphics (charts, diagrams, maps): a short alt plus a long description in the surrounding
  text or via aria-describedby. The data behind a chart should also be available as a table.
□ Video: captions for recorded content. Audio-only: a transcript. Live: captions where feasible.
□ Media does not autoplay with sound; a pause/stop control exists for anything that plays over 3 s
```

### 4. Colour and contrast (SC 1.4.1, 1.4.3, 1.4.11, 1.4.13)

```text
□ Colour is never the only channel. "Errors are red" fails; an icon and text alongside the colour
  passes. This is the most commonly missed criterion because it looks fine to a sighted reviewer.
□ Text contrast ≥ 4.5:1 normal size, ≥ 3:1 for large text (≥ 24px, or ≥ 18.66px bold)
□ Non-text contrast ≥ 3:1 for UI component boundaries and graphical objects required to understand
  the content — form field borders, focus indicators, chart lines, icon strokes
□ Text over images and gradients: check the worst region, not the average. Gradients guarantee a
  region that fails even when the midpoint passes.
□ Content that appears on hover or focus (tooltips, popovers) can be dismissed without moving the
  pointer, can be hovered over, and persists until dismissed (SC 1.4.13)
```

### 5. Layout, zoom and reflow (SC 1.4.4, 1.4.10, 1.4.12, 2.5.8)

```text
□ Text resizes to 200% without loss of content or function, and without requiring horizontal scroll
□ Content reflows at 320 CSS px width (or 256 px height for vertical text) — no two-dimensional
  scrolling. Test at 400% zoom in a 1280 px viewport.
□ Text spacing can be overridden (line-height 1.5×, paragraph 2×, letter 0.12×, word 0.16×) without
  clipping. Fixed heights on text containers are what break this.
□ Target size ≥ 24×24 CSS px (WCAG 2.2 AA, SC 2.5.8), or adequate spacing to an equivalent target.
  Dense icon toolbars routinely fail this and are hard to use without a pointer as well.
□ Nothing essential is only reachable by a hover gesture or a path-based gesture (drag, pinch) —
  a single-pointer alternative exists
```

### 6. Dynamic content and motion (SC 2.2.1, 2.3.1, 4.1.3, 2.2.2, 2.3.3)

```text
□ Status changes are announced: aria-live="polite" for non-urgent updates (results count, save
  status), "assertive" for errors. A silently-updating region is invisible to a screen-reader user.
□ Focus is not moved by the page without the user's action
□ Timing: any time limit can be turned off, adjusted or extended, except where it is essential
  (a real-time auction, a timed exam)
□ Motion: nothing flashes more than three times per second. Auto-playing animation, parallax and
  video can be paused, stopped or hidden.
□ prefers-reduced-motion is honoured: animation reduces to opacity or is removed. This is both a
  vestibular-safety requirement and the S10 AI-slop symptom.
□ Single-page route changes update the document title and move focus to the new view's heading
```

### 7. Cognitive and predictable behaviour (SC 3.1.1, 3.2.1–3.2.4, 3.3.1, 3.3.3, 3.3.7)

```text
□ The document language is declared, and language changes within the document are marked
□ Focus, input and navigation do not unexpectedly change context. A select that submits on change
  without warning fails SC 3.2.2.
□ Consistent navigation and consistent identification: the same component has the same name and
  behaviour everywhere in the product
□ Errors are identified in text, described specifically, and a suggestion for correction is offered
  where it can be given without compromising security
□ Destructive and legal/financial actions are reversible, or a confirmation step exists (SC 3.3.7
  redundant entry / accessible authentication in 2.2)
□ Authentication does not require a cognitive test (memorising, transcribing) without an alternative
  — passkeys, OAuth, email links, or an available paste (SC 3.3.8, WCAG 2.2 AA)
```

## How to test

```text
1. KEYBOARD-ONLY PASS      Tab through every view. No mouse. Note every trap, every missing
                           indicator, every unreachable control. Highest value per minute of any
                           accessibility test.
2. SCREEN-READER PASS      VoiceOver (macOS/iOS), NVDA (Windows, free), TalkBack (Android). Learn
                           the basic navigation before judging the product — an unfamiliar screen
                           reader produces false failures.
3. ZOOM AND REFLOW         400% zoom at 1280 px; 320 px viewport width; text-spacing override.
4. AUTOMATED SCAN          axe-core, Lighthouse accessibility, or pa11y in CI. Treat results as the
                           floor: they catch the mechanical 30–40%.
5. COLOUR-BLINDNESS SIM    Deuteranopia and protanopia simulation on every colour-coded UI, plus a
                           greyscale render to confirm nothing depends on hue alone.
6. CONTENT REVIEW          Read the alt text, labels, error messages and headings aloud. Do they
                           describe the action and the information, out of visual context?
```

## Anti-patterns

```text
✗ ARIA as a substitute for HTML.   role and aria-* do not add behaviour. A div with role="button"
                                   is still not focusable and still does not respond to Space.
✗ outline: none with no replacement. Deliberate removal of the focus indicator for aesthetics.
✗ Placeholder-as-label.            Disappears on input; fails SC 3.3.2 and 1.3.1.
✗ "We have an accessibility statement."  A statement is not an implementation.
✗ An overlay widget marketed as an accessibility fix.  These do not repair the DOM and have been
                                   the subject of litigation rather than protection.
✗ Automated audit passed, shipped.  See the framing above.
✗ Alt text describing the image rather than the information. "Photo of a team" tells a blind user
   nothing a sighted user learns from looking at it.
```

## References

- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> · Understanding WCAG — <https://www.w3.org/WAI/WCAG22/Understanding/>
- WAI-ARIA Authoring Practices — <https://www.w3.org/WAI/ARIA/apg/> · HTML spec, ARIA in HTML — <https://www.w3.org/TR/html-aria/>
- [`skills/accessibility-audit/SKILL.md`](../../skills/accessibility-audit/SKILL.md) — the audit workflow
- [`knowledge/ui-ux/visual-hierarchy.md`](../ui-ux/visual-hierarchy.md) — hierarchy and accessibility share mechanisms
- [`patterns/ui/`](../../patterns/ui/) · [`anti-patterns/`](../../anti-patterns/) · [`gotchas/`](../../gotchas/)
