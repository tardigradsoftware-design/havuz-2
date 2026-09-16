---
name: architecture-design
version: 1.0.0
description: >-
  Design a system architecture from stated requirements: decompose the problem, choose boundaries and consistency levels per data type, enumerate failure modes, and record the irreversible decisions with their reasoning.
category: architecture
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [architecture, system-design, boundaries, tradeoffs, adr, scalability, failure-modes]
applies_to: [backend, distributed-systems, new-project, rearchitecture]
priority: 3
requires: []
conflicts_with: []
estimated_tokens: 2346
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
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: "Heroku"
    license: MIT
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Config in the environment, backing services as attached resources, dev/prod parity and disposability are recurring sections of the design checklist this skill implements."
  - title: "Google SRE Book — Monitoring Distributed Systems"
    url: https://sre.google/sre-book/monitoring-distributed-systems/
    type: official-docs
    organization: "Google"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "The four golden signals — latency, traffic, errors, saturation — used as the observability requirement in step 8."
  - title: "PostgreSQL documentation — Transaction Isolation"
    url: https://www.postgresql.org/docs/current/transaction-iso.html
    type: official-docs
    organization: "PostgreSQL Global Development Group"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "What each isolation level actually prevents in a real engine, which is the basis for assigning consistency per data type in step 3."
related_skills: [database-design, api-design, performance-audit, security-audit, threat-modeling, project-planning, dont-reinvent-the-wheel]
related_repositories: [heroku/12factor]
tests: 9
---
# Architecture Design

## Purpose

Produce an architecture whose decisions were made explicitly, are written down, and can be argued
with — rather than one assembled from defaults and framework conventions. The deliverable is not a
diagram; it is a set of decisions with their reasoning, their reversibility and their review dates.

## When to Use

```text
✓ a new system or service is being designed
✓ an existing system is being restructured, split or merged
✓ a decision with a high exit cost is on the table: data model, storage engine, primary language,
  public API shape, synchrony vs asynchrony
✓ a review needs to establish whether the decisions were made or inherited
```

## When NOT to Use

```text
✗ The change is local and reversible — a function, a component, an internal module boundary.
  Refactoring skill applies; architecture does not.
✗ The real question is build vs adopt for one capability. Use dont-reinvent-the-wheel and
  competitive-analysis, then return here only if the answer is "build".
✗ Performance is the question and nothing has been measured. Profile first; architecture decisions
  made against an unmeasured bottleneck are guesses with a diagram attached.
✗ The system does not yet have a stated requirement. Architecture without numbers is decoration.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| Requirements as numbers | yes | read:write ratio, volume now and at 12 months, latency percentiles, availability target, data growth |
| Domain model | yes | entities, identities, ownership |
| Constraints | yes | regulatory, data residency, existing estate, team skills, budget, deadline |
| Existing system inventory | when modifying | what exists, what is load-bearing, what is deprecated |
| Non-goals | yes | what this design deliberately does not solve |

Missing a numeric requirement is a blocker, not a gap to fill with an assumption.

## Workflow

```text
1. STATE THE REQUIREMENTS AS NUMBERS.   Latency as a percentile, volume as a rate, availability as a
   target with a cost of downtime. Mark each as hard or aspirational. A design cannot optimise for all
   of them and pretending otherwise produces one that satisfies none.

2. MODEL THE DATA BEFORE THE SERVICES.  Entities, identities, ownership, access patterns (by ID, by
   foreign key, by range, by full-text, by similarity), retention. Service boundaries that contradict
   data ownership are the source of distributed monoliths.

3. ASSIGN CONSISTENCY PER DATA TYPE.    Not per system. Money, inventory, identity and access control
   usually need strong consistency; search, analytics, recommendations and derived views usually do
   not. Where eventual consistency is chosen, write down the staleness budget and make the
   authoritative view reachable.

4. DRAW THE BOUNDARIES AND NAME WHAT CROSSES THEM.  Every crossing is a failure domain, a latency
   cost and a security boundary. Fewer crossings is almost always better; each one needs a reason.

5. ENUMERATE FAILURE MODES PER DEPENDENCY.  Slow, erroring, partial data, unreachable — four cases,
   not one. For each: timeout, retry policy with a budget, circuit breaker, degraded behaviour.
   Name what fails hard. "Everything degrades gracefully" is false and will be discovered during the
   incident.

6. IDENTIFY THE IRREVERSIBLE DECISIONS.  Data model, storage engine, language, public API shape,
   sync vs async. Spend the most effort here; spend almost none on the reversible ones, which should
   be deferred deliberately rather than decided early.

7. CHECK THE SCALING AXIS.              Which limit is hit first: compute, connections, storage IOPS,
   network, memory, a third-party rate limit. Sum connection pools across instances and compare with
   the resource's ceiling. State what breaks at 10× and the plan.

