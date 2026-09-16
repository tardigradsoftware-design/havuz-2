# Test cases — `testing-strategy`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Decide what the suite must prove, and at which level each thing can be proved. The question is never "do we have tests" but "which failure modes are covered by which level" — because each level has a class of bug it is the only one able to…
WHEN     the agent executes `testing-strategy` end to end on that task
THEN     the workflow runs in its stated order — "ENUMERATE THE FAILURE MODES THAT MATTER" through to "RECORD THE STRATEGY AND ITS REVISIT TRIGGER"; and before delivery these specific conditions hold: "the failure modes that matter are enumerated from requirements, threats and incidents"; "run tiers are defined: commit, PR, merge/nightly, non-blocking"; "the strategy is recorded with its revisit trigger"
FAIL IF  "the failure modes that matter are enumerated from requirements, threats and incidents" is false, or "the strategy is recorded with its revisit trigger" is false, or the result is delivered before "RECORD THE STRATEGY AND ITS REVISIT TRIGGER" has run
```

## Case 2 — Declines: A single failing test needs fixing.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single failing test needs fixing.
WHEN     the agent considers `testing-strategy` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is debugging, not strategy."
FAIL IF  the skill is run on a task where "A single failing test needs fixing.", and the consequence that exclusion states follows — "That is debugging, not strategy."; or `testing-strategy` is declined without naming that exclusion
```

## Case 3 — Declines: Nothing has shipped and the domain is unknown.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing has shipped and the domain is unknown.
WHEN     the agent considers `testing-strategy` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Write tests against what you have learned; a strategy designed before the first feature is speculative."
FAIL IF  the skill is run on a task where "Nothing has shipped and the domain is unknown.", and the consequence that exclusion states follows — "Write tests against what you have learned; a strategy designed before the first feature is speculative."; or `testing-strategy` is declined without naming that exclusion
```

## Case 4 — Declines: The goal is a coverage number.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The goal is a coverage number.
WHEN     the agent considers `testing-strategy` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Coverage measures execution, not assertion, and a quota produces tests that execute lines without checking behaviour."
FAIL IF  the skill is run on a task where "The goal is a coverage number.", and the consequence that exclusion states follows — "Coverage measures execution, not assertion, and a quota produces tests that execute lines without checking behaviour."; or `testing-strategy` is declined without naming that exclusion
```

