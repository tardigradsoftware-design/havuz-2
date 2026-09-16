---
id: ui-ux-visual-hierarchy
title: "Visual hierarchy: the mechanisms that determine what a user sees first"
domain: ui-ux
summary: >-
  The perceptual channels through which hierarchy is communicated — size, weight, colour, contrast, position, space, isolation and motion — how they combine and conflict, and the diagnostic for a view where nothing stands out.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [visual-hierarchy, design, perception, typography, layout, contrast, ui, ux]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/ui-ux/what-makes-a-website-look-professional.md, knowledge/ui-ux/what-makes-ai-websites-look-generic.md]
sources:
  - title: "WCAG 2.2"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Contrast minimums (4.5:1 text, 3:1 non-text) bound the hierarchy mechanisms available at small sizes and low weights — a hierarchy built on light grey text is also an accessibility failure."
---
# Visual Hierarchy

## What hierarchy is

Hierarchy is the designer deciding what matters and making that decision visible. It is not
decoration and not aesthetics — it is the removal of work from the user. Without it, a user must
evaluate every element to find the one they need, which is the experience described as "cluttered" or
"overwhelming" or, when it is uniform rather than crowded, "flat".

```text
THE TEST   Squint at the screen, or blur the screenshot. What is the one thing that remains distinct?
           If the answer is "nothing" or "everything", there is no hierarchy — regardless of how many
           different font sizes are present.
```

## The channels

Each channel communicates importance independently, and they combine. The common failure is using one
channel (usually size) and expecting it to carry the whole decision.

```text
SIZE            larger reads as more important. The weakest channel on its own: a large light-grey
                heading loses to a small bold dark link.
WEIGHT          bold reads as more important at the same size. Stronger than size per unit of change.
CONTRAST        darker against the background reads as more important. The strongest channel available,
                and the one most often spent on decoration instead of meaning.
COLOUR / HUE    a saturated accent among neutrals reads as important. Extremely strong — which is why
                one accent works and three do not. A second accent needs a second meaning.
POSITION        top-left and centre receive attention first in a left-to-right reading context; the
                end of a sequence receives a recency effect. Position alone is weak but it multiplies
                the others.
SPACE           more space around an element isolates and elevates it. The most underused channel:
                importance can be increased without changing the element at all, only its surroundings.
ISOLATION       an element that differs from everything near it — one button among text, one image
                among cards — reads as important. Also the mechanism behind "the odd one out" layouts.
MOTION          anything that moves is looked at first, involuntarily. Powerful and therefore
                dangerous: it cannot be ignored, it competes with everything else, and it must have a
                reduced-motion path.
LAYER / ELEVATION  a shadow or overlap indicating "above" reads as more immediately actionable —
                modals, popovers, floating actions. Use for actual layer relationships, not decoration.
```

## Combining channels

The reliable way to make something primary is to move **several channels at once** in the same
direction:

```text
PRIMARY CTA      larger + bolder + highest-contrast fill + the accent colour + space around it + first
                 in the reading order. Six channels agreeing.
SECONDARY CTA    smaller + outlined + lower contrast + neutral colour + after the primary. Deliberately
                 quieter on four channels.
TERTIARY         text-only link, no fill, no border, smallest size. Still discoverable, unmistakably
                 lower.
```

When two elements compete, it is almost always because they agree on some channels and disagree on
others — same size, different weight; same colour, different position. The fix is not to weaken one; it
is to decide which is primary and move every channel consistently.

## Levels, and how many there should be

```text
A view usually supports THREE levels of heading and TWO or THREE levels of action. More than that and
the levels become indistinguishable, because each step is smaller than the perceptual threshold.

  LEVEL 1    page or section title. One per view. Largest, heaviest, most space above it.
  LEVEL 2    subsection or card title. Several per view, visually clearly below level 1.
  LEVEL 3    label, meta, caption, timestamp. Quietest, but still above the contrast minimum.
  BODY       the reading layer. Never competing with a heading for attention.

The spacing between levels must exceed the spacing within a level. A heading closer to the following
paragraph than to the section above it inverts the grouping — the classic cause of "this looks
unorganised" with nothing visibly wrong.
```

