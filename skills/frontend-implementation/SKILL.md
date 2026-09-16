---
name: frontend-implementation
version: 1.0.0
description: >-
  Build approved designs into production frontend code — component architecture, state management,
  data fetching, rendering strategy, performance budgets and the checks that keep the result
  matching the design.
category: frontend
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [frontend, implementation, components, state, performance, rendering, react, next]
applies_to: [web, saas, dashboard, marketing-site]
priority: 87
requires: [design-systems]
conflicts_with: []
estimated_tokens: 2845
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Architecture decisions
    anchor: "#architecture-decisions"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: Google Chrome team
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Defines LCP, INP and CLS. Thresholds change over time — verify current values before quoting numbers."
  - title: "MDN Web Docs"
    url: https://developer.mozilla.org/
    type: official-docs
    organization: Mozilla
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [design-systems, frontend-design, performance-audit, accessibility-audit, browser-testing, testing]
related_repositories: [vercel/next.js, vitejs/vite, TanStack/query, radix-ui/primitives, shadcn-ui/ui, microsoft/playwright]
tests: 24
---

# Frontend Implementation

## Purpose

Turn an approved design into code that stays correct under real content, real networks and
real devices. This skill assumes the design exists — if it does not, run
[`frontend-design`](../frontend-design/SKILL.md) first. Implementing without a design
produces the default layout, which is the AI-slop failure mode.

The three recurring implementation failures: state placed where it cannot be kept
consistent, data fetched without a caching/error/retry strategy, and rendering chosen by
habit rather than by what the page needs.

## When to Use

```text
□ Implementing a new page, screen or component set from a design
□ Choosing a rendering strategy, state approach or data-fetching layer
□ When a UI is correct in the design file and wrong in the browser
□ Performance or hydration problems in an existing frontend
```

## When NOT to Use

```text
✗ Producing the visual design itself — frontend-design
✗ Defining the token/component system — design-systems
✗ Backend concerns except at the contract boundary — see api-design / backend-engineering
```

## Inputs

```text
design            tokens, components, compositions, all states (empty/loading/error/partial)
content model     real data shapes, variances and volumes
contract          the API/schema, including error shapes and pagination
constraints       SEO requirement, auth, latency budget, device matrix, bundle budget
existing stack    framework and version, build tool, what is already a dependency
```

## Architecture decisions

Decide these **before** writing components. Each is a one-line record in the PR or ADR.

### Rendering strategy — per route, not per app
```text
SSG / static        content known at build; fastest; needs a rebuild or ISR to change
ISR / on-demand revalidation  content changes on a schedule or an event
SSR                 per-request personalised or fresh content; cost: TTFB + infra
Streaming SSR       slow data after a fast shell; best perceived performance for mixed pages
CSR                 post-auth app surfaces behind a shell; cost: blank first paint, SEO
RSC / server components  server-only data access, zero client JS for that subtree
                      (framework-specific semantics — verify against the installed version)
Hybrid              the normal answer: static shell + streamed/CSR islands

Decide from: SEO need · personalisation · freshness · interactivity · cost
Then verify: does this framework version actually behave that way? Check the CHANGELOG.
```

### State — four kinds, four homes
```text
SERVER STATE        belongs to the server; cache it, do not "store" it.
                    Use a data-fetching library with cache, retry, refetch, optimistic
                    update and dedupe (TanStack Query, SWR, RTK Query, or the framework's
                    own loader). Hand-rolled useEffect+useState fetching loses all five.
URL STATE           filters, sort, page, selected tab, search query, modal open.
                    If the user should be able to bookmark, share or go back to it —
                    it goes in the URL. This is the most commonly misplaced state.
CLIENT/UI STATE     form drafts, hover, focus, transient UI. Local to the component that
                    owns it; lift only when a second component needs it.
CROSS-CUTTING STATE theme, locale, auth session, feature flags. Context or a small store;
                    never duplicated per component.

Escalate deliberately: local → lifted → context → store. A global store as the first
choice produces an app where nothing can be reasoned about locally.
```

### Components — three layers
```text
PRIMITIVES      unstyled behaviour: Radix, Headless UI, React Aria, Ark. Do not rebuild
                focus management, roving tabindex, listbox semantics or dialog trapping.
DESIGN SYSTEM   your tokens + your variants, closed prop sets (see design-systems)
FEATURE         composition for one domain: <OrderTable>, <CheckoutSummary>
PAGE/ROUTE      data loading + layout + feature composition; as little logic as possible
```
Rules: server/data logic stays out of presentational components; feature components own
their data hooks; pages compose and pass minimal props. Colocate a component with its
tests and styles; extract only on second use.

### Data & contracts
```text
□ Types generated from the API schema (OpenAPI → client), never hand-copied
□ Validate at the boundary (zod/valibot/Pydantic-equivalent) — the network is untrusted
□ Every fetch declares: loading, empty, error, partial-failure, stale-while-revalidate
□ Pagination/infinite scroll uses cursors; the UI survives concurrent mutation
□ Mutations declare their cache invalidation explicitly
□ Optimistic updates have a rollback path
□ Timeouts and retries with backoff on every call; no infinite retry
```

### Performance budgets (set numbers, then enforce them)
```text
LCP / INP / CLS targets agreed against web.dev's current Core Web Vitals thresholds
  (verify current values — they change; do not quote numbers from memory)
JS budget per route: initial kB, and total for the interactive surface
Font budget: subsets, woff2, font-display strategy, no layout shift from FOUT
Image budget: modern formats, responsive srcset, explicit dimensions always
Third-party budget: an allowlist with a measured cost per script
```

