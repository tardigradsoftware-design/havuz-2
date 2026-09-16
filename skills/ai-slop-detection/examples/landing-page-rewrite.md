---
name: landing-page-rewrite
version: 1.0.0
description: >-
  A worked ai-slop-detection example on a SaaS landing page: the generated copy scored against the
  content rubric, a rewrite that keeps the same information, and the measurable differences. Shows the
  copy-specific signatures — the em-dash triad, rule-of-three reflex, inflated abstractions and the
  negative parallelism construction — being removed one at a time.
category: ui-ux
status: active
confidence: high
source_type: reference
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [example, ai-slop, landing-page, copywriting, cro, rewrite, content]
---

# Before / After: SaaS landing page copy

A generic B2B SaaS landing page for an inventory-planning product. Both states are reconstructions of
common patterns; no real company copy is reproduced.

## 1. Before — the hero

```text
✦  Inventory, reimagined.

   Seamlessly orchestrate your supply chain with our cutting-edge
   AI-powered platform — designed to unlock efficiency, drive growth,
   and empower your team.

   Not just another tool. A complete transformation.

   [ Get Started ]   [ Learn More ]

   Trusted by 10,000+ teams worldwide
```

### Rubric score, hero only

| Criterion | Score | Evidence |
|---|---|---|
| Specific over generic | 1/5 | No product behaviour is named. "Inventory, reimagined" could headline any of ten thousand products |
| Plain over inflated | 1/5 | `seamlessly`, `cutting-edge`, `AI-powered`, `unlock`, `drive growth`, `empower`, `transformation` — seven inflated terms in 34 words |
| One idea per sentence | 2/5 | Sentence two carries three claims joined by an em-dash and a rule-of-three |
| Rhythm varies | 1/5 | Three sentences, each built on a triad; the negative parallelism adds a fourth |
| Claims are grounded | 1/5 | "10,000+ teams worldwide" with no definition of a team, no date, no source |
| Reader addressed directly | 3/5 | "your" appears four times — but always attached to an abstraction, never to an action the reader takes |
| No slop signatures | 1/5 | Em-dash triad, rule-of-three reflex, negative parallelism ("Not just X. A Y."), inflated abstraction, hedged superlative |
| **Total** | **10/40** | Slop, with high confidence |

### Signatures found

| Signature | Instance |
|---|---|
| Em-dash triad | "platform — designed to unlock efficiency, drive growth, and empower your team" |
| Rule-of-three reflex | "unlock efficiency, drive growth, and empower your team" |
| Negative parallelism | "Not just another tool. A complete transformation." |
| Inflated abstraction | "reimagined", "seamlessly", "cutting-edge", "orchestrate", "unlock", "empower", "transformation" |
| Unearned authority | "Trusted by 10,000+ teams worldwide" |
| Decorative emphasis | The `✦` mark, and a centred composition with two equally weighted CTAs |

## 2. The rewrite

Two questions decided it: **what does the product do**, and **who is the reader**. Answered as
"it forecasts what to reorder and when, for operations managers running 50-500 SKUs across several
locations", the copy could be written from facts rather than from adjectives.

```text
Know what to reorder, and when.

   Stockout forecasts for operations teams running 50-500 SKUs
   across multiple locations. Per-SKU reorder points, updated
   nightly from your own sales history.

   [ Start a 14-day trial ]   See a sample forecast →

   2,340 companies used it in August 2026. Median reorder-point
   error: 8% against actual demand.
```

### What changed

| Before | After | Why |
|---|---|---|
| "Inventory, reimagined." | "Know what to reorder, and when." | The headline now states the outcome the reader wants, in the reader's words. It is also checkable — the product either produces reorder points or it does not |
| "Seamlessly orchestrate your supply chain with our cutting-edge AI-powered platform" | "Stockout forecasts for operations teams running 50-500 SKUs across multiple locations." | Names the artefact (a forecast), the reader (operations teams), and the scope (50-500 SKUs, multiple locations). The scope also disqualifies readers it does not serve, which is a feature |
| "designed to unlock efficiency, drive growth, and empower your team" | "Per-SKU reorder points, updated nightly from your own sales history." | Three benefits nobody can verify replaced by two mechanisms the reader can check: granularity and cadence, with the data source named |
| "Not just another tool. A complete transformation." | *(deleted)* | Negative parallelism says nothing about the product and exists only to create emphasis. Deleting it lost no information |
| `[ Get Started ] [ Learn More ]` | `[ Start a 14-day trial ] [ See a sample forecast → ]` | One primary CTA that names the actual action and its cost (14 days, no card). The secondary CTA is a concrete artefact rather than a vague invitation, and is visually subordinated |
| "Trusted by 10,000+ teams worldwide" | "2,340 companies used it in August 2026. Median reorder-point error: 8% against actual demand." | A countable number, a period, and a definition. The 8% figure is the product's actual measured accuracy — a claim that can be wrong, and therefore a claim worth making |
| `✦` decoration, centred composition | Mark removed; left-aligned, asymmetric layout | Decoration that carries no meaning; centring was a composition habit rather than a decision |
| Em-dash triad | No em-dashes; two sentences of 9 and 14 words | Sentence length now varies and no sentence carries three parallel claims |

