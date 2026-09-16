---
name: backend-engineering
version: 1.0.0
description: >-
  Build server-side systems that stay correct under load and failure — request lifecycle, data
  access, concurrency, idempotency, observability and the operational decisions that must be made
  before the first line of code.
category: backend
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [backend, architecture, data, concurrency, observability, reliability]
applies_to: [backend, api, infrastructure]
priority: 84
requires: [api-design, database-design]
conflicts_with: []
estimated_tokens: 2772
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Request lifecycle
    anchor: "#request-lifecycle"
    purpose: implementation
  - heading: Reliability rules
    anchor: "#reliability-rules"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "RFC 9110 — HTTP Semantics"
    url: https://www.rfc-editor.org/rfc/rfc9110
    type: specification
    organization: IETF
    published: 2022-06-01
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: Heroku
    license: MIT
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Canonical slug is heroku/12factor; 12factor/12factor redirects to an unrelated Brazilian fork."
related_skills: [api-design, database-design, security-audit, deployment, performance-audit, testing]
related_repositories: [fastapi/fastapi, django/django, tokio-rs/axum, open-telemetry/opentelemetry-specification, postmanlabs/newman]
tests: 24
---

# Backend Engineering

## Purpose

Produce server-side code whose behaviour is **predictable under concurrency, partial failure
and load**. Backend defects are rarely logic errors in the happy path; they are races, retries,
timeouts, unbounded queries and silent partial failures.

Decide the operational shape first — data model, consistency requirements, failure behaviour —
then write code that fits it. The reverse order produces systems that work in development and
misbehave in production.

## When to Use

```text
□ Designing or implementing a service, API or background processing system
□ Adding persistence, queues, caching or third-party calls to an existing service
□ Anything where a retry, a timeout or a concurrent write can occur
□ Preparing a system for real traffic rather than demo traffic
```

## When NOT to Use

```text
✗ A single-user local script with no concurrency and no network
✗ Pure API contract design — see api-design
✗ Schema and query design in depth — see database-design
```

## Inputs

```text
behaviour        what the service does, and what "correct" means when two callers disagree
consistency      what must be strongly consistent vs eventually consistent (be explicit)
load             today's and 12-month's request rate, payload sizes, fan-out
failure budget   what may fail, what must never fail, what must never happen twice
data             classification, retention, residency, deletion obligations
platform         runtime, hosting, database, queue, existing observability stack
```

## Request lifecycle

Every inbound request passes through the same stages. Implement each explicitly; missing
stages are where incidents come from.

```text
1  EDGE          TLS termination, request size limit, connection limits, WAF rules
2  IDENTIFY      authenticate (who) — reject early, before any work is done
3  AUTHORISE     permit (may this principal do this to this object) — object-level, per operation
4  VALIDATE      parse + schema-validate the body and query; reject 400/422 with an
                 actionable error; never trust types from the wire
5  CORRELATE     assign/propagate a request id and trace context; put it in every log line
6  RATE LIMIT    per principal and per endpoint; publish limits; 429 + Retry-After
7  EXECUTE       the domain operation — inside a transaction only where one is required
8  PERSIST       write with the consistency the operation actually needs (see below)
9  RESPOND       the contract's shape; no internals leaked; correct status per RFC 9110
10 RECORD        structured log (redacted), metrics, audit entry for side-effecting operations
```

Rules per stage:

```text
□ Authn and authz happen before expensive work; authorisation is re-checked on every
  ID-addressed access, not once per session
□ Validation is at the boundary, once, with a schema — not scattered `if`s in handlers
□ The transaction boundary is the smallest that preserves the invariant. Long transactions
  holding locks during network calls are a self-inflicted outage.
□ Idempotency: every mutating operation is idempotent or accepts an Idempotency-Key with
  documented scope, TTL and replay behaviour
□ Every outbound call has: connect timeout, read timeout, total deadline, bounded retries
  with exponential backoff + jitter, and a circuit breaker
□ Deadlines propagate: an upstream 2 s budget must reach the database call, not be
  re-invented per hop
□ No unbounded query: every list is paginated with a server-enforced maximum
□ No N+1: batch, join, or dataloader — and measure the query count per request
```

## Reliability rules

