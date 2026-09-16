---
id: databases-consistency-models
title: "Consistency models and transaction isolation, from the database seat"
domain: databases
summary: >-
  What each SQL isolation level actually prevents in a real engine, where write skew appears, how SERIALIZABLE differs from snapshot isolation, and the retry obligations an application takes on when it chooses the strongest level.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [isolation, mvcc, serializable, write-skew, transactions, consistency, databases]
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
  - title: "A Critique of ANSI SQL Isolation Levels"
    url: https://www.microsoft.com/en-us/research/publication/a-critique-of-ansi-sql-isolation-levels/
    type: research-paper
    organization: Microsoft Research
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Berenson et al., 1995 — the paper showing the ANSI definitions are phrased in terms of phenomena rather than mechanisms and therefore admit multiple interpretations, which is why engines differ at the same named level."
---
# Consistency Models (database view)

## Why the names mislead

The SQL standard defines isolation levels by the **phenomena they prevent**, and Berenson et al.
(1995) showed those definitions are ambiguous — the same name admits different implementations.
So "REPEATABLE READ" in PostgreSQL and in MySQL are not the same guarantee, and reading the name as
a specification is the root of most isolation bugs.

```text
READ UNCOMMITTED   permits dirty reads (reading data another transaction has not committed).
                   Postgres implements it as READ COMMITTED — dirty reads are not actually
                   possible. Choosing it buys nothing and misleads readers of your code.
READ COMMITTED     default almost everywhere. Prevents dirty reads. Permits non-repeatable reads
                   and phantom reads. Each statement sees a fresh snapshot.
REPEATABLE READ    prevents non-repeatable reads. In Postgres this is snapshot isolation, which
                   is still vulnerable to WRITE SKEW. In MySQL/InnoDB it uses gap locks and
                   behaves differently again.
SERIALIZABLE       prevents all three phenomena plus write skew — if it is actually serializable.
                   Postgres implements SSI (serializable snapshot isolation) with predicate locks.
```

## Write skew

The anomaly that survives snapshot isolation, and the one engineers most often discover in
production:

```text
Constraint: at least one doctor must be on call.
Two doctors, Alice and Bob, are both on call. Both request leave simultaneously.

  T1 (Alice): reads on_call_count = 2 → 2 - 1 = 1 ≥ 1 → OK, sets alice.on_call = false
  T2 (Bob):   reads on_call_count = 2 → 2 - 1 = 1 ≥ 1 → OK, sets bob.on_call = false
  Both commit. Neither wrote a row the other wrote. on_call_count = 0. Constraint violated.
```

Each transaction read a consistent snapshot and wrote disjoint rows, so no write conflict exists to
detect. Under READ COMMITTED and under snapshot-isolation REPEATABLE READ, both commit.

Three fixes, in order of preference:

```text
1. EXPRESS IT AS A CONSTRAINT the database can enforce — a deferred constraint, a unique index on
   a computed column, a CHECK on a materialised aggregate. Correctness that lives in the database
   cannot be bypassed by a second code path.
2. SELECT ... FOR UPDATE the rows the decision depends on. Both transactions now contend on the
   same rows and one blocks. Explicit, and it costs concurrency.
3. Use SERIALIZABLE and retry on failure. Broadest protection, and it moves the burden to the
   application: serialisation failures are expected, not exceptional.
```

## The retry obligation

Choosing SERIALIZABLE in Postgres means accepting aborts:

```text
SQLSTATE 40001  serialization_failure   → retry the whole transaction
SQLSTATE 40P01  deadlock_detected       → retry the whole transaction

RULES   The retry must re-execute the transaction from the beginning, not resume it.
        Bound the retries (3-5) and back off with jitter, otherwise a contention storm becomes a
        retry storm.
        Make the transaction idempotent or the retry can double-apply a side effect — see
        knowledge/backend/idempotency.md.
        An application that does not retry will surface these as user-visible errors under load and
        be diagnosed as "the database is flaky". It is not; the contract was not implemented.
```

## CAP and PACELC, correctly

```text
CAP        Under a network Partition, choose Consistency or Availability. It says nothing about
           normal operation, which is why it is a poor everyday design tool.
PACELC     else (no partition): choose Latency or Consistency. This is the tradeoff you actually
           make most days.

A single-node Postgres is not "CP" in the CAP sense — it has no partition to survive. A replicated
cluster with synchronous replication and automatic failover is making a PACELC latency choice on
every write.
```

## Practical selection

```text
Most CRUD work                    READ COMMITTED + explicit row locks where a decision spans rows.
                                  Understandable, fast, and the failure modes are visible.
Money, inventory, scheduling      SERIALIZABLE with retries, or an enforced constraint. Write skew
                                  in these domains is a real loss, not a curiosity.
Read-heavy reporting              READ COMMITTED on a replica, or REPEATABLE READ for a consistent
                                  snapshot across a long report.
Long-running transactions         Avoid. They hold the xmin horizon, block vacuum and bloat the
                                  database. Batch instead.
```

## References

- [`knowledge/backend/consistency-models.md`](../backend/consistency-models.md) — the distributed-systems view
- [`knowledge/backend/idempotency.md`](../backend/idempotency.md) — required for safe retries
- [`knowledge/databases/postgres-gotchas.md`](postgres-gotchas.md) · [`indexing-strategy.md`](indexing-strategy.md)
- [`skills/database-optimization/SKILL.md`](../../skills/database-optimization/SKILL.md) · [`skills/architecture-design/SKILL.md`](../../skills/architecture-design/SKILL.md)
- Berenson et al., "A Critique of ANSI SQL Isolation Levels" (1995) · Cahill, "Serializable Isolation for Snapshot Databases" (2008) · PostgreSQL: Transaction Isolation — <https://www.postgresql.org/docs/current/transaction-iso.html>
