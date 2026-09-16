# Test cases — `prompt-engineering`

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
GIVEN    A task inside this skill's stated purpose: Change model behaviour deliberately and measurably. The skill is not writing clever instructions — it is specifying the behaviour, building a set of cases that shows whether the behaviour occurred, changing one thing, and measuring.
WHEN     the agent executes `prompt-engineering` end to end on that task
THEN     the workflow runs in its stated order — "SPECIFY THE BEHAVIOUR AS CHECKABLE PROPERTIES" through to "MOVE WHAT CAN BE CODE OUT OF THE PROMPT"; and before delivery these specific conditions hold: "the behaviour is specified as checkable properties"; "the full set was re-measured, not only the target cases"; "anything enforceable in code has been moved out of the prompt"
FAIL IF  "the behaviour is specified as checkable properties" is false, or "anything enforceable in code has been moved out of the prompt" is false, or the result is delivered before "MOVE WHAT CAN BE CODE OUT OF THE PROMPT" has run
```

## Case 2 — Declines: The failure is a capability limit rather than a specification problem.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The failure is a capability limit rather than a specification problem.
WHEN     the agent considers `prompt-engineering` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "If the model cannot do the task, no phrasing will make it able. Test the capability separately first."
FAIL IF  the skill is run on a task where "The failure is a capability limit rather than a specification problem.", and the consequence that exclusion states follows — "If the model cannot do the task, no phrasing will make it able. Test the capability separately first."; or `prompt-engineering` is declined without naming that exclusion
```

## Case 3 — Declines: The failure is retrieval: the model does not have the information.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The failure is retrieval: the model does not have the information.
WHEN     the agent considers `prompt-engineering` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Fix the retrieval, not the prompt."
FAIL IF  the skill is run on a task where "The failure is retrieval: the model does not have the information.", and the consequence that exclusion states follows — "Fix the retrieval, not the prompt."; or `prompt-engineering` is declined without naming that exclusion
```

## Case 4 — Declines: The output is non-deterministic and there is no evaluation set.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The output is non-deterministic and there is no evaluation set.
WHEN     the agent considers `prompt-engineering` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Build the set first; a single example cannot distinguish an improvement from noise."
FAIL IF  the skill is run on a task where "The output is non-deterministic and there is no evaluation set.", and the consequence that exclusion states follows — "Build the set first; a single example cannot distinguish an improvement from noise."; or `prompt-engineering` is declined without naming that exclusion
```

## Case 5 — Declines: The problem is a missing control.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The problem is a missing control.
WHEN     the agent considers `prompt-engineering` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Formatting, validation and gating belong in code around the model, not in an instruction that may or may not be followed."
FAIL IF  the skill is run on a task where "The problem is a missing control.", and the consequence that exclusion states follows — "Formatting, validation and gating belong in code around the model, not in an instruction that may or may not be followed."; or `prompt-engineering` is declined without naming that exclusion
```

## Case 6 — Declines: The intended change is a security boundary.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The intended change is a security boundary.
WHEN     the agent considers `prompt-engineering` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Prompt instructions are not a control boundary — see prompt-injection-defense."
FAIL IF  the skill is run on a task where "The intended change is a security boundary.", and the consequence that exclusion states follows — "Prompt instructions are not a control boundary — see prompt-injection-defense."; or `prompt-engineering` is declined without naming that exclusion
```

## Case 7 — Detects: Improved the target, regressed another case

```text
GIVEN    A run of this skill in which the known failure mode is present: Improved the target, regressed another case
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "full-set pass rate fell" — and the response applied is the documented one: "revert; the change was too broad — narrow it"
FAIL IF  "Improved the target, regressed another case" reaches the output because "full-set pass rate fell" was never checked; or it is caught but the response taken is not "revert; the change was too broad — narrow it"
```

## Case 8 — Detects: Improvement inside the noise floor

