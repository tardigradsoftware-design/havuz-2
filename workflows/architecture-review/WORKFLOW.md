---
name: architecture-review
version: 1.0.0
description: >-
  Review an existing or proposed architecture against its stated requirements — boundaries, data
  ownership, consistency, failure behaviour, operability and reversibility — producing ADRs for what
  changes and a sequenced evolution plan.
trigger: >-
  A new design before implementation; an existing system that has outgrown its structure; a proposed
  service extraction, storage change or vendor adoption; a recurring incident class pointing at
  structure rather than code; or a one-way-door decision about to be taken.
not_for: >-
  Code-level review of a single change (use skills/code-review); a security-specific review (use
  workflows/security-review); a performance investigation (use workflows/performance-review);
  relitigating a decision that has an accepted ADR unless its stated revisit trigger has fired.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [architecture, review, adr, boundaries, tradeoffs, evolution, workflow]
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
estimated_duration: half a day for a focused design review; days for a full system review
stages:
  - id: 1
    name: Recover the requirements
    goal: Establish what the architecture is actually for, including the non-functional requirements that decide structure.
    skill: project-planning
    inputs: [product requirements, existing ADRs, incident history, growth and load data, compliance scope]
    outputs: [functional requirements, non-functional requirements with numeric targets, hard constraints, team and operational capability]
    exit_gate: Scale, latency, consistency, availability, durability, compliance, team size and budget are each stated with a number or an explicit "unknown", and unknowns that would change the design are flagged for resolution.
    on_gate_failure: Stop and gather them. Reviewing an architecture without its requirements produces an opinion about taste.
  - id: 2
    name: Rank the quality attributes
    goal: Force the tradeoffs into the open, because unranked quality attributes produce a design that optimises nothing.
    skill: project-planning
    inputs: [non-functional requirements, business priorities]
    outputs: [ranked quality attributes with numeric targets, and the pairs that conflict irreconcilably]
    exit_gate: Attributes are ranked with numbers, and every conflicting pair is named — those conflicts are the escalation points for the owner rather than decisions for the reviewer.
    max_loops: 2
    on_gate_failure: Escalate the conflict. "Fast, consistent and cheap" is not a specification; one of the three must yield, and that is a business decision.
  - id: 3
    name: Map the current or proposed structure
    goal: Draw what exists or what is proposed, at context and container level, with data flows and trust boundaries.
    skill: repository-analysis
    agent: architect
    inputs: [codebase or design document, deployment topology, integration list]
    outputs: [context diagram, container diagram, data-flow diagram with trust boundaries, integration inventory with direction and contract per edge]
    exit_gate: Every component, store, queue and external integration appears exactly once, every edge has a direction and a named contract, and every trust boundary is marked.
    max_loops: 2
    on_gate_failure: Trace real requests through logs or traces to find the edges nobody documented. Undocumented integrations are where outages originate.
  - id: 4
    name: Audit boundaries and data ownership
    goal: Check that each entity has one owner, each boundary has an interface, and the dependency direction is acyclic and deliberate.
    skill: backend-engineering
    inputs: [structure map, data model, module and service inventory]
    outputs: [ownership table per entity, boundary interface inventory, dependency graph with cycles flagged, coupling hotspots]
    exit_gate: Every entity has exactly one owning component and every other access is a read through a contract; dependency cycles are either eliminated or recorded as accepted with a reason; the highest-coupling modules are identified by measured import counts.
    max_loops: 2
    on_gate_failure: Name the owner. Two writers to one entity without a coordination mechanism is a data-corruption schedule, not a design.
  - id: 5
    name: Audit consistency and failure behaviour
    goal: Verify that every integration has a designed answer to "what happens when this fails", and that consistency claims match the operations that need them.
    skill: backend-engineering
    inputs: [integration inventory, data flows, invariants list]
    outputs: [per-integration failure behaviour — timeout, retry policy, idempotency, circuit breaking, degradation; consistency model per operation; invariant enforcement location]
    exit_gate: No integration lacks a timeout, a bounded retry policy and a stated degradation; every invariant is enforced by a constraint rather than by convention; operations requiring strong consistency are identified and the rest are explicitly eventual.
    max_loops: 2
    on_gate_failure: Design the missing failure behaviour before proceeding. An unspecified failure path is decided by whoever is on call, at 3 a.m., during the incident.
  - id: 6
    name: Audit operability
    goal: Check whether the team that must run this can actually run it.
    skill: deployment
    inputs: [structure map, deployment topology, observability stack, on-call model]
    outputs: [operational assessment — deployability, observability coverage, on-call load per component, scaling mechanism, backup and recovery, cost model]
    exit_gate: Every component is deployable, observable and recoverable by the team that owns it; on-call load is within the team's capacity; and the cost model is stated rather than assumed.
    on_gate_failure: Simplify. A design the team cannot operate is a bad design regardless of its elegance — reduce components before adding headcount.
  - id: 7
    name: Test against the alternatives
    goal: Establish whether the chosen structure is justified, including the simpler one nobody proposed.
    skill: competitive-analysis
    inputs: [structure map, ranked quality attributes, constraints]
    outputs: [comparison of the design against at least two alternatives, always including the simplest viable option and the do-nothing option]
    exit_gate: At least two alternatives are compared against the ranked attributes, the simplest viable option is among them, and every additional component is justified by a requirement it serves.
    max_loops: 2
    on_gate_failure: Remove the unjustified component. Complexity that cannot be traced to a requirement is decoration, and decoration in architecture is operational cost paid forever.
  - id: 8
    name: Classify decision reversibility
    goal: Separate two-way doors from one-way doors, because they deserve opposite amounts of caution.
    skill: dont-reinvent-the-wheel
    inputs: [findings, proposed changes]
    outputs: [decision register with each decision classified as reversible or irreversible, the exit plan for irreversible ones, and the escalation list]
    exit_gate: Every proposed change is classified, every irreversible decision has a written exit plan or an explicit statement that none exists, and all irreversible decisions are on the escalation list for owner sign-off.
    on_gate_failure: Escalate before proceeding. Taking a one-way door without sign-off is how teams end up unable to change anything.
  - id: 9
    name: Write the ADRs
    goal: Record the decisions with the reasoning and the rejected alternatives, so the design survives the people who made it.
    skill: documentation
    agent: architect
    inputs: [decision register, findings, alternatives comparison]
    outputs: [one ADR per consequential decision — context, options considered, decision, consequences, status, date, deciders]
    exit_gate: Every consequential decision has an ADR naming the alternatives that were rejected and why, and a reader of the ADRs alone could reconstruct the design and would not reverse it by accident.
    max_loops: 2
    on_gate_failure: Write the missing ADR. A decision without a record will be reversed by the next person who finds it inconvenient.
  - id: 10
    name: Sequence the evolution
    goal: Produce an order of work that retires risk early and keeps the system working at every step.
    skill: migration
    inputs: [ADRs, decision register, current state, target state]
    outputs: [evolution plan — walking skeleton first, increments ordered riskiest-first, expand-migrate-contract phases for structural changes, gates per milestone, point of no return marked]
    exit_gate: The first milestone is a demonstrable end-to-end vertical slice rather than a layer, each milestone has an observable gate, the riskiest item is earliest, and every irreversible step is marked with the sign-off it requires.
    on_gate_failure: Re-sequence. De-risking in the final milestone is not de-risking; it is discovering the risk when there is no time left to react.
