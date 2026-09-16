---
id: performance-frontend-budgets
title: "Frontend performance budgets: what to measure and what to enforce"
domain: performance
summary: >-
  Concrete budgets for Core Web Vitals and payload size, the measurement methodology that makes numbers comparable, the causes of each regression class, and the CI enforcement that keeps a budget from decaying.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [performance, core-web-vitals, lcp, cls, inp, budgets, bundle-size, frontend, ci]
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
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: Google
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The normative definitions and thresholds for LCP, INP and CLS, and the CrUX field-data percentile (75th) used as the measurement basis here."
---
# Frontend Performance Budgets

## The budgets

Thresholds are the published "good" boundaries, measured at the **75th percentile of real user
sessions**. A budget means nothing without a stated percentile and environment — a lab number and a
field number are different quantities.

```text
CORE WEB VITALS (field, p75)
  LCP   Largest Contentful Paint    ≤ 2.5 s    the main content is visible
  INP   Interaction to Next Paint   ≤ 200 ms   the page responds to input
  CLS   Cumulative Layout Shift     ≤ 0.1      the page does not move unexpectedly

PAYLOAD
  initial JS, compressed            ≤ 170 kB   a common practical ceiling for a fast mobile first
                                               load; tighter for content-heavy pages
  total initial weight, compressed  ≤ 500 kB   HTML + CSS + JS + critical above-the-fold images
  CSS delivered initially           ≤ 50 kB    critical above-the-fold CSS inlined or first
  above-the-fold images             modern format (AVIF/WebP), explicitly sized, nothing below the
                                               fold eager-loaded

REQUESTS
  third-party scripts, first load   ≤ 3        each is a latency, privacy and failure domain
  render-blocking requests          0          no render-blocking CSS beyond critical, no synchronous
                                               JS in <head>

SERVER
  TTFB (field, p75)                 ≤ 800 ms   above this, no client-side work can reach a good LCP
```

Starting points, not laws. A marketing page and a dense internal tool have different budgets; state
yours per **page template**, not per site.

## Measurement methodology

Numbers that are not comparable are not measurements.

```text
FIELD (RUM)   real users, devices and networks. The only data describing the actual experience.
              CrUX or your own RUM. Moves slowly, and it is the number that matters.
LAB           reproducible, controllable, immediate — Lighthouse, WebPageTest, Playwright tracing.
              Use it to ATTRIBUTE a change; never to claim an outcome.
CONDITIONS    state them every time: device class, connection profile, region, cache state (cold vs
              warm), authenticated vs anonymous, exact URL. A Lighthouse score without these is
              uninterpretable.
PERCENTILE    p75 for field data, per the published methodology. A median hides the users on slow
              devices and poor networks — the ones failing the budget.
SEGMENT       by page template, device class and geography. An aggregate that passes can hide a
              template failing badly for mobile users in one region.
FREQUENCY     lab budgets on every PR against a fixed emulated profile; field data reviewed weekly.
              Field data moves too slowly to gate a PR and too importantly to ignore.
```

## What causes each regression

```text
LCP    a slow TTFB — server, DNS, TLS, redirect chains. Fix this first; nothing downstream
       compensates for it.
       a render-blocking stylesheet or synchronous script in <head>
       the LCP element being an image discovered late: no fetchpriority, no preload, no explicit
       dimensions, or loaded through CSS background-image
       client-side rendering where the content could have been server-rendered
       a webfont blocking text rendering — font-display: swap plus preload of the one weight used
       a redirect chain, an unoptimised CDN, or an origin far from the users

INP    long tasks on the main thread (> 50 ms) — the dominant cause
       a large framework bundle parsed and compiled at interaction time
       synchronous layout or style recalculation in an event handler (reading offsetHeight after
       writing a style)
       heavy work in a handler that should be deferred, chunked or moved to a worker
       third-party script executing on the main thread
       unvirtualised lists rendering thousands of DOM nodes

CLS    images, ads and embeds without explicit width and height
       dynamically injected content above existing content — banners, notifications, cookie bars
       pushing the page down after load
       webfonts swapping after text renders with different metrics — fix with size-adjust,
       ascent-override and fallback metric matching
       animations that move layout rather than using transform
       content appearing after an async call without reserved space — reserve with min-height or
       aspect-ratio

BUNDLE a dependency imported wholesale for one function (an icon library without tree-shaking, a date
       library imported whole)
       a polyfill for a browser nobody supports
       route or modal code loaded on first paint instead of on demand
       the same library duplicated at two versions in the tree
       source maps shipped to production
```

## Enforcement

A budget that is not enforced is a document. Three mechanisms:

```text
1. FAIL THE BUILD ON SIZE.     Compare bundle size against the budget in CI and fail above it, with
                               the delta reported per chunk. Size is the one performance metric that
                               is deterministic and cheap to gate. size-limit, bundlesize, or a custom
                               step over the build manifest.
2. GATE THE LAB RUN.           Lighthouse CI or Playwright tracing on a fixed emulated profile
                               against a preview deployment, asserting LCP, TBT/INP, CLS and TTFB.
                               Assert with a tolerance, not an equality — lab numbers move a few
                               percent between runs.
3. TRACK THE FIELD.            A weekly p75 dashboard per template, alerting on regression beyond a
                               threshold. Field data cannot gate a PR, but it is the only measure of
                               whether the work succeeded.

PLUS
  □ Every new dependency states its compressed size in the PR that adds it.
  □ A regression that cannot be fixed immediately gets a budget EXCEPTION with an owner and a date,
    recorded in the repository — not silently absorbed.
  □ The budget file is versioned and reviewed like code. Changing it is a design decision.
```

## Anti-patterns

```text
✗ Optimising the Lighthouse score.   A proxy measured in conditions your users are not in. Optimise
  the field p75; use the lab run to attribute changes.
✗ One site-wide number.              Page templates differ by an order of magnitude in what they load.
✗ Deferring everything.              Lazy-loading below the fold is right; lazy-loading the LCP element
  makes LCP worse.
✗ Preloading everything.             Every preload competes for bandwidth with resources the browser
  already knows it needs. One or two, at most.
✗ Ignoring TTFB.                     No client-side work rescues a 2 s server response.
✗ Removing a third-party script but keeping its consent banner, cookie and layout reservation.
✗ Shipping the budget as prose.      If it is not in CI, it decays within one quarter.
```

## References

- web.dev Core Web Vitals — <https://web.dev/articles/vitals> · CrUX — <https://developer.chrome.com/docs/crux/>
- [`../frontend/rendering-strategies.md`](../frontend/rendering-strategies.md) — the server/client decision that dominates LCP
- [`../frontend/react/best-practices.md`](../frontend/react/best-practices.md) — re-renders, long tasks, bundle
- [`../accessibility/wcag-practical-checklist.md`](../accessibility/wcag-practical-checklist.md) — motion, target size and reflow overlap here
- [`backend-profiling.md`](backend-profiling.md) — the same discipline, server side
- [`skills/performance-optimization/SKILL.md`](../../skills/performance-optimization/SKILL.md) · [`skills/frontend-design/SKILL.md`](../../skills/frontend-design/SKILL.md) · [`skills/seo-audit/SKILL.md`](../../skills/seo-audit/SKILL.md)
- [`workflows/performance-review/WORKFLOW.md`](../../workflows/performance-review/WORKFLOW.md) · [`workflows/build-website/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
