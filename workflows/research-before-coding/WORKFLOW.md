---
name: research-before-coding
version: 1.0.0
description: >-
  The mandatory gate before any non-trivial implementation: understand the request, research the
  unknowns, compare options, verify the evidence, and produce a Research Decision Record that
  implementation must follow.
trigger: >-
  Any task that will produce code intended to be kept, especially one naming a specific library,
  framework, API, cloud service or protocol, or one containing an implicit technology choice
  ("build me auth", "add caching", "make it fast").
not_for: >-
  One-line typo fixes; purely local refactoring proved correct by an existing suite; explicitly
  disposable spikes; tasks whose conventions are already pinned in the repository's own AGENTS.md
  (read that instead of the internet); work where a human has already fixed the library, version
  and pattern.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [research, planning, evidence, gate, workflow, anti-hallucination]
confidence: high
claim_type: recommendation
evidence_level: cross-checked
estimated_duration: 20-90 minutes depending on risk class and unknown count
stages:
  - id: 1
    name: Understand and frame
    goal: Restate the task, name every implicit technology decision it assumes, classify the risk, and define the observable success test.
    skill: research-before-code
    inputs: [task description, stated constraints, repository AGENTS.md]
    outputs: [framed task, implicit-choices list, risk class, success test]
    exit_gate: At least one implicit choice is named, or the task is explicitly marked research_skipped with a written reason.
    on_gate_failure: Return to the requester for clarification; do not proceed on an unframed task.
  - id: 2
    name: Load local context first
    goal: Answer as much as possible from the cheapest and most specific sources before searching the internet.
    skill: research-before-code
    inputs: [framed task, AGENTS.md, lockfiles and manifests, indexes/topics.md, metadata/repositories.json, gotchas/, failure-modes/]
    outputs: [local-context findings, remaining unknowns list]
    exit_gate: Every unknown is either answered from local context or carried forward with a statement of what external evidence would resolve it.
    max_loops: 2
    on_gate_failure: Record the unknown as UNRESOLVED and continue; never invent an answer to close the gap.
  - id: 3
    name: Research the unknowns
    goal: Gather evidence per unknown from official documentation for the correct version, the official repository, and at least one independent source.
    skill: web-research
    agent: researcher
    inputs: [remaining unknowns list, required confidence from the risk class]
    outputs: [evidence table with URL, type, publisher, page date, verified_at, confidence]
    exit_gate: At least two independent provenances per load-bearing unknown, or the unknown is marked UNRESOLVED with the resolving evidence named.
    max_loops: 3
    on_gate_failure: Downgrade the claim's confidence and record the single-sourcing explicitly; escalate if the decision is high-risk.
  - id: 4
    name: Compare options
    goal: Build a decision matrix over real candidates, always including a hand-roll or do-nothing row, and reject at least one option for a stated reason.
    skill: competitive-analysis
    inputs: [evidence table, constraints, weights agreed before scoring]
    outputs: [decision matrix, rejected options with reasons]
    exit_gate: At least two options compared, weights fixed before scoring, and every rejected option has a specific, checkable reason.
    on_gate_failure: Return to stage 3 for the missing candidate; a matrix with one row is not a comparison.
  - id: 5
    name: Verify the chosen option
    goal: Apply the twelve evidence-validation checks to the selected dependency or approach, including existence, status, license, version-specific API and maintenance outlook.
    skill: evidence-validation
    agent: fact-checker
    inputs: [decision matrix, chosen option, metadata/repositories.json record]
    outputs: [verification report, per-claim confidence, license_risk, re-verify-by date]
    exit_gate: Every load-bearing claim has confidence at or above the level the risk class requires, and each carries a verified_at date.
    max_loops: 2
    on_gate_failure: Re-verify, choose the runner-up, or escalate. Never proceed on an unverified load-bearing claim.
  - id: 6
    name: Write the Research Decision Record
    goal: Produce the artifact that implementation must follow, including the decision, the why, the rejections, the evidence, the open risks and the validation plan.
    skill: research-synthesis
    inputs: [verified evidence, decision matrix, verification report]
    outputs: [Research Decision Record]
    exit_gate: A reader who was not present could execute the plan without asking questions, and every load-bearing claim in it is cited with a date.
    on_gate_failure: Rewrite until the record is self-sufficient; do not start implementation with an incomplete record.
  - id: 7
    name: Plan the implementation
    goal: Sequence the work into steps, each with an observable completion condition, ordered riskiest-first, with a walking skeleton as the first milestone.
    skill: project-planning
    inputs: [Research Decision Record, constraints, deadline]
    outputs: [sequenced plan with per-step gates, stop conditions, escalation triggers]
    exit_gate: Every step has a checkable done-condition, dependencies are explicit, and stop conditions and escalation triggers are written down.
    on_gate_failure: Re-decompose; a step without a gate is a hope, not a plan.
  - id: 8
    name: Implement against the record
    goal: Build to the plan. When reality contradicts the research, stop and update the record rather than improvising silently.
    inputs: [Research Decision Record, sequenced plan]
    outputs: [implementation, amended record where reality diverged]
    exit_gate: The implemented solution matches the record, or the record was updated before the divergence took effect.
    max_loops: 4
    on_gate_failure: Halt and re-enter stage 5 with the contradicting observation; silent improvisation converts verified research back into hallucination.
  - id: 9
    name: Validate
    goal: Run the validation plan defined in stage 6 and add regression tests for each open risk.
    skill: testing
    agent: qa-engineer
    inputs: [validation plan, open risks, implementation]
    outputs: [test results, regression tests, defect reports]
    exit_gate: Every item in the validation plan passes, and each open risk has a regression test or a recorded acceptance.
    max_loops: 3
    on_gate_failure: Return to stage 8 with the failing evidence; do not weaken an assertion to pass.
  - id: 10
    name: Feed back into the knowledge base
    goal: Convert the experience into durable memory so the next agent does not relearn it.
    skill: agent-memory-design
    agent: skill-curator
    inputs: [Research Decision Record, implementation outcome, defects found]
    outputs: [knowledge candidates, gotchas entries, refreshed verified_at on cited sources, changelog entry]
    exit_gate: What worked, what failed, what was outdated and what was missing are each recorded somewhere retrievable, or explicitly judged not durable.
    on_gate_failure: File the minimum — a gotcha entry for the trap and a verified_at refresh for the sources used.
