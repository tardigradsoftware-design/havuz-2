---
name: performance-audit
version: 1.0.0
description: >-
  Find and fix the performance problems that matter, in measurement order — profile before
  optimising, set budgets, verify the fix on the affected population, and stop when the budget is met.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [performance, profiling, latency, throughput, core-web-vitals, optimization]
applies_to: [web, backend, frontend, infrastructure]
priority: 82
requires: []
conflicts_with: []
estimated_tokens: 2691
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Where the time goes
    anchor: "#where-the-time-goes"
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
    note: "Metric definitions and thresholds are revised periodically; verify current values before quoting numbers."
  - title: "Lighthouse"
    url: https://github.com/GoogleChrome/lighthouse
    type: github-repository
    organization: Google Chrome
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [frontend-implementation, backend-engineering, database-design, browser-testing, debugging]
related_repositories: [GoogleChrome/lighthouse, grafana/k6, locustio/locust, open-telemetry/opentelemetry-specification]
tests: 6
---

# Performance Audit

## Purpose

Make a system meet a **stated budget on a stated workload for a stated population**, using
measurement to decide where to spend effort. Performance work without a budget is
entertainment; performance work without measurement is guesswork.

## When to Use

```text
□ Latency, throughput or page-load complaints backed by a symptom (not a vibe)
□ Before scaling infrastructure — the cheapest fix is usually not more machines
□ Setting budgets for a new product or a redesign
□ A regression: something got slower and you know roughly when
□ Load/capacity planning for a known event
```

## When NOT to Use

```text
✗ Optimising a path nobody uses (measure traffic first — the profile decides)
✗ Micro-optimising code whose cost is dominated by a network call
✗ Before correctness: a fast wrong answer is worse
✗ When the real complaint is a UX/design problem misreported as "slow"
```

## Inputs

```text
budget        the numeric target, per metric, agreed before measuring
workload      realistic traffic shape: rate, concurrency, payload sizes, data volume
population    the users who matter: device class, network class, geography, data scale
environment   where it will actually run, with its limits
baseline      current measurements, with method and date
```

**No budget, no audit.** "Make it faster" has no stopping condition, so it either never
finishes or stops arbitrarily.

## Workflow

```text
BUDGET → MEASURE → PROFILE → RANK → FIX → VERIFY → ENFORCE
```

### 1. BUDGET
```text
Latency      p50 / p95 / p99 per endpoint or interaction — p99, not the mean.
             Means hide the users who are having a bad time.
Throughput   requests/sec or jobs/sec at an acceptable error rate
Frontend     Core Web Vitals as defined by web.dev for the current revision
             (verify current metric names and thresholds; they have changed over time),
             measured on the target device/network profile, at the p75 field value
Resources    CPU, memory, connection count, DB query count per request, JS kB per route
Cost         per 1k requests — performance and cost are the same optimisation
Error rate   performance changes that raise errors are regressions, not wins
```

### 2. MEASURE
Two kinds, and they disagree for good reasons:

```text
LAB      reproducible, controlled, good for regression detection and attribution.
         Lighthouse/WebPageTest/k6/locust/profiler on a fixed environment.
FIELD    real users, real devices, real networks — the truth about experience.
         RUM / OpenTelemetry / server access logs, reported as percentiles by segment.
```
Report percentiles **by segment** (device class, network, geography, tenant, data volume).
A global p95 hides the tenant with 10M rows.

### 3. PROFILE
Attribute the time before touching code.

```text
□ Traces across every hop — where does the request actually spend its wall time?
□ Query count and per-query time for the request (N+1 is the single most common finding)
□ Profiler on the hot function (CPU time, allocations, lock contention, GC)
□ Network waterfall: serial dependencies, TTFB, payload size, cache hit rate, compression
□ Render path (frontend): main-thread work, long tasks, layout thrash, re-render counts
□ Bundle: what is shipped, what is used, what blocks first paint
□ Saturation: connection pools, thread pools, queue depth, DB connections, file descriptors
```
Produce a ranked list: `component | measured cost | share of the budget | evidence`.

### 4. RANK
Effort vs effect, largest share first. Fix the top item completely rather than five items
partially. Explicitly list what you are **not** fixing and why (usually: below the noise
floor, or the fix costs more than the budget breach).

### 5. FIX — in this order, cheapest and highest-yield first
```text
1  REMOVE WORK      do not compute, fetch, render or transfer it. Delete the call, the
                    column, the widget, the third-party script. This beats every other fix.
2  DO IT LESS       cache (with TTL and invalidation), memoise, batch, dedupe, paginate,
                    debounce, lazily load, code-split.
3  DO IT EARLIER    preload, prefetch, preconnect, warm pools, start independent work in
                    parallel instead of serially, hoist data to the edge/server.
4  DO IT CLOSER     CDN, edge compute, regional replicas, colocation with the data.
5  DO IT CHEAPER    better algorithm or data structure; index instead of scan; keyset
                    instead of offset; streaming instead of buffering.
6  DO IT WITH MORE  scale up/out — last, because it multiplies cost without fixing cause.
```

