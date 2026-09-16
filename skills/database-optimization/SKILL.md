---
name: database-optimization
version: 1.0.0
description: >-
  Diagnose and fix database performance problems from measured evidence: locate the query, read the plan, choose the narrowest index or query change that fixes the diagnosed cause, and verify the improvement outside the noise floor.
category: database
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [database, postgres, query-optimization, explain, indexes, slow-queries, performance]
applies_to: [postgres, sql, backend, data-intensive]
priority: 4
requires: []
conflicts_with: []
estimated_tokens: 2492
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
  - title: "PostgreSQL documentation — Using EXPLAIN"
    url: https://www.postgresql.org/docs/current/using-explain.html
    type: official-docs
    organization: "PostgreSQL Global Development Group"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The plan-reading procedure in step 3 and the ANALYZE/BUFFERS semantics."
  - title: "PostgreSQL documentation — pg_stat_statements"
    url: https://www.postgresql.org/docs/current/pgstatstatements.html
    type: official-docs
    organization: "PostgreSQL Global Development Group"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Total execution time across calls, which is the ranking basis in step 1."
  - title: "PostgreSQL documentation — CREATE INDEX CONCURRENTLY"
    url: https://www.postgresql.org/docs/current/sql-createindex.html
    type: official-docs
    organization: "PostgreSQL Global Development Group"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Locking behaviour, the no-transaction-block restriction and the INVALID-index failure mode in step 9."
related_skills: [performance-optimization, database-design, debugging, backend-engineering, migration]
related_repositories: []
tests: 23
---
# Database Optimization

## Purpose

Make the database faster by finding the actual cause from measured evidence and applying the narrowest
change that addresses it. Not "add an index" — which is a guess — but "this query does a sequential scan
over 4M rows because no index serves `(tenant_id, created_at)`, and adding one moves p95 from 1.8 s to
40 ms".

## When to Use

```text
✓ a query, endpoint or job is measurably slow and the database is the suspected layer
✓ database CPU, IOPS or connection saturation is the observed bottleneck
✓ a new query pattern is being introduced against a large existing table
✓ a migration or index change needs to be evaluated before it is applied
```

## When NOT to Use

```text
✗ Nothing has been measured. Establish the baseline and confirm the database is the layer first — see
  performance-optimization. Optimising a query that accounts for 4% of request time is a net loss.
✗ The slowness is in the application: N+1 queries are an application bug, and the fix is the query
  pattern, not an index.
✗ The dataset is empty or tiny in the test environment. Everything is fast with no data; measure against
  production-shaped volume.
✗ The real constraint is a lock, a long transaction or connection-pool exhaustion. Those are
  concurrency problems, and an index will not touch them.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| The slow query, verbatim | yes | with its bind parameters, not a paraphrase |
| `EXPLAIN (ANALYZE, BUFFERS)` output | yes | the actual plan with real timings, not the estimated plan |
| Table and index definitions | yes | including sizes and row estimates |
| `pg_stat_statements` rows | strongly recommended | total time across executions, not the slowest one |
| Data volume and distribution | yes | row counts, cardinality of the filtered columns, skew |
| Baseline latency percentiles | yes | p50 / p95 / p99 before the change |

## Workflow

```text
1. RANK BY TOTAL TIME, NOT BY WORST CASE.   From pg_stat_statements, order by total_exec_time. A 40 ms
   query executed 100,000 times an hour is a bigger problem than a 6 s query executed twice a day.
   Optimising the slowest single query is the most common misallocation of effort here.

2. REPRODUCE WITH PRODUCTION-SHAPED DATA.   Row counts, cardinality and skew determine the plan. A plan
   over 1,000 rows tells you nothing about the plan over 10 million, and the planner's choice changes.

3. READ THE PLAN, NOT THE QUERY.            EXPLAIN (ANALYZE, BUFFERS) gives actual rows, actual time
   and buffer hits. Look for, in order:
     - a sequential scan on a large table with a selective predicate
     - estimated rows differing from actual rows by more than ~10× — a statistics problem, and the
       cause of most genuinely surprising plans
     - a nested loop whose inner side is large
     - a sort or hash spill to disk (Buffers: read/write, "Sort Method: external merge")
     - an index scan followed by a large heap fetch count — the index is not covering

4. FIX THE STATISTICS BEFORE THE INDEX.     If estimates are wildly wrong, ANALYZE the table and check
   whether the column needs a higher statistics target or an extended statistic on a column pair. An
   index added to compensate for bad statistics is a permanent cost fixing a temporary problem.

5. REWRITE THE QUERY IF THE SHAPE IS WRONG. Before adding anything:
     - NOT IN (subquery) with possible NULLs → NOT EXISTS
     - deep OFFSET → keyset pagination on a stable total order
     - a function or implicit cast on an indexed column → move it to the parameter side, or create a
       matching expression index
     - SELECT * on a wide table → the columns actually used
     - OR across columns with different indexability → UNION ALL of two indexed branches
     - a correlated subquery → JOIN or LATERAL

6. ADD THE NARROWEST INDEX THAT FIXES IT.   One at a time. Column order follows the predicates:
   equality columns first, then the range column, then sort columns. A range predicate ends the usable
   prefix. Consider a partial index when only a subset of rows is queried, and INCLUDE columns when an
   index-only scan is available.