quality_gates:
  - Requirements recovered with numeric non-functional targets before any review of structure.
  - Quality attributes ranked; irreconcilable conflicts escalated rather than silently resolved.
  - Every component, store and integration appears once, with a direction and a named contract.
  - Every entity has exactly one owner; dependency cycles eliminated or accepted with a reason.
  - No integration lacks a timeout, bounded retry and stated degradation.
  - Invariants enforced by constraints, not by convention.
  - Every component deployable, observable and recoverable by its owning team.
  - On-call load within team capacity.
  - At least two alternatives compared, including the simplest viable option.
  - Every component traced to a requirement it serves.
  - Every decision classified reversible or irreversible, with exit plans for the latter.
  - An ADR exists per consequential decision, naming rejected alternatives.
  - First milestone is a walking skeleton; riskiest work is earliest; points of no return marked.
artifacts:
  - requirements and constraints record
  - ranked quality attributes with conflicts named
  - context, container and data-flow diagrams with trust boundaries
  - data ownership table and dependency graph
  - failure-behaviour and consistency matrix
  - operability and cost assessment
  - alternatives comparison
  - decision register with reversibility classification
  - ADRs
  - sequenced evolution plan with gates and points of no return
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "C4 model for software architecture"
    url: https://c4model.com/
    type: methodology
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; verify current diagram conventions before citing specifics."
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    license: MIT
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
  - title: "Strangler Fig Application (Martin Fowler)"
    url: https://martinfowler.com/bliki/StranglerFigApplication.html
    type: methodology
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; verify before citing specifics."
related: [agents/architect/AGENT.md, skills/api-design/SKILL.md, decision-records/, patterns/architecture/]
---

