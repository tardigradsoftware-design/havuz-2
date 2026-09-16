# Test cases — `reasoning-strategies`

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
GIVEN    A task inside this skill's stated purpose: Match the reasoning strategy to the structure of the task and pay for only as much of it as the task needs. The strategies differ by orders of magnitude in cost,
WHEN     the agent executes `reasoning-strategies` end to end on that task
THEN     the workflow runs in its stated order — "CLASSIFY THE TASK BY STRUCTURE" through to "DO NOT TREAT STATED REASONING AS AN AUDIT TRAIL"; and before delivery these specific conditions hold: "the task structure was classified before a strategy was chosen"; "the compute budget is stated, and the accuracy/compute point was chosen deliberately"; "inputs, outputs and tool calls are logged; stated reasoning is not relied on as evidence"
FAIL IF  "the task structure was classified before a strategy was chosen" is false, or "inputs, outputs and tool calls are logged; stated reasoning is not relied on as evidence" is false, or the result is delivered before "DO NOT TREAT STATED REASONING AS AN AUDIT TRAIL" has run
```

## Case 2 — Declines: The model lacks the information.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The model lacks the information.
WHEN     the agent considers `reasoning-strategies` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is a retrieval problem; a strategy will not supply facts."
FAIL IF  the skill is run on a task where "The model lacks the information.", and the consequence that exclusion states follows — "That is a retrieval problem; a strategy will not supply facts."; or `reasoning-strategies` is declined without naming that exclusion
```

## Case 3 — Declines: The output format is the problem.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The output format is the problem.
WHEN     the agent considers `reasoning-strategies` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Fix the format with a schema and validation."
FAIL IF  the skill is run on a task where "The output format is the problem.", and the consequence that exclusion states follows — "Fix the format with a schema and validation."; or `reasoning-strategies` is declined without naming that exclusion
```

## Case 4 — Declines: The task is a single deterministic operation.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The task is a single deterministic operation.
WHEN     the agent considers `reasoning-strategies` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Call a function."
FAIL IF  the skill is run on a task where "The task is a single deterministic operation.", and the consequence that exclusion states follows — "Call a function."; or `reasoning-strategies` is declined without naming that exclusion
```

## Case 5 — Declines: There is no evaluation set.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: There is no evaluation set.
WHEN     the agent considers `reasoning-strategies` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Without one, strategy selection is aesthetic and the cost is real."
FAIL IF  the skill is run on a task where "There is no evaluation set.", and the consequence that exclusion states follows — "Without one, strategy selection is aesthetic and the cost is real."; or `reasoning-strategies` is declined without naming that exclusion
```

## Case 6 — Declines: The correct behaviour is to refuse or escalate.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The correct behaviour is to refuse or escalate.
WHEN     the agent considers `reasoning-strategies` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Strategy choice does not substitute for a boundary."
FAIL IF  the skill is run on a task where "The correct behaviour is to refuse or escalate.", and the consequence that exclusion states follows — "Strategy choice does not substitute for a boundary."; or `reasoning-strategies` is declined without naming that exclusion
```

## Case 7 — Detects: Strategy chosen by fashion

```text
GIVEN    A run of this skill in which the known failure mode is present: Strategy chosen by fashion
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "cost is high and accuracy is not" — and the response applied is the documented one: "re-measure the cheapest strategy that fits the structure"
FAIL IF  "Strategy chosen by fashion" reaches the output because "cost is high and accuracy is not" was never checked; or it is caught but the response taken is not "re-measure the cheapest strategy that fits the structure"
```

## Case 8 — Detects: CoT added by default

```text
GIVEN    A run of this skill in which the known failure mode is present: CoT added by default
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "neutral or negative delta on a reasoning-tuned model" — and the response applied is the documented one: "remove it; keep only measured interventions"
FAIL IF  "CoT added by default" reaches the output because "neutral or negative delta on a reasoning-tuned model" was never checked; or it is caught but the response taken is not "remove it; keep only measured interventions"
```

## Case 9 — Detects: Chain produced, answer still wrong

```text
GIVEN    A run of this skill in which the known failure mode is present: Chain produced, answer still wrong
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "failure not localised" — and the response applied is the documented one: "find the first incorrect intermediate step"
FAIL IF  "Chain produced, answer still wrong" reaches the output because "failure not localised" was never checked; or it is caught but the response taken is not "find the first incorrect intermediate step"
```

## Case 10 — Detects: Self-consistency on free-form output

```text
GIVEN    A run of this skill in which the known failure mode is present: Self-consistency on free-form output
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "votes are not comparable" — and the response applied is the documented one: "constrain the answer format so votes can be counted"
FAIL IF  "Self-consistency on free-form output" reaches the output because "votes are not comparable" was never checked; or it is caught but the response taken is not "constrain the answer format so votes can be counted"
```

## Case 11 — Detects: Search where sampling suffices

```text
GIVEN    A run of this skill in which the known failure mode is present: Search where sampling suffices
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "cost rose far more than accuracy" — and the response applied is the documented one: "ablate: sampling-only versus search"
FAIL IF  "Search where sampling suffices" reaches the output because "cost rose far more than accuracy" was never checked; or it is caught but the response taken is not "ablate: sampling-only versus search"
```

## Case 12 — Detects: Reasoning over parametric memory

```text
GIVEN    A run of this skill in which the known failure mode is present: Reasoning over parametric memory
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "confident fabrication" — and the response applied is the documented one: "retrieve first and ground the claims"
FAIL IF  "Reasoning over parametric memory" reaches the output because "confident fabrication" was never checked; or it is caught but the response taken is not "retrieve first and ground the claims"
```