### Rubric score, hero only

| Criterion | Score | Evidence |
|---|---|---|
| Specific over generic | 5/5 | Every clause names a thing: a forecast, reorder points, SKU counts, locations, nightly cadence, sales history, a trial length, a company count, an error percentage |
| Plain over inflated | 5/5 | Zero inflated terms. The longest word is "operations" |
| One idea per sentence | 4/5 | Sentence two carries scope and audience together, which is defensible; sentence three carries two mechanisms |
| Rhythm varies | 4/5 | Headline 6 words, then 14, 9, 14. No triads |
| Claims are grounded | 5/5 | Both numbers are countable with a stated period; the accuracy figure is stated as a median against actual demand, which is falsifiable |
| Reader addressed directly | 4/5 | Addressed by role and by situation rather than by "your" |
| No slop signatures | 5/5 | No em-dash triad, no rule-of-three, no negative parallelism, no inflated abstraction, no unearned authority |
| **Total** | **32/40** | No slop signatures detected |

## 3. The rest of the page

The same method applied to the sections below the hero, summarised because the pattern repeats:

| Section | Before | After |
|---|---|---|
| Features | Six identical cards: "Real-time Visibility", "Smart Forecasting", "Seamless Integration", "Advanced Analytics", "Team Collaboration", "Enterprise Security" | Four rows, each with a mechanism and a number: forecast cadence and horizon, the integrations actually shipped with their sync interval, the reorder-point calculation with its inputs, and the permission model with its roles |
| Social proof | Three testimonial cards with first names and job titles, no companies | Two named companies with the specific problem, the specific number before and after, and a date |
| Pricing | "Simple, transparent pricing" above three tiers named Starter, Professional, Enterprise | Three tiers with what is metered, what the limit is, and what happens at the limit. The Enterprise tier states that pricing is quoted and why |
| FAQ | Four questions about the company | Six questions the sales team actually gets, answered in the first sentence with the qualification after |
| Final CTA | "Ready to transform your business?" | "Start with your last 90 days of sales data." — names the smallest real first step and its input |

## 4. What the rewrite did not do

- **It did not invent the numbers.** `2,340 companies`, `August 2026` and `8% median error` are
  placeholders standing in for figures that must come from the product's own data. Writing a specific
  number is not a licence to make one up; the rubric rewards grounded claims, and a fabricated specific
  claim is worse than a vague honest one. Any real application of this method requires the actual
  metrics.
- **It did not test conversion.** The rewrite is argued from the rubric, not from an A/B test. Copy
  changes are hypotheses until measured, and `landing-page-cro` requires the measurement.
- **It did not address the visual design.** Typography, spacing, colour and the imagery are untouched;
  only the words changed. A page with clean copy and slop visuals still fails the full rubric.
- **It did not check the reading level formally.** The sentences are shorter and plainer, but no
  readability metric was computed.
- **Tone was not deliberately set.** The rewrite is neutral-professional. A consumer product or a
  developer tool would want a different register, and nothing here decided which.

## References

- [`skills/ai-slop-detection/SKILL.md`](../SKILL.md) — the content rubric applied here
- [`skills/frontend-design/SKILL.md`](../../frontend-design/SKILL.md) — hero, CTA, social proof and pricing conventions
- - - [`skills/visual-hierarchy/SKILL.md`](../../visual-design-research/SKILL.md) — the single primary CTA rule
- [`knowledge/ai-engineering/ai-slop-taxonomy.md`](../../../knowledge/ui-ux/ai-slop-signature-catalogue.md) — the 12 categories, with this example mapped to 1, 2, 6, 8, 9 and 10
- [`anti-patterns/frontend/`](../../../anti-patterns/frontend/) — the identical-card-grid signature in the features section