```text
GIVEN    A run of this skill in which the known failure mode is present: Improvement inside the noise floor
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "run-to-run spread exceeds the delta" — and the response applied is the documented one: "more runs, or a bigger change; do not claim the improvement"
FAIL IF  "Improvement inside the noise floor" reaches the output because "run-to-run spread exceeds the delta" was never checked; or it is caught but the response taken is not "more runs, or a bigger change; do not claim the improvement"
```

## Case 9 — Detects: Works on one model, fails on another

```text
GIVEN    A run of this skill in which the known failure mode is present: Works on one model, fails on another
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no model version recorded with the prompt" — and the response applied is the documented one: "record model and version; re-measure per model"
FAIL IF  "Works on one model, fails on another" reaches the output because "no model version recorded with the prompt" was never checked; or it is caught but the response taken is not "record model and version; re-measure per model"
```

## Case 10 — Detects: Instruction followed inconsistently

```text
GIVEN    A run of this skill in which the known failure mode is present: Instruction followed inconsistently
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "pass rate varies run to run on the same input" — and the response applied is the documented one: "add a worked example, or enforce in code"
FAIL IF  "Instruction followed inconsistently" reaches the output because "pass rate varies run to run on the same input" was never checked; or it is caught but the response taken is not "add a worked example, or enforce in code"
```

## Case 11 — Detects: Prompt grew until it stopped working

```text
GIVEN    A run of this skill in which the known failure mode is present: Prompt grew until it stopped working
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "length doubled, adherence fell" — and the response applied is the documented one: "restructure and cut; instructions compete with each other"
FAIL IF  "Prompt grew until it stopped working" reaches the output because "length doubled, adherence fell" was never checked; or it is caught but the response taken is not "restructure and cut; instructions compete with each other"
```

## Case 12 — Detects: Schema adherence unreliable

```text
GIVEN    A run of this skill in which the known failure mode is present: Schema adherence unreliable
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "occasional malformed output" — and the response applied is the documented one: "constrain with structured output or a schema, plus validation and one retry"
FAIL IF  "Schema adherence unreliable" reaches the output because "occasional malformed output" was never checked; or it is caught but the response taken is not "constrain with structured output or a schema, plus validation and one retry"
```

## Case 13 — Detects: The example was invented

```text
GIVEN    A run of this skill in which the known failure mode is present: The example was invented
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the eval set contains cases nobody actually hit" — and the response applied is the documented one: "replace with real failures from logs"
FAIL IF  "The example was invented" reaches the output because "the eval set contains cases nobody actually hit" was never checked; or it is caught but the response taken is not "replace with real failures from logs"
```

## Case 14 — Detects: A security property was implemented in the prompt

```text
GIVEN    A run of this skill in which the known failure mode is present: A security property was implemented in the prompt
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "injection succeeded" — and the response applied is the documented one: "move the control outside the model"
FAIL IF  "A security property was implemented in the prompt" reaches the output because "injection succeeded" was never checked; or it is caught but the response taken is not "move the control outside the model"
```

## Case 15 — Avoids: EDITING BY VIBE

```text
GIVEN    A situation that invites the anti-pattern "EDITING BY VIBE", whose stated consequence is: Changing a prompt because one output looked wrong, with no set and no baseline. The most common failure in this discipline.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "EDITING BY VIBE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Changing a prompt because one output looked wrong, with no set and no baseline. The most common failure in this discipline."
FAIL IF  "EDITING BY VIBE" appears in the output — that is, "Changing a prompt because one output looked wrong, with no set and no baseline. The most common failure in this discipline."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 16 — Avoids: ONE-EXAMPLE TUNING

```text
GIVEN    A situation that invites the anti-pattern "ONE-EXAMPLE TUNING", whose stated consequence is: Optimising until a single case works, which usually breaks three others.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "ONE-EXAMPLE TUNING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Optimising until a single case works, which usually breaks three others."
FAIL IF  "ONE-EXAMPLE TUNING" appears in the output — that is, "Optimising until a single case works, which usually breaks three others."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 17 — Avoids: INSTRUCTION ACCUMULATION