## Workflow

```text
SCAFFOLD → TOKENS → PRIMITIVES → COMPONENTS → STATES → DATA → ROUTES → A11Y → PERF → VERIFY
```

```text
1 SCAFFOLD     confirm framework version and its actual rendering semantics for this version
2 TOKENS       wire the design tokens into the build (CSS custom properties or the framework's
               theme); components may only consume tokens — lint-enforced
3 PRIMITIVES   adopt accessible primitives for dialog, menu, listbox, tabs, tooltip, disclosure
4 COMPONENTS   build the design-system layer, closed variants, all states, tested in isolation
5 STATES       implement empty / loading / skeleton / error / partial / success for every
               data-bound component BEFORE wiring real data
6 DATA         add the fetching layer with cache, retry, invalidation, optimistic rollback
7 ROUTES       compose pages; choose the rendering strategy per route and record why
8 A11Y         run accessibility-audit passes 1–3 (automated, keyboard, screen reader)
9 PERF         measure against the budget; fix the top three regressions, not all of them
10 VERIFY      real content at all variances; device matrix; visual regression; cross-browser
```

## Failure Modes

```text
DESIGN DRIFT          Implemented pixels diverge from tokens; hard-coded values creep in.
                      Fix: lint against raw values; visual regression tests.
STATE MISPLACEMENT    Server state duplicated in a global store; URL state in useState.
                      Fix: the four-kinds rule, applied at review.
USE-EFFECT FETCHING   No cache, no dedupe, race conditions, waterfalls.
MANUAL TYPES          Hand-copied API types that silently diverge from the contract.
HAPPY-PATH ONLY       No empty, error or partial states — the app breaks on the first 500.
HYDRATION MISMATCH    Server and client render differently (Date.now, locale, random, storage).
WATERFALL FETCHING    Sequential dependent requests that could be parallel or hoisted.
IMAGE DIMENSION GUESS Missing width/height → CLS on every page.
FONT SWAP SHIFT       Unreserved space for webfonts.
THIRD-PARTY CREEP     An analytics script costing more than the app.
PRIMITIVE REBUILD     A custom modal with broken focus trapping and no escape key.
OVER-ABSTRACTION      A <GenericRenderer config={...}/> instead of readable components.
```

## Quality Checklist

```text
□ Rendering strategy chosen per route, recorded with the reason
□ Framework version's actual behaviour verified against its CHANGELOG, not memory
□ Tokens wired into the build; no raw colour/spacing/type values in components (lint-enforced)
□ Accessible primitives used for dialog, menu, listbox, tabs, tooltip, disclosure
□ Components have closed variant sets and every state implemented
□ Empty / loading / skeleton / error / partial states built before real data is wired
□ Server state in a fetching layer with cache, retry, dedupe, invalidation, rollback
□ URL state in the URL; global store used only for genuinely cross-cutting state
□ Types generated from the API contract; runtime validation at the boundary
□ No request waterfalls; dependent fetches hoisted or parallelised
□ Images have explicit dimensions, modern formats and responsive sources
□ Fonts subset, preloaded where critical, with a no-shift strategy
□ Performance budgets set as numbers and enforced in CI
□ Accessibility passes 1–3 run (automated, keyboard, screen reader)
□ Verified with real content at all variances, at 360/768/1440 px, in both themes
□ Visual regression tests on every design-system component
□ No hydration mismatches; no Date/random/storage in the render path
□ Third-party scripts allowlisted with a measured cost
```

## Anti-Patterns

```text
✗ `useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling
✗ A modal built from a `<div>` with `onClick` on the backdrop
✗ Filter state that vanishes on refresh
✗ Hand-writing `interface Order` next to a generated OpenAPI client
✗ `style={{ marginTop: 17 }}`
✗ Rendering a 10,000-row table without virtualisation
✗ `any` at the API boundary
✗ An `<img>` with no width or height
✗ A global store holding one component's hover state
```

## References

- [`design-systems`](../design-systems/SKILL.md) · [`frontend-design`](../frontend-design/SKILL.md)
- [`performance-audit`](../performance-audit/SKILL.md) · [`accessibility-audit`](../accessibility-audit/SKILL.md)
- [`browser-testing`](../browser-testing/SKILL.md) · [`testing`](../testing/SKILL.md)
- [`patterns/frontend/`](../../patterns/frontend/) · [`knowledge/frontend/`](../../knowledge/frontend/)
- [`anti-patterns/frontend/`](../../anti-patterns/frontend/)
- Core Web Vitals — <https://web.dev/articles/vitals> · MDN — <https://developer.mozilla.org/>

## Related Skills

`design-systems` · `frontend-design` · `performance-audit` · `accessibility-audit` ·
`browser-testing` · `api-design` · `testing`

## Evaluation Criteria

```text
1. Design fidelity: visual regression diff against the approved design ≈ 0 unexplained px.
2. Token compliance: 0 raw visual values in component code.
3. State coverage: 100% of data-bound components implement empty/loading/error/partial.
4. Performance: Core Web Vitals within the agreed budget on the target device profile.
5. Accessibility: audit passes 1–3 clean on every route.
6. Type safety: 0 hand-copied contract types; 0 `any` at the boundary.
7. Bug rate in the first 30 days after ship, by category.
```

Test cases in [`tests/`](tests/).
