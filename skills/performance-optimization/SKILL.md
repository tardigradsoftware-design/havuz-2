---
name: performance-optimization
version: 1.0.0
description: >-
  Improve performance from measured evidence: establish a baseline, localise the layer, profile with the tool that answers the question, change one thing, re-measure against the noise floor, and keep or revert.
category: performance
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [performance, profiling, latency, throughput, measurement, core-web-vitals, optimisation]
applies_to: [any]
priority: 4
requires: []
conflicts_with: []
estimated_tokens: 2061
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Inputs"
    anchor: "#inputs"
    purpose: implementation
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Brendan Gregg — USE Method"
    url: https://www.brendangregg.com/usemethod.html
    type: methodology
    organization: "brendangregg.com"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "Utilisation, Saturation and Errors per resource — the checklist in step 5 that prevents profiling the CPU while the constraint is a connection pool."
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: "Google"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "LCP, INP and CLS definitions and the p75 field-data percentile used as the frontend target basis."
  - title: "PostgreSQL documentation — Using EXPLAIN"
    url: https://www.postgresql.org/docs/current/using-explain.html
    type: official-docs
    organization: "PostgreSQL Global Development Group"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The database branch of step 5."
related_skills: [database-optimization, debugging, frontend-design, architecture-design, testing]
related_repositories: []
tests: 9
---
# Performance Optimization

## Purpose

Make a system faster by finding where the time actually goes and changing that. The discipline is the
skill: measure, localise, change one thing, re-measure, keep or revert. Optimising from intuition is a
net loss — it costs the change, the review, the regression risk and the readability, and buys nothing
when the guess was wrong, which is the usual case.

## When to Use

```text
✓ latency, throughput or resource use is measurably outside its budget
✓ a specific request, job or page is slow and the layer is not yet identified
✓ a change is about to be made that is expected to improve performance and needs to be verified
✓ capacity planning requires knowing which limit is hit first
```

## When NOT to Use

```text
✗ Nothing has been measured. Establish the baseline first; a complaint of "slow" is not a measurement.
✗ The problem is a correctness bug that manifests as slowness — a lock, a retry loop, a leaked
  connection. Diagnose it as a bug.
✗ The workload being measured is not production-shaped: empty tables, one user, warm caches, a laptop.
✗ The cost is external and immutable — a third-party API's latency, the speed of light to a distant
  region. Architecture or vendor change applies, not optimisation.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| Baseline metrics | yes | p50/p95/p99 latency, throughput, error rate, resource utilisation, before any change |
| Workload definition | yes | real data volume, real concurrency, real payload sizes, cache state |
| Environment description | yes | device/network class for frontend; instance size and region for backend |
| The budget or target | yes | the number this must reach, and whether it is a percentile |
| Noise floor | yes | run-to-run variance with no change; improvements inside it are not improvements |

## Workflow

```text
1. DEFINE THE TARGET AS A NUMBER AND A PERCENTILE.   "Faster" is not a target. p95 under 300 ms for
   this endpoint under this load is. Without it there is no done condition and no way to stop.

2. REPRODUCE A PRODUCTION-SHAPED WORKLOAD.   Real data volume, real concurrency, real payloads. A
   benchmark over an empty database measures the framework, not the system.

3. ESTABLISH THE BASELINE AND THE NOISE FLOOR.   Run the workload several times with no change. Record
   the percentiles and the run-to-run spread. Every later comparison is against both.

4. LOCALISE THE LAYER BEFORE THE FUNCTION.   Is the time in network, database, an external API,
   serialisation, application code, GC, lock contention or the browser main thread? For distributed
   systems, a trace (OpenTelemetry) is the only tool that answers this. For a page, the browser
   Performance panel and the network waterfall are.

5. PROFILE WITH THE TOOL THAT ANSWERS THE QUESTION.   Wall time across services → tracing. CPU by
   function → a sampling profiler (py-spy, async-profiler, pprof, perf). Blocked time → off-CPU or
   wall-clock profiling; a CPU profiler reports a blocked thread as doing nothing. Allocation and GC →
   an allocation profiler plus GC logs. Database → pg_stat_statements and EXPLAIN ANALYZE. Machine
   limits → USE per resource: utilisation, saturation, errors.