8. DESIGN FOR OBSERVABILITY.            The four golden signals per service, a trace across every
   boundary, correlation IDs in logs, alerts with runbooks and owners. If a failure cannot be
   attributed, the architecture is not operable.

9. WRITE THE DECISION RECORDS.          One ADR per significant decision: context, options with their
   costs, the choice, the reasoning, what would reopen it, and the review date. The reasoning is the
   deliverable; the diagram is the summary.

10. STATE THE NON-GOALS AND THE DEFERRALS.  What is deliberately not built, and for each deferred
   decision, the condition that would make it urgent.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Requirements were adjectives | no percentile, rate or target appears in the document | stop and obtain numbers; do not design against "fast" |
| Boundaries follow the org chart, not the data | one entity written by three services | re-cut along data ownership; accept the reorganisation cost |
| Consistency assumed uniform | "the system is strongly consistent" applied to analytics too | assign per data type; state staleness budgets |
| Failure handling for errors only | timeouts and retries exist, slow-dependency behaviour does not | add the slow and partial cases; they are more common |
| Retries without a budget | retry count unbounded, no breaker | add exponential backoff with jitter, a budget, a breaker |
| Irreversible decisions taken casually | no ADR, no alternatives recorded | write the ADR now, before the exit cost is paid |
| Observability deferred | "we will add tracing later" | tracing added later does not cover the boundaries that were already built |
| Architecture by framework default | the design is a description of the framework's conventions | state what the framework decided for you and whether it was reviewed |

## Quality Checklist

```text
□ every requirement is a number with a percentile or a rate, marked hard or aspirational
□ every entity has one owner and one authoritative store
□ consistency level is stated per data type, with staleness budgets where eventual
□ every dependency has timeout, retry budget, breaker and degraded behaviour defined
□ what fails hard is named explicitly
□ the irreversible decisions have ADRs with alternatives and reasoning
□ the scaling axis is identified from measurement or a stated estimate, and the 10× answer is written
□ golden signals, traces, correlation IDs and alert runbooks are specified
□ non-goals are stated
□ deferred decisions list the condition that makes them urgent
□ the design can be read by someone who was not in the room
```

## Anti-Patterns

```text
✗ DIAGRAM-FIRST DESIGN.   Boxes and arrows without the decisions behind them. The diagram is the
  output of the reasoning, not a substitute for it.
✗ RESUME-DRIVEN ARCHITECTURE.  Adopting a technology because it is interesting rather than because a
  stated requirement demands it.
✗ DISTRIBUTED MONOLITH.   Services split so finely that every change touches several and every
  request crosses five boundaries, with none of the independence that justified the split.
✗ PREMATURE ABSTRACTION.   A plugin system, an extension mechanism or a generic engine built before a
  second concrete case exists. Two examples is the minimum for finding the real seam.
✗ SHARED DATABASE AS AN INTEGRATION MECHANISM.  Two services writing one table couples them more
  tightly than an API would, invisibly, and with no versioning.
✗ "WE'LL SCALE LATER."   Deferring is legitimate; deferring without naming the axis and the trigger is
  not a plan.
✗ DESIGNING FOR THE DEMO PATH.  The architecture that works for one tenant with 100 rows and fails for
  the tenant with 10 million.
✗ NO RECORD.  A decision made in a meeting and never written is re-litigated by the next engineer,
  without the reasoning that rejected the plausible alternative.
```

## References

- [`knowledge/architecture/system-design-checklist.md`](../../knowledge/architecture/system-design-checklist.md) — the full question set this workflow summarises
- [`knowledge/architecture/build-vs-adopt.md`](../../knowledge/architecture/build-vs-adopt.md) · [`knowledge/backend/consistency-models.md`](../../knowledge/backend/consistency-models.md) · [`knowledge/databases/consistency-models.md`](../../knowledge/databases/consistency-models.md)
- [`knowledge/performance/backend-profiling.md`](../../knowledge/performance/backend-profiling.md) — measure before choosing the scaling axis
- [`knowledge/security/threat-modeling.md`](../../knowledge/security/threat-modeling.md) — boundaries are also trust boundaries
- [`decision-records/adr-template.md`](../../decision-records/adr-template.md) · [`decision-records/matrix-template.md`](../../decision-records/matrix-template.md)
- [`workflows/architecture-review/WORKFLOW.md`](../../workflows/architecture-review/WORKFLOW.md) · [`agents/architect/AGENT.md`](../../agents/architect/AGENT.md)
- The Twelve-Factor App — <https://github.com/heroku/12factor> · Google SRE Book — <https://sre.google/sre-book/table-of-contents/>