## Case 5 — Declines: The system is entirely deterministic and small.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The system is entirely deterministic and small.
WHEN     the agent considers `testing-strategy` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Test it directly; the level analysis still applies but the distribution question does not."
FAIL IF  the skill is run on a task where "The system is entirely deterministic and small.", and the consequence that exclusion states follows — "Test it directly; the level analysis still applies but the distribution question does not."; or `testing-strategy` is declined without naming that exclusion
```

## Case 6 — Detects: A failure mode has no level

```text
GIVEN    A run of this skill in which the known failure mode is present: A failure mode has no level
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "it is absent from the mapping" — and the response applied is the documented one: "assign one, or record the acceptance with a reason"
FAIL IF  "A failure mode has no level" reaches the output because "it is absent from the mapping" was never checked; or it is caught but the response taken is not "assign one, or record the acceptance with a reason"
```

## Case 7 — Detects: Effort concentrated at the wrong level

```text
GIVEN    A run of this skill in which the known failure mode is present: Effort concentrated at the wrong level
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "e2e suite is the primary net; slow, brittle, imprecise" — and the response applied is the documented one: "move assertions down to the level that diagnoses them"
FAIL IF  "Effort concentrated at the wrong level" reaches the output because "e2e suite is the primary net; slow, brittle, imprecise" was never checked; or it is caught but the response taken is not "move assertions down to the level that diagnoses them"
```

## Case 8 — Detects: Tests coupled to call structure

```text
GIVEN    A run of this skill in which the known failure mode is present: Tests coupled to call structure
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "failures on correct refactors" — and the response applied is the documented one: "assert outcomes, not call counts"
FAIL IF  "Tests coupled to call structure" reaches the output because "failures on correct refactors" was never checked; or it is caught but the response taken is not "assert outcomes, not call counts"
```

## Case 9 — Detects: Fake collaborators prove nothing

```text
GIVEN    A run of this skill in which the known failure mode is present: Fake collaborators prove nothing
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "integration tests pass against an in-memory stub" — and the response applied is the documented one: "use a real engine in a container for the wiring"
FAIL IF  "Fake collaborators prove nothing" reaches the output because "integration tests pass against an in-memory stub" was never checked; or it is caught but the response taken is not "use a real engine in a container for the wiring"
```

## Case 10 — Detects: Coverage rose, defects did not fall

```text
GIVEN    A run of this skill in which the known failure mode is present: Coverage rose, defects did not fall
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "execution without assertion" — and the response applied is the documented one: "measure mutation score on critical modules"
FAIL IF  "Coverage rose, defects did not fall" reaches the output because "execution without assertion" was never checked; or it is caught but the response taken is not "measure mutation score on critical modules"
```

## Case 11 — Detects: No evaluation layer

```text
GIVEN    A run of this skill in which the known failure mode is present: No evaluation layer
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "probabilistic regressions found by users" — and the response applied is the documented one: "add a labelled task set with a baseline and threshold"
FAIL IF  "No evaluation layer" reaches the output because "probabilistic regressions found by users" was never checked; or it is caught but the response taken is not "add a labelled task set with a baseline and threshold"
```

## Case 12 — Detects: Flaky tests left in

```text
GIVEN    A run of this skill in which the known failure mode is present: Flaky tests left in
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "just re-run it" becomes normal" — and the response applied is the documented one: "quarantine the same day, with an owner and a deadline"
FAIL IF  "Flaky tests left in" reaches the output because "just re-run it" becomes normal" was never checked; or it is caught but the response taken is not "quarantine the same day, with an owner and a deadline"
```

## Case 13 — Detects: Regression added at the easy level

```text
GIVEN    A run of this skill in which the known failure mode is present: Regression added at the easy level
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the bug recurs elsewhere" — and the response applied is the documented one: "add it at the level that should have caught it"
FAIL IF  "Regression added at the easy level" reaches the output because "the bug recurs elsewhere" was never checked; or it is caught but the response taken is not "add it at the level that should have caught it"
```

## Case 14 — Detects: One run tier

```text
GIVEN    A run of this skill in which the known failure mode is present: One run tier
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "CI too slow or too shallow" — and the response applied is the documented one: "split into commit, PR, merge and nightly tiers"
FAIL IF  "One run tier" reaches the output because "CI too slow or too shallow" was never checked; or it is caught but the response taken is not "split into commit, PR, merge and nightly tiers"
```

## Case 15 — Avoids: AN E2E SUITE AS THE SAFETY NET

```text
GIVEN    A situation that invites the anti-pattern "AN E2E SUITE AS THE SAFETY NET", whose stated consequence is: Slow, brittle, imprecise; failures need a human to diagnose, so they get skipped, so the suite rots.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "AN E2E SUITE AS THE SAFETY NET" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Slow, brittle, imprecise; failures need a human to diagnose, so they get skipped, so the suite rots."
FAIL IF  "AN E2E SUITE AS THE SAFETY NET" appears in the output — that is, "Slow, brittle, imprecise; failures need a human to diagnose, so they get skipped, so the suite rots."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 16 — Avoids: COVERAGE AS A TARGET

