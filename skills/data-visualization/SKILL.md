---
name: data-visualization
version: 1.0.0
description: >-
  Choose the chart that answers the question, encode data honestly, and make the visual accessible,
  performant and readable at real data volumes.
category: design
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [data-visualization, charts, dashboards, analytics, accessibility, frontend]
applies_to: [web, dashboard, saas, analytics]
priority: 76
requires: [design-systems]
conflicts_with: []
estimated_tokens: 3296
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Chart selection
    anchor: "#chart-selection"
    purpose: decision
  - heading: Honesty rules
    anchor: "#honesty-rules"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "D3.js"
    url: https://github.com/d3/d3
    type: github-repository
    license: ISC
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "WCAG 2.2 — non-text contrast and use of colour"
    url: https://www.w3.org/TR/WCAG22/
    type: specification
    organization: W3C
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [design-systems, frontend-design, accessibility-audit, frontend-implementation, performance-audit]
related_repositories: [d3/d3, apache/echarts, vega/vega-lite, observablehq/plot, apache/superset]
tests: 26
---

# Data Visualization

## Purpose

Answer a question about data in the shortest honest path from question to perception. A chart
is an argument; the encoding choices are the rhetoric, and most "misleading chart" problems are
rhetoric applied without disclosure.

## When to Use

```text
□ Any chart, graph, dashboard, sparkline, heatmap, map or metric tile
□ Choosing between chart types for a given question
□ Reviewing an analytics surface for honesty and legibility
□ Rendering large datasets in a browser without destroying performance
```

## When NOT to Use

```text
✗ When a single number answers the question — show the number, not a chart of one point
✗ When a table answers it better (few categories, exact values needed, comparison of many
  attributes at once)
✗ Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)
```

## Chart selection

Start from the **question**, not the data.

```text
COMPARISON across categories          bar (horizontal if labels are long or numerous)
COMPARISON of parts to a whole        stacked bar; or a table if precision matters.
                                      Pie/donut only for ≤3 categories AND when the ratio is
                                      obvious at a glance — humans compare angles badly
CHANGE OVER TIME                      line for continuous series; column for discrete periods;
                                      area only for a cumulative whole; slope/dumbbell for
                                      two-point change
DISTRIBUTION                          histogram, box/violin plot, strip plot, ECDF.
                                      Never a bar chart of averages alone — it hides the spread
RELATIONSHIP between two variables    scatter; add a third with size or colour (sparingly);
                                      hexbin/2D-density when points overplot
RANKING                               sorted horizontal bar; a table when exact values matter
CORRELATION MATRIX / MULTIVARIATE     heatmap, small multiples, parallel sets
GEOGRAPHIC                            choropleth (rate per area, never raw counts on unequal
                                      areas), symbol map, flow map
HIERARCHY / PART-OF                   treemap (quantitative parts of a whole), sunburst
                                      (deep hierarchy), tree/indented list (structure)
FLOW / PROCESS                        sankey, alluvial, funnel (only for genuine stage attrition)
MAGNITUDE OF A SINGLE METRIC          a big number with a delta, a sparkline, and a target line
MANY SERIES / SMALL MULTIPLES         one repeated chart per series — beats 30 lines in one frame
```

Selection rules:

```text
1. Fewer marks is better. If a chart needs a legend with >7 entries, it needs splitting
   (small multiples) or filtering.
2. Sort deliberately: by value (default for comparison), by time (for series), or by a
   meaningful category order. Alphabetical sorting of a comparison chart is usually an
   unmade decision.
3. Direct-label instead of using a legend wherever space allows — it removes a lookup step.
4. One chart, one question. A chart answering three questions answers none well.
5. Dashboards: hierarchy of metric tile → trend → breakdown → detail table. Let the reader
   zoom from "is anything wrong" to "what exactly".
```

## Honesty rules

