---
name: testing-strategy
version: 1.0.0
description: >-
  Design a test strategy from the failure modes that matter: assign each to the level that can catch it, distribute effort by cost and diagnostic value, and choose the metrics that reveal whether the suite is doing its job.
category: testing
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [testing, test-strategy, test-levels, coverage, ci, evaluation, quality]
applies_to: [any]
priority: 5
requires: []
conflicts_with: []
estimated_tokens: 2438
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
  - title: "Martin Fowler — The Practical Test Pyramid"
    url: https://martinfowler.com/articles/practical-test-pyramid.html
    type: methodology
    organization: "martinfowler.com"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "The cost, speed and isolation tradeoff across levels that step 3 reasons about; treated as a cost statement rather than a virtue statement."
  - title: "Martin Fowler — Eradicating Non-Determinism in Tests"
    url: https://martinfowler.com/articles/nonDeterminism.html
    type: methodology
    organization: "martinfowler.com"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "The argument behind step 8: a flaky suite is worse than a smaller honest one because it destroys the meaning of red."
  - title: "Pact documentation"
    url: https://docs.pact.io
    type: official-docs
    organization: "Pact Foundation"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Consumer-driven contract testing — the mechanism for the exclusive contract-level class in step 2."
related_skills: [testing, code-review, debugging, ai-safety-evaluation, browser-testing]
related_repositories: []
tests: 23
---
# Testing Strategy

## Purpose

Decide what the suite must prove, and at which level each thing can be proved. The question is never
"do we have tests" but "which failure modes are covered by which level" — because each level has a class
of bug it is the only one able to catch, and covering the same class at the wrong level costs more and
diagnoses worse.

## When to Use

```text
✓ a project is starting and its test approach must be chosen
✓ an existing suite is slow, flaky or failing to catch real defects
✓ a new risk class is being introduced: a payment path, an agent, a data migration, a public API
✓ test cost or CI duration has become a constraint on delivery
```

## When NOT to Use

```text
✗ A single failing test needs fixing. That is debugging, not strategy.
✗ Nothing has shipped and the domain is unknown. Write tests against what you have learned; a strategy
  designed before the first feature is speculative.
✗ The goal is a coverage number. Coverage measures execution, not assertion, and a quota produces tests
  that execute lines without checking behaviour.
✗ The system is entirely deterministic and small. Test it directly; the level analysis still applies but
  the distribution question does not.
```

## Workflow

