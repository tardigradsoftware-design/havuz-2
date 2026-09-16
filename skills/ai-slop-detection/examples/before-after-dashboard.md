---
name: before-after-dashboard
version: 1.0.0
description: >-
  A worked ai-slop-detection example on a SaaS analytics dashboard: the before state scored against
  the rubric, the specific changes applied, and the after state with the contrast pairings measured.
  Both the design decisions and the slop signatures are generic; no proprietary interface is reproduced.
category: ui-ux
status: active
confidence: high
source_type: reference
updated: 2026-09-15
tags: [example, ai-slop, dashboard, ui, before-after, contrast, typography, design-tokens]
---

# Before / After: SaaS analytics dashboard

A generic B2B analytics dashboard — overview metrics, a time-series chart, a data table, filters.
Both states are reconstructions of common patterns, not copies of any product.

## 1. Before

The layout was generated in one pass from the prompt "make a modern analytics dashboard".

```text
┌────────────────────────────────────────────────────────────────┐
│  ✦ Acme Analytics                    🔍  ⚙  🔔  👤              │
├──────────┬─────────────────────────────────────────────────────┤
│          │  Welcome back! Here's what's happening today.       │
│ Overview │                                                     │
│ Reports  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                │
│ Settings │  │ 12.4K│ │ 847  │ │ 3.2% │ │ $48K │                │
│ Team     │  │Users │ │Active│ │Churn │ │ MRR  │                │
│ Billing  │  └──────┘ └──────┘ └──────┘ └──────┘                │
│ Support  │                                                     │
│          │  ┌───────────────────────────────────────────┐      │
│ ───────  │  │      Revenue over time                    │      │
│ ● Online │  │   ╱╲    ╱╲                                │      │
│          │  │ ╱   ╲╱╱   ╲___                            │      │
│          │  └───────────────────────────────────────────┘      │
└──────────┴─────────────────────────────────────────────────────┘
```

### Measured state

| Property | Value | Problem |
|---|---|---|
| Type sizes in use | 11, 12, 13, 13.5, 14, 15, 16, 18, 20, 24, 28, 32 px | 12 sizes, no scale |
| Spacing values in use | 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 22, 24, 28, 30, 32, 40, 48, 64 px | 20 values, no step |
| Font families | Inter, system-ui, Segoe UI, Helvetica Neue | 4 stacks declared |
| Border radii | 4, 6, 8, 10, 12, 16, 9999 px | 7 values |
| Grey scale | #f9fafb #f3f4f6 #e5e7eb #d1d5db #9ca3af #6b7280 #4b5563 #374151 #1f2937 #111827 | A full off-the-shelf grey ramp |
| Body text contrast | #6b7280 on #ffffff = 4.83:1 | Passes AA for normal text at 4.5:1, marginally |
| Secondary label contrast | #9ca3af on #ffffff = 2.54:1 | **Fails AA** (needs 4.5:1) |
| Placeholder contrast | #d1d5db on #ffffff = 1.61:1 | **Fails AA** |
| Disabled button | #f3f4f6 on #ffffff, text #9ca3af = 2.4:1 | Exempt as inactive, but visually absent |
| Icon contrast (nav, inactive) | #9ca3af on #ffffff = 2.54:1 | **Fails** the 3:1 non-text requirement |
| Focus indicator | `outline: none`, replaced by `box-shadow: 0 0 0 1px #e5e7eb` | 1.12:1 against white — **no visible focus** |

### Rubric score

| Criterion | Score | Evidence |
|---|---|---|
| Intentional hierarchy | 1/5 | Four metric cards are visually identical; the greeting is the largest text in the content area; no primary action exists anywhere |
| Typographic system | 1/5 | 12 sizes, no modular relationship, 4 font stacks |
| Spacing discipline | 1/5 | 20 spacing values, no step; card gutters vary between 14 and 22 px for no reason |
| Colour with a job | 2/5 | Grey ramp plus one accent; the accent is used on the logo, one button and a chart series with no distinction |
| Content specificity | 1/5 | "Welcome back! Here's what's happening today." says nothing; metric labels are single words with no units or comparison period |
| Distinct identity | 1/5 | Centreed hero-style greeting, four equal cards, gradient-adjacent accent, decorative emoji in the nav — the generic SaaS signature |
| Accessibility | 1/5 | Four contrast failures, no visible focus indicator, chart has no text alternative |
| **Total** | **8/35** | Slop, with high confidence |

