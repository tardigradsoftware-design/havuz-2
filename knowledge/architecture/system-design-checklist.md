---
id: architecture-system-design-checklist
title: "System design checklist: the decisions that must be made explicitly"
domain: architecture
summary: >-
  The ordered set of design decisions a system review must be able to answer — requirements as numbers, data model, consistency, failure modes, scaling, observability, security, configuration, evolution and the agent-system additions — with the omission behind each question.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [architecture, system-design, review, checklist, scalability, failure-modes, data-model, evolution]
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
    note: "Config in the environment, backing services as attached resources, strict dev/prod parity and disposability are four of the checklist sections below, and among the most commonly violated."
---
# System Design Checklist

A design is not reviewed by asking whether it works. It is reviewed by asking whether the decisions
that determine how it fails, scales and changes were made explicitly — or defaulted into.

Every question below corresponds to a real class of incident. The order matters, because later
answers depend on earlier ones.

## 1. Requirements, stated as numbers

```text
□ Read:write ratio, per day and at peak
□ Expected volume now, in 12 months, and at the stated business goal
□ Latency budget — and is it p50, p95 or p99? "Under 200 ms" is not a budget.
□ Availability target, and the cost of downtime per hour
□ Data volume now and at 12 months, including growth rate
□ Which of these are hard requirements and which are aspirations? A design cannot optimise for all.
```

Omission behind the question: designs built against adjectives ("fast", "scalable", "reliable") that
cannot be tested, budgeted or argued with.

## 2. Data model

```text
□ Entities, their identities, and who owns each
□ Consistency requirement PER DATA TYPE, not per system — money, inventory and identity usually need
  strong; search, analytics and derived views usually do not
□ Where the authoritative copy of each datum lives, and how a derived copy is invalidated
□ Access pattern per entity: by ID, foreign key, range, full-text, similarity. Indexes and stores
  follow access patterns, not the schema.
□ Retention policy; deleted versus anonymised
□ How the schema migrates, and what happens to in-flight requests during a migration
□ Largest single row / document / partition, and whether there is a hard limit above it
```

Omission: a schema designed from the domain diagram rather than the query list — indexes nobody uses,
queries nobody can serve.

## 3. Consistency and transactions

```text
□ Which operations must be atomic, and at what isolation level
□ Where write skew becomes possible, and how it is prevented — a constraint, a row lock, or
  serializable isolation with retries
□ Are retries implemented for serialisation failure and deadlock (SQLSTATE 40001 / 40P01), and is the
  retried operation idempotent
□ Transaction boundaries — does any transaction include an external call? Holding a lock across a
  network call is an outage waiting for a slow dependency.
□ Where eventual consistency is chosen, and whether the staleness budget is written down and
  reachable by the consumer
```

See [`../databases/consistency-models.md`](../databases/consistency-models.md) and
[`../backend/idempotency.md`](../backend/idempotency.md).

## 4. Failure modes

```text
□ For every dependency: slow, erroring, partial data, unreachable. Four cases, not one.
□ Timeouts on every outbound call — connect, read, total. "Default" is not an answer; most defaults
  exceed the caller's own budget.
□ Retry with exponential backoff and jitter, and a retry BUDGET. Retries without a budget convert one
  failure into a stampede.
□ Circuit breaker, and what the caller does while it is open
□ What degrades gracefully and what fails hard — name them. "Everything degrades gracefully" is false
  and will be discovered during the incident.
□ Partial success: the write committed but the notification did not send
□ Recovery procedure — rehearsed, not merely written
□ Blast radius of one bad request, one bad deploy, one compromised credential
```

Omission: failure handling designed for the error case only, so slow dependencies — more common and
harder to detect — cascade.

## 5. Scaling

```text
□ The current bottleneck, measured rather than assumed
□ Which axis scales first: compute, connections, storage IOPS, network, memory, or a third-party rate
  limit. Usually not the one the architecture diagram implies.
□ What is stateless and what is not — anything stateful is a scaling constraint and a failover problem
□ Single points of failure, including organisational ones: one maintainer, one region, one vendor
□ Connection pool size against every shared resource, and whether the sum across instances exceeds the
  resource's limit. A pool of 20 across 50 replicas against max_connections=100 is an outage at scale.
□ What breaks first at 10× traffic, and the plan
□ Backpressure, or does load accumulate until the process dies
```

## 6. Observability

