---
id: backend-consistency-models
title: "Consistency models in distributed systems: the practical ladder"
domain: backend
summary: >-
  The consistency spectrum from strong to eventual, what each level costs in latency and availability, the specific bugs each one admits, and how to choose per data type rather than per system.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [consistency, distributed-systems, cap, pacelc, replication, eventual-consistency, linearizability]
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
    note: "Establishes that isolation-level names admit multiple implementations — the same ambiguity that makes consistency vocabulary unreliable across systems."
---
# Consistency Models (distributed-systems view)

## The ladder

From strongest to weakest, with the cost each level pays:

```text
LINEARIZABLE      Every operation appears to take effect atomically at some point between its
                  invocation and its response; all clients agree on the order. Cost: coordination
                  on every write, a quorum on every read, and unavailability during partition.
SEQUENTIAL        A single total order all clients agree on, but not necessarily respecting real
                  time. Weaker than linearizable; cheaper because it does not need to track
                  invocation time.
CAUSAL            Operations respect happens-before. Concurrent writes may be ordered differently
                  by different clients, but a write that follows a read is always after it. The
                  sweet spot for many collaborative systems: it rules out the anomalies users
                  actually notice.
READ-YOUR-WRITES  A client always sees its own writes. Often implemented with session affinity or
                  a per-session read marker, and much cheaper than full linearizability.
MONOTONIC READS   A client never sees older data after newer data. Prevents the "the page went
                  backwards" bug without global coordination.
EVENTUAL          Absent further writes, all replicas converge. Says nothing about when, and
                  nothing about what a reader sees meanwhile. Cheapest, most available, and the
                  source of the largest category of user-visible bugs.
```

## What each level admits

The bugs are the specification. Choose by asking which of these you can tolerate:

```text
EVENTUAL          lost updates (concurrent writes, last-writer-wins, one user's work disappears)
                  read-your-writes violations (you post a comment and cannot see it)
                  monotonic-read violations (a list shrinks then grows on refresh)
                  stale aggregates (a balance, a counter or a cart total that is wrong for a window)

CAUSAL            concurrent-write divergence, resolved by a CRDT or a merge policy you must design
                  but never the "I can't see what I just did" class

LINEARIZABLE      nothing of the above; pays in latency and in availability during partition
```

**Lost updates are the expensive one.** They are silent, they destroy user work, and they surface
as support tickets rather than errors. Any data a human edits concurrently needs at least causal
consistency or an explicit conflict-resolution strategy.

## CAP and PACELC

```text
CAP        During a network Partition, choose Consistency or Availability. It is a statement about
           failure, not about normal operation, which is why it is a poor everyday design tool.
PACELC     else (no partition), choose Latency or Consistency. This is the tradeoff made on every
           write in a healthy system, and it is the one worth reasoning about.

A system is not "CP" or "AP" globally. Each data type makes its own choice, and the interesting
engineering is in noticing that they differ.
```

## Choosing per data type

```text
STRONG (linearizable or a serializable transaction)
  money movement · inventory decrements · unique-identity assignment · access-control decisions ·
  anything where two people acting at once must not both succeed

CAUSAL / SESSION
  user-generated content a user expects to see immediately · collaborative editing (with a CRDT or
  an operational-transform layer) · shopping carts · follow/like graphs

EVENTUAL (deliberately, with a stated staleness budget)
  search indexes · recommendation features · analytics and reporting · notification fan-out ·
  cache layers · derived views and materialised aggregates
```

The pattern that makes eventual consistency safe: **state the staleness budget explicitly** ("search
reflects writes within ~5 s; the authoritative view is the record page") and make the authoritative
view reachable. Most "the data is inconsistent" complaints are not consistency failures — they are
missing statements of where the truth lives.

## Conflict resolution

Where concurrent writes are permitted, the merge policy is a design decision, not an implementation
detail:

```text
LAST-WRITER-WINS   simple, destroys work. Requires a trustworthy clock — a logical clock (Lamport
                   or hybrid logical) rather than wall time, because wall clocks across machines
                   are wrong by more than the interval between writes.
MULTI-VALUE        return all concurrent versions and let the application or the user merge.
                   Honest, and it moves complexity to the reader.
CRDT               merge automatically and commutatively. Correct for counters, sets, registers and
                   text; expensive for anything with an invariant across fields.
DOMAIN MERGE       a hand-written merge for the specific type — a cart unions its lines, a profile
                   merges per field. Usually the right answer, and the one nobody writes down.
```

## Anti-patterns

```text
✗ "Eventual consistency everywhere, it's more scalable."  The scalability is real; the bug surface
  is larger than the gain for money, inventory and identity.
✗ Reading from a replica and writing to the primary without a session guarantee.  The immediate
  read-after-write failure is the most-reported consistency bug in production systems.
✗ Wall-clock timestamps as the conflict arbiter.  Clock skew across machines exceeds the write
  interval; use a logical clock.
✗ Treating a cache as a consistency layer.  Invalidation is a correctness problem, not a
  performance one.
✗ Choosing a level without writing it down.  If the staleness budget is not stated, every consumer
  assumes strong consistency and files bugs against the assumption.
```

## References

- [`knowledge/databases/consistency-models.md`](../databases/consistency-models.md) — the single-engine view: isolation levels and write skew
- [`knowledge/backend/idempotency.md`](idempotency.md) — required for safe retries at every level
- [`knowledge/architecture/system-design-checklist.md`](../architecture/system-design-checklist.md)
- [`skills/architecture-design/SKILL.md`](../../skills/architecture-design/SKILL.md) · [`skills/api-design/SKILL.md`](../../skills/api-design/SKILL.md)
- Brewer, "CAP Twelve Years Later" (2012) · Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design" (PACELC, 2012) · Kleppmann, *Designing Data-Intensive Applications*
