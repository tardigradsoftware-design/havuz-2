---
name: project-planning
version: 1.0.0
description: >-
  Turn an ambiguous goal into a sequenced, gated plan with explicit unknowns, evidence-backed
  estimates and stop conditions — so work is verifiable at every step rather than at the end.
category: planning
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [planning, decomposition, estimation, milestones, risk, execution]
applies_to: [any]
priority: 86
requires: [research-before-code]
conflicts_with: []
estimated_tokens: 2750
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Decomposition
    anchor: "#decomposition"
    purpose: implementation
  - heading: Estimation
    anchor: "#estimation"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    url: https://arxiv.org/abs/2305.10601
    type: research-paper
    published: 2023-05-17
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Deliberate search with lookahead and self-evaluation outperforms linear generation on tasks requiring exploration."
related_skills: [research-before-code, documentation, testing, deployment, release-engineering]
related_repositories: [langchain-ai/langgraph, microsoft/agent-framework]
tests: 6
---

# Project Planning

## Purpose

Convert an ambiguous goal into a sequence of steps, each with an **observable completion
condition**, so progress is verifiable continuously and failure is detected early rather
than at the end.

The two planning failures this prevents: the plan that is a list of nouns ("auth, database,
UI") with no order and no gates, and the plan that is so detailed it collapses on first
contact with reality and is then abandoned.

## When to Use

```text
□ Any effort spanning more than one session, more than one person, or more than one subsystem
□ A request whose scope is unclear ("build me a dashboard")
□ Work with a deadline, a budget or a dependency on someone else
□ A migration, integration or rewrite where sequencing determines risk
□ An agent task expected to run autonomously for many steps
```

## When NOT to Use

```text
✗ A single well-understood change — do it
✗ Genuine exploration where the goal is to learn what the problem is (timebox a spike instead,
  and plan the follow-up)
✗ When the plan will be discarded: planning has a cost; spend it where sequencing matters
```

## Inputs

```text
goal             the outcome, in the requester's words, plus the success condition
constraints      deadline, budget, people, stack, compliance, deployment target
knowns           what is already decided, built or available
unknowns         what must be learned before parts of this can be planned
risk appetite    what may fail, what must not
evidence         research findings (see research-before-code) — a plan without research is a guess
```

## Decomposition

```text
GOAL → OUTCOMES → MILESTONES → TASKS → STEPS
```

```text
OUTCOMES      What must be true when this succeeds? 3–7 observable statements.
              "A user can sign up, verify their email and see their first report."
              Outcomes are the acceptance criteria; everything else serves them.

MILESTONES    A milestone is a state where the system DEMONSTRABLY works end to end at
              reduced scope — not "backend done". Walking skeleton first: the thinnest
              vertical slice through every layer, deployed, observable, tested.
              Each milestone proves a class of risk is retired.

TASKS         Each task is completable in one sitting (< ~1 day), has one owner, and has a
              done-condition that someone else can check. If it needs "and also", split it.

STEPS         For agents: the ordered actions within a task, each with a verification.
              A step without a verification is a hope.
```

Rules:

```text
1. DEPENDENCIES EXPLICIT. Draw them. A task whose prerequisite is unstated will be started
   too early and blocked.
2. RISKIEST FIRST. The item most likely to invalidate the plan goes in milestone 1, not
   milestone 4. De-risking late is not de-risking.
3. VERTICAL SLICES, NOT HORIZONTAL LAYERS. "All the database work" produces nothing
   demonstrable for weeks; "one journey working end to end" produces evidence in days.
4. UNKNOWNS ARE TASKS. An unknown is not a gap in the plan — it is a research or spike task
   with a budget and a decision it must produce. "TBD" is a planning defect.
5. INTEGRATION IS A TASK, AND IT IS BIG. The step where the pieces meet is where schedules die.
6. EVERY TASK HAS A GATE: the observable condition that proves it is done, and who checks it.
7. PLAN TO THE HORIZON YOU CAN SEE. Detailed for the next milestone; directional for the rest.
   Re-plan at every milestone boundary — deliberately, not silently.
```

## Estimation

Estimates are ranges with a stated basis. A single number is a false precision.

```text
BASIS         Choose and state it:
              reference class   "the last three integrations of this kind took 2–4 days each"
              decomposition     "8 tasks, 6 of them known-small, 2 unknown"
              expert judgement  "based on X's experience with this stack" — attributed
              NOT: gut feel presented as a number

FORM          three-point: optimistic / likely / pessimistic, plus the assumption that
              separates them. Report the likely and the pessimistic; never only the optimistic.

DRIVERS       Name the 2–3 factors that dominate the estimate. Usually: unknowns, integration,
              third-party response time, data migration, review latency — rarely typing speed.

CONFIDENCE    low | medium | high, and what would raise it (usually: finishing a spike).

BUFFER       Explicit, at the plan level, not hidden inside each task. Hidden per-task padding
              is invisible to the person making the tradeoff.

CALENDAR ≠ EFFORT   Elapsed time includes review latency, third-party approval, on-call
              interruptions and context switching. A 2-day-effort task in a 3-person queue
              is a 2-week calendar item.

RE-ESTIMATE   At each milestone boundary, re-estimate the remainder using the observed rate.
              Record the estimate-vs-actual delta — that history is the only thing that
              improves future estimates.
```

## Risk register

One row per risk; reviewed at every milestone.

```text
| risk | likelihood | impact | early-warning signal | mitigation | owner | contingency |
```

Rules:

```text
□ The early-warning signal must be observable BEFORE the impact lands. A risk with no
  leading indicator cannot be managed, only suffered.
□ Mitigation reduces likelihood or impact; contingency is what you do when it happens anyway.
  Both are required.
□ The top three risks drive milestone 1's content.
□ Unknown-unknowns get a budget and a stop condition, not a register entry.
```

## Stop conditions and gates

Every plan states, in advance:

```text
STOP          the conditions under which we halt and reassess rather than continue:
              budget exhausted · a blocking unknown unresolved after its timebox ·
              two consecutive milestones missed · a dependency withdrawn ·
              the goal no longer worth the remaining cost
GATE          what must be true to proceed from one milestone to the next
ESCALATE      what must be raised to a human, and when (security, spend, data deletion,
              irreversible actions, scope change, deadline at risk)
DEFINITION OF DONE  the shared standard for "complete": tested, reviewed, documented,
              deployed, observable, rolled back if needed
```

For autonomous agents this section is mandatory — an agent without a stop condition will
convert a blocked task into an expensive loop.

## Failure Modes

```text
NOUN LIST             "Auth, DB, API, UI" — no order, no gates, no outcomes.
HORIZONTAL SLICING    Layer-by-layer delivery; nothing demonstrable for weeks.
LATE DE-RISKING       The riskiest item scheduled last, when there is no time left to react.
HIDDEN UNKNOWN        "TBD" in a plan, with no owner, budget or decision attached.
OPTIMISM AS PLAN      Quoting the optimistic number and treating the pessimistic as noise.
EFFORT = CALENDAR     Ignoring review latency and third-party response time.
NO STOP CONDITION     Continuing a blocked or worthless task because stopping was never defined.
PLAN ABANDONMENT      The detailed plan diverges from reality on day 2 and is never updated.
SILENT RE-PLAN        Scope changes without the constraint conversation that should follow.
INTEGRATION AS A FOOTNOTE  The hardest task assumed to be "wiring it up".
BUFFER SMearing       Padding inside every task so nobody can see or trade the total.
NO RETROSPECTIVE      Estimate-vs-actual never recorded, so nothing improves.
```

## Quality Checklist

```text
□ Outcomes written as 3–7 observable statements, agreed with the requester
□ Research completed for load-bearing unknowns before the plan was fixed
□ Milestones are demonstrable working states, ordered riskiest-first
□ First milestone is a walking skeleton: thinnest end-to-end vertical slice
□ Tasks < ~1 day, one owner each, with a checkable done-condition
□ Dependencies drawn explicitly; integration scheduled as its own task
□ Every unknown converted to a research/spike task with a budget and a required decision
□ Estimates as three-point ranges with a stated basis and confidence level
□ Dominant estimate drivers named; buffer explicit at plan level
□ Effort distinguished from calendar time
□ Risk register with observable early-warning signals, mitigations, owners, contingencies
□ Stop conditions, gates, escalation triggers and definition of done written in advance
□ Plan detailed to the current horizon, directional beyond; re-planned at each milestone
□ Estimate-vs-actual recorded and reviewed
```

## Anti-Patterns

```text
✗ A Gantt chart of layers with no demonstrable milestone until the end
✗ "Should take about a day" with no basis, no range and no confidence
✗ The riskiest integration scheduled in the final week
✗ "TBD: caching strategy" left in an approved plan
✗ A plan written once and never updated after reality diverged
✗ An autonomous agent with no stop condition and no escalation trigger
✗ Buffer distributed invisibly across twenty tasks
✗ Declaring a milestone complete because the tasks are done, not because the outcome is observable
```

## References

- [`research-before-code`](../research-before-code/SKILL.md) — evidence before the plan
- [`documentation`](../documentation/SKILL.md) · [`testing`](../testing/SKILL.md)
- [`release-engineering`](../release-engineering/SKILL.md) · [`deployment`](../deployment/SKILL.md)
- [`workflows/`](../../workflows/) — orchestrated multi-skill plans
- [`decision-records/`](../../decision-records/) — recording the decisions a plan depends on
- Tree of Thoughts, arXiv:2305.10601 (verified 2026-09-15)

## Related Skills

`research-before-code` · `testing` · `deployment` · `release-engineering` · `documentation` ·
`competitive-analysis`

## Evaluation Criteria

```text
1. Outcome attainment: fraction of declared outcomes demonstrably achieved.
2. Estimate accuracy: actual/pessimistic ratio per milestone, trending toward 1.0 over time.
3. Early risk detection: fraction of realised risks that had a registered early-warning signal
   which fired before impact.
4. Gate discipline: 0 milestones declared complete without their observable condition met.
5. Stop-condition usage: blocked or worthless work halted within one milestone, not at the end.
6. Re-plan frequency and quality: plans updated at each boundary with recorded deltas.
```

Test cases in [`tests/`](tests/).