## Case 13 — Detects: No compute budget stated

```text
GIVEN    A run of this skill in which the known failure mode is present: No compute budget stated
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "strategy comparisons are meaningless" — and the response applied is the documented one: "state latency and cost ceilings before comparing"
FAIL IF  "No compute budget stated" reaches the output because "strategy comparisons are meaningless" was never checked; or it is caught but the response taken is not "state latency and cost ceilings before comparing"
```

## Case 14 — Detects: Reasoning text used as an audit trail

```text
GIVEN    A run of this skill in which the known failure mode is present: Reasoning text used as an audit trail
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the chain does not explain the action" — and the response applied is the documented one: "log the actual inputs, outputs and tool calls"
FAIL IF  "Reasoning text used as an audit trail" reaches the output because "the chain does not explain the action" was never checked; or it is caught but the response taken is not "log the actual inputs, outputs and tool calls"
```

## Case 15 — Avoids: ALWAYS THINK STEP BY STEP

```text
GIVEN    A situation that invites the anti-pattern "ALWAYS THINK STEP BY STEP", whose stated consequence is: The default that the evidence does not support across models and tasks.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "ALWAYS THINK STEP BY STEP" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The default that the evidence does not support across models and tasks."
FAIL IF  "ALWAYS THINK STEP BY STEP" appears in the output — that is, "The default that the evidence does not support across models and tasks."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 16 — Avoids: REASONING INSTEAD OF RETRIEVAL

```text
GIVEN    A situation that invites the anti-pattern "REASONING INSTEAD OF RETRIEVAL", whose stated consequence is: Asking a model to reason its way to a fact it does not have produces confident fabrication.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "REASONING INSTEAD OF RETRIEVAL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Asking a model to reason its way to a fact it does not have produces confident fabrication."
FAIL IF  "REASONING INSTEAD OF RETRIEVAL" appears in the output — that is, "Asking a model to reason its way to a fact it does not have produces confident fabrication."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 17 — Avoids: SEARCH BY DEFAULT

```text
GIVEN    A situation that invites the anti-pattern "SEARCH BY DEFAULT", whose stated consequence is: One to two orders of magnitude more calls, much of the benefit available from cheaper sampling.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "SEARCH BY DEFAULT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "One to two orders of magnitude more calls, much of the benefit available from cheaper sampling."
FAIL IF  "SEARCH BY DEFAULT" appears in the output — that is, "One to two orders of magnitude more calls, much of the benefit available from cheaper sampling."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 18 — Avoids: INVISIBLE INTERMEDIATE STEPS

```text
GIVEN    A situation that invites the anti-pattern "INVISIBLE INTERMEDIATE STEPS", whose stated consequence is: A failure that cannot be localised cannot be fixed.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "INVISIBLE INTERMEDIATE STEPS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A failure that cannot be localised cannot be fixed."
FAIL IF  "INVISIBLE INTERMEDIATE STEPS" appears in the output — that is, "A failure that cannot be localised cannot be fixed."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 19 — Avoids: SELF-CONSISTENCY ON UNSTRUCTURED OUTPUT

```text
GIVEN    A situation that invites the anti-pattern "SELF-CONSISTENCY ON UNSTRUCTURED OUTPUT", whose stated consequence is: Majority voting requires comparable answers.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "SELF-CONSISTENCY ON UNSTRUCTURED OUTPUT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Majority voting requires comparable answers."
FAIL IF  "SELF-CONSISTENCY ON UNSTRUCTURED OUTPUT" appears in the output — that is, "Majority voting requires comparable answers."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 20 — Avoids: NO COMPUTE BUDGET

```text
GIVEN    A situation that invites the anti-pattern "NO COMPUTE BUDGET", whose stated consequence is: Then the strategy is chosen by preference and the cost is discovered in production.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "NO COMPUTE BUDGET" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Then the strategy is chosen by preference and the cost is discovered in production."
FAIL IF  "NO COMPUTE BUDGET" appears in the output — that is, "Then the strategy is chosen by preference and the cost is discovered in production."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 21 — Avoids: TRUSTING THE STATED REASONING

```text
GIVEN    A situation that invites the anti-pattern "TRUSTING THE STATED REASONING", whose stated consequence is: It may be post-hoc; it is not an audit trail.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "TRUSTING THE STATED REASONING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It may be post-hoc; it is not an audit trail."
FAIL IF  "TRUSTING THE STATED REASONING" appears in the output — that is, "It may be post-hoc; it is not an audit trail."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 22 — Avoids: ONE STRATEGY FOR ALL TASK CLASSES

```text
GIVEN    A situation that invites the anti-pattern "ONE STRATEGY FOR ALL TASK CLASSES", whose stated consequence is: Structure differs; so should the strategy.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "ONE STRATEGY FOR ALL TASK CLASSES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Structure differs; so should the strategy."
FAIL IF  "ONE STRATEGY FOR ALL TASK CLASSES" appears in the output — that is, "Structure differs; so should the strategy."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```

## Case 23 — Avoids: CARRYING A 2022 RESULT FORWARD UNMEASURED

```text
GIVEN    A situation that invites the anti-pattern "CARRYING A 2022 RESULT FORWARD UNMEASURED", whose stated consequence is: Reasoning behaviour changed with RL training.
WHEN     the agent applies `reasoning-strategies` in that situation
THEN     "CARRYING A 2022 RESULT FORWARD UNMEASURED" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Reasoning behaviour changed with RL training."
FAIL IF  "CARRYING A 2022 RESULT FORWARD UNMEASURED" appears in the output — that is, "Reasoning behaviour changed with RL training."; or it is absent by accident, with nothing in `reasoning-strategies` having ruled it out
```