7. ACCOUNT FOR THE WRITE COST.              Every index is maintained on every INSERT and on every
   UPDATE touching an indexed column. Indexing a frequently-updated column also removes heap-only-update
   eligibility. Check the table's write rate before adding the index, not after.

8. VERIFY.                                  Re-run EXPLAIN (ANALYZE, BUFFERS) and confirm the plan
   changed AND the time dropped. Re-measure the endpoint percentiles under the same workload. If the
   improvement is inside the noise floor, revert — however plausible the change seemed.

9. APPLY THE CHANGE SAFELY.                 CREATE INDEX CONCURRENTLY and DROP INDEX CONCURRENTLY in
   production; the non-concurrent forms take locks that block writes. Note that CONCURRENTLY cannot run
   inside a transaction block and leaves an INVALID index if it fails, which must be dropped and retried.

10. RECORD IT.                              The query, the plan before and after, the change, the
   measured delta and the workload conditions. Without this the next engineer repeats the investigation
   and cannot tell whether the index is still load-bearing.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Index added, planner ignores it | plan unchanged after the index exists | check the predicate shape, column order, statistics and whether the table is small enough that a seq scan is correct |
| Index helps reads, writes regress | insert/update latency rose after the change | measure the write cost; consider a partial index, or drop it and fix the query instead |
| Plan good in dev, bad in production | different row counts, cardinality or skew | reproduce with production-shaped data; never trust a dev plan |
| Statistics stale after a bulk load | estimates far below actuals | ANALYZE; consider autovacuum tuning for high-churn tables |
| CONCURRENTLY left an INVALID index | `pg_index.indisvalid = false` | drop and recreate; it is not used and still costs space and write time |
| Optimised the wrong query | total time unchanged after the fix | re-rank by total_exec_time; the worst-case query was not the expensive one |
| Fix works, then stops | plan flips after a data distribution change | pin the shape with a query rewrite rather than relying on planner luck; add a regression test with volume |
| Vacuum blocked by a long transaction | table bloat grows, xmin horizon held | set `idle_in_transaction_session_timeout`; find and kill the holder |

## Quality Checklist

```text
□ the target query was selected by total time, not by worst case
□ the baseline percentiles and the workload are recorded
□ EXPLAIN (ANALYZE, BUFFERS) was read, not just EXPLAIN
□ estimated vs actual rows were compared and a statistics problem ruled out first
□ the query shape was corrected before an index was added
□ at most one change was made at a time
□ the write cost of any new index was assessed against the table's write rate
□ the improvement is outside the noise floor, measured on the same workload
□ production changes use CONCURRENTLY, and index validity was confirmed afterwards
□ the before/after plans and the delta are recorded
```

## Anti-Patterns

```text
✗ ADDING AN INDEX ON A GUESS.        The most common form of this work and the least effective. Read
  the plan first.
✗ INDEXING EVERY FOREIGN KEY.        Some are never filtered or joined on; each is a write cost and a
  vacuum cost.
✗ OPTIMISING THE SLOWEST QUERY.      Rank by total time. A rarely-run slow query is usually not the
  problem.
✗ TESTING AGAINST AN EMPTY TABLE.    The planner's decisions are a function of the data.
✗ SELECT * EVERYWHERE.              Defeats index-only scans and pulls TOAST data unnecessarily.
✗ OFFSET PAGINATION ON A LARGE SET.  It scans and discards. Keyset pagination is not optional at scale.
✗ A WRAPPER ORM QUERY NOBODY HAS READ.  The generated SQL is what runs. Log it and read it.
✗ NON-CONCURRENT INDEX BUILDS IN PRODUCTION.  A write lock for the duration of the build is an outage.
✗ KEEPING A CHANGE INSIDE THE NOISE. Revert it. Plausibility is not evidence.
✗ NO RECORD OF WHY THE INDEX EXISTS.  It will never be removed, and nobody will know whether it still
  matters.
```

## References

- [`knowledge/databases/indexing-strategy.md`](../../knowledge/databases/indexing-strategy.md) — composite order, covering and partial indexes, retirement
- [`knowledge/databases/postgres-gotchas.md`](../../knowledge/databases/postgres-gotchas.md) — NULL semantics, MVCC, planner defeats
- [`knowledge/performance/backend-profiling.md`](../../knowledge/performance/backend-profiling.md) — measuring the layer before the query
- [`knowledge/data-engineering/vector-search.md`](../../knowledge/data-engineering/vector-search.md) — pgvector inherits Postgres vacuum and memory behaviour
- [`skills/performance-optimization/SKILL.md`](../performance-optimization/SKILL.md) · [`skills/database-design/SKILL.md`](../database-design/SKILL.md) · [`skills/debugging/SKILL.md`](../debugging/SKILL.md)
- [`workflows/performance-review/WORKFLOW.md`](../../workflows/performance-review/WORKFLOW.md)
- Using EXPLAIN — <https://www.postgresql.org/docs/current/using-explain.html> · pg_stat_statements — <https://www.postgresql.org/docs/current/pgstatstatements.html>