## 2. What changed, and why

| Change | Signature it removes | Rationale |
|---|---|---|
| Deleted the greeting sentence entirely | "Welcome back! Here's what's happening today." | It occupies the most prominent position and carries zero information. The date range control replaces it and is the thing the user actually manipulates |
| Made the date-range control the single primary element of the view | No primary action | Everything on the page is a function of the selected range; the control that sets it is the primary element |
| Metric cards: one becomes large, three become a compact inline row | Four identical cards in a grid | Revenue is the number the dashboard exists to show. Equal treatment asserted an equal importance that was never true |
| Type scale reduced to 12, 14, 18, 24, 32 px (1.5 ratio, 5 steps) | 12 ad-hoc sizes | A modular scale with a stated relationship. Body 14/22, headings 18, 24, 32 |
| Spacing reduced to 4, 8, 16, 24, 32 px (spacing step 4, with a doubling relationship) | 20 ad-hoc values | Card padding 16, gutters 24, section separation 32. The relationship is now legible |
| Font stack reduced to one family, Inter with a system fallback | 4 stacks | Four stacks meant four different metrics for the same nominal size |
| Grey ramp reduced to 5 values mapped to roles: surface, surface-raised, border, text-secondary, text-primary | 10-value ramp | Roles, not shades. A shade with no role is a shade nobody can defend |
| `#9ca3af` → `#5b6472` for secondary text (6.02:1 on white) | Fails AA at 2.54:1 | Secondary text carries the units and comparison periods — it is not decoration |
| Placeholder `#d1d5db` → `#6b7280` (4.83:1) | Fails AA at 1.61:1 | A placeholder that cannot be read is not a hint |
| Focus indicator: `outline: 2px solid #1d4ed8; outline-offset: 2px` | `outline: none` plus an invisible shadow | 2px at ≥3:1 against both the surface and the adjacent colour, visible on every focusable element |
| Chart: added a text summary above it and a data table toggle | Decorative chart with no alternative | The trend and the two values that matter are stated in text; the table is reachable by keyboard |
| Metric labels now read "Revenue, last 30 days" with "+12.4% vs previous 30 days" | Single-word labels | The comparison period is what makes a number interpretable |
| Removed the decorative emoji from the nav; icons are now 20px, single weight, `currentColor` | Mixed icon systems | Three icon sources at four sizes was three design languages in one rail |
| Radius reduced to 4 (inputs, small elements) and 8 (cards, panels) | 7 radii including 9999px pills | Two values with a size relationship. Pills on nav items were decoration |
| Elevation: one shadow, used only on the dropdown that overlays content | Shadow on every card | Shadow that means nothing everywhere means nothing |

## 3. After

```text
┌────────────────────────────────────────────────────────────────┐
│  Acme Analytics      [Overview] [Reports] [Team]     Search ⌘K │
├────────────────────────────────────────────────────────────────┤
│  Revenue  ▾ Last 30 days ▾                     [ Export ]      │
│                                                                │
│  $48,210                                                       │
│  ▲ 12.4% vs previous 30 days                                   │
│                                                                │
│  Active 847 (-2.1%)   Churn 3.2% (+0.4pp)   Users 12,402       │
│                                                                │
│  Revenue, last 30 days — up 12.4%, driven by 4 Sep             │
│  ┌───────────────────────────────────────────────────────┐     │
│  │  ╱╲      ╱╲                                           │     │
│  │ ╱   ╲╱╱╱   ╲__________                                │     │
│  │  1 Sep        15 Sep        30 Sep                    │     │
│  └───────────────────────────────────────────────────────┘     │
│  [ Show data table ]                                           │
└────────────────────────────────────────────────────────────────┘
```

