---
name: seo-audit
version: 1.0.0
description: >-
  Audit technical and content search visibility — crawlability, indexation, rendering, structured
  data, Core Web Vitals and internal linking — with fixes ordered by measured impact rather than
  by checklist convenience.
category: frontend
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [seo, search, crawlability, indexation, structured-data, core-web-vitals, content]
applies_to: [web, marketing-site, saas, ecommerce]
priority: 74
requires: [performance-audit, accessibility-audit]
conflicts_with: []
estimated_tokens: 2567
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Audit layers
    anchor: "#audit-layers"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Google Search Central documentation"
    url: https://developers.google.com/search/docs
    type: official-docs
    organization: Google
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run. Ranking behaviour and documentation change frequently; verify current guidance before acting on any specific claim."
  - title: "Schema.org"
    url: https://schema.org/
    type: specification
    organization: W3C Schema.org Community Group
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: Google Chrome team
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [performance-audit, accessibility-audit, frontend-implementation, documentation, data-visualization]
related_repositories: [GoogleChrome/lighthouse, screamingfrog/seo-spider, google/search-samples]
tests: 6
---

# SEO Audit

## Purpose

Determine whether the pages that should be found **can be crawled, rendered, indexed and ranked**,
and fix the highest-impact blocker first. Most "SEO problems" are one of four things: the page
cannot be crawled, the content is not in the HTML the crawler sees, the page is a duplicate of
another, or the page does not answer the query.

> **Confidence note.** Search-engine behaviour is proprietary and changes without notice.
> Specific ranking claims here are `medium` confidence with a 90-day review window. The
> technical mechanics (crawlability, indexation, rendering, structured data, performance)
> are stable and verifiable; the ranking-weight folklore is not. Verify current guidance at
> <https://developers.google.com/search/docs> before acting on any specific claim.

## When to Use

```text
□ Launching or migrating a site (the highest-risk moment — most visibility is lost in migrations)
□ Traffic dropped without a content change
□ New pages are not appearing in search after a reasonable period
□ Before a redesign, framework change or URL restructure
□ Periodic technical health review of an existing property
```

## When NOT to Use

```text
✗ An app behind authentication with no public pages — technical SEO is mostly irrelevant
✗ As a substitute for content quality: no technical fix compensates for a page nobody wants
✗ To chase algorithm rumours; audit what is observable and documented
```

## Inputs

```text
property          the domain(s) and URL patterns in scope, and what is out of scope
goals             which pages/queries must be found, and what "success" means (traffic,
                  conversions, discovery of specific content)
access            Search Console or equivalent, server logs, analytics, CMS access, robots/sitemap control
baseline          current indexation counts, traffic, rankings for target queries, with dates
stack             rendering strategy (SSR/SSG/CSR/hybrid), framework and version, CDN, hosting
```

**Server log analysis is the only ground truth** about what crawlers actually request, how
often, and what status they receive. Everything else is inference.

## Audit layers

Work top-down: a failure at layer 1 makes layers 2–7 irrelevant.

### 1. Crawlability
```text
□ robots.txt: does it accidentally block the pages that matter? Check disallow rules,
  wildcard behaviour, and per-user-agent sections. A blocked resource (CSS/JS) can prevent
  correct rendering even when the HTML is allowed
□ Crawl budget: how many requests does the crawler make, and what does it waste them on?
  (faceted navigation, infinite parameter combinations, duplicate paginated listings,
  soft-404s, redirect chains). Large sites lose visibility to wasted crawl, not to bad meta tags
□ Internal links: every indexable page reachable within a few clicks from the home page,
  via real <a href> elements — not via JS click handlers or router-only navigation
□ XML sitemap: present, valid, one per ≤50k URLs / ≤50 MB, only canonical indexable URLs,
  accurate lastmod, submitted and its read/errors checked in Search Console
□ HTTP status: no unintended 4xx/5xx on indexable URLs; no soft-404s (a 200 page with no content);
  no redirect chains or loops; 301 for permanent moves, 308 where method preservation matters
□ Server response: TTFB low enough that crawling is not throttled; no rate-limiting of the crawler;
  no intermittent 5xx under crawl load
□ Authentication/walls: nothing that should be public behind a login, a cookie wall or a paywall
  that is not correctly annotated
```

The full detail — every entry with its detection rule, severity and fix direction — lives in [`references/audit-layers.md`](references/audit-layers.md). Load it when this step is reached rather than keeping it in context for the whole run.

## Migration-specific checks

Migrations destroy more visibility than any other single event. Run these on every restructure:

```text
□ Complete URL inventory BEFORE the change, with status, canonical, traffic and indexation
□ 1:1 301/308 map from every old URL to its new equivalent; no blanket redirect to the home page
□ Redirects validated for chains, loops and orphans before launch
□ Internal links, sitemaps, canonicals, hreflang and structured data all updated to the new URLs
□ robots.txt and CDN/cache rules reviewed for the new structure
□ Staging environment blocked from indexation (auth or noindex), and unblocked correctly at launch
□ Post-launch: crawl the new site, compare indexation counts, monitor 404s and Search Console
  coverage daily for at least a month; keep the old redirect map live indefinitely
□ Third-party signals updated: profiles, backlinks you control, feeds, ads, documentation
```