quality_gates:
  - No implementation code exists before the Research Decision Record does.
  - Every load-bearing claim in the record carries a URL, a page date and a confidence level.
  - At least one option was rejected for a stated, checkable reason.
  - 100% of cited URLs were actually fetched during the run.
  - Chosen dependencies verified to exist, with license known, status known and version pinned.
  - Any repository with license null is flagged no-license-do-not-redistribute and never vendored.
  - Security-critical primitives were escalated or adopted, never hand-rolled.
  - The record's outcome was fed back into the knowledge base.
artifacts:
  - Research Decision Record (the primary output)
  - evidence table (json)
  - decision matrix
  - verification report
  - sequenced implementation plan with gates
  - test results and regression tests
  - knowledge-base entries filed in stage 10
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: https://arxiv.org/abs/2210.03629
    type: research-paper
    published: 2022-10-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Interleaving reasoning with external lookups reduces hallucination and error propagation."
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Basis for updating the record on contradiction rather than improvising."
related: [skills/research-before-code/SKILL.md, agents/researcher/AGENT.md, agents/fact-checker/AGENT.md, decision-records/]
---

# Workflow: Research Before Coding

The ten-stage gate between a request and its implementation. Stages 1–7 produce the **Research
Decision Record**; stage 8 is the only stage that writes production code, and it writes it against
that record.

```text
1 UNDERSTAND → 2 LOCAL CONTEXT → 3 RESEARCH → 4 COMPARE → 5 VERIFY
   → 6 RECORD → 7 PLAN → 8 IMPLEMENT → 9 VALIDATE → 10 FEED BACK
```

## Why the order matters

```text
Stage 2 before 3    Local sources are cheaper, more specific and more current for this codebase
                    than anything on the internet. Searching first wastes budget and imports
                    generic answers into a specific problem.
Stage 4 before 5    Compare before verifying deeply, so verification effort goes to the option
                    that will actually be used.
Stage 5 before 6    The record must not contain claims that have not been graded.
Stage 6 before 8    This is the gate. A record written after the code is documentation of a
                    decision already made by instinct, and it will not contain the rejected
                    options — which is where the learning is.
Stage 10 always     Without feedback, the next agent repeats the whole investigation.
```

## Fast paths

```text
LOW RISK, ANSWERED LOCALLY      stages 1, 2, 6 (abbreviated record), 8, 9, 10
MEDIUM RISK                     all stages, budgeted
HIGH RISK (security, payments,  all stages with a human sign-off at stage 6,
data loss, auth, migrations)     and an independent fact-checker pass at stage 5
PINNED BY A HUMAN               stages 1, 2, 5 (verify the pinned version's API), 6, 7, 8, 9, 10
```

The fast path is a decision, not a shortcut: record which path was taken and why.

## Failure modes specific to this workflow

```text
STAGE SKIPPING        Jumping to stage 8 because the answer "seems obvious". The record is the
                      control; without it there is no evidence the research happened.
LOCAL-CONTEXT SKIP    Going straight to web search and importing a generic answer that contradicts
                      the project's own conventions.
PERPETUAL RESEARCH    Looping stages 3-5 without budget. The max_loops values exist for this.
SILENT IMPROVISATION  Stage 8 diverges from the record without amending it. This is the single
                      most damaging failure — it makes the record a lie.
WEAKENED VALIDATION   Stage 9 assertions loosened to pass. Return to stage 8 instead.
NO FEEDBACK           Stage 10 skipped under time pressure, so the knowledge is lost.
```

## References

- [`skills/research-before-code/SKILL.md`](../../skills/research-before-code/SKILL.md) — the detailed procedure
- [`skills/web-research/SKILL.md`](../../skills/web-research/SKILL.md) · [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md)
- [`skills/competitive-analysis/SKILL.md`](../../skills/competitive-analysis/SKILL.md) · [`skills/project-planning/SKILL.md`](../../skills/project-planning/SKILL.md)
- [`agents/researcher/AGENT.md`](../../agents/researcher/AGENT.md) · [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md)
- [`decision-records/`](../../decision-records/) — record and matrix templates
- [`AGENTS.md`](../../AGENTS.md) — the policy this workflow enforces
