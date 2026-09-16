---
id: testing-test-levels
title: "Test levels: what belongs where and what each level can prove"
domain: testing
summary: >-
  The unit / integration / contract / end-to-end / property / snapshot ladder, what each level can and cannot prove, the cost-benefit distribution that determines where effort goes, and the specific bugs each level is the only one able to catch.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [testing, unit-tests, integration-tests, e2e, contract-testing, property-testing, test-strategy, coverage]
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
  - title: "Martin Fowler — The Practical Test Pyramid"
    url: https://martinfowler.com/articles/practical-test-pyramid.html
    type: methodology
    organization: martinfowler.com
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The canonical statement of the cost/speed/isolation tradeoff across test levels; the guidance here is the operational version of it, with the agent-specific levels added."
---
# Test Levels

## What each level can prove

The question is never "do we have tests" but "which failure modes are covered by which level". Each
level has a class of bug it is the **only** level that can catch.

```text
UNIT                a function or class behaves correctly in isolation, given its inputs.
                    Proves: logic, edge cases, error handling, boundary arithmetic.
                    Cannot prove: that the collaborators exist, that the wiring is right, or that
                    the assumptions about the database, the network or the framework are true.
                    Only level that catches: off-by-one, null handling, rounding, state-machine
                    transitions, pure-function edge cases.

INTEGRATION         components work together against real (or realistic) collaborators — a real
                    database in a container, a real HTTP client against a stub server.
                    Proves: wiring, serialisation, transaction boundaries, schema agreement.
                    Only level that catches: a query that is valid SQL and wrong for the schema, a
                    JSON field name that differs by case, a timezone that is stored naive, a
                    transaction that aborts and is not retried.

CONTRACT            two independently deployed services agree on an interface. Consumer-driven
                    (Pact-style) or schema-validated (OpenAPI).
                    Proves: the producer's change does not break a consumer that is not in this
                    repository.
                    Only level that catches: a breaking API change that passes every test in both
                    repositories separately.

END-TO-END          the deployed system performs a user journey.
                    Proves: the whole path works, including configuration, DNS, TLS and deployment.
                    Cannot prove: much about why it fails — the diagnostic surface is enormous.
                    Only level that catches: environment and configuration errors, missing secrets,
                    CORS and cookie policy, reverse-proxy behaviour, migration ordering.

PROPERTY-BASED      a stated invariant holds across generated inputs.
                    Proves: the invariant, over a far wider input space than examples reach.
                    Only level that catches: rare edge cases no example author would think of —
                    unicode, empty collections, extreme numbers, deeply nested structures.

SNAPSHOT / GOLDEN   output matches a recorded baseline.
                    Proves: nothing changed unintentionally. Proves nothing about correctness — the
                    baseline may have been wrong when recorded.
                    Useful for: serialisation formats, generated code, rendered markup, prompts.
                    Dangerous when: the diff is routinely approved without reading, which turns it
                    into a ceremony that hides regressions.

VISUAL REGRESSION   rendered pixels or DOM structure match a baseline across viewports.
                    Only level that catches: layout breakage from a dependency upgrade, a CSS change
                    that affects an unrelated component, responsive failures at widths nobody tests.

EXPLORATORY / MANUAL human judgement about whether the thing is right and usable.
                    Only level that catches: "this works exactly as specified and is still wrong".
```

## Agent-specific levels

Systems whose behaviour is probabilistic need levels that classical testing does not have:

```text
EVALUATION SUITE      a labelled task set scored by a deterministic metric or a validated judge.
                      Proves: aggregate quality on a distribution, not correctness of one run.
                      Requires: a baseline, a threshold, and a statement of what the score does not
                      establish. See knowledge/evaluation/llm-judge-validation.md.
ADVERSARIAL TASKS     prompt-injection attempts, jailbreaks, malformed tool results, hostile
                      content in retrieved documents, with a known correct behaviour (refuse, or
                      escalate, and take no action).
DETERMINISM-BOUNDARY  tests that assert the deterministic parts are deterministic — schema
                      validation of structured output, tool-argument shapes, routing decisions —
                      while the non-deterministic parts are evaluated statistically.
TOOL-SANDBOX TESTS    the agent against a mock tool layer that records every call. Proves: which
                      tools are reached, with what arguments, in what order, and that Tier-3
                      actions gate on approval.
COST AND LATENCY      token counts and wall time per task class, as a regression metric. A quality
                      improvement that triples cost is a change in the product, not a win.
```

