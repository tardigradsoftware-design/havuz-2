---
name: database-design
version: 1.0.0
description: >-
  Model data so integrity is enforced by the database, queries stay fast as volume grows, and
  migrations are reversible — including the choice between relational, document and vector storage.
category: backend
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [database, schema, sql, postgres, indexing, migrations, modelling, vector]
applies_to: [backend, database]
priority: 84
requires: []
conflicts_with: []
estimated_tokens: 2895
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Modelling rules
    anchor: "#modelling-rules"
    purpose: implementation
  - heading: Indexing and query performance
    anchor: "#indexing-and-query-performance"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "PostgreSQL documentation"
    url: https://www.postgresql.org/docs/
    type: official-docs
    organization: PostgreSQL Global Development Group
    license: PostgreSQL License
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Verify behaviour against the major version in use — defaults and features differ across versions."
related_skills: [backend-engineering, api-design, migration, security-audit, performance-audit]
related_repositories: [postgres/postgres, supabase/supabase, prisma/prisma, pgvector/pgvector]
tests: 4
---

# Database Design

## Purpose

Design a schema where **the database prevents the bad state**, queries are fast at the volume
you will actually reach, and changes can be applied and rolled back without downtime.

The most expensive mistake is not a slow query — it is a schema that cannot express a
constraint, so the constraint lives in application code, where it is eventually bypassed.

## When to Use

```text
□ Designing or reviewing a schema before the first migration
□ Adding a table/column/relationship to an existing system
□ A query that was fine at 10k rows and is not at 10M
□ Choosing between relational, document, key-value, search or vector storage
□ Planning a migration on a live system
```

## When NOT to Use

```text
✗ A local cache or scratch file — use the simplest store that works
✗ Tuning a query whose real problem is an N+1 in application code
```

## Modelling rules

```text
IDENTIFIERS     Opaque, non-sequential, non-meaningful. UUIDv7 or ULID where ordering helps;
                bigserial only if you accept enumeration and hot-index-page contention.
                Never encode meaning into an ID you will be stuck with ("USR_ADMIN_01").
                Expose IDs as opaque strings at the API boundary even when they are numeric.
TYPES           Use the domain type the engine provides: timestamptz (never timestamp without
                time zone), numeric/integer minor units for money (never float), enum or a
                lookup table for closed sets, jsonb only for genuinely schema-less data.
CONSTRAINTS     NOT NULL by default; add NULL deliberately with a reason.
                UNIQUE on anything that must be unique — the application check is not enough.
                FOREIGN KEY on every relationship, with an explicit ON DELETE behaviour
                (RESTRICT is the safe default; CASCADE deletes more than you expect).
                CHECK for domain rules: positive quantities, valid ranges, state transitions.
                Exclusion constraints for "no overlapping bookings".
                Every constraint you skip is a bug you have scheduled.
NORMALISATION   Normalise to 3NF for transactional data. Denormalise deliberately, for a
                named read pattern, with the update path documented and enforced
                (trigger, generated column, or a single writer).
                Denormalising first and regretting it later is the common failure.
NAMING          Consistent, plural or singular but never both; snake_case;
                explicit FK names (`order_items_order_id_fkey`); no reserved words;
                no abbreviations nobody can expand. A rename later is a migration.
TEMPORAL        created_at / updated_at on everything, timestamptz, server-defaulted.
                Soft delete only if a real requirement (audit, undo) — otherwise it poisons
                every query with `WHERE deleted_at IS NULL`. Use a separate history table.
                For "state as of a date", model validity ranges, not mutation in place.
MULTI-TENANCY   Decide once: separate database, separate schema, or shared table with
                tenant_id + row-level security. Shared table without RLS is the most common
                data-leak source in B2B systems.
ENUMS           Prefer a lookup table or a CHECK constraint over a native enum type when the
                set will grow — native enum changes can require locks and cannot be rolled back
                cleanly on some engines.
JSONB           Fine for sparse, unqueried, per-row-variable data. Wrong for anything you
                filter, join, aggregate or constrain heavily — then it is a table you avoided.
```

## Indexing and query performance

```text
START FROM THE QUERIES   List the real read patterns with their expected selectivity and
                         volume. Indexes serve queries; a schema without a query list is guesswork.
B-TREE COMPOSITE ORDER   Equality columns first, then range, then sort. (a, b) does not
                         serve `WHERE b = ?`. Leftmost-prefix rule; design for the actual predicates.
COVERING INDEXES         Include the selected columns to avoid heap lookups on hot paths.
PARTIAL INDEXES          Index only the rows you query (`WHERE status = 'open'`) — smaller, faster.
EXPRESSION INDEXES       Index the expression you filter on (`lower(email)`), or the filter cannot use it.
UNIQUE INDEXES           A uniqueness rule is an index. Declare the constraint, get both.
DO NOT OVER-INDEX        Every index slows every write and costs storage. Measure; do not collect.
ANALYSE THE PLAN         EXPLAIN (ANALYZE, BUFFERS) on realistic data volume. A plan on 100 rows
                         tells you nothing about 10M.
WATCH FOR                sequential scans on large tables · nested loops over big sets ·
                         sorts and hash spills to disk · index scans returning most of the table ·
                         functions on indexed columns in WHERE (kills index use) ·
                         implicit casts between types · `OR` across unrelated columns ·
                         `LIKE '%x'` (needs trigram/full-text search instead)
N+1                      Count queries per request. Batch, join, or use a dataloader.
PAGINATION               Keyset/cursor (`WHERE (created_at, id) < (?, ?)`) over OFFSET —
                         OFFSET degrades linearly with depth and skips/duplicates under writes.
LOCKS                    Know the isolation level and what it does not prevent. Short transactions.
                         No network calls inside a transaction. `SELECT … FOR UPDATE` only where needed.
VACUUM/STATS             Autovacuum tuning and fresh statistics matter more than most query tricks.
PARTITIONING             For time-series or very large tables, partition by the range you always
                         filter on — and ensure every query includes the partition key.
VECTOR SEARCH            Embeddings are an index type, not a data model. Store the source of truth
                         relationally; add a vector column/index for similarity. Choose the index
                         (HNSW vs IVFFlat) by recall/latency/memory tradeoff, measured on your data.
                         Always pair similarity search with metadata filters and re-ranking.
```