### 6. VERIFY
```text
□ Same method, same workload, same environment as the baseline — otherwise the comparison
  is meaningless
□ Report percentiles by segment, not just the headline number
□ Confirm no other metric regressed: error rate, memory, cost, correctness, accessibility
□ Test at 2× the expected peak, not at the average
□ Field data confirms the lab result (lab wins that do not appear in field data are usually
  measuring the wrong thing)
```

### 7. ENFORCE
```text
□ Budgets as CI assertions: fail the build on regression, with a documented threshold
□ Lighthouse/k6 in CI on the affected routes; bundle-size gate on the frontend
□ Performance dashboards with alerts on p95/p99, not on the mean
□ Every new endpoint, query and third-party script reviewed against the budget
□ Re-measure on a schedule — performance decays with feature additions
```

## Where the time goes

The usual distribution of findings, in the order to check them:

```text
FRONTEND   unoptimised images and missing dimensions · render-blocking JS/CSS · oversized
           bundles with no code splitting · third-party scripts · font loading causing shift ·
           waterfalls of dependent fetches · long main-thread tasks · layout thrash from
           interleaved read/write DOM access · no virtualisation on long lists ·
           missing cache headers · unreserved space causing CLS
BACKEND    N+1 queries · missing or wrong index · unbounded queries · work inside a
           transaction · serial calls that could be parallel · no caching on an expensive
           read · synchronously waiting on something that could be queued · oversized
           payloads · missing compression · connection-pool exhaustion · lock contention ·
           retries without jitter creating a storm
DATA       OFFSET pagination at depth · SELECT * with large columns · denormalised reads
           that scan · missing partitioning on time-series · stale statistics · autovacuum
           starvation · hot index page from sequential IDs
INFRA      cold starts · cross-region hops · DNS/TLS handshake per request · saturation with
           no backpressure · an autoscaler reacting too slowly · a single unbalanced shard
```

## Failure Modes

```text
NO BUDGET             Optimising without a target; never finishes, never proves anything.
MEAN-BASED REVIEW     Averages hide the p99 users who are complaining.
LAB-ONLY EVIDENCE     A Lighthouse score improved; real users saw nothing.
OPTIMISE THE COLD PATH Improving a function that runs twice per day.
GUESS-DRIVEN FIXING   Rewriting the module that "feels slow" without a profile.
PARTIAL VERIFICATION  Measuring a different workload than the baseline.
REGRESSION BLINDNESS  Fixing latency while raising error rate or memory.
PREMATURE ABSTRACTION Caching, queues and microservices added before measurement.
ONE-SHOT EFFORT       No CI gate; the budget is re-breached in the next release.
VENDOR METRIC TRUST   Accepting a provider's benchmark without the measurement method.
```

## Quality Checklist

```text
□ Numeric budgets agreed per metric before measuring (latency p50/p95/p99, throughput, CWV, resources, cost)
□ Target population and workload defined; measurements segmented by device/network/data volume
□ Baseline captured with method, environment and date
□ Both lab and field measurements taken; percentiles reported, never only means
□ Time attributed by trace/profile before any change; ranked list produced with evidence
□ Fixes applied in order: remove → less → earlier → closer → cheaper → more
□ N+1, index, cache, payload and waterfall checks run explicitly
□ Verified with the same method and workload as the baseline, at 2× peak
□ No other metric regressed (errors, memory, cost, correctness, a11y)
□ Not-fixed items listed with reasons
□ Budgets enforced in CI; dashboards alert on p95/p99
□ Re-measurement scheduled
```

## Anti-Patterns

```text
✗ "The average response time is 120 ms" as the whole report
✗ Adding a cache layer before checking whether the query has an index
✗ Scaling out to fix an N+1
✗ Optimising a Lighthouse score instead of the user experience
✗ Citing a vendor benchmark whose method is not published
✗ Rewriting a service because it "feels slow"
✗ Measuring a warm cache and reporting it as cold-start performance
✗ Shipping a performance fix with no CI gate, then re-regressing next sprint
```

## References

- [`frontend-implementation`](../frontend-implementation/SKILL.md) · [`backend-engineering`](../backend-engineering/SKILL.md)
- [`database-design`](../database-design/SKILL.md) · [`debugging`](../debugging/SKILL.md)
- [`workflows/performance-review/`](../../workflows/performance-review/)
- [`knowledge/performance/`](../../knowledge/performance/)
- Core Web Vitals — <https://web.dev/articles/vitals> · Lighthouse — <https://github.com/GoogleChrome/lighthouse>

## Related Skills

`frontend-implementation` · `backend-engineering` · `database-design` · `browser-testing` ·
`debugging` · `deployment`

## Evaluation Criteria

```text
1. Budget attainment: every metric within the agreed budget on the target population.
2. Attribution accuracy: profiled share of cost predicts achieved improvement (target ≥ 0.7 correlation).
3. No regressions: error rate, memory, cost and correctness unchanged or improved.
4. Reproducibility: a second engineer re-runs the measurement and gets the same conclusion.
5. Durability: budgets still met one quarter later, with CI gates in place.
6. Cost efficiency: improvement per unit of infrastructure spend.
```

Test cases in [`tests/`](tests/).
