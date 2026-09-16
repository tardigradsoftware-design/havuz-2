# Test cases — `threat-modeling`

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
GIVEN    A task inside this skill's stated purpose: Answer in writing, before building: what can go wrong, who would want it to, what it would cost, and what is being done about it. Skipping this does not remove the threats;
WHEN     the agent executes `threat-modeling` end to end on that task
THEN     the workflow runs in its stated order — "DRAW THE DATA FLOWS AND MARK THE BOUNDARIES" through to "SET THE REVISIT TRIGGER"; and before delivery these specific conditions hold: "the data-flow diagram exists with boundaries marked"; "every threat has a disposition, and every acceptance has a reason, an owner and a date"; "the revisit trigger is stated"
FAIL IF  "the data-flow diagram exists with boundaries marked" is false, or "the revisit trigger is stated" is false, or the result is delivered before "SET THE REVISIT TRIGGER" has run
```

## Case 2 — Declines: The data flows are unknown.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The data flows are unknown.
WHEN     the agent considers `threat-modeling` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "A threat model against a vague description produces vague threats. Draw the diagram first."
FAIL IF  the skill is run on a task where "The data flows are unknown.", and the consequence that exclusion states follows — "A threat model against a vague description produces vague threats. Draw the diagram first."; or `threat-modeling` is declined without naming that exclusion
```

## Case 3 — Declines: The goal is compliance evidence rather than risk reduction.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The goal is compliance evidence rather than risk reduction.
WHEN     the agent considers `threat-modeling` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Produce the artifact the standard asks for, and model separately — conflating them yields a document that satisfies nobody."
FAIL IF  the skill is run on a task where "The goal is compliance evidence rather than risk reduction.", and the consequence that exclusion states follows — "Produce the artifact the standard asks for, and model separately — conflating them yields a document that satisfies nobody."; or `threat-modeling` is declined without naming that exclusion
```

## Case 4 — Declines: A penetration test or an audit is what is needed.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A penetration test or an audit is what is needed.
WHEN     the agent considers `threat-modeling` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Those verify controls against a live system; this enumerates threats against a design. They are complements."
FAIL IF  the skill is run on a task where "A penetration test or an audit is what is needed.", and the consequence that exclusion states follows — "Those verify controls against a live system; this enumerates threats against a design. They are complements."; or `threat-modeling` is declined without naming that exclusion
```

## Case 5 — Declines: The system is unchanged since the last model.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The system is unchanged since the last model.
WHEN     the agent considers `threat-modeling` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Revisit on change, not on a calendar."
FAIL IF  the skill is run on a task where "The system is unchanged since the last model.", and the consequence that exclusion states follows — "Revisit on change, not on a calendar."; or `threat-modeling` is declined without naming that exclusion
```

## Case 6 — Detects: Modeled services instead of flows

```text
GIVEN    A run of this skill in which the known failure mode is present: Modeled services instead of flows
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no boundary crossings in the diagram" — and the response applied is the documented one: "redraw around data movement; boxes hide the crossings"
FAIL IF  "Modeled services instead of flows" reaches the output because "no boundary crossings in the diagram" was never checked; or it is caught but the response taken is not "redraw around data movement; boxes hide the crossings"
```

## Case 7 — Detects: Mitigations before enumeration

```text
GIVEN    A run of this skill in which the known failure mode is present: Mitigations before enumeration
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "we use TLS" appears with no threat attached" — and the response applied is the documented one: "return to step 2; the control answers a question nobody asked"
FAIL IF  "Mitigations before enumeration" reaches the output because "we use TLS" appears with no threat attached" was never checked; or it is caught but the response taken is not "return to step 2; the control answers a question nobody asked"
```

## Case 8 — Detects: Threats without mechanisms

```text
GIVEN    A run of this skill in which the known failure mode is present: Threats without mechanisms
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "register entries are one word ("injection")" — and the response applied is the documented one: "expand each to actor, path, action and impact"
FAIL IF  "Threats without mechanisms" reaches the output because "register entries are one word ("injection")" was never checked; or it is caught but the response taken is not "expand each to actor, path, action and impact"
```

## Case 9 — Detects: No disposition

```text
GIVEN    A run of this skill in which the known failure mode is present: No disposition
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "threats listed, nothing decided" — and the response applied is the documented one: "disposition every row; unaccepted risk is unmanaged risk"
FAIL IF  "No disposition" reaches the output because "threats listed, nothing decided" was never checked; or it is caught but the response taken is not "disposition every row; unaccepted risk is unmanaged risk"
```

## Case 10 — Detects: Acceptance without owner or date

```text
GIVEN    A run of this skill in which the known failure mode is present: Acceptance without owner or date
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "accepted" with no follow-up" — and the response applied is the documented one: "add an owner and a revisit date, or mitigate"
FAIL IF  "Acceptance without owner or date" reaches the output because "accepted" with no follow-up" was never checked; or it is caught but the response taken is not "add an owner and a revisit date, or mitigate"
```

## Case 11 — Detects: Mitigations that depend on the model

```text
GIVEN    A run of this skill in which the known failure mode is present: Mitigations that depend on the model
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the prompt tells it not to" — and the response applied is the documented one: "move the control outside the model: capability removal, a wrapper gate, a policy check"
FAIL IF  "Mitigations that depend on the model" reaches the output because "the prompt tells it not to" was never checked; or it is caught but the response taken is not "move the control outside the model: capability removal, a wrapper gate, a policy check"
```

## Case 12 — Detects: No tests

```text
GIVEN    A run of this skill in which the known failure mode is present: No tests
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "mitigations asserted, never verified" — and the response applied is the documented one: "add adversarial cases to the evaluation suite"
FAIL IF  "No tests" reaches the output because "mitigations asserted, never verified" was never checked; or it is caught but the response taken is not "add adversarial cases to the evaluation suite"
```

## Case 13 — Detects: Model never revisited

```text
GIVEN    A run of this skill in which the known failure mode is present: Model never revisited
WHEN     the agent executes `threat-modeling` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "diagram predates three integrations" — and the response applied is the documented one: "add the revisit trigger to the register"
FAIL IF  "Model never revisited" reaches the output because "diagram predates three integrations" was never checked; or it is caught but the response taken is not "add the revisit trigger to the register"
```

## Case 14 — Avoids: STARTING WITH CONTROLS

```text
GIVEN    A situation that invites the anti-pattern "STARTING WITH CONTROLS", whose stated consequence is: A list of technologies in use is not a threat model.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "STARTING WITH CONTROLS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A list of technologies in use is not a threat model."
FAIL IF  "STARTING WITH CONTROLS" appears in the output — that is, "A list of technologies in use is not a threat model."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 15 — Avoids: MODELING THE ORG CHART