```text
□ The four golden signals for this service — latency, traffic, errors, saturation — and where each is
  measured
□ A trace that follows one request across every service and external call
□ What a log line contains, and whether it carries a correlation ID. Logs without correlation are
  unsearchable in a distributed system.
□ What is alerted on; does every alert have a runbook and an owner. An alert with no runbook is noise
  that trains people to ignore the page.
□ Whether the last N requests can be replayed or reconstructed for debugging
□ For anything LLM-mediated: token counts, model versions, tool calls and prompt hashes. Without them
  a probabilistic failure cannot be reproduced.
□ The dashboard that answers "is it healthy right now" in under ten seconds
```

## 7. Security and privacy

```text
□ Trust boundaries, and what crosses each one
□ Authentication; and authorisation enforced per request, at the data layer — or only in the UI
□ Where secrets live, how they rotate, and whether they can be revoked without a deploy
□ Personal data stored, lawful basis, retention, deletion on request
□ Encryption in transit and at rest, and key management
□ For agent systems: what capability the model holds, what is gated behind a human, and where
  untrusted content can reach a tool
□ What the audit log records, and whether it is append-only
□ A threat model produced, with accepted risks written down with dates
```

## 8. Configuration and deployment

```text
□ Config in the environment, separate from code, different per deploy. A config file in the repo is
  not configuration management.
□ Dev, staging and production as similar as possible — same engine and major version, same OS family,
  same mechanism. A sqlite dev environment against Postgres production produces bugs that only exist
  in production.
□ Deploy atomic and reversible; rollback time stated
□ Progressive rollout — canary, blue/green, feature flag — with an abort criterion
□ Migrations before, during or after the deploy, and backwards compatible with the previous version
  still running
□ A new instance can start, pass a health check and serve traffic without manual steps
□ The build-to-production path, and whether artifacts are signed or at least checksummed
```

## 9. Evolution

```text
□ The interface contract, and how a breaking change is communicated and versioned
□ Which decisions are reversible and which are not. Spend the most effort on the irreversible ones:
  the data model, the primary language, the storage engine, the public API shape.
□ The extension point — and whether there is exactly one. Several competing extension mechanisms
  means none of them is supported.
□ What is deliberately NOT built, and why. Write it down, or it will be built later without the
  reasoning that rejected it.
□ The deprecation path for whatever this design replaces
□ Which dependency is most likely to be archived in two years, and the exit plan
```

## 10. Agent-system additions

```text
□ What the agent holds in context, and the compaction or eviction policy when it overflows
□ Where durable state lives, and how a run recovers after a restart mid-task
□ Action budget per session, and what happens when it is exceeded
□ Which tool calls are Tier 3 (irreversible or externally visible) and how approval is obtained
□ Cost per task and the budget — cost is a design constraint, not an ops surprise
□ What happens when the model returns malformed output, refuses, or exceeds its output limit
□ How quality is evaluated over time, against what baseline, with what regression threshold
□ What is logged per model call — prompt hash, model version, tokens, latency, tool calls
□ Whether untrusted content is fenced from instructions, and whether the design assumes injection
  will eventually succeed
```

## Using this in a review

```text
1. Answer each section in writing, in the design document, before the review meeting. A question
   nobody answered is a finding.
2. Mark every answer DECIDED, DEFERRED (with a date and an owner) or ASSUMED. Assumptions are the
   review's highest-value target.
3. For each DEFERRED, state what would make it urgent — which condition, if true, forces the decision.
4. Record the whole thing as a decision record, so the reasoning outlives the people who had it.
```

## References

- [`build-vs-adopt.md`](build-vs-adopt.md) · [`../backend/consistency-models.md`](../backend/consistency-models.md) · [`../databases/consistency-models.md`](../databases/consistency-models.md)
- [`../backend/idempotency.md`](../backend/idempotency.md) · [`../security/threat-modeling.md`](../security/threat-modeling.md) · [`../security/mcp-security/mcp-threat-model.md`](../security/mcp-security/mcp-threat-model.md)
- [`../performance/backend-profiling.md`](../performance/backend-profiling.md) — measuring the bottleneck rather than assuming it
- [`skills/architecture-design/SKILL.md`](../../skills/architecture-design/SKILL.md) · [`workflows/architecture-review/WORKFLOW.md`](../../workflows/architecture-review/WORKFLOW.md)
- [`decision-records/adr-template.md`](../../decision-records/adr-template.md) · [`decision-records/matrix-template.md`](../../decision-records/matrix-template.md)
- [`patterns/architecture/`](../../patterns/architecture/) · [`anti-patterns/architecture/`](./) · [`failure-modes/`](../../failure-modes/)
- The Twelve-Factor App — <https://github.com/heroku/12factor> · Google SRE Book — <https://sre.google/sre-book/table-of-contents/>
