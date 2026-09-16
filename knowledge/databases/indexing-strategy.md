---
id: databases-indexing-strategy
title: "Index strategy: choosing, verifying and retiring indexes"
domain: databases
summary: >-
  How to decide what to index from observed query patterns rather than guesswork, how to verify an index is used, the write-cost accounting that makes indexes expensive, and the retirement process for indexes nobody queries.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [indexes, query-planning, performance, databases, postgres, explain, write-amplification]
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
  - title: "PostgreSQL documentation — Using EXPLAIN"
    url: https://www.postgresql.org/docs/current/using-explain.html
    type: official-docs
    organization: PostgreSQL Global Development Group
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The planner behaviour this file reasons about, and the tool used to verify every claim that an index is actually chosen by the planner."
---
# Index Strategy

## The rule

**Index from observed query patterns, not from the schema.** An index justified by a column's
importance rather than by a query that filters or joins on it is a write cost with no read benefit.

```text
1. COLLECT      Turn on pg_stat_statements (or the equivalent) and slow-query logging. Get the real
                distribution: which queries run, how often, what they filter on, what they sort by.
2. RANK         Rank by total time (frequency × mean latency), not by mean latency. A 50 ms query
                run 10,000 times a minute beats a 5 s query run once a day.
3. DIAGNOSE     EXPLAIN (ANALYZE, BUFFERS) each top query. Find the sequential scan, the sort, the
                nested loop over a large set.
4. ADD ONE      Add the narrowest index that fixes the diagnosed problem. One at a time.
5. VERIFY       Re-run EXPLAIN ANALYZE. Confirm the plan changed and the time dropped. An index the
                planner declines to use is pure cost.
6. MEASURE WRITES  Check insert/update latency and table size after the change.
7. RETIRE       Periodically query pg_stat_user_indexes for idx_scan = 0 on indexes older than a
                full business cycle, and drop them.
```

## Composite index column order

The order of columns in a composite index determines which queries it can serve:

```text
INDEX (a, b, c) serves:
  WHERE a = ?                    yes
  WHERE a = ? AND b = ?          yes
  WHERE a = ? AND b = ? AND c = ? yes
  WHERE b = ?                    NO — leading column not constrained
  WHERE a = ? AND c = ?          partially — a only; c cannot be used without b

RULE   Equality columns first, then the range column, then sort columns.
       (a = ?, b > ?) wants INDEX (a, b). INDEX (b, a) will not serve it well.
```

A range predicate ends the usable prefix. `WHERE tenant_id = ? AND created_at > ? ORDER BY id`
wants `(tenant_id, created_at)` and will sort on `id` separately — or `(tenant_id, created_at, id)`
if the sort must also be served.

## Covering indexes

`INCLUDE` adds columns to the leaf without adding them to the key, enabling index-only scans:

```sql
CREATE INDEX ON orders (customer_id, created_at DESC) INCLUDE (total_cents, status);
```

Worth it when a hot query selects few columns and the visibility map is well maintained. Useless if
the table is heavily updated, because index-only scans still require visibility information and a
poorly-vacuumed table forces heap fetches anyway.

## Write-cost accounting

```text
Every index is maintained on every INSERT, and on every UPDATE that touches an indexed column.
Rough accounting before adding one:

  write-heavy table (> 30% writes)     each index costs proportionally more; prefer partial and
                                       covering indexes over broad ones
  HOT-update eligibility               an update touching no indexed column can stay on the same
                                       page; indexing a frequently-updated column removes that
  index count on a table               beyond roughly six, review the set as a whole — several
                                       narrow indexes often duplicate a well-ordered composite
  GIN on jsonb                         fast containment, materially slower writes; do not index a
                                       jsonb column that is rewritten on every update
```

## When an index will not help

```text
✗ Low-cardinality column alone.  A boolean or status column with two values across a million rows
  gives the planner nothing; a sequential scan is genuinely faster. Combine with other predicates
  or use a partial index on the rare value.
✗ Leading wildcard LIKE '%x'.  B-tree cannot. Use pg_trgm GIN or full-text search.
✗ Function applied to the column.  Index the expression, or the index is not a candidate.
✗ Implicit type coercion on the column side.
✗ A small table.  The planner will seq-scan a table that fits in a few pages regardless of indexes,
  correctly.
✗ Deep OFFSET pagination.  Indexing does not fix scanning and discarding 100,000 rows; keyset
  pagination does.
```

## Partial and expression indexes

```sql
-- only the rows that matter
CREATE UNIQUE INDEX one_active_per_user ON subscriptions (user_id) WHERE status = 'active';

-- the expression the query actually uses
CREATE INDEX lower_email ON users (lower(email));

-- a narrow index for a rare but critical lookup
CREATE INDEX failed_payments ON payments (created_at) WHERE status = 'failed';
```

Partial indexes are the highest-value-per-byte tool in Postgres: a unique constraint scoped to the
rows where uniqueness is meaningful cannot be expressed any other way.

## Retiring indexes

```sql
SELECT schemaname, relname, indexrelname, idx_scan, pg_size_pretty(pg_relation_size(indexrelid))
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;
```

`idx_scan = 0` since the last statistics reset, on an index older than a full business cycle
(including month-end and seasonal jobs), is a retirement candidate. Drop with
`DROP INDEX CONCURRENTLY` — the non-concurrent form takes an ACCESS EXCLUSIVE lock and blocks writes.

Reset the statistics before concluding, and check that unique constraints are not being relied on for
correctness rather than speed: an unused unique index is still enforcing something.

## References

- [`knowledge/databases/postgres-gotchas.md`](postgres-gotchas.md) · [`consistency-models.md`](consistency-models.md)
- [`knowledge/performance/backend-profiling.md`](../performance/backend-profiling.md) — measuring before and after
- [`skills/database-optimization/SKILL.md`](../../skills/database-optimization/SKILL.md)
- [`patterns/database/`](../../patterns/database/) · [`anti-patterns/`](../../anti-patterns/)
- PostgreSQL: Using EXPLAIN — <https://www.postgresql.org/docs/current/using-explain.html> · pg_stat_statements — <https://www.postgresql.org/docs/current/pgstatstatements.html>