## Distribution of effort

```text
                fast  cheap  precise failure        slow  expensive  broad coverage
UNIT            ████████████████████░░░░            ░░░░
INTEGRATION     ░░░░████████████░░░░░░░░            ░░░░░░░░
CONTRACT        ░░░░░░░░████████░░░░░░░░            ░░░░░░░░
E2E             ░░░░░░░░░░░░░░░░████████            ░░░░░░░░

Target distribution (a starting point, not a law):
  ~70% unit        fast feedback, precise diagnosis, cheap to run on every commit
  ~20% integration the wiring and the real collaborators, run on every PR
  ~10% contract + e2e  the deployed path and cross-repo agreements, run on merge and nightly
  plus: property tests on anything with a stated invariant, and an evaluation suite for anything
  probabilistic
```

The pyramid is a cost statement, not a virtue statement. A system whose risk is concentrated in
integration — a data pipeline, an orchestration layer — should invert its distribution and say why.

## Coverage

```text
Coverage measures what was executed, not what was asserted. 100% coverage with no assertions is
worth zero.

USE IT FOR     finding code that is never executed by any test — genuinely untested paths, dead
               code, error branches nobody simulated
DO NOT USE IT  as a quality target. A coverage quota produces tests that execute lines without
               checking behaviour, which is worse than no tests because it creates false assurance.

MORE USEFUL METRICS
  mutation score          do the tests fail when the code is deliberately broken? Measures assertion
                          strength rather than execution.
  escaped-defect analysis every production bug gets a question: which level should have caught it,
                          and why did it not? The answer is the test to add.
  failure-diagnosis time  when a test fails, how long to identify the cause? A proxy for whether
                          failures are at the right level.
```

## Anti-patterns

```text
✗ An e2e suite as the primary safety net.   Slow, brittle, imprecise. Failures require a human to
  diagnose, so they get skipped, so the suite rots.
✗ Unit tests that mock the thing under test.  Testing the mock's behaviour.
✗ Mocking so deeply that the test asserts on call counts rather than outcomes.  The test now fails
  when the implementation is refactored correctly — it has coupled to structure, not behaviour.
✗ Integration tests with no real collaborator.  An in-memory fake database that accepts any SQL
  proves nothing about the SQL.
✗ Snapshot tests approved without reading.  A regression recorded as the new baseline.
✗ Flaky tests left in the suite.  A suite that intermittently fails trains everyone to re-run
  instead of investigate, which destroys the signal for real failures. See flaky-tests.md.
✗ Testing framework behaviour.  That React renders a component when its state changes is not your
  code. Test your decisions, not the library's contract.
✗ No evaluation suite for a probabilistic system.  Unit tests on the deterministic shell give false
  confidence about the model's behaviour inside it.
```

## References

- [`knowledge/testing/flaky-tests.md`](flaky-tests.md) — the failure mode that destroys suite signal
- [`knowledge/evaluation/llm-judge-validation.md`](../evaluation/llm-judge-validation.md) — the probabilistic level
- [`skills/testing-strategy/SKILL.md`](../../skills/testing-strategy/SKILL.md) · [`skills/code-review/SKILL.md`](../../skills/code-review/SKILL.md) · [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md)
- [`patterns/testing/`](../../patterns/testing/) · [`anti-patterns/testing/`](./)
- The Practical Test Pyramid — <https://martinfowler.com/articles/practical-test-pyramid.html> · Pact — <https://docs.pact.io> · Hypothesis — <https://hypothesis.readthedocs.io>