## Migrations

```text
□ Every migration is reversible, or explicitly marked irreversible with the reason
□ Schema and data changes are separate migrations
□ Expand → migrate → contract for anything touching a live column:
    add the new column (nullable) → dual-write → backfill → switch reads → drop the old
□ No long lock in a migration: adding a NOT NULL with a default, or an index, can lock a
  large table — use the online/concurrent variant your engine provides
□ Backfills are batched and resumable, with progress logged and a bounded transaction size
□ Migrations run in CI against a copy of the production-shaped schema
□ The migration tool and its state table are versioned with the application
□ A rollback is rehearsed, not assumed
□ Downtime requirements stated explicitly; "zero downtime" is a claim that needs a plan
```

## Failure Modes

```text
CONSTRAINT-FREE SCHEMA    Integrity lives in application code and is bypassed by the second writer.
FLOAT MONEY               Rounding errors in financial data. Never.
TIMESTAMP WITHOUT TZ      Ambiguous instants across DST and deployments.
MISSING FK                Orphan rows discovered during a report, months later.
INDEX GUESSWORK           Indexes added for hypothetical queries; the real query still scans.
PLAN ON TINY DATA         Performance verified on a development database of 500 rows.
OFFSET PAGINATION         Multi-second deep pages and duplicate rows under concurrent writes.
LONG-RUNNING TRANSACTION  Locks held across an HTTP call; the whole table stalls.
SOFT DELETE EVERYWHERE    Every query needs a filter somebody will forget once.
IRREVERSIBLE MIGRATION    No way back after a failed deploy.
SHARED-TABLE TENANCY      No RLS; one missing WHERE clause leaks a customer's data.
JSONB AS A SCHEMA         Unqueryable, unconstrainable, undocumented data at the core.
```

## Quality Checklist

```text
□ Read patterns listed with selectivity and expected volume before indexing
□ Opaque, non-meaningful identifiers; correct domain types (timestamptz, integer money)
□ NOT NULL by default; UNIQUE, FK and CHECK constraints on every real rule
□ Explicit ON DELETE behaviour per relationship
□ Normalised for writes; denormalisation deliberate, named and maintained
□ Multi-tenancy strategy chosen, with RLS or equivalent enforcement
□ Consistent naming; FK and index names explicit
□ Indexes derived from the query list: composite order, partial, covering where hot
□ EXPLAIN ANALYZE run on production-scale data for every hot query
□ Query count per request measured; no N+1
□ Keyset pagination, not OFFSET, on mutable large tables
□ Transactions short; no network calls inside them; isolation level understood
□ Migrations reversible, expand-migrate-contract, no long locks, batched backfills
□ Migrations tested in CI; rollback rehearsed
□ Soft delete only where required; history modelled explicitly where time travel is needed
□ Vector search built on a relational source of truth with filters and re-ranking
```

## Anti-Patterns

```text
✗ `price FLOAT`
✗ `created_at TIMESTAMP` with no time zone
✗ A uniqueness rule enforced only by `SELECT … then INSERT`
✗ `ORDER BY created_at LIMIT 50 OFFSET 100000`
✗ An HTTP call inside `BEGIN … COMMIT`
✗ `tenant_id` in the table but no row-level security
✗ Adding an index because a query felt slow, without reading the plan
✗ A migration that drops a column in the same release that stops writing it
✗ Storing the whole domain model in one JSONB column
```

## References

- [`backend-engineering`](../backend-engineering/SKILL.md) · [`migration`](../migration/SKILL.md)
- [`api-design`](../api-design/SKILL.md) · [`performance-audit`](../performance-audit/SKILL.md)
- [`patterns/database/`](../../patterns/database/) · [`knowledge/databases/`](../../knowledge/databases/)
- [`datasets/`](../../datasets/)
- PostgreSQL documentation — <https://www.postgresql.org/docs/> (verify against your major version)

## Related Skills

`backend-engineering` · `api-design` · `migration` · `performance-audit` · `security-audit`

## Evaluation Criteria

```text
1. Constraint coverage: every stated business invariant enforced in the schema (target 100%).
2. Query performance: hot queries within latency budget on production-scale data, verified
   by EXPLAIN ANALYZE.
3. Write amplification: index count justified by measured read benefit.
4. Migration safety: 100% reversible or explicitly justified; zero long-lock migrations.
5. Leak resistance: no cross-tenant read possible with a missing filter (RLS enforced).
6. Integrity incidents: 0 orphan/constraint-violating rows discovered in production.
```

Test cases in [`tests/`](tests/).
