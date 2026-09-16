---
name: bug-investigation
version: 1.0.0
description: >-
  Systematic defect investigation from symptom to root cause — reproduce automatically, isolate to
  the smallest subsystem, test one hypothesis per change, fix the cause rather than the symptom, and
  file the lesson where the next agent will find it.
trigger: >-
  Any incorrect behaviour, crash, flake, regression, performance anomaly, security incident, or an
  agent about to make its third consecutive change to the same code without progress.
not_for: >-
  A known and understood defect with an agreed fix (implement it); a feature request described as a
  bug; cosmetic preference changes; a question about intended behaviour that documentation answers.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [debugging, incident, root-cause, testing, workflow, methodology]
confidence: high
claim_type: recommendation
evidence_level: cross-checked
estimated_duration: 30 minutes for an isolated defect; hours for intermittent or cross-system failures
stages:
  - id: 1
    name: Capture the symptom exactly
    goal: Record what is observed verbatim — the real error text, not a paraphrase — with the expected behaviour and how that expectation is known.
    skill: debugging
    inputs: [report, error output, logs, screenshots, user description]
    outputs: [symptom statement, expected behaviour with its source, first-seen date, affected scope]
    exit_gate: The symptom is stated as observed text plus expected text, and the scope is bounded — which users, tenants, requests, data shapes, environments and versions are affected.
    on_gate_failure: Gather more observations before hypothesising. A paraphrased symptom sends the investigation in the wrong direction.
  - id: 2
    name: Establish what changed
    goal: Correlate first-seen with deploys, dependency bumps, config changes, data migrations, feature flags, traffic shifts and schema changes.
    inputs: [first-seen date, deploy history, dependency and lockfile diffs, config history, feature-flag changes, release notes]
    outputs: [candidate change list ranked by temporal and causal proximity]
    exit_gate: Either a specific change is correlated with first-seen, or the investigation has established that nothing changed in the relevant window — which itself redirects the search to data or load.
    max_loops: 2
    on_gate_failure: Widen the window and check upstream dependencies and third-party changes; a defect with no local cause often has a remote one.
  - id: 3
    name: Reproduce automatically
    goal: Build the smallest deterministic reproduction, as a command or test, that fails reliably.
    skill: debugging
    inputs: [symptom, affected scope, candidate changes]
    outputs: [automated reproduction — script, test or curl — plus its determinism rate and trigger variable]
    exit_gate: A command exists that reproduces the failure, its determinism is measured (10/10, 3/10 or once), and the trigger variable is identified — input shape, timing, ordering, concurrency, state, environment, version or data volume.
    max_loops: 4
    on_gate_failure: For intermittent failures, change the goal to raising the reproduction rate — parallelise, amplify timing, add load, replay recorded traffic — before hypothesising. Escalate if it cannot be reproduced at all.
  - id: 4
    name: Observe the real error
    goal: Get the untruncated error at the correct layer, with symbols resolved and the exact input that caused it.
    inputs: [reproduction, logs, traces, error tracking]
    outputs: [full stack trace, exact failing input with secrets redacted, surrounding log context, version of every component in the path]
    exit_gate: The error message has been read literally, the trace is resolved to source lines, and the failing input's shape is known — not merely its identity.
    on_gate_failure: Add instrumentation at the boundary of the suspected subsystem and reproduce again. Guessing from an unresolved trace wastes the rest of the investigation.
  - id: 5
    name: Isolate
    goal: Reduce to the smallest subsystem in which the defect still reproduces.
    skill: debugging
    inputs: [reproduction, trace, failing input]
    outputs: [isolated subsystem, the boundary inputs and outputs around it, evidence that everything outside is innocent]
    exit_gate: A component has been identified such that the defect reproduces inside it and not when it is replaced by a known-good stub.
    max_loops: 4
    on_gate_failure: Use bisection — git bisect on the regression range, binary search on the payload, halve the call path — and diff working against broken across environment, config, versions, data, flags, headers, timezone, locale and seed.
  - id: 6
    name: Hypothesise and test
    goal: Test one falsifiable hypothesis per change, recording every attempt whether it confirms or kills.
    skill: debugging
    inputs: [isolated subsystem, trace, failing input]
    outputs: [attempt log — hypothesis, predicted observation, specific test, result, conclusion]
    exit_gate: One hypothesis is confirmed by an observation that could have falsified it, and no attempt is repeated after being disproved.
    max_loops: 6
    on_gate_failure: Return to stage 5 — a hypothesis that cannot be tested usually means the isolation is wrong. Never change two variables at once; if the bug disappears, nothing has been learned.
  - id: 7
    name: Establish root cause
    goal: Ask down the causal chain to the level of the missing check, not just the immediate defect.
    inputs: [confirmed hypothesis, attempt log]
    outputs: [root cause at four levels — why it failed, why the defect existed, why the assumption was made, why it was not caught]
    exit_gate: The chain reaches "why was it not caught", identifying the missing test, validation or review gate — which becomes a fix in its own right.
    on_gate_failure: Continue asking why. Stopping at level one yields a patch that returns in a different shape.
  - id: 8
    name: Fix minimally
    goal: Apply the smallest change that removes the root cause, with no unrelated improvements bundled in.
    inputs: [root cause, reproduction]
    outputs: [fix, plus the prevention fix for the missing gate identified in stage 7]
    exit_gate: The fix addresses the cause rather than the symptom, contains no unrelated changes, and the missing gate from stage 7 has been closed — a test, a validation, a constraint or a lint rule.
    max_loops: 2
    on_gate_failure: Split the change. A bug fix bundled with a refactor cannot be verified or reviewed, and a symptom patch must be replaced by a cause fix.
  - id: 9
    name: Prove the fix
    goal: Verify with the automated reproduction, in the environment where the defect appeared, without collateral damage.
    skill: testing
    agent: qa-engineer
    inputs: [fix, reproduction, surrounding suite]
    outputs: [green reproduction, committed regression test named after the issue, full-suite results, verification in the failing environment]
    exit_gate: The reproduction passes, a regression test is committed with a name referencing the issue, the surrounding suite passes unchanged, and the fix is verified in the environment where the defect occurred — not only locally.
    max_loops: 3
    on_gate_failure: Return to stage 6. Declaring success without a reproduction is a guess with a commit message.
  - id: 10
    name: File the lesson
    goal: Put the knowledge where the next agent will find it before making the same mistake.
    skill: agent-memory-design
    agent: skill-curator
    inputs: [root cause, fix, attempt log, prevention gate]
    outputs: [gotchas entry for the trap, failure-modes entry if systemic, knowledge entry if it generalises, changelog entry]
    exit_gate: The trap, its trigger and the safe alternative are recorded in a retrievable location, and any generalisable lesson has been filed with sources and a review date.
    on_gate_failure: File at minimum a gotcha entry. An unrecorded lesson will be paid for again.