```text
GIVEN    A situation that invites the anti-pattern "COVERAGE AS A TARGET", whose stated consequence is: A quota produces tests that execute lines without checking behaviour, which is worse than no tests because it creates false assurance.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "COVERAGE AS A TARGET" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A quota produces tests that execute lines without checking behaviour, which is worse than no tests because it creates false assurance."
FAIL IF  "COVERAGE AS A TARGET" appears in the output — that is, "A quota produces tests that execute lines without checking behaviour, which is worse than no tests because it creates false assurance."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 17 — Avoids: MOCKING THE THING UNDER TEST

```text
GIVEN    A situation that invites the anti-pattern "MOCKING THE THING UNDER TEST", whose stated consequence is: Testing the mock's behaviour.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "MOCKING THE THING UNDER TEST" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Testing the mock's behaviour."
FAIL IF  "MOCKING THE THING UNDER TEST" appears in the output — that is, "Testing the mock's behaviour."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 18 — Avoids: INTEGRATION TESTS WITH NO REAL COLLABORATOR

```text
GIVEN    A situation that invites the anti-pattern "INTEGRATION TESTS WITH NO REAL COLLABORATOR", whose stated consequence is: The wiring is what integration tests are for.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "INTEGRATION TESTS WITH NO REAL COLLABORATOR" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The wiring is what integration tests are for."
FAIL IF  "INTEGRATION TESTS WITH NO REAL COLLABORATOR" appears in the output — that is, "The wiring is what integration tests are for."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 19 — Avoids: SNAPSHOT TESTS APPROVED WITHOUT READING

```text
GIVEN    A situation that invites the anti-pattern "SNAPSHOT TESTS APPROVED WITHOUT READING", whose stated consequence is: A regression recorded as the new baseline.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "SNAPSHOT TESTS APPROVED WITHOUT READING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A regression recorded as the new baseline."
FAIL IF  "SNAPSHOT TESTS APPROVED WITHOUT READING" appears in the output — that is, "A regression recorded as the new baseline."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 20 — Avoids: TESTING THE FRAMEWORK

```text
GIVEN    A situation that invites the anti-pattern "TESTING THE FRAMEWORK", whose stated consequence is: That React renders a component when its state changes is not your code.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "TESTING THE FRAMEWORK" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "That React renders a component when its state changes is not your code."
FAIL IF  "TESTING THE FRAMEWORK" appears in the output — that is, "That React renders a component when its state changes is not your code."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 21 — Avoids: NO EVALUATION LAYER FOR A PROBABILISTIC SYSTEM

```text
GIVEN    A situation that invites the anti-pattern "NO EVALUATION LAYER FOR A PROBABILISTIC SYSTEM", whose stated consequence is: Deterministic tests around a non-deterministic core measure the shell.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "NO EVALUATION LAYER FOR A PROBABILISTIC SYSTEM" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Deterministic tests around a non-deterministic core measure the shell."
FAIL IF  "NO EVALUATION LAYER FOR A PROBABILISTIC SYSTEM" appears in the output — that is, "Deterministic tests around a non-deterministic core measure the shell."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 22 — Avoids: LEAVING FLAKY TESTS IN

```text
GIVEN    A situation that invites the anti-pattern "LEAVING FLAKY TESTS IN", whose stated consequence is: The cost is not the occasional failure; it is the erosion of the meaning of failure.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "LEAVING FLAKY TESTS IN" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The cost is not the occasional failure; it is the erosion of the meaning of failure."
FAIL IF  "LEAVING FLAKY TESTS IN" appears in the output — that is, "The cost is not the occasional failure; it is the erosion of the meaning of failure."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```

## Case 23 — Avoids: A STRATEGY DESIGNED BEFORE THE FIRST FEATURE

```text
GIVEN    A situation that invites the anti-pattern "A STRATEGY DESIGNED BEFORE THE FIRST FEATURE", whose stated consequence is: Speculative levels for risks nobody has met yet.
WHEN     the agent applies `testing-strategy` in that situation
THEN     "A STRATEGY DESIGNED BEFORE THE FIRST FEATURE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Speculative levels for risks nobody has met yet."
FAIL IF  "A STRATEGY DESIGNED BEFORE THE FIRST FEATURE" appears in the output — that is, "Speculative levels for risks nobody has met yet."; or it is absent by accident, with nothing in `testing-strategy` having ruled it out
```