```text
CONCURRENCY       Assume every handler runs concurrently with itself. Shared mutable state
                  is a bug; use the database, a lock service, or single-writer queues.
                  Know your isolation level and what it does NOT prevent (write skew,
                  phantom reads). Use SELECT … FOR UPDATE, unique constraints or optimistic
                  versioning — never check-then-act without one.
IDEMPOTENCY       Retries WILL happen (clients, proxies, queues, your own backoff).
                  A payment charged twice is a defect, not an edge case.
QUEUES            At-least-once is the norm: consumers must be idempotent. Order is not
                  guaranteed unless you pay for a partitioned/ordered queue. Poison messages
                  go to a DLQ with an alert, not an infinite retry loop.
CACHING           Every cache entry has a TTL and an invalidation path. Decide up front:
                  cache-aside, read-through, or write-through. Stale reads must be tolerable
                  or the cache must not exist. Never cache authenticated responses without
                  keying on the principal.
PARTIAL FAILURE   Define it per operation: what does the user see when 1 of 5 downstream
                  calls fails? Degrade explicitly; never return success for a failed write.
BACKPRESSURE      Bound every queue, pool and buffer. Unbounded = memory exhaustion =
                  a worse outage than refusing work. Shed load deliberately with 429/503.
TIMEOUTS          A timeout must be shorter than the caller's patience, and the whole chain
                  must add up. Set the outermost deadline first and derive inward.
GRACEFUL SHUTDOWN Stop accepting, drain in-flight, close pools, exit — within the platform's
                  termination grace period.
CONFIGURATION     Environment, not code (12-factor). Secrets from a manager. Every required
                  variable validated at boot with a clear failure message.
OBSERVABILITY     Logs (structured, correlated, redacted), metrics (RED: rate, errors,
                  duration; plus saturation), traces (spans across every hop). If you cannot
                  answer "what happened to request X" from the data you emit, you cannot
                  operate it.
HEALTH            Liveness ("restart me") and readiness ("stop sending traffic") are
                  different checks. Readiness must depend on real dependencies; liveness
                  must not, or an outage cascades into a restart storm.
DATA INTEGRITY    Constraints in the database, not only in application code: NOT NULL,
                  UNIQUE, FK, CHECK. The application will have bugs; the schema is the last line.
```

## Failure Modes

```text
CHECK-THEN-ACT RACE       Two concurrent requests both pass the uniqueness check.
                          Fix: a unique constraint and handle the violation.
UNBOUNDED FAN-OUT         One request triggers 500 downstream calls. Fix: batch and bound.
RETRY STORM               Every layer retries; a small outage becomes a 10× load event.
                          Fix: retry budget, jitter, circuit breaking, retry only idempotent ops.
TIMEOUT LADDER INVERSION  Inner timeout longer than outer → work continues after the client left.
SILENT PARTIAL FAILURE    200 returned though a downstream write failed.
LOG STARVATION            No request id; debugging is archaeology.
SECRET IN LOGS            Tokens and PII in structured logs, shipped to a third party.
HEALTH CHECK LYING        Readiness 200 while the database is unreachable.
LONG-LOCKED TRANSACTION   A network call inside a transaction holding row locks.
CONFIG DRIFT              Behaviour differs per environment because config is not validated at boot.
QUEUE POISON LOOP         One bad message retried forever, blocking the partition.
```

## Quality Checklist

```text
□ Consistency requirements stated per operation before implementation
□ Request lifecycle stages all present: authn, authz, validate, correlate, limit, execute, respond, record
□ Transaction boundary minimal; no network calls inside a transaction
□ Every mutating operation idempotent or Idempotency-Key aware
□ Timeouts, deadlines, bounded retries with jitter and circuit breakers on every outbound call
□ Deadline propagation across the whole call chain
□ Every list paginated with a server-enforced maximum; no N+1 (query count measured)
□ Uniqueness and integrity enforced by database constraints, not only in code
□ Queues: idempotent consumers, DLQ + alert, bounded concurrency, no poison loop
□ Caches: TTL, invalidation path, principal-keyed where authenticated, stale-read tolerance stated
□ Partial-failure behaviour defined per operation; never success on a failed write
□ Backpressure and load shedding configured; all buffers bounded
□ Graceful shutdown drains in-flight work within the platform grace period
□ Configuration validated at boot; secrets from a manager; no secret in logs
□ Structured correlated logs, RED + saturation metrics, traces across every hop
□ Distinct liveness and readiness checks; readiness depends on real dependencies
□ Load test run at ≥2× expected peak with an injected dependency failure
```

## Anti-Patterns

```text
✗ `if not exists: insert` with no unique constraint
✗ Retrying a non-idempotent POST on timeout
✗ A 30 s database timeout behind a 2 s client timeout
✗ `SELECT *` on a table with a TEXT column, unpaginated, in a loop
✗ Returning 200 with a partially-applied batch
✗ An unbounded in-memory queue "just for now"
✗ Logging the full request body on an auth endpoint
✗ A liveness probe that queries the database
✗ Business rules enforced only in the frontend
```

## References

- [`api-design`](../api-design/SKILL.md) · [`database-design`](../database-design/SKILL.md)
- [`security-audit`](../security-audit/SKILL.md) · [`performance-audit`](../performance-audit/SKILL.md)
- [`deployment`](../deployment/SKILL.md) · [`patterns/backend/`](../../patterns/backend/)
- [`knowledge/backend/`](../../knowledge/backend/) · [`anti-patterns/backend/`](../../anti-patterns/backend/)
- RFC 9110 — <https://www.rfc-editor.org/rfc/rfc9110> · Twelve-Factor — <https://github.com/heroku/12factor>

## Related Skills

`api-design` · `database-design` · `security-audit` · `performance-audit` · `deployment` ·
`testing` · `debugging`

## Evaluation Criteria

```text
1. Correctness under concurrency: 0 race conditions in a parallel load test.
2. Failure behaviour: injected dependency failures produce the defined degradation, never
   a false success.
3. Idempotency: replaying any mutating request produces no duplicate effect.
4. Boundedness: no unbounded query, buffer or retry chain (verified by load test).
5. Operability: any request traceable end-to-end from the emitted telemetry.
6. Error rate and p99 latency at 2× expected peak, within budget.
```

Test cases in [`tests/`](tests/).
