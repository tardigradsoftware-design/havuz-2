---
id: frontend-rendering-strategies
title: "Rendering strategies: choosing where and when HTML is produced"
domain: frontend
summary: >-
  The CSR / SSR / SSG / ISR / streaming / RSC / islands decision — what each costs in infrastructure, latency and staleness control; the two content questions that determine the answer; and the migrations that are harder than they look.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [rendering, ssr, ssg, isr, csr, streaming, rsc, islands, hydration, ttfb, architecture]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: []
sources:
  - title: "Next.js documentation — Rendering"
    url: https://nextjs.org/docs/app/building-your-application/rendering
    type: official-docs
    organization: Vercel
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The reference implementation of the server/client, static/dynamic and streaming combinations described here; framework-specific behaviour is version-dependent and carries a 90-day freshness window."
---
# Rendering Strategies

## The two questions that decide everything

```text
1. WHEN IS THE CONTENT KNOWN?     at build time · on every request · partially both · only in the
                                  browser after data arrives
2. HOW MUCH INTERACTIVITY, WHERE? none (a document) · some (a form, a filter) · pervasive (an app)
```

Every strategy is an answer to those two. Choosing by framework preference, or by what the tutorial
used, is how a documentation site ends up with a database round trip per page view and how a dense
internal tool ends up statically generated and stale.

## The strategies

```text
CSR — client-side rendering
  HTML shell from the server; the browser fetches data and builds the DOM.
  Cost:      blank until JS loads and executes; poor LCP; content invisible to crawlers that do not
             execute JS and slow for those that do; the whole bundle ships before anything is usable.
  Use when:  the view is post-authentication, highly interactive, personalised per session, with no
             SEO or first-paint requirement. Dashboards, editors, admin tools.

SSR — server-side rendering per request
  HTML produced on the server for each request, then hydrated.
  Cost:      a server on every request; TTFB now includes your data fetching; caching is harder
             because output is per-user; hydration cost across the whole tree.
  Use when:  content is request-specific — personalised, authenticated or live — AND must be visible
             fast and indexable.

SSG — static generation at build time
  HTML produced during the build, served from a CDN.
  Cost:      build time grows with page count; a content change requires a rebuild; nothing
             per-request or per-user.
  Use when:  content is known at build time and identical for everyone. Documentation, marketing,
             blogs. The cheapest and fastest option that exists, and the right default when it applies.

ISR — incremental regeneration
  Static pages regenerated on a schedule or on demand, stale-while-revalidate semantics.
  Cost:      a staleness window the content owner must understand; a persistence layer for the cache
             in a multi-instance deployment; the regeneration path is a code path that needs tests.
  Use when:  content changes often but not per request, and a bounded staleness window is acceptable.
             Catalogues, news, documentation with frequent edits.

STREAMING / Suspense
  The shell and known parts flush immediately; slow parts arrive later, in place, with a fallback.
  Cost:      error handling changes shape — a failure after the shell has flushed cannot change the
             status code, so errors surface in-band; ordering constraints; harder caching.
  Use when:  some parts are fast and others slow, and the fast parts are worth showing now. The
             largest TTFB/LCP win available for a page with one slow dependency.

ISLANDS / partial hydration
  Static HTML everywhere; JS only on interactive components, hydrated independently.
  Cost:      framework constraints; shared state between islands needs an explicit mechanism; two
             mental models in one page.
  Use when:  a mostly-content page with a few interactive widgets. The best hydration cost profile
             available.

RSC — server components
  Component-level split: some render only on the server and ship serialised output, never their JS;
  others are client components and hydrate.
  Cost:      a boundary that must be designed deliberately — "use client" is an architectural
             decision, not an annotation. Data fetching moves into components, changing how caching
             and revalidation work. Debugging spans two environments.
  Use when:  a large app where bundle size is the constraint and much of the tree is presentational
             over server-fetched data.

EDGE RENDERING
  SSR or RSC in a runtime close to the user.
  Cost:      a restricted runtime (no arbitrary Node APIs, limited CPU, different cold starts), a
             different observability story, vendor coupling.
  Use when:  per-request personalisation or geo-dependence where latency dominates.
```

## Cost comparison

| Strategy | TTFB | LCP | JS shipped | Infra | Caching | Staleness control |
|---|---|---|---|---|---|---|
| SSG | lowest | best | none needed | CDN only | trivial | rebuild |
| ISR | low | best | none needed | CDN + store | good | revalidate interval |
| Islands | low | best | minimal | CDN | trivial | rebuild |
| Streaming SSR | medium | good | full tree | server | hard | per request |
| SSR | medium-high | good | full tree | server | hard | none — always fresh |
| RSC | medium | good | partial | server + CDN | medium | per component |
| CSR | lowest server cost | worst | full tree | static host | trivial | none |

These describe the strategy in isolation. A badly built SSG page loses to a well built SSR page — the
strategy sets the ceiling, the implementation sets the result.

## Choosing

```text
DOCUMENTATION, MARKETING, BLOG      SSG; ISR when content changes often enough that rebuilds hurt.
                                    Islands or zero JS where interactivity is a search box and a menu.
E-COMMERCE CATALOGUE                ISR for category and product pages; SSR or streaming for cart and
                                    checkout, where freshness is correctness.
AUTHENTICATED DASHBOARD             CSR inside the shell, or SSR/streaming for the first view.
                                    Per-request personalisation rules out static; bundle size rules in
                                    islands or RSC.
CONTENT SITE WITH LIVE DATA         Streaming SSR — the article shell flushes, comments and
                                    recommendations arrive.
INTERNAL TOOL, POST-AUTH            CSR. The SEO and first-paint arguments do not apply; the
                                    interactivity does.
MIXED                               Per-route. One strategy for a whole product is usually wrong, and
                                    the framework choice should permit per-route selection.
```

## Migrations harder than they look

```text
CSR → SSR         Every data fetch must work on the server: no window, no localStorage, no
                  browser-only library at module scope. Environment-dependent module initialisation
                  is the common blocker, and it fails at import time rather than at render.
SSR → streaming   A failure after the shell flushes cannot change the status code, so errors must be
                  surfaced in-band with a fallback. Caching headers become per-segment.
Anything → RSC    The client/server boundary must be designed. Context, event handlers and hooks
                  cannot cross into a server component, so a provider high in the tree forces
                  "use client" over a large subtree and negates the bundle benefit.
Static → dynamic  A single per-request value — a cookie, a header, a timestamp, a random ID — makes a
                  page dynamic. Audit for these before assuming a route is cacheable; they are easy to
                  introduce accidentally and the failure is a silent cache miss.
```

## References

- [`../performance/frontend-budgets.md`](../performance/frontend-budgets.md) — the budgets these strategies are chosen against
- [`react/best-practices.md`](react/best-practices.md) — the hydration and re-render side
- [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/seo-audit/SKILL.md`](../../skills/seo-audit/SKILL.md) · [`skills/architecture-design/SKILL.md`](../../skills/architecture-design/SKILL.md) · [`skills/performance-optimization/SKILL.md`](../../skills/performance-optimization/SKILL.md)
- [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md) · [`patterns/frontend/`](../../patterns/frontend/)
- Next.js rendering — <https://nextjs.org/docs/app/building-your-application/rendering> · Astro islands — <https://docs.astro.build/en/concepts/islands/> · patterns.dev — <https://www.patterns.dev/>