```text
AXES              Zero-based for bar/column/area, because length and area are compared
                  against the baseline. Truncated axes are legitimate for line charts of a
                  narrow range — and must be labelled as truncated.
                  Broken axes require a visible break marker.
ASPECT RATIO      Distorts slope perception. Do not stretch a time series to fill a container;
                  choose the ratio deliberately (banking to 45° for slope judgement).
AREA AND VOLUME   Never encode a value with area or 3D volume unless the encoding is exact.
                  3D charts, pictograms scaled by height, and bubble charts with radius mapped
                  to value (rather than area) all overstate differences.
DOUBLE AXES       Two y-axes invite a false correlation and hide a scale mismatch. Prefer
                  small multiples or an indexed common baseline. If unavoidable, colour-code
                  the axes to their series and label both units.
CHERRY-PICKING    Time windows, filters and cohorts change conclusions. State the window,
                  the filter and the exclusions on the chart or beside it.
AVERAGES          Report the distribution or the spread, not only the mean. A mean without
                  variance can hide bimodality entirely. Label which statistic is shown
                  (mean/median/p75) — "average" is ambiguous.
SAMPLE SIZE       Show n. A 40% change on n=5 is noise. Suppress or annotate small-n cells.
CORRELATION       Never imply causation from a scatter without saying so explicitly.
BASE RATES        Percentages need their denominators. "Up 200%" from 1 to 3 is a different
                  fact from 200 to 600.
COLOUR ENCODING   Sequential for ordered quantities · diverging for deviation from a midpoint ·
                  categorical (qualitative) for unordered classes. Using a rainbow/sequential
                  scale for categories implies an order that does not exist.
COLOURBLIND SAFETY Do not rely on red/green contrast alone. Use a colourblind-safe palette,
                  and add a second channel (shape, pattern, direct label) for every distinction.
                  Simulate deuteranopia/protanopia before shipping.
ACCESSIBILITY     Non-text contrast ≥3:1 for meaningful graphical objects (WCAG 2.2).
                  Every chart needs a text alternative carrying the INSIGHT, not "chart of
                  revenue". Provide the underlying data as a table (visually hidden or
                  downloadable). SVG with titles/descriptions, or a canvas fallback with an
                  accessible table. Keyboard-navigable where interactive.
PERFORMANCE       Aggregate server-side or in the worker — never ship 100k points to render
                  500 pixels. Downsample for the viewport; use canvas/WebGL above ~5k marks;
                  virtualise tables. Do not re-animate the whole chart on data update.
```

## Implementation notes

```text
LIBRARY CHOICE    Declarative grammar (Vega-Lite) for standard charts and fast iteration;
                  D3 for anything bespoke; a framework-native wrapper for dashboards;
                  ECharts/Plot for breadth with less code. Choose the lowest-level tool that
                  still covers your chart set — see dont-reinvent-the-wheel.
TOKENS            Chart colours, type and spacing come from the design system, not the
                  library's default theme. Default palettes are how every dashboard ends up
                  looking identical.
STATES            empty (no data yet), zero (data exists, all values are 0 — different from
                  empty), loading, error, partial, and too-many/too-few to be meaningful.
                  A chart that renders nothing on empty data is indistinguishable from a bug.
INTERACTION       hover/focus tooltips with the exact value, unit, period and n; brushing and
                  zoom that preserve the axis semantics; drill-down that keeps context.
                  Touch targets ≥24×24 CSS px; no hover-only information.
EXPORT            the underlying data downloadable; the chart exportable at sufficient
                  resolution for print; numbers formatted per locale.
FORMATTING        consistent units, thousands separators, decimal places matched to precision,
                  percentages vs percentage points distinguished, currency and timezone stated.
TESTING           snapshot or golden-image tests for deterministic charts; property tests for
                  scale/axis logic; test with 0, 1, 2, many, negative, null and huge values.
```

## Failure Modes

