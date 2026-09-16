---
id: performance-backend-profiling
title: "Backend profiling: measuring before optimising"
domain: performance
summary: >-
  The measurement-first procedure for backend performance work — what to measure, which profiler answers which question, how to read a profile without being misled by self time or off-CPU waits, and the optimisation classes ranked by typical payoff.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [performance, profiling, backend, latency, throughput, measurement, optimisation, database]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: []
sources:
  - title: "Brendan Gregg — USE Method"
    url: https://www.brendangregg.com/usemethod.html
    type: methodology
    organization: brendangregg.com
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Utilisation, Saturation and Errors for every resource — the checklist that prevents profiling the CPU while the actual constraint is a connection pool."
---
# Backend Profiling

## The rule

**Measure, then optimise.** Intuition about where the time goes is wrong often enough that acting on
it is a net loss: optimising code that was not the bottleneck costs the change, the review, the
regression risk and the readability, and buys nothing.

```text
1. REPRODUCE      a stable workload resembling production: real data volume, real concurrency, real
                  payload sizes. A benchmark over an empty table measures the framework.
2. BASELINE       record the numbers before touching anything: p50/p95/p99 latency, throughput, error
                  rate, resource utilisation. Without a baseline there is no "improved".
3. LOCALISE       find which LAYER the time is in before which function: network, database,
                  serialisation, application code, GC, lock contention, external API.
4. PROFILE        the right tool for the question (below).
5. CHANGE ONE THING  the smallest change that addresses the diagnosed cause.
6. RE-MEASURE     same workload, same conditions, same percentiles. Report the delta.
7. KEEP OR REVERT  if the delta is inside the noise, it was not an improvement — revert it, however
                  plausible it seemed.
```

## Which tool for which question

```text
WHERE IS THE WALL TIME?     distributed tracing (OpenTelemetry). The only tool that answers "which
                            service and which external call" rather than "which function". Without a
                            trace, a distributed system's latency is unattributable.
WHICH FUNCTION BURNS CPU?   sampling profiler — py-spy, async-profiler, pprof, perf, pyroscope. Low
                            overhead, production-safe, statistically sound.
WHICH LINE, EXACTLY?        instrumenting or line profiler. Higher overhead; use locally, after
                            sampling has narrowed it down.
IS IT ALLOCATION / GC?      allocation profiler plus GC logs. High allocation rate is a latency
                            source CPU profiling does not show, because the cost is in the collector.
IS IT I/O OR LOCKS?         off-CPU / wall-clock profiling, or a thread dump. CPU profilers report a
                            blocked thread as doing nothing — which is the case under investigation.
IS IT THE DATABASE?         pg_stat_statements plus EXPLAIN (ANALYZE, BUFFERS). Total time across
                            executions, not the slowest single query.
IS THE MACHINE THE LIMIT?   USE method per resource: Utilisation, Saturation, Errors — CPU, memory,
                            disk, network, connection pools, file handles.
IS IT A TAIL PROBLEM?       percentile analysis, plus whether the tail correlates with GC pauses,
                            pool waits, cold caches, noisy neighbours or a specific input shape.
```

## Reading a profile without being misled

```text
SELF vs CUMULATIVE      Self time is time in the function itself; cumulative includes callees. High
                        cumulative with low self time is a caller, not a cost. Optimise high SELF
                        time in hot paths.
SAMPLING IS STATISTICAL A 2% difference between two functions is noise. Read the shape, not the
                        ordering of near-equal entries.
THE FLAT PROFILE        Time spread evenly across many functions usually means the cost is in
                        dispatch, allocation or I/O — not in an algorithm. A different tool is needed,
                        not a different function to optimise.
OFF-CPU IS INVISIBLE    If the profile looks inexplicably cheap and the request is slow, the time is
                        off-CPU.
FIRST RUN ≠ STEADY STATE JIT warmup, cold caches, connection setup and lazy init dominate the first
                        requests. Discard warmup, then measure.
MICROBENCHMARKS LIE     Dead-code elimination, constant folding, unrolling and cache effects make a
                        microbenchmark of a helper unrepresentative of that helper in the system.
                        Benchmark the request, not the function.
AVERAGE HIDES THE TAIL  A p99 at 20× the p50 with a good average is a bad system for the users in the
                        tail. Always report percentiles.
```

## Optimisation classes, by typical payoff

```text
1. THE QUERY                A missing index, an N+1, SELECT * on a wide table, a deep OFFSET, or a
                            query inside a loop. Usually the largest single win and the cheapest.
                            Check here first, always.
2. THE NUMBER OF ROUND TRIPS Batching, eager loading, pipelining, connection reuse. Latency × count
                            is a cost no local optimisation touches.
3. CACHING                  Correct invalidation, right layer, right TTL. Large win when access is
                            skewed; a consistency bug source when it is not. State the staleness budget.
4. ALLOCATION AND COPIES    Avoidable serialisation round trips, large intermediate collections,
                            string concatenation in loops, per-request object graphs that could be reused.
5. CONCURRENCY              Parallelise independent work; remove lock contention; shrink critical
                            sections. Only after the single-threaded path is right — parallelising an
                            N+1 produces N parallel queries.
6. ALGORITHM                The real complexity change. Genuine, and usually ranked lower than
                            engineers expect, because the dominant cost in most services is I/O.
7. THE LANGUAGE RUNTIME     Interpreter vs compiled, GC tuning, JIT settings. Last, and only with a
                            measured reason.
```

## What "done" means

```text
□ baseline and result both recorded, with the workload description and the percentiles
□ the change is explained by the profile, not by plausibility
□ the noise floor is stated and the improvement is outside it
□ correctness tests still pass and no new flake was introduced
□ the resource cost of the improvement is stated — memory for speed, storage for latency, consistency
  for throughput. There is always a trade; the design should say which side was bought.
□ the measurement is repeatable: a committed script or benchmark anyone can re-run
```

## Anti-patterns

```text
✗ Optimising from a guess.              The most common failure, and invisible in the diff.
✗ Caching as the first response.         It is second or third, and it introduces a correctness
  problem that outlives the performance gain.
✗ Measuring the average.                 The tail is the user experience.
✗ Profiling locally against an empty database.  Everything is fast with no data.
✗ Benchmarking without warmup.           You are measuring class loading, JIT compilation and cold caches.
✗ Optimising the demo path.              The slow path is usually the large tenant, the old data or the
  unusual query shape.
✗ Reverting nothing.                     A change inside the noise should be reverted, however elegant.
✗ No committed benchmark.                If the measurement cannot be re-run, the improvement cannot be
  defended or revisited.
```

## References

- [`../databases/indexing-strategy.md`](../databases/indexing-strategy.md) · [`../databases/postgres-gotchas.md`](../databases/postgres-gotchas.md)
- [`frontend-budgets.md`](frontend-budgets.md) — the client-side counterpart
- [`../backend/idempotency.md`](../backend/idempotency.md) · [`../architecture/system-design-checklist.md`](../architecture/system-design-checklist.md)
- [`skills/performance-optimization/SKILL.md`](../../skills/performance-optimization/SKILL.md) · [`skills/database-optimization/SKILL.md`](../../skills/database-optimization/SKILL.md) · [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md)
- [`workflows/performance-review/WORKFLOW.md`](../../workflows/performance-review/WORKFLOW.md)
- USE Method — <https://www.brendangregg.com/usemethod.html> · OpenTelemetry — <https://opentelemetry.io/docs/> · pg_stat_statements — <https://www.postgresql.org/docs/current/pgstatstatements.html>
