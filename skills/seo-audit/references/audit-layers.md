---
id: audit-layers
title: "The seven SEO audit layers in dependency order"
domain: seo
summary: >-
  Crawlability, indexation, rendering, on-page signals, structured data, performance and off-page context, each with its checks — extracted from the skill so the skill body stays inside its context budget.
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
tags: [reference, seo]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [seo-audit]
---

# The seven SEO audit layers in dependency order

Reference material for [`seo-audit`](../SKILL.md), extracted so the skill body stays
within its context budget. Load this file only when the step that needs it is reached.


Work top-down: a failure at layer 1 makes layers 2–7 irrelevant.

## 1. Crawlability
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

## 2. Indexation
```text
□ Which URLs are indexed vs not, and why (Search Console coverage / site: queries as a rough check)
□ canonical tags: self-referencing on every indexable page; pointing to the intended version on
  duplicates; not conflicting with the sitemap, internal links or redirects (mixed signals are ignored)
□ noindex: absent from pages that should be indexed; present on thank-you, search-result,
  staging, parameter and thin pages. Check noindex is not delivered via a blocked resource
  (a noindex in a robots-blocked page cannot be seen)
□ robots meta and X-Robots-Tag headers consistent with each other
□ Duplicate content: parameter variants, session IDs, http/https, www/non-www, trailing slash,
  case variants, index.php vs /, paginated series, printer/mobile variants, staging mirrors
□ Domain-level canonicalisation: one preferred host, 301 from every variant, consistent internal links
□ Hreflang: correct language/region codes, self-referencing plus reciprocal annotations,
  x-default where needed — hreflang errors are extremely common and silently ignored
□ Index bloat: thousands of near-identical or thin pages dilute crawl and index attention
```

## 3. Rendering
```text
□ Is the content in the raw HTML? Fetch with a plain HTTP client (no JS) and look.
  If the primary content is absent, you depend on the crawler's JS rendering — which is
  slower, budget-limited, and not guaranteed for every page
□ Client-side-only routing: does each route have a real URL, a real server response and its own
  title/meta? A single-page app returning identical HTML for every route is one page to a crawler
□ Hydration mismatches: server HTML and client render must agree, or the crawled DOM differs
  from the served DOM
□ Lazy-loaded content: images/content below the fold must use standard loading attributes and
  still resolve to real URLs and alt text; content behind an interaction is not indexable
□ Blocked resources: CSS/JS required for rendering must be crawlable
□ Verify with the URL Inspection tool's rendered HTML and screenshot, plus a no-JS fetch
```

## 4. On-page signals
```text
□ title: unique per page, describes the page, primary intent early, ~50–60 characters visible,
  branded consistently. Duplicate or missing titles are the most common on-page defect
□ meta description: unique, accurate, a call to action; not used as a ranking factor but
  heavily used as the snippet — write it, or accept a generated one
□ One h1 that matches the page's subject; a real heading outline (this is also accessibility)
□ Body content answers the query completely: intent, depth, freshness, originality
□ Images: descriptive filenames, alt text conveying the same information (also a11y),
  responsive sizes, modern formats, explicit dimensions
□ Internal links with descriptive anchor text; a sensible hub-and-spoke structure;
  orphan pages found and linked or removed
□ URL structure: readable, stable, lowercase, hyphenated, shallow, no session parameters
□ Freshness: lastmod accurate, dates visible where recency matters, updated content actually updated
```

## 5. Structured data
```text
□ Correct type from schema.org for the content that actually exists on the page — never mark up
  content that is not visible to the user (a manual-action risk)
□ Required properties present per the current documentation; validate with the official tool
□ Matching the page: Organisation/WebSite on the home page, Article/Product/FAQ/HowTo/Breadcrumb
  on the relevant pages, with values identical to the visible content
□ JSON-LD in the head or body, server-rendered, not injected after load where avoidable
□ Breadcrumbs markup matching the real navigation path
□ Monitor structured-data reports for errors and for rich-result eligibility (eligibility is not
  a guarantee of display)
```

## 6. Performance & experience
```text
□ Core Web Vitals at the field p75 on mobile and desktop (verify current metric names and
  thresholds at web.dev — they have changed over time)
□ HTTPS everywhere, no mixed content, valid certificates, HSTS
□ Mobile-friendly: viewport set, no horizontal scroll, tap targets adequate, no intrusive interstitials
□ No layout shift from images, fonts, ads or late content
□ JavaScript weight: the crawler's rendering budget is finite; heavy client bundles delay indexation
□ Server reliability: 5xx and timeouts during crawl directly reduce indexed pages
```

## 7. Off-page & content context (audit, do not manipulate)
```text
□ Brand and entity consistency: the same name, logo, descriptions and identifiers across the site,
  structured data and public profiles
□ Inbound link profile: is the site discoverable at all? (a page with no internal or external
  links may never be found)
□ E-E-A-T signals where they matter (health, finance, legal): authorship, credentials, citations,
  contact and about information, editorial policy, correction policy
□ Content gaps: queries with impressions but no clicks, queries you rank position 5–20 for
  (the highest-leverage improvements), topics competitors cover that you do not
□ Do NOT: buy links, participate in link schemes, generate doorway pages, cloak content,
  or produce scaled low-value AI content. These are documented policy violations and the
  audit must flag them if present, not recommend them
```