### Measured state

| Property | Value | Result |
|---|---|---|
| Type sizes in use | 12, 14, 18, 24, 32 px | 5 steps, ratio 1.5 |
| Spacing values in use | 4, 8, 16, 24, 32 px | 5 values, base 4 |
| Font families | 1 (Inter, system fallback) | — |
| Border radii | 4, 8 px | 2 values with a size relationship |
| Colour roles | surface, surface-raised, border, text-primary, text-secondary, accent, accent-hover, positive, negative | 9 roles, each with one value |
| Body text contrast | #1f2937 on #ffffff | 14.7:1 — AAA |
| Secondary text contrast | #5b6472 on #ffffff | 6.02:1 — AA |
| Placeholder contrast | #6b7280 on #ffffff | 4.83:1 — AA |
| Focus indicator | #1d4ed8 2px, offset 2px | 6.29:1 against white, 3.1:1 against the raised surface |
| Non-text contrast (icons, borders that convey state) | ≥ 3.1:1 | Passes |
| Chart alternative | Text summary plus a toggleable data table | Present |
| Primary element per view | The date-range control (page), the revenue figure (metric block) | Exactly one each |

### Rubric score

| Criterion | Score | Evidence |
|---|---|---|
| Intentional hierarchy | 4/5 | One primary element per view; the three secondary metrics are visually grouped and subordinated; the chart follows the number it explains |
| Typographic system | 5/5 | 5 sizes from a 1.5 ratio, one family, line-heights paired to sizes |
| Spacing discipline | 5/5 | 5 values from a base-4 step with a doubling relationship |
| Colour with a job | 4/5 | 9 named roles; positive and negative are used only for deltas, never decoratively |
| Content specificity | 4/5 | Labels carry units and comparison periods; the chart has a one-line finding rather than a title |
| Distinct identity | 3/5 | The generic signatures are gone and the layout follows the data, but the identity is still neutral — a distinctive type or colour decision would raise this |
| Accessibility | 5/5 | All pairings meet their required ratio; focus is visible everywhere; the chart has a text alternative and a table |
| **Total** | **30/35** | No slop signatures detected |

## 4. What the score did not fix

Honest reporting, because the rubric is not a completeness proof:

- **Identity is at 3/5, not 5/5.** Removing slop produces a competent neutral interface. A distinctive
  typographic or colour decision is a separate act of design and was not attempted here.
- **Motion was not addressed.** The dashboard has two transitions (the dropdown, the table toggle) and
  neither was timed or eased deliberately.
- **Density was not tested with real data.** The card row works with three metrics; with eight, the
  hierarchy decision changes and this layout would need revisiting.
- **Only two viewport widths were checked.** The 1440px and 375px cases were measured; tablet widths
  were not.
- **The deltas are illustrative.** `+12.4%` and `+0.4pp` are sample values, and the direction of the
  comparison period is stated rather than verified against a real data source.

## References

- [`skills/ai-slop-detection/SKILL.md`](../SKILL.md) — the rubric applied here
- [`skills/wcag-compliance/SKILL.md`](../../accessibility-audit/SKILL.md) — the contrast ratios and the focus requirements
- [`skills/design-system-tokens/SKILL.md`](../../design-systems/SKILL.md) — how the type, spacing and colour sets were constructed
- [`skills/visual-hierarchy/SKILL.md`](../../visual-design-research/SKILL.md) — the primary-element rule
- - [`skills/frontend-design/SKILL.md`](../../frontend-design/SKILL.md) — content specificity
- [`knowledge/ui-ux/color-accessibility.md`](../../../knowledge/ui-ux/visual-hierarchy.md) — WCAG 2.2 AA values
- [`knowledge/ai-engineering/ai-slop-taxonomy.md`](../../../knowledge/ui-ux/ai-slop-signature-catalogue.md) — the 12 slop categories, with this example mapped to 1, 2, 3, 4, 5, 7 and 11
- [`anti-patterns/ui/identical-card-grid.md`](../../../anti-patterns/ui/) — the four-equal-cards signature
