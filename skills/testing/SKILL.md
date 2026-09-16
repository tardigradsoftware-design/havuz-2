---
name: testing
version: 1.0.0
description: >-
  Choose what to test and at which level, write tests that fail for the right reason, and keep the
  suite fast, deterministic and trusted — including how to test agents and LLM behaviour.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [testing, tdd, unit, integration, e2e, flaky, llm-evaluation]
applies_to: [any]
priority: 89
requires: []
conflicts_with: []
estimated_tokens: 2916
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Test selection
    anchor: "#test-selection"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Testing non-deterministic systems
    anchor: "#testing-non-deterministic-systems"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "GAIA: a benchmark for General AI Assistants"
    url: https://arxiv.org/abs/2311.12983
    type: research-paper
    published: 2023-11-24
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "Playwright"
    url: https://github.com/microsoft/playwright
    type: github-repository
    organization: Microsoft
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [debugging, code-review, browser-testing, performance-audit, refactoring]
related_repositories: [microsoft/playwright, vitest-dev/vitest, pytest-dev/pytest, EleutherAI/lm-evaluation-harness, promptfoo/promptfoo]
tests: 6
---

# Testing

## Purpose

Produce tests that **fail when the behaviour is wrong and for no other reason**. Coverage
percentages, test counts and green CI badges are outputs of that property, not substitutes
for it.

Two failure modes dominate in practice: tests that pass while the system is broken
(false confidence), and tests that fail while the system is fine (erosion of trust, then
deletion of the suite).

## When to Use

```text
□ Writing new behaviour (write the test alongside or first)
□ Fixing a bug (the regression test comes before the fix)
□ Refactoring (tests are the safety net; without them, refactoring is rewriting)
□ Deciding whether an existing suite is worth keeping
□ Building any LLM/agent feature, where "test" means "evaluate"
```

## When NOT to Use

```text
✗ Testing framework internals or language semantics — test your use of them
✗ Exhaustive getter/setter coverage to inflate a metric
✗ Snapshot tests as the primary strategy for logic (they assert "unchanged", not "correct")
✗ Throwaway spikes — but delete the spike before it becomes production code
```

## Test selection

Choose the **lowest level that can prove the property**, and reserve higher levels for
properties that only exist at that level.

```text
UNIT            a function/class in isolation; milliseconds; no I/O
                proves: logic, edge cases, error handling, pure transformations
INTEGRATION     your code + one real collaborator (database, queue, HTTP client, filesystem)
                proves: contract correctness, query validity, transaction behaviour,
                        serialisation, migrations
CONTRACT        producer and consumer tested against a shared schema
                proves: two services still speak the same language
COMPONENT/UI    one rendered component with a real DOM and user events
                proves: interaction, states, accessibility behaviour
E2E             the whole system through a real browser or API client
                proves: user-visible journeys, wiring, configuration, deployment shape
EXPLORATORY     a human or agent probing without a script
                proves: what the suite did not think of
```

Allocation (**RECOMMENDATION**, tune per system): most tests at UNIT and INTEGRATION;
COMPONENT for anything with interaction states; E2E limited to a small set of critical
journeys (login, checkout, the one thing your product does). An E2E-heavy suite is slow,
flaky and tells you *that* something broke rather than *what*.

What must always be tested, whatever the level:

```text
□ every boundary: empty, one, many, maximum, maximum+1, negative, null, unicode, whitespace
□ every error path: what the user sees, what is logged, what is retried
□ every state transition that money, auth or data integrity depends on
□ every bug you have ever fixed (regression test, named after the issue)
□ concurrency and ordering where the system assumes either
□ idempotency of anything retried
```

## Workflow

```text
CHARACTERISE → DESIGN → WRITE → RUN → DIAGNOSE → MAINTAIN
```

### 1. CHARACTERISE
For existing code, capture today's behaviour before changing it — even where you suspect
it is wrong. A characterisation test says "this is what it does", which is the only safe
starting point for "this is what it should do".

### 2. DESIGN
List the properties to prove, then the cases per property. Design the cases from the
**specification and the boundaries**, not from the implementation — tests derived from
the implementation only prove the implementation equals itself.

```text
Property: <observable behaviour>
Cases:    <input> → <expected output/side effect>
Oracle:   <how we know the expectation is right: spec, standard, human decision, prior behaviour>
```

The oracle question is the one most often skipped. An assertion with no oracle is a guess
frozen into CI.

### 3. WRITE
```text
AAA / Given-When-Then structure, visibly
one behaviour per test; a test with two assertions about different things is two tests
names that read as a specification: "rejects an expired token with 401", not "testToken2"
no logic in tests: no loops, no conditionals, no computed expectations
fixtures are data, not code paths; builders over giant literal blobs
deterministic inputs: fixed clocks, fixed seeds, fixed UUIDs, fixed locale and timezone
independent: any test runs alone, in any order, in parallel
assertions on outcomes, not on implementation details (no asserting private call counts
  unless the interaction IS the contract)
```

### 4. RUN
```text
fast feedback: the inner loop (< 10 s for the tests relevant to the change) must exist
CI gates: lint → type-check → unit → integration → component → e2e, failing fast
flakiness budget: zero. A flaky test is quarantined with an owner and a date, not re-run.
measure: duration per suite, failure rate over 30 days, time-to-detect for real bugs
```

### 5. DIAGNOSE
A failing test is answered with [`debugging`](../debugging/SKILL.md): reproduce, isolate,
one hypothesis per change. Never "fix" a failure by weakening the assertion without
writing down why the old assertion was wrong.