```text
1. ENUMERATE THE FAILURE MODES THAT MATTER.   From the requirements, the threat model and every past
   incident: wrong computation, broken wiring, contract violation, environment failure, data corruption,
   race condition, security bypass, cost or latency regression, incorrect probabilistic behaviour. A
   strategy that does not start here allocates effort by habit.

2. ASSIGN EACH TO THE LEVEL THAT CAN CATCH IT.   Each level has an exclusive class:
     - unit            off-by-one, null handling, rounding, state-machine transitions, pure edge cases
     - integration     a valid query that is wrong for the schema, a field name differing by case, a
                       naive timezone, a transaction that aborts and is not retried
     - contract        a breaking API change that passes every test in both repositories separately
     - end-to-end      configuration, secrets, CORS and cookie policy, proxy behaviour, migration order
     - property-based  the edge case no example author would think of: unicode, empty collections,
                       extreme numbers, deep nesting
     - visual          layout breakage from a dependency upgrade, responsive failures at untested widths
     - evaluation      aggregate quality of probabilistic behaviour, over a distribution rather than a run
     - adversarial     injection attempts, malformed tool results, hostile retrieved content
   A failure mode with no level assigned is uncovered, and that is a finding.

3. SET THE DISTRIBUTION FROM RISK, NOT FROM A PYRAMID DEFAULT.   Roughly 70% unit, 20% integration, 10%
   contract and end-to-end is a starting point. A data pipeline or an orchestration layer concentrates its
   risk in integration and should invert the distribution — and say why. The pyramid is a cost statement,
   not a virtue statement.

4. DECIDE WHAT IS MOCKED AND WHAT IS REAL.   Mock at boundaries you do not own; use real collaborators
   for the wiring you do. An in-memory fake database that accepts any SQL proves nothing about the SQL.
   Assert on outcomes, not on call counts — a test coupled to call structure fails when the
   implementation is refactored correctly.

5. DEFINE THE RUN TIERS.   What runs on every commit (fast, precise, unit-heavy), on every PR
   (integration and contract), on merge and nightly (end-to-end, visual, property, evaluation), and what
   never blocks (real network, long-running, quarantined). A suite with one tier is either too slow or too
   shallow.

6. ADD THE EVALUATION LAYER FOR PROBABILISTIC BEHAVIOUR.   A labelled task set with a deterministic metric
   or a validated judge, a baseline, a threshold and a statement of what the score does not establish.
   Unit tests around the deterministic shell give false confidence about the model inside it.

7. CHOOSE THE METRICS THAT REVEAL SUITE HEALTH.   Not coverage as a target. Use: mutation score on the
   critical modules (do the tests fail when the code is deliberately broken?), escaped-defect analysis
   (every production bug answers "which level should have caught this, and why did it not?"), CI duration
   at each tier, flake rate, and failure-diagnosis time.

8. BUILD THE QUARANTINE PATH BEFORE YOU NEED IT.   A flaky test must leave the blocking path the same day,
   with a recorded failure signature, an owner, a repair-by date, and a CI policy that fails on a
   quarantine older than the deadline. Silently skipped tests become permanent.

9. WRITE THE ESCAPED-DEFECT RULE.   Every production bug produces a test at the level that should have
   caught it — not at the level that is easiest. This is what makes the strategy converge on the real risk
   distribution instead of the imagined one.

10. RECORD THE STRATEGY AND ITS REVISIT TRIGGER.   The failure-mode-to-level mapping, the distribution and
   its justification, the run tiers and the metrics. Revisit on a new risk class, a new integration, a
   change in CI duration, or an escaped defect.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| A failure mode has no level | it is absent from the mapping | assign one, or record the acceptance with a reason |
| Effort concentrated at the wrong level | e2e suite is the primary net; slow, brittle, imprecise | move assertions down to the level that diagnoses them |
| Tests coupled to call structure | failures on correct refactors | assert outcomes, not call counts |
| Fake collaborators prove nothing | integration tests pass against an in-memory stub | use a real engine in a container for the wiring |
| Coverage rose, defects did not fall | execution without assertion | measure mutation score on critical modules |
| No evaluation layer | probabilistic regressions found by users | add a labelled task set with a baseline and threshold |
| Flaky tests left in | "just re-run it" becomes normal | quarantine the same day, with an owner and a deadline |
| Regression added at the easy level | the bug recurs elsewhere | add it at the level that should have caught it |
| One run tier | CI too slow or too shallow | split into commit, PR, merge and nightly tiers |

## Quality Checklist

```text
□ the failure modes that matter are enumerated from requirements, threats and incidents
□ every failure mode is assigned to the level that can catch it, or its absence is accepted in writing
□ the distribution is justified by risk, not defaulted from a pyramid
□ mocking is at unowned boundaries and real collaborators cover the wiring
□ assertions are on outcomes, not call structure
□ run tiers are defined: commit, PR, merge/nightly, non-blocking
□ an evaluation layer exists for probabilistic behaviour, with a baseline and threshold
□ health metrics are chosen: mutation score, escaped defects, CI duration, flake rate
□ the quarantine path exists with an owner, a deadline and a CI policy
□ the escaped-defect rule is stated
□ the strategy is recorded with its revisit trigger
```

## Anti-Patterns

```text
✗ AN E2E SUITE AS THE SAFETY NET.   Slow, brittle, imprecise; failures need a human to diagnose, so
  they get skipped, so the suite rots.
✗ COVERAGE AS A TARGET.   A quota produces tests that execute lines without checking behaviour, which is
  worse than no tests because it creates false assurance.
✗ MOCKING THE THING UNDER TEST.   Testing the mock's behaviour.
✗ INTEGRATION TESTS WITH NO REAL COLLABORATOR.   The wiring is what integration tests are for.
✗ SNAPSHOT TESTS APPROVED WITHOUT READING.   A regression recorded as the new baseline.
✗ TESTING THE FRAMEWORK.   That React renders a component when its state changes is not your code.
✗ NO EVALUATION LAYER FOR A PROBABILISTIC SYSTEM.   Deterministic tests around a non-deterministic core
  measure the shell.
✗ LEAVING FLAKY TESTS IN.   The cost is not the occasional failure; it is the erosion of the meaning of
  failure.
✗ A STRATEGY DESIGNED BEFORE THE FIRST FEATURE.   Speculative levels for risks nobody has met yet.
```

## References

- [`knowledge/testing/test-levels.md`](../../knowledge/testing/test-levels.md) — what each level can and cannot prove
- [`knowledge/testing/flaky-tests.md`](../../knowledge/testing/flaky-tests.md) — diagnosis, quarantine and repair
- [`knowledge/evaluation/llm-judge-validation.md`](../../knowledge/evaluation/llm-judge-validation.md) — the probabilistic layer
- [`skills/testing/SKILL.md`](../testing/SKILL.md) · [`skills/code-review/SKILL.md`](../code-review/SKILL.md) · [`skills/debugging/SKILL.md`](../debugging/SKILL.md) · [`skills/ai-safety-evaluation/SKILL.md`](../ai-safety-evaluation/SKILL.md)
- [`agents/qa-engineer/AGENT.md`](../../agents/qa-engineer/AGENT.md) · [`workflows/release-checklist/WORKFLOW.md`](../../workflows/release-checklist/WORKFLOW.md)
- [`patterns/testing/`](../../patterns/testing/) · [`anti-patterns/testing/`](../../knowledge/testing/)
- The Practical Test Pyramid — <https://martinfowler.com/articles/practical-test-pyramid.html> · Pact — <https://docs.pact.io> · Hypothesis — <https://hypothesis.readthedocs.io>
