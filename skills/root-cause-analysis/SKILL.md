---
name: root-cause-analysis
version: 1.0.0
description: >-
  Find the actual cause of a defect or incident rather than its nearest symptom: reproduce it, form falsifiable hypotheses, bisect to the introducing change, distinguish cause from contributor, and verify the fix removes the cause.
category: debugging
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [root-cause, debugging, incidents, hypothesis, bisection, postmortem, diagnosis]
applies_to: [any]
priority: 3
requires: []
conflicts_with: []
estimated_tokens: 2188
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
  - title: "Martin Fowler — Eradicating Non-Determinism in Tests"
    url: https://martinfowler.com/articles/nonDeterminism.html
    type: methodology
    organization: "martinfowler.com"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "The stress-reproduction and randomisation techniques used in steps 1 and 6 when the failure is intermittent."
  - title: "Google SRE Book — Postmortem Culture: Learning from Failure"
    url: https://sre.google/sre-book/postmortem-culture/
    type: official-docs
    organization: "Google"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "Blameless analysis, the distinction between cause and contributing factors, and the systemic-question step."
  - title: "git-bisect documentation"
    url: https://git-scm.com/docs/git-bisect
    type: official-docs
    organization: "Git project"
    license: GPL-2.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The automated bisection procedure in step 6, which requires a deterministic reproduction to score each commit."
related_skills: [debugging, testing-strategy, performance-optimization, code-review]
related_repositories: []
tests: 9
---
# Root Cause Analysis

## Purpose

Identify the cause whose removal prevents recurrence — not the nearest thing that looked wrong. The
discipline is hypothesis-driven: reproduce, predict, test, eliminate. A fix applied to a symptom produces
a system that fails again in a different shape, and the second failure is harder to diagnose than the
first because the obvious explanation has already been used.

## When to Use

```text
✓ a defect recurs after being "fixed"
✓ an incident needs a cause that can be acted on
✓ a failure is intermittent and no hypothesis has survived contact with it
✓ a fix is proposed and it is not clear whether it addresses the cause
```

## When NOT to Use

```text
✗ The bug is obvious, local and reproducible, and the fix is one line. Fix it; a full analysis is
  overhead.
✗ Nothing can be reproduced and no telemetry exists. Restore observability first — analysis without
  evidence is speculation with confidence.
✗ The goal is attribution of blame. A blame-oriented analysis produces defensive reports and hidden
  information.
✗ The cause is a decision rather than a defect. That is an architecture or process question.
```

## Workflow