```text
GIVEN    A situation that invites the anti-pattern "MODELING THE ORG CHART", whose stated consequence is: Service boxes without data flows hide every crossing.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "MODELING THE ORG CHART" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Service boxes without data flows hide every crossing."
FAIL IF  "MODELING THE ORG CHART" appears in the output — that is, "Service boxes without data flows hide every crossing."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 16 — Avoids: TREATING "ACCEPT" AS FAILURE

```text
GIVEN    A situation that invites the anti-pattern "TREATING "ACCEPT" AS FAILURE", whose stated consequence is: Written acceptance with a date is the mature outcome; silent acceptance is the failure.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "TREATING "ACCEPT" AS FAILURE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Written acceptance with a date is the mature outcome; silent acceptance is the failure."
FAIL IF  "TREATING "ACCEPT" AS FAILURE" appears in the output — that is, "Written acceptance with a date is the mature outcome; silent acceptance is the failure."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 17 — Avoids: ONE-TIME EXERCISE

```text
GIVEN    A situation that invites the anti-pattern "ONE-TIME EXERCISE", whose stated consequence is: The model must be revisited when the diagram changes.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "ONE-TIME EXERCISE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The model must be revisited when the diagram changes."
FAIL IF  "ONE-TIME EXERCISE" appears in the output — that is, "The model must be revisited when the diagram changes."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 18 — Avoids: MITIGATIONS WITHOUT OWNERS

```text
GIVEN    A situation that invites the anti-pattern "MITIGATIONS WITHOUT OWNERS", whose stated consequence is: Nobody owns it, nobody schedules it.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "MITIGATIONS WITHOUT OWNERS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Nobody owns it, nobody schedules it."
FAIL IF  "MITIGATIONS WITHOUT OWNERS" appears in the output — that is, "Nobody owns it, nobody schedules it."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 19 — Avoids: ASSUMING THE MODEL IS A TRUST BOUNDARY

```text
GIVEN    A situation that invites the anti-pattern "ASSUMING THE MODEL IS A TRUST BOUNDARY", whose stated consequence is: It is not. Instructions to a model are not a control boundary; capability removal and external gates are.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "ASSUMING THE MODEL IS A TRUST BOUNDARY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It is not. Instructions to a model are not a control boundary; capability removal and external gates are."
FAIL IF  "ASSUMING THE MODEL IS A TRUST BOUNDARY" appears in the output — that is, "It is not. Instructions to a model are not a control boundary; capability removal and external gates are."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 20 — Avoids: THREAT INFLATION

```text
GIVEN    A situation that invites the anti-pattern "THREAT INFLATION", whose stated consequence is: Listing 200 threats nobody will disposition produces a document that is ignored. Depth on the reachable ones beats breadth on the theoretical.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "THREAT INFLATION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Listing 200 threats nobody will disposition produces a document that is ignored. Depth on the reachable ones beats breadth on the theoretical."
FAIL IF  "THREAT INFLATION" appears in the output — that is, "Listing 200 threats nobody will disposition produces a document that is ignored. Depth on the reachable ones beats breadth on the theoretical."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```

## Case 21 — Avoids: NO ARTIFACTS

```text
GIVEN    A situation that invites the anti-pattern "NO ARTIFACTS", whose stated consequence is: A meeting where threats were discussed is not a threat model.
WHEN     the agent applies `threat-modeling` in that situation
THEN     "NO ARTIFACTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A meeting where threats were discussed is not a threat model."
FAIL IF  "NO ARTIFACTS" appears in the output — that is, "A meeting where threats were discussed is not a threat model."; or it is absent by accident, with nothing in `threat-modeling` having ruled it out
```