## Failure Modes

```text
JS-ONLY CONTENT          Primary content absent from the served HTML.
BLOCKED RENDER RESOURCES CSS/JS disallowed in robots.txt, so rendering is incomplete.
CANONICAL CONFLICTS      Sitemap, canonical tag, internal links and redirects disagree.
NOINDEX INVISIBLE        noindex on a page whose HTML the crawler cannot fetch.
REDIRECT CHAINS          A→B→C→D; each hop costs crawl budget and dilutes signals.
SOFT 404S                200 responses with no content; the crawler wastes budget and distrusts the site.
DUPLICATE TITLES         One template, thousands of identical titles.
INDEX BLOAT              Faceted navigation and parameter URLs generating endless near-duplicates.
HREFLANG ERRORS          Non-reciprocal or wrong-code annotations silently ignored.
STAGING INDEXED          A pre-launch mirror competing with production.
MIGRATION BLANKET REDIRECT Every old URL → home page; visibility lost permanently.
MARKUP OF INVISIBLE CONTENT  Structured data for content not on the page — a policy violation.
CHECKLIST WITHOUT LOGS   Auditing meta tags while the crawler receives 503s.
RANKING FOLKLORE         Acting on undocumented algorithm claims instead of observable mechanics.
```

## Quality Checklist

```text
□ Scope, goals, baseline and access confirmed; server logs obtained where possible
□ Layer 1 crawlability: robots.txt, crawl-budget waste, internal links, sitemap validity,
  status codes, TTFB, no unintended walls
□ Layer 2 indexation: coverage reasons, self-referencing canonicals, correct noindex,
  duplicate variants consolidated, host canonicalised, hreflang reciprocal and correct
□ Layer 3 rendering: content present in raw HTML (verified with a no-JS fetch), per-route
  server responses, no hydration mismatch, lazy content resolvable, render resources crawlable
□ Layer 4 on-page: unique titles and descriptions, real heading outline, content answers intent,
  image alt and dimensions, descriptive internal anchors, no orphans, stable readable URLs
□ Layer 5 structured data: correct types, required properties, values matching visible content,
  validated with the official tool, server-rendered
□ Layer 6 performance: Core Web Vitals at field p75, HTTPS with no mixed content,
  mobile-friendly, no CLS, JS weight within the rendering budget, no 5xx during crawl
□ Layer 7 context: entity consistency, discoverability, E-E-A-T where applicable, content gaps
  from query data; no link schemes, doorway pages, cloaking or scaled low-value content
□ Migration checks run in full if any URL structure changed; old redirects kept live
□ Findings prioritised by measured impact (traffic, indexation, crawl waste), not by ease
□ Every claim about search behaviour verified against current official documentation and dated
□ Re-audit scheduled with the metrics that will show whether the fixes worked
```

## Anti-Patterns

```text
✗ Recommending changes based on a ranking factor nobody can document
✗ A single-page app returning the same HTML shell for every route
✗ `robots.txt` disallowing `/assets/` and breaking rendering
✗ Canonicalising every paginated page to page 1
✗ Marking up an FAQ that is not on the page
✗ Redirecting 4,000 retired URLs to the home page during a migration
✗ Auditing titles while the origin returns 503 to the crawler half the time
✗ Buying links or generating doorway pages as a "quick win"
✗ Leaving the staging subdomain indexable after launch
```

## References

- Google Search Central — <https://developers.google.com/search/docs> (verify current guidance)
- Schema.org — <https://schema.org/> · Core Web Vitals — <https://web.dev/articles/vitals>
- robots.txt specification — <https://www.rfc-editor.org/rfc/rfc9309>
- [`performance-audit`](../performance-audit/SKILL.md) · [`accessibility-audit`](../accessibility-audit/SKILL.md)
- [`frontend-implementation`](../frontend-implementation/SKILL.md) — rendering strategy choice
- [`knowledge/seo/`](../../knowledge/seo/) · [`workflows/build-website/`](../../workflows/build-website/)
- [`data-visualization`](../data-visualization/SKILL.md) — reporting the findings

## Related Skills

`performance-audit` · `accessibility-audit` · `frontend-implementation` · `documentation` ·
`data-visualization` · `web-research`

## Evaluation Criteria

```text
1. Indexation: fraction of intended URLs indexed, and unintended URLs excluded (target 100% both).
2. Crawl efficiency: fraction of crawler requests spent on indexable, canonical URLs (from logs).
3. Rendering fidelity: 100% of primary content present in the served HTML or verified as rendered.
4. Core Web Vitals: field p75 within current thresholds on mobile and desktop.
5. Validation: 0 structured-data errors; 0 hreflang reciprocity failures; 0 canonical conflicts.
6. Migration safety: 0 lost URLs without a 1:1 redirect; indexation restored within the stated window.
7. Outcome: impressions and clicks for target queries improve after remediation, measured against baseline.
```

Test cases in [`tests/`](tests/).