```text
1. REPRODUCE, OR EXPLAIN WHY YOU CANNOT.   A deterministic reproduction is worth more than any amount of
   reasoning. If it is intermittent, characterise the conditions: what differs between the runs that fail
   and the runs that do not. Record the reproduction as a script or a test before going further — it is
   what verifies the fix later.

2. ESTABLISH THE TIMELINE FROM EVIDENCE.   Logs, traces, metrics, deploys, config changes, migrations and
   data changes, ordered by timestamp. "What changed" is the highest-yield question available, and the
   answer is usually in the timeline rather than in the code.

3. WRITE THE OBSERVED BEHAVIOUR PRECISELY.   What happened, what was expected, what the difference is, and
   what is NOT happening that could have been. Vague symptom descriptions generate vague hypotheses.

4. FORM MULTIPLE FALSIFIABLE HYPOTHESES.   At least three, including one you expect to be wrong and one
   that is uncomfortable. Each must make a prediction that an observation can refute. A hypothesis that
   cannot be refuted by any evidence is not a hypothesis.

5. TEST THE CHEAPEST DISCRIMINATING OBSERVATION FIRST.   Choose the observation that separates the most
   hypotheses for the least effort — not the one that confirms your favourite. Log a value, read a trace,
   run the reproduction with one variable changed.

6. BISECT WHEN SOMETHING CHANGED.   Code: git bisect against the reproduction. Data: partition the input
   set until the failing subset is minimal. Time: narrow the window between the last known-good and the
   first known-bad. Bisection converts a search into a logarithm and is the most underused tool here.

7. DISTINGUISH CAUSE FROM CONTRIBUTOR.   A latent bug plus a triggering condition plus a missing guard is
   three factors, and removing any one prevents recurrence. Name all of them, then decide which to fix —
   usually the guard, because it is cheapest and covers the class, and the latent bug, because it will be
   triggered again differently.

8. ASK WHY THE SYSTEM PERMITTED IT.   The defect had a cause; the fact that it reached production has a
   different one. Which test was missing, which review did not catch it, which alert did not exist, which
   assumption was undocumented. This is where the durable fixes are.

9. VERIFY THE FIX REMOVES THE CAUSE.   Run the reproduction: it must fail before the fix and pass after.
   Run the suite at the level that should have caught it. Confirm the contributing factors are addressed
   or explicitly accepted. A fix that cannot be shown to remove the cause is a mitigation.

10. ADD THE TEST AT THE RIGHT LEVEL.   The level that should have caught it, not the level that is easiest
   — see testing-strategy. A regression test added at the wrong level will not catch the next variant.

11. WRITE IT DOWN.   Symptom, timeline, hypotheses considered and how each was eliminated, the cause and
   its contributors, the fix, the verification, and the systemic change. Including the eliminated
   hypotheses: that is what stops the next person re-walking the same path.

12. QUARANTINE WHAT YOU COULD NOT EXPLAIN.   If the investigation stopped without a cause, record what is
   known, what was ruled out, and what observation would restart it. An unexplained failure recorded as
   resolved will recur and will be harder the second time.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Fixed the symptom, it recurred | the reproduction still fails in a new shape | return to step 4; the cause was not identified |
| No reproduction | hypotheses cannot be tested | restore observability before analysing |
| One hypothesis, pursued to confirmation | no alternatives were written | generate at least three, including an uncomfortable one |
| Hypothesis is unfalsifiable | no observation could refute it | restate it as a prediction |
| Cause found, system question skipped | the same class returns elsewhere | ask why it reached production and fix that too |
| Fix cannot be shown to work | no before/after on the reproduction | the fix is a mitigation; say so |
| Regression test at the easy level | the variant recurs | add it at the level that should have caught it |
| Timeline assembled from memory | deploys and config changes are missing | build it from logs and records, not recall |
| Investigation abandoned silently | nobody knows what was ruled out | record what is known and what would restart it |
| Blame framing | information is withheld | analyse the system; people acted on the information they had |

## Quality Checklist

```text
□ the behaviour is reproducible, or the reason it is not is recorded
□ the timeline was built from logs, deploys and config changes
□ the observed and expected behaviours are stated precisely
□ at least three falsifiable hypotheses were written, each with a prediction
□ the cheapest discriminating observation was tested first
□ bisection was used where something changed
□ cause and contributing factors are distinguished
□ the systemic question was asked and answered
□ the reproduction fails before the fix and passes after
□ the regression test is at the level that should have caught it
□ the write-up includes the eliminated hypotheses
□ anything unexplained is quarantined with a restart condition
```

## Anti-Patterns

```text
✗ FIXING THE FIRST PLAUSIBLE THING.   The most common failure, and invisible in the diff.
✗ ONE HYPOTHESIS.   Confirmation follows, and the cause survives.
✗ UNFALSIFIABLE HYPOTHESES.   "It might be a race" with no observation that would refute it.
✗ ANALYSIS WITHOUT A REPRODUCTION.   Speculation with confidence.
✗ STOPPING AT THE DEFECT.   The reason it reached production is a separate cause with a cheaper fix.
✗ A FIX NOBODY VERIFIED AGAINST THE CAUSE.   A mitigation recorded as a resolution.
✗ REGRESSION TEST AT THE EASIEST LEVEL.   The next variant is not caught.
✗ TIMELINE FROM MEMORY.   Deploys, config changes and migrations are the usual cause and are never
  remembered accurately.
✗ OMITTING THE ELIMINATED HYPOTHESES.   The next investigator repeats the work.
✗ BLAME.   Defensive reports, hidden information, and no systemic fix.
```

## References

- [`skills/debugging/SKILL.md`](../debugging/SKILL.md) — the interactive loop this formalises
- [`knowledge/testing/test-levels.md`](../../knowledge/testing/test-levels.md) — choosing the level for the regression test
- [`knowledge/testing/flaky-tests.md`](../../knowledge/testing/flaky-tests.md) — when the defect is non-determinism itself
- [`knowledge/performance/backend-profiling.md`](../../knowledge/performance/backend-profiling.md) — the measurement discipline, applied to latency
- [`knowledge/architecture/system-design-checklist.md`](../../knowledge/architecture/system-design-checklist.md) — the failure-mode and observability questions
- [`workflows/bug-investigation/WORKFLOW.md`](../../workflows/bug-investigation/WORKFLOW.md) · [`agents/qa-engineer/AGENT.md`](../../agents/qa-engineer/AGENT.md)
- [`failure-modes/`](../../failure-modes/) · [`gotchas/`](../../gotchas/) · [`anti-patterns/`](../../anti-patterns/)