# Workflow: Architecture Review

```text
1 REQUIREMENTS → 2 RANK ATTRIBUTES → 3 MAP STRUCTURE → 4 BOUNDARIES+OWNERSHIP
  → 5 CONSISTENCY+FAILURE → 6 OPERABILITY → 7 ALTERNATIVES → 8 REVERSIBILITY
  → 9 ADRs → 10 EVOLUTION PLAN
```

## The question this workflow answers

Not "is this architecture good?" — that has no answer without a referent. The question is
**"does this structure serve these ranked requirements, at this cost, with this team, and can it
be changed later?"** Every stage collects part of that answer.

## Why requirements come first

An architecture reviewed without its requirements can only be reviewed against the reviewer's
preferences, which produces two failure modes: resume-driven design is approved because it is
interesting, and a correct boring design is criticised because it is boring. Stages 1 and 2
exist to make the referent explicit before any judgement is formed.

## The three findings that matter most

In practice, most architecture reviews reduce to these:

```text
1. UNOWNED DATA          Two components able to write one entity, with the invariant enforced
                         in application code that one of them bypasses.
2. UNSPECIFIED FAILURE   An integration with no timeout, no retry bound and no degradation —
                         so its failure behaviour is decided during the incident.
3. UNJUSTIFIED COMPONENT A service, queue or store that exists because it was interesting,
                         with no requirement it serves and an on-call cost somebody pays.
```

Stages 4, 5 and 7 are aimed at exactly these.

## Scaling

```text
DESIGN REVIEW (pre-build)   stages 1, 2, 3, 5, 7, 8, 9, 10
EXISTING SYSTEM REVIEW      all stages
SERVICE EXTRACTION DECISION stages 1, 2, 4, 5, 6, 7, 8, 9, 10
POST-INCIDENT STRUCTURAL    stages 1, 3, 4, 5, 6, 9 — focused on the failure's structural cause
ONE-WAY-DOOR DECISION       stages 1, 2, 7, 8, 9 — the reversible/irreversible classification
                            and the alternatives comparison are the point
```

## References

- [`agents/architect/AGENT.md`](../../agents/architect/AGENT.md) · [`agents/backend-engineer/AGENT.md`](../../agents/backend-engineer/AGENT.md)
- [`skills/api-design/SKILL.md`](../../skills/api-design/SKILL.md) · [`skills/database-design/SKILL.md`](../../skills/database-design/SKILL.md)
- [`skills/backend-engineering/SKILL.md`](../../skills/backend-engineering/SKILL.md) · [`skills/migration/SKILL.md`](../../skills/migration/SKILL.md)
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../skills/dont-reinvent-the-wheel/SKILL.md)
- [`decision-records/`](../../decision-records/) — ADR and matrix templates
- [`patterns/architecture/`](../../patterns/architecture/) · [`knowledge/architecture/`](../../knowledge/architecture/)
- [`workflows/analyze-existing-project/WORKFLOW.md`](../analyze-existing-project/WORKFLOW.md)