## Proximity and grouping

Hierarchy is not only about importance; it is about which things belong together.

```text
Gestalt proximity: elements closer together are read as a group. The gap WITHIN a group must be visibly
smaller than the gap BETWEEN groups. When the two gaps are similar, grouping becomes ambiguous and the
user must read the content to work out the structure.

Practical rule: if the intra-group gap is 8 px, the inter-group gap is 24 px or more. A ratio below
roughly 2:1 does not read as grouping.

A card's internal padding, the gap between its elements, and the gap between cards form three levels of
the same decision. Getting them equal — a common generated-output signature — destroys the grouping.
```

## Reading order and hierarchy

Visual hierarchy and DOM order must agree, or one of two things breaks:

```text
□ Keyboard and screen-reader users traverse DOM order. If the visual primary action is last in the DOM,
  it is last for them.
□ A layout that reorders visually (flexbox order, absolute positioning, grid areas) can separate visual
  hierarchy from focus order, which is a WCAG 1.3.1 and 2.4.3 failure and a usability failure at once.
□ Focus order should follow the hierarchy: the primary action first, then secondary, then the rest.
```

## The diagnostic

When a view "looks flat" or "nothing stands out", check in this order:

```text
1. IS THERE A DECIDED PRIMARY?   If nobody chose, nothing will stand out. This is a decision problem
                                 before it is a styling problem, and it is the cause most often.
2. ARE THE CHANNELS CONSISTENT?  List the channels for the top three elements. If they disagree —
                                 element A is larger but element B is darker — the hierarchy is
                                 ambiguous and reads as flat.
3. IS THE CONTRAST RANGE TOO NARROW?  A page where everything is between 40% and 60% opacity has no
                                 hierarchy available. Professional pages use a wide range: near-black
                                 text, mid-grey secondary, light-grey meta — all above their contrast
                                 minimums.
4. IS SPACE UNIFORM?             Equal spacing everywhere destroys grouping and elevation. Space is the
                                 cheapest channel to fix: increase the gap above the primary element and
                                 between sections, decrease it within groups.
5. IS EVERYTHING THE SAME SIZE?   A type scale with two steps too close together reads as one step.
                                 Increase the ratio between levels.
6. ARE THERE TOO MANY ACCENTS?    Three saturated colours means none of them is the accent. Reduce to
                                 one, and let contrast and weight carry the rest.
```

## Anti-patterns

```text
✗ Hierarchy by size alone.      The weakest channel used as the only one; produces large quiet
                                headings that lose to small loud links.
✗ Two primaries per view.       An unresolved decision rendered in CSS.
✗ Equal weight everywhere.      "Clean and minimal" as a description of a hierarchy that was never
                                built. Restraint is not uniformity.
✗ Accent colour on decoration.  Spending the strongest channel on a gradient, an icon or a border
                                leaves nothing for the action that needs it.
✗ Motion as the only emphasis.  Involuntary attention, no reduced-motion path, and it competes with
                                the actual primary.
✗ Grey text below the contrast minimum as a hierarchy level.  A level that is invisible to low-vision
                                users is not a level.
✗ Grouping gaps equal to intra-group gaps.  Structure becomes ambiguous and reads as clutter.
✗ Visual order differing from DOM order.  Breaks keyboard and screen-reader hierarchy simultaneously.
```

## References

- [`what-makes-a-website-look-professional.md`](what-makes-a-website-look-professional.md) — hierarchy as one of the six professional properties
- [`what-makes-ai-websites-look-generic.md`](what-makes-ai-websites-look-generic.md) — the absence of a hierarchy decision as a root cause
- [`ai-slop-signature-catalogue.md`](ai-slop-signature-catalogue.md) — the layout and typography signatures
- [`../accessibility/wcag-practical-checklist.md`](../accessibility/wcag-practical-checklist.md) — contrast, reading order, focus order
- [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/design-systems/SKILL.md`](../../skills/design-systems/SKILL.md) · [`skills/ai-slop-detection/SKILL.md`](../../skills/ai-slop-detection/SKILL.md)
- [`patterns/ui/`](../../patterns/ui/) · [`anti-patterns/ui/`](../../patterns/ui/)
