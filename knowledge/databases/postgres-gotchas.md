---
id: databases-postgres-gotchas
title: "PostgreSQL gotchas that produce silent wrong answers"
domain: databases
summary: >-
  The Postgres behaviours that differ from what developers assume — NULL semantics, MVCC and vacuum, index types that do not do what their name suggests, transaction isolation defaults, and the query patterns that defeat the planner.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [postgres, sql, null-semantics, mvcc, vacuum, indexes, isolation, query-planning, gotchas]
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
  - title: "PostgreSQL documentation"
    url: https://www.postgresql.org/docs/current/
    type: official-docs
    organization: PostgreSQL Global Development Group
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Every behaviour described here is documented; the value of this file is collecting the ones that contradict common assumptions from other databases."
---
# PostgreSQL Gotchas

These are the behaviours that produce **silently wrong answers** rather than errors. An error is
cheap; a wrong result set that looks plausible is expensive.

## NULL semantics

```text
NULL is not a value, it is the absence of one, and three-valued logic follows.

  WHERE col <> 'x'          does NOT return rows where col IS NULL. Use:
  WHERE col IS DISTINCT FROM 'x'

  NOT IN (subquery)         returns zero rows if the subquery yields any NULL — the whole
                            predicate becomes UNKNOWN. Use NOT EXISTS instead.

  COUNT(col)                counts non-NULL values. COUNT(*) counts rows. These differ.

  UNIQUE constraints        permit multiple NULLs, because NULL <> NULL. If uniqueness must hold
                            including "absent", use a sentinel or a partial unique index with
                            COALESCE.

  Aggregates over empty sets  SUM returns NULL, not 0. COUNT returns 0. Wrap SUM in COALESCE when
                            a zero matters downstream.

  ORDER BY                  NULLs sort last ascending, first descending, by default. State
                            NULLS FIRST / NULLS LAST explicitly when the order is load-bearing.
```

## MVCC, vacuum and bloat

```text
UPDATE is delete + insert.   A row updated in place does not exist; the old version stays until
                             vacuum reclaims it. High-churn tables bloat, and bloat is invisible
                             to a query that returns correct results slowly.

HOT updates                  An update that touches no indexed column and fits the same page can
                             be heap-only. Adding an index to a frequently-updated column can
                             therefore make writes materially slower — measure before indexing.

xmin horizon                 A single long-running transaction, or an abandoned replication slot,
                             holds back the xmin horizon and prevents vacuum from reclaiming
                             anything. One idle-in-transaction session can bloat an entire database.

autovacuum is not enough     For high-churn tables the default thresholds are too lax. Tune
                             per-table (autovacuum_vacuum_scale_factor) rather than globally.

Wraparound                   VACUUM FREEZE is mandatory maintenance, not optional. An unvacuumed
                             database eventually forces a shutdown to prevent wraparound.
```

## Index types and what they actually do

```text
B-tree        default; equality and range. Does NOT help LIKE '%pattern%' (leading wildcard).
              Use trigram (pg_trgm) or full-text search for that.
GIN           multi-value columns (arrays, jsonb, tsvector). Slower writes, fast containment.
              jsonb_ops vs jsonb_path_ops: the path_ops variant is smaller and faster for
              containment (@>) but cannot answer existence (?). Choose per query shape.
GiST          geometric, ranges, nearest-neighbour. Lossy — may return false positives that the
              executor rechecks.
BRIN          huge, physically-ordered append-only tables (time series). Tiny index, but useless
              if the data is not correlated with physical order.
Hash          equality only. Before Postgres 10 it was not WAL-logged; that history still shapes
              advice you will read online.

Partial index     WHERE clause on the index. A partial unique index is the correct tool for
                  "unique among active rows".
Expression index  Index the expression, not the column: CREATE INDEX ON t (lower(email)).
                  The query must use the same expression or the index is not chosen.
```

## Isolation levels

```text
Default is READ COMMITTED, which does not prevent:
  - non-repeatable reads within a transaction
  - write skew (two transactions each reading and then writing disjoint rows whose combination
    violates a constraint)

SERIALIZABLE in Postgres is true serializable snapshot isolation, implemented with predicate
locks. It aborts transactions on detected conflicts — so the application MUST retry on
serialisation_failure (SQLSTATE 40001) and deadlock (40P01). An application that does not retry
will see spurious failures under load and will be told "Postgres is unreliable".

SELECT ... FOR UPDATE is the lighter tool when the conflict is over known rows.
```

## Query patterns that defeat the planner

```text
✗ Implicit casts on an indexed column.  WHERE bigint_col = '123' can be fine;
  WHERE varchar_col = 123 cannot use the index — the cast is applied to the column.
✗ Functions on an indexed column without a matching expression index.
✗ OFFSET for deep pagination.  OFFSET 100000 scans and discards 100000 rows. Use keyset
  pagination: WHERE (created_at, id) < ($1, $2) ORDER BY created_at DESC, id DESC LIMIT 50.
✗ SELECT * on a wide table.  Defeats index-only scans and pulls TOAST data unnecessarily.
✗ Correlated subqueries where a JOIN or LATERAL would do.  Read the plan, not the shape.
✗ OR across columns with different indexability.  Often better as UNION ALL of two indexed
  branches.
✗ Assuming a count is cheap.  COUNT(*) on a large table is a full scan under MVCC because
  visibility must be checked per row. Cache it, estimate from pg_class.reltuples, or accept it.
```

## Transaction and connection gotchas

```text
An aborted transaction stays aborted.   After any error, every statement fails with
                                        "current transaction is aborted" until ROLLBACK. ORM
                                        users see this as mysterious cascading failures.
idle in transaction is a hazard, not a state.  It holds locks and the xmin horizon. Set
                                        idle_in_transaction_session_timeout.
Prepared statements and pgbouncer in transaction mode do not mix well — session-level state
                                        (SET, advisory locks, temp tables) does not survive
                                        transaction pooling.
Advisory locks are session-scoped by default and are silently released if the session dies —
                                        which is usually what you want, and occasionally not.
```

## References

- [`knowledge/databases/indexing-strategy.md`](indexing-strategy.md) · [`consistency-models.md`](consistency-models.md)
- [`knowledge/backend/idempotency.md`](../backend/idempotency.md) — retries on serialisation failures
- [`skills/database-optimization/SKILL.md`](../../skills/database-optimization/SKILL.md) · [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md)
- [`gotchas/`](../../gotchas/) — the cross-domain gotcha register
- PostgreSQL documentation — <https://www.postgresql.org/docs/current/>