6. READ THE PROFILE WITHOUT BEING MISLED.   High cumulative with low self time is a caller, not a cost.
   A 2% gap between entries in a sampling profile is noise. A flat profile means the cost is in
   dispatch, allocation or I/O — a different tool is needed, not a different function.

7. CHANGE ONE THING.   The smallest change addressing the diagnosed cause. Two simultaneous changes
   make the result unattributable.

8. RE-MEASURE UNDER IDENTICAL CONDITIONS.   Same workload, same environment, same percentiles, same
   number of runs. Report the delta against the baseline and against the noise floor.

9. KEEP OR REVERT.   Inside the noise → revert, however elegant. Outside it → keep, and record the
   before/after with the workload description.

10. STATE WHAT THE IMPROVEMENT COST.   Memory for speed, storage for latency, consistency for
   throughput, complexity for a percentile. There is always a trade; write down which side was bought.

11. COMMIT THE BENCHMARK.   A measurement nobody can re-run cannot be defended, revisited or protected
   against regression. Add it to CI where the runtime permits.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Optimised the wrong layer | the delta is inside the noise floor | go back to step 4; the localisation was wrong |
| Benchmark measured warmup | the first runs dominate | discard warmup, then measure steady state |
| Improvement in the lab, not in the field | RUM percentiles unmoved | lab conditions differ from users; re-measure on field data |
| Tail improved, median regressed | p50 rose while p99 fell | report both; decide which the budget covers |
| Caching introduced a correctness bug | stale or inconsistent data reported | the cache layer needs an invalidation design and a stated staleness budget |
| Parallelised an N+1 | N parallel queries instead of N sequential | fix the query pattern first, then parallelise independent work |
| Profile looked cheap but the request was slow | time is off-CPU | use off-CPU or wall-clock profiling |
| Resource cost ignored | memory or connection use rose | measure resource utilisation as part of the result, not only latency |

## Quality Checklist

```text
□ the target is a number with a percentile
□ the workload is production-shaped and documented
□ baseline and noise floor are recorded
□ the layer was localised before the function
□ the profiling tool matched the question
□ exactly one change was made
□ the delta is outside the noise floor
□ resource cost of the improvement is recorded
□ correctness tests still pass and no new flake was introduced
□ the benchmark is committed and re-runnable
```

## Anti-Patterns

```text
✗ OPTIMISING FROM A GUESS.   The most common failure, and invisible in the diff.
✗ MEASURING THE AVERAGE.   The tail is the user experience; a good mean with a p99 at 20× is a bad
  system for the users in the tail.
✗ CACHING AS THE FIRST RESPONSE.   It is second or third, and it introduces a correctness problem that
  outlives the performance gain.
✗ PROFILING AN EMPTY DATABASE.   Everything is fast with no data.
✗ BENCHMARKING WITHOUT WARMUP.   You are measuring class loading, JIT compilation and cold caches.
✗ OPTIMISING THE DEMO PATH.   The slow path is the large tenant, the old data or the unusual query shape.
✗ PREMATURE OPTIMISATION OF COLD CODE.   Effort spent on a path executed twice a day.
✗ KEEPING A CHANGE INSIDE THE NOISE.   Plausibility is not evidence.
✗ NO COMMITTED BENCHMARK.   The regression returns within a quarter and nobody can prove it.
```

## References

- [`knowledge/performance/backend-profiling.md`](../../knowledge/performance/backend-profiling.md) — tool selection and profile reading in detail
- [`knowledge/performance/frontend-budgets.md`](../../knowledge/performance/frontend-budgets.md) — Core Web Vitals budgets and enforcement
- [`knowledge/databases/indexing-strategy.md`](../../knowledge/databases/indexing-strategy.md) · [`knowledge/databases/postgres-gotchas.md`](../../knowledge/databases/postgres-gotchas.md)
- [`skills/database-optimization/SKILL.md`](../database-optimization/SKILL.md) · [`skills/debugging/SKILL.md`](../debugging/SKILL.md) · [`skills/architecture-design/SKILL.md`](../architecture-design/SKILL.md)
- [`workflows/performance-review/WORKFLOW.md`](../../workflows/performance-review/WORKFLOW.md) · [`agents/performance-engineer/AGENT.md`](../../agents/performance-engineer/AGENT.md)
- USE Method — <https://www.brendangregg.com/usemethod.html> · OpenTelemetry — <https://opentelemetry.io/docs/> · web.dev — <https://web.dev/articles/vitals>