quality_gates:
  - An automated reproduction exists before any hypothesis is tested.
  - Determinism rate and trigger variable are recorded.
  - The full error was read literally at the correct layer, with symbols resolved.
  - The defect is isolated to a subsystem that reproduces it and only it.
  - One variable changed per test; the attempt log is complete, including killed hypotheses.
  - No disproved hypothesis is retried.
  - Root cause reaches "why was it not caught", and that gate is closed.
  - The fix is minimal, cause-directed and free of unrelated changes.
  - A regression test is committed and named after the issue.
  - The fix is verified in the environment where the defect appeared.
  - The lesson is filed in gotchas/, failure-modes/ or knowledge/.
artifacts:
  - symptom statement with expected behaviour and scope
  - candidate change list
  - automated reproduction with determinism rate
  - full resolved trace and exact failing input
  - isolation evidence
  - attempt log
  - four-level root cause analysis
  - fix plus prevention gate
  - regression test
  - gotchas / failure-modes / knowledge entry
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
    note: "Interleaving a hypothesis with an observation beats long ungrounded reasoning chains."
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Recording failed attempts in language prevents repeating them — the basis of the attempt log."
related: [skills/debugging/SKILL.md, skills/testing/SKILL.md, agents/qa-engineer/AGENT.md, failure-modes/, gotchas/]
---

# Workflow: Bug Investigation

```text
1 SYMPTOM → 2 WHAT CHANGED → 3 REPRODUCE → 4 OBSERVE → 5 ISOLATE
  → 6 HYPOTHESISE → 7 ROOT CAUSE → 8 FIX → 9 PROVE → 10 FILE THE LESSON
```

## The rule that makes this work

**No hypothesis is tested before an automated reproduction exists.** Without one, every
subsequent step is unverifiable: you cannot isolate what you cannot trigger, you cannot confirm
a hypothesis without an observation, and you cannot prove a fix without a failure to compare it to.

For intermittent defects, stage 3 changes goal: raise the reproduction rate first — parallelise,
amplify timing, add load, replay recorded traffic. A flake is a timing bug with a low reproduction
rate, not a different category of problem.

## The second rule

**One variable per test.** Change two things and the bug disappears, and you have learned nothing
except that you will see it again. The attempt log exists so that no disproved hypothesis is
retried — which is the most common failure mode in agent-driven debugging.

## Fast paths

```text
CLEAR DEPLOY CORRELATION   stages 1, 2, then revert-and-confirm; the full investigation still
                           runs afterwards to find why the change was not caught
KNOWN TRAP                 check gotchas/ and failure-modes/ at stage 1 — the answer is often
                           already recorded, which is the point of stage 10
ESCALATION                 if stage 3 cannot produce a reproduction after its loop budget,
                           escalate with everything gathered rather than guessing a fix
```

## Failure modes specific to this workflow

```text
SYMPTOM PATCHING        A try/catch, a null check, a sleep. The cause survives and returns
                        in a new shape. Stage 7 exists to prevent this.
UNREPRODUCED FIX        Declaring success with no reproduction — a guess with a commit message.
SHOTGUN DEBUGGING       Five changes at once; the bug "goes away" and nobody knows why.
ATTEMPT AMNESIA         Retrying a hypothesis the attempt log already disproved.
BLAME THE FRAMEWORK     Assuming a widely-used library is wrong before checking your own call,
                        then the version, then its issue tracker.
ENVIRONMENT BLINDNESS   Fixed locally, shipped to production, where the config differs.
ROOT-CAUSE STOPPING     Answering only "why did it fail" and never "why was it not caught".
NO LESSON FILED         Stage 10 skipped, so the same defect is re-diagnosed next quarter.
```

## References

- [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md) — techniques and isolation methods in detail
- [`skills/testing/SKILL.md`](../../skills/testing/SKILL.md) · [`skills/code-review/SKILL.md`](../../skills/code-review/SKILL.md)
- [`agents/qa-engineer/AGENT.md`](../../agents/qa-engineer/AGENT.md)
- [`failure-modes/`](../../failure-modes/) · [`gotchas/`](../../gotchas/) · [`knowledge/debugging/`](../../knowledge/debugging/)
- [`prompts/debugging/`](../../prompts/debugging/)