```text
TRUNCATED BAR AXIS       A 2% difference rendered as a 5× visual difference.
PIE WITH 12 SLICES       Unreadable, and the comparison is false precision.
RAINBOW ON CATEGORIES    Implies an order that does not exist.
RED/GREEN ONLY           Invisible to ~8% of men.
MEAN WITHOUT SPREAD      Bimodal or long-tailed data presented as a single number.
MISSING n                A dramatic percentage on five observations.
CHERRY-PICKED WINDOW     The trend that appears depends entirely on the unstated start date.
PERCENT VS PERCENT POINT "Up 50%" when the change was 2 points on a 4% base.
3D AND PICTOGRAMS        Area/volume encoding that overstates differences.
TOO MANY MARKS           40 lines, a 20-entry legend, and no readable insight.
NO EMPTY/ZERO STATES     Blank chart on empty data; indistinguishable from failure.
CLIENT-SIDE AGGREGATION  100k rows shipped to the browser to draw one line.
ANIMATION ON EVERY UPDATE The value change is obscured by the transition.
DEFAULT LIBRARY THEME    Every dashboard looks the same, and off-system colours break contrast.
NO TEXT ALTERNATIVE      The only copy of a number is inside a canvas element.
```

## Quality Checklist

```text
□ Question stated; chart type chosen from the question, not from the data shape
□ A table or single number was considered and rejected with a reason where applicable
□ Bar/area axes zero-based; truncated or broken axes visibly labelled
□ Aspect ratio deliberate; no stretching to fill a container
□ No area/volume/3D encoding unless exact; no double axes unless justified and colour-coded
□ Sorted deliberately; direct labels preferred over legends; ≤7 series per frame
□ Statistic labelled (mean/median/p75) with spread or distribution shown
□ n displayed; small-n cells annotated or suppressed
□ Time window, filters and exclusions stated on or beside the chart
□ Percentages carry their denominators; percent vs percentage point distinguished
□ Sequential/diverging/categorical scale matched to the data type
□ Colourblind-safe palette; a second channel for every colour-only distinction
□ Non-text contrast ≥3:1 for meaningful marks; text alternative carrying the insight
□ Underlying data available as a table or download; keyboard operable if interactive
□ Aggregation server-side or in a worker; downsampling above ~5k marks; canvas/WebGL when needed
□ States implemented: empty, zero, loading, error, partial, too-many
□ Chart colours/type/spacing from design-system tokens, not library defaults
□ Formatting consistent: units, separators, decimals, locale, timezone, currency
□ Deterministic chart tests including 0, 1, many, negative, null and huge values
□ No animation on routine data updates
```

## Anti-Patterns

```text
✗ A 12-slice pie chart
✗ A bar chart starting at 95 instead of 0
✗ Red/green status colours with no icon or label
✗ "Average response time: 120 ms" with no distribution and no n
✗ Revenue "up 300%" from 1 to 4 units
✗ Two y-axes with unrelated units on one frame
✗ Shipping 100k points to render a trend line
✗ A canvas chart with no table, no alt text and no keyboard access
✗ The library's default colour palette in a product with a design system
✗ An empty chart that renders as blank white space
```

## References

- [`design-systems`](../design-systems/SKILL.md) · [`frontend-design`](../frontend-design/SKILL.md)
- [`accessibility-audit`](../accessibility-audit/SKILL.md) · [`performance-audit`](../performance-audit/SKILL.md)
- [`frontend-implementation`](../frontend-implementation/SKILL.md) · [`patterns/ui/`](../../patterns/ui/)
- [`knowledge/ui-ux/`](../../knowledge/ui-ux/) · [`datasets/`](../../datasets/)
- WCAG 2.2 — <https://www.w3.org/TR/WCAG22/> · D3 — <https://github.com/d3/d3>
- Vega-Lite — <https://github.com/vega/vega-lite>

## Related Skills

`design-systems` · `frontend-design` · `accessibility-audit` · `frontend-implementation` ·
`performance-audit` · `database-design`

## Evaluation Criteria

```text
1. Question-match: a reviewer agrees the chart type answers the stated question.
2. Honesty: 0 encoding choices that overstate a difference without disclosure.
3. Accessibility: text alternative present; colourblind-safe; contrast ≥3:1; keyboard operable.
4. Performance: renders within budget at the real data volume, with aggregation off the main thread.
5. State coverage: empty/zero/loading/error/partial all designed and tested.
6. Interpretation accuracy: a reader extracts the intended insight without prompting (user test).
```

Test cases in [`tests/`](tests/).