### 6. MAINTAIN
```text
□ Delete tests that assert nothing (they cost time and teach nothing)
□ Merge duplicates; a property should have one canonical test
□ Re-check the suite after every refactor: did coverage of *behaviour* survive?
□ Review tests in code review with the same seriousness as production code
□ Track escaped defects: every production bug becomes a test, and prompts the question
  "why did the suite not catch this?" — the answer updates the test strategy
```

## Testing non-deterministic systems

LLM and agent features cannot be unit-tested with equality assertions. Use evaluation
instead — see [`evaluations/`](../../evaluations/) and [`skills/`](../../evaluations/methodology/).

```text
DETERMINISTIC PARTS      Everything around the model is ordinary code and gets ordinary tests:
                         prompt assembly, retrieval, parsing, validation, tool dispatch,
                         retries, budgets, output schemas, error handling. Test these hard —
                         most "model bugs" are bugs here.
FIXTURE THE MODEL        For logic tests, replace the model with recorded responses.
                         Contract-test the parser against many recorded outputs, including
                         malformed ones.
TASK SUITE              A versioned set of tasks with inputs, a rubric and a scoring method.
                         Run on every change to prompts, models or retrieval.
SCORING                 exact match / structured-field match where possible;
                        rubric-graded by a judge model only where necessary, and the judge
                        itself must be validated against human labels;
                        never score with a vague "is this good?" prompt.
STATISTICS              n repetitions per task (≥3 for stochastic outputs), report mean and
                        spread, and compare with a stated significance threshold.
                        A single run proves nothing.
REGRESSION BASELINE     Keep the previous version's scores; regressions block release.
COST/LATENCY AS METRICS Track tokens and wall time alongside accuracy — a 2% accuracy gain
                        at 5× cost may be a regression.
HUMAN SPOT-CHECK        Sample graded outputs periodically; judge drift is real.
```

Rules:

```text
1. Separate "did the system behave correctly" from "was the output good".
   The first is testable; the second is evaluable.
2. Never ship a prompt change without running the task suite.
3. Record the model name, version, temperature, seed and date with every result —
   results are not comparable without them.
4. A passing eval with n=1 is an anecdote.
```

## Failure Modes

```text
IMPLEMENTATION MIRRORING  Tests derived from the code assert the code equals itself.
ASSERTION-FREE TESTS      "It didn't throw" is not a property.
SNAPSHOT AS ORACLE        Snapshots bless whatever the code did, including the bug.
FLAKE TOLERANCE           Re-running until green hides real concurrency defects.
OVER-MOCKING              Mocking so much that the test proves the mock, not the system.
E2E GRAVITY               Everything tested at the top: slow, flaky, uninformative failures.
TESTS NOT REVIEWED        Production code reviewed carefully; tests merged unread.
COVERAGE THEATRE          High line coverage, no boundary or error-path coverage.
SINGLE-RUN EVALS          One sample of a stochastic system treated as a result.
JUDGE UNVALIDATED         An LLM judge scoring outputs it was never calibrated against.
```

## Quality Checklist

```text
□ Level chosen as the lowest that can prove the property
□ Boundaries and error paths covered, not just the happy path
□ Every assertion has a stated oracle
□ Names read as specifications; one behaviour per test
□ Deterministic: fixed clock/seed/locale/timezone; no network in unit tests
□ Independent and parallel-safe
□ The inner loop runs in seconds; CI fails fast in level order
□ Zero tolerated flakes; quarantined ones have an owner and a date
□ Every fixed bug has a named regression test
□ For LLM features: deterministic parts unit-tested; task suite versioned; n ≥ 3;
  baseline compared; cost and latency tracked; model/version/date recorded
□ Tests reviewed as seriously as production code
□ Escaped defects analysed and the strategy updated
```

## Anti-Patterns

```text
✗ `expect(true).toBe(true)` and its many disguises
✗ A test that fails only when run after another test
✗ Mocking the database and then being surprised by a SQL error in production
✗ Sleeping instead of waiting for a condition
✗ Snapshot-testing a timestamp
✗ Testing the framework: "does React render a div"
✗ One E2E test covering fourteen assertions so nobody can tell what broke
✗ Running an agent eval once and reporting the number
```

## References

- [`debugging`](../debugging/SKILL.md) · [`browser-testing`](../browser-testing/SKILL.md)
- [`code-review`](../code-review/SKILL.md) · [`refactoring`](../refactoring/SKILL.md)
- [`evaluations/`](../../evaluations/) — task suites and scoring rubrics
- [`patterns/testing/`](../../patterns/testing/)
- [`knowledge/testing/`](../../knowledge/testing/)
- GAIA benchmark, arXiv:2311.12983 (verified 2026-09-15)
- Playwright — <https://github.com/microsoft/playwright> (Apache-2.0, verified 2026-09-15)

## Related Skills

`debugging` · `browser-testing` · `code-review` · `refactoring` · `performance-audit`

## Evaluation Criteria

```text
1. Escape rate: production defects per quarter that the suite should have caught (target → 0).
2. False-failure rate: failures with no real defect (target < 1% of runs).
3. Diagnostic value: fraction of failures where the message alone identifies the cause.
4. Speed: inner loop < 10 s; full CI < 15 min.
5. Behaviour coverage of boundaries and error paths, not line coverage.
6. For evals: repetitions per task ≥ 3, baseline comparison present, judge validated
   against human labels.
```

Test cases in [`tests/`](tests/).
