---
id: backend-idempotency
title: "Idempotency: making retries safe"
domain: backend
summary: >-
  Why at-least-once delivery makes idempotency mandatory rather than optional, the four implementation patterns ranked by strength, the key-generation rules that determine whether they work, and the failure modes that appear only under retry storms.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [idempotency, retries, at-least-once, distributed-systems, payments, messaging, api-design]
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
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: Heroku
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Backing services as attached resources and disposability of processes are what make at-least-once delivery — and therefore idempotency — unavoidable in practice."
---
# Idempotency

## Why it is mandatory

Every delivery mechanism you will actually use is **at-least-once**: message queues redeliver on
acknowledgement timeout, HTTP clients retry on network error, load balancers retry on connection
reset, cron jobs overlap when a run exceeds its interval, and database transactions retry on
serialisation failure. Exactly-once delivery is a property of the *effect*, achieved by making the
operation idempotent — not a transport feature you can enable.

```text
If a handler can be invoked twice for one logical request, and invoking it twice has a different
effect than invoking it once, the system is incorrect. Not fragile — incorrect.
```

## The four patterns, ranked

```text
1. NATURALLY IDEMPOTENT (strongest)
   The operation is a write of absolute state, not a delta.
     SET balance = 100        idempotent — the second write is a no-op
     SET balance = balance - 5 NOT idempotent — the second write deducts again
   Prefer absolute state over deltas wherever the domain allows. This removes the mechanism
   entirely, which is better than any bookkeeping.

2. UNIQUE CONSTRAINT ON AN IDEMPOTENCY KEY (strong, and the standard for money)
   A unique index on (idempotency_key) or (customer_id, order_id, line) makes the second insert
   fail at the database. Catch the unique violation and return the original result.
   Correctness lives where it cannot be bypassed by a second code path.

3. DEDUPLICATION TABLE / PROCESSED-MESSAGE LOG (strong, general)
   Record the key before doing the work, in the same transaction as the effect. On a repeat, look
   up and return the stored result. This is what makes the response idempotent, not just the
   side effect — the client sees the same answer both times.

4. STATE-MACHINE TRANSITION GUARD (adequate)
   Only permit a transition from a specific prior state: UPDATE orders SET status = 'shipped'
   WHERE id = ? AND status = 'paid'. Check the affected-row count; zero means someone else got
   there first. Weaker than 2 or 3 because it protects the transition, not the response.

✗ OPTIMISTIC LOCKING ALONE.  A version check prevents a lost update; it does not prevent a
  duplicated side effect that has already been dispatched (an email sent, a webhook fired, a
  payment authorised).
```

## Key generation

The key determines whether any of this works. Rules:

```text
FROM THE CLIENT for user-initiated operations.  The client generates a UUID per logical intent and
                sends it on every retry. This is the only way to distinguish "the user pressed pay
                twice" from "the network retried the same press" — the server cannot tell them apart.
FROM THE PRODUCER for events.  A stable event ID assigned once at emission, not regenerated on
                redelivery. A redelivery that carries a new ID is indistinguishable from a new
                event, and no deduplication scheme survives that.
DERIVED from the domain for natural keys.  (tenant, invoice_number) is better than a UUID because
                it is idempotent by construction and survives client bugs.
NEVER from mutable inputs.  A timestamp, a request hash including a nonce, or an auto-increment
                value changes between retries and defeats the mechanism silently.
```

Scope the key: globally unique is simplest; per-tenant or per-customer uniqueness allows smaller
indexes but requires the scope to be part of every lookup, and a missing scope is a collision.

## The response problem

Idempotency is usually implemented as "don't do the work twice" and then fails at "return the same
answer twice":

```text
FIRST CALL    performs the work, stores the result, returns 201 with the created resource
RETRY         must return the SAME 201 and the same body — not 200 "already processed", not 409,
              not an empty success

Store the response (status, headers that matter, body) with the key, and replay it. A client that
receives 409 on a retry of its own successful request will treat the operation as failed and will
often compensate — which is how a duplicate charge becomes a duplicate charge plus a refund.
```

## Failure modes

```text
TTL EXPIRES WHILE A RETRY IS PENDING    The dedup record is garbage-collected after 24 h; a queue
                                        with a long retry backoff redelivers on day 3. Size the TTL
                                        to the maximum retry window plus margin, not to a round
                                        number.
CRASH BETWEEN EFFECT AND RECORD         The side effect completes and the dedup row is not written.
                                        Write both in the same transaction, or use the transactional
                                        outbox pattern so the effect and the record commit together.
NON-TRANSACTIONAL SIDE EFFECTS          An email, an SMS, a webhook and a card charge cannot be
                                        rolled back. Order them: durable state first, external
                                        effect last, and make the external effect itself carry an
                                        idempotency key the provider honours.
RETRY STORM WITHOUT BACKOFF             A failing dependency plus immediate retries amplifies load
                                        exactly when the dependency is weakest. Exponential backoff
                                        with jitter, and a circuit breaker.
CONCURRENT DUPLICATES                   Two retries in flight simultaneously, neither sees the
                                        other's record yet. The unique constraint (pattern 2) handles
                                        this; a check-then-insert does not. Use INSERT ... ON
                                        CONFLICT or catch the violation — never SELECT then INSERT.
IDEMPOTENT HANDLER, NON-IDEMPOTENT CHAIN  Handler A is idempotent and calls B, which is not. The
                                        property does not compose. Every handler in the chain needs
                                        it.
```

## Testing it

```text
□ invoke the operation twice with the same key; assert one effect and identical responses
□ invoke concurrently with the same key; assert one effect (this is the test that catches
  check-then-insert)
□ invoke with a different key; assert two effects
□ kill the process between the effect and the record; assert the retry produces one effect
□ expire the dedup record; assert the behaviour is still correct or explicitly fails safe
□ redeliver a queue message with its original event ID; assert deduplication
```

## References

- [`knowledge/databases/consistency-models.md`](../databases/consistency-models.md) — serialisation-failure retries require this
- [`knowledge/backend/consistency-models.md`](consistency-models.md) — the distributed-systems frame
- [`knowledge/databases/postgres-gotchas.md`](../databases/postgres-gotchas.md) — aborted-transaction behaviour on retry
- [`patterns/backend/`](../../patterns/backend/) · [`anti-patterns/`](../../anti-patterns/) · [`failure-modes/`](../../failure-modes/)
- [`skills/api-design/SKILL.md`](../../skills/api-design/SKILL.md) · [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md)