```text
GIVEN    A situation that invites the anti-pattern "INSTRUCTION ACCUMULATION", whose stated consequence is: Adding a rule for every observed failure until the prompt is a pile of conflicting constraints the model attends to unevenly.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "INSTRUCTION ACCUMULATION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Adding a rule for every observed failure until the prompt is a pile of conflicting constraints the model attends to unevenly."
FAIL IF  "INSTRUCTION ACCUMULATION" appears in the output — that is, "Adding a rule for every observed failure until the prompt is a pile of conflicting constraints the model attends to unevenly."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 18 — Avoids: PROSE WHERE A SCHEMA BELONGS

```text
GIVEN    A situation that invites the anti-pattern "PROSE WHERE A SCHEMA BELONGS", whose stated consequence is: "Return JSON with fields a, b and c" instead of a schema plus validation plus one retry.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "PROSE WHERE A SCHEMA BELONGS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Return JSON with fields a, b and c" instead of a schema plus validation plus one retry."
FAIL IF  "PROSE WHERE A SCHEMA BELONGS" appears in the output — that is, "Return JSON with fields a, b and c" instead of a schema plus validation plus one retry."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 19 — Avoids: CLEVERNESS OVER CLARITY

```text
GIVEN    A situation that invites the anti-pattern "CLEVERNESS OVER CLARITY", whose stated consequence is: Elaborate framing, personas and incantations that cannot be reviewed or diffed, and whose effect cannot be attributed.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "CLEVERNESS OVER CLARITY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Elaborate framing, personas and incantations that cannot be reviewed or diffed, and whose effect cannot be attributed."
FAIL IF  "CLEVERNESS OVER CLARITY" appears in the output — that is, "Elaborate framing, personas and incantations that cannot be reviewed or diffed, and whose effect cannot be attributed."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 20 — Avoids: NO MODEL VERSION

```text
GIVEN    A situation that invites the anti-pattern "NO MODEL VERSION", whose stated consequence is: A prompt with no recorded model is unmaintainable; the behaviour it produces is a property of the pair.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "NO MODEL VERSION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A prompt with no recorded model is unmaintainable; the behaviour it produces is a property of the pair."
FAIL IF  "NO MODEL VERSION" appears in the output — that is, "A prompt with no recorded model is unmaintainable; the behaviour it produces is a property of the pair."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 21 — Avoids: PROMPT AS SECURITY CONTROL

```text
GIVEN    A situation that invites the anti-pattern "PROMPT AS SECURITY CONTROL", whose stated consequence is: Instructions reduce likelihood; they are not a boundary.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "PROMPT AS SECURITY CONTROL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Instructions reduce likelihood; they are not a boundary."
FAIL IF  "PROMPT AS SECURITY CONTROL" appears in the output — that is, "Instructions reduce likelihood; they are not a boundary."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 22 — Avoids: DISCARDING NEGATIVE RESULTS

```text
GIVEN    A situation that invites the anti-pattern "DISCARDING NEGATIVE RESULTS", whose stated consequence is: The next person will try the same thing and reach the same dead end.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "DISCARDING NEGATIVE RESULTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The next person will try the same thing and reach the same dead end."
FAIL IF  "DISCARDING NEGATIVE RESULTS" appears in the output — that is, "The next person will try the same thing and reach the same dead end."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```

## Case 23 — Avoids: TUNING THE SYSTEM PROMPT FOR A USER-SPECIFIC CASE

```text
GIVEN    A situation that invites the anti-pattern "TUNING THE SYSTEM PROMPT FOR A USER-SPECIFIC CASE", whose stated consequence is: A change to shared instructions to fix one user's input is a regression for everyone else.
WHEN     the agent applies `prompt-engineering` in that situation
THEN     "TUNING THE SYSTEM PROMPT FOR A USER-SPECIFIC CASE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A change to shared instructions to fix one user's input is a regression for everyone else."
FAIL IF  "TUNING THE SYSTEM PROMPT FOR A USER-SPECIFIC CASE" appears in the output — that is, "A change to shared instructions to fix one user's input is a regression for everyone else."; or it is absent by accident, with nothing in `prompt-engineering` having ruled it out
```
