# Test cases — `root-cause-analysis`

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
GIVEN    A task inside this skill's stated purpose: Identify the cause whose removal prevents recurrence — not the nearest thing that looked wrong. The discipline is hypothesis-driven: reproduce, predict, test, eliminate.
WHEN     the agent executes `root-cause-analysis` end to end on that task
THEN     the workflow runs in its stated order — "REPRODUCE, OR EXPLAIN WHY YOU CANNOT" through to "QUARANTINE WHAT YOU COULD NOT EXPLAIN"; and before delivery these specific conditions hold: "the behaviour is reproducible, or the reason it is not is recorded"; "cause and contributing factors are distinguished"; "anything unexplained is quarantined with a restart condition"
FAIL IF  "the behaviour is reproducible, or the reason it is not is recorded" is false, or "anything unexplained is quarantined with a restart condition" is false, or the result is delivered before "QUARANTINE WHAT YOU COULD NOT EXPLAIN" has run
```

## Case 2 — Declines: The bug is obvious, local and reproducible, and the fix is one line.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The bug is obvious, local and reproducible, and the fix is one line.
WHEN     the agent considers `root-cause-analysis` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Fix it; a full analysis is overhead."
FAIL IF  the skill is run on a task where "The bug is obvious, local and reproducible, and the fix is one line.", and the consequence that exclusion states follows — "Fix it; a full analysis is overhead."; or `root-cause-analysis` is declined without naming that exclusion
```

## Case 3 — Declines: Nothing can be reproduced and no telemetry exists.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing can be reproduced and no telemetry exists.
WHEN     the agent considers `root-cause-analysis` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Restore observability first — analysis without evidence is speculation with confidence."
FAIL IF  the skill is run on a task where "Nothing can be reproduced and no telemetry exists.", and the consequence that exclusion states follows — "Restore observability first — analysis without evidence is speculation with confidence."; or `root-cause-analysis` is declined without naming that exclusion
```

## Case 4 — Declines: The goal is attribution of blame.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The goal is attribution of blame.
WHEN     the agent considers `root-cause-analysis` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "A blame-oriented analysis produces defensive reports and hidden information."
FAIL IF  the skill is run on a task where "The goal is attribution of blame.", and the consequence that exclusion states follows — "A blame-oriented analysis produces defensive reports and hidden information."; or `root-cause-analysis` is declined without naming that exclusion
```

## Case 5 — Declines: The cause is a decision rather than a defect.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The cause is a decision rather than a defect.
WHEN     the agent considers `root-cause-analysis` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is an architecture or process question."
FAIL IF  the skill is run on a task where "The cause is a decision rather than a defect.", and the consequence that exclusion states follows — "That is an architecture or process question."; or `root-cause-analysis` is declined without naming that exclusion
```

## Case 6 — Detects: Fixed the symptom, it recurred

```text
GIVEN    A run of this skill in which the known failure mode is present: Fixed the symptom, it recurred
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the reproduction still fails in a new shape" — and the response applied is the documented one: "return to step 4; the cause was not identified"
FAIL IF  "Fixed the symptom, it recurred" reaches the output because "the reproduction still fails in a new shape" was never checked; or it is caught but the response taken is not "return to step 4; the cause was not identified"
```

## Case 7 — Detects: No reproduction

```text
GIVEN    A run of this skill in which the known failure mode is present: No reproduction
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "hypotheses cannot be tested" — and the response applied is the documented one: "restore observability before analysing"
FAIL IF  "No reproduction" reaches the output because "hypotheses cannot be tested" was never checked; or it is caught but the response taken is not "restore observability before analysing"
```

## Case 8 — Detects: One hypothesis, pursued to confirmation

```text
GIVEN    A run of this skill in which the known failure mode is present: One hypothesis, pursued to confirmation
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no alternatives were written" — and the response applied is the documented one: "generate at least three, including an uncomfortable one"
FAIL IF  "One hypothesis, pursued to confirmation" reaches the output because "no alternatives were written" was never checked; or it is caught but the response taken is not "generate at least three, including an uncomfortable one"
```

## Case 9 — Detects: Hypothesis is unfalsifiable

```text
GIVEN    A run of this skill in which the known failure mode is present: Hypothesis is unfalsifiable
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no observation could refute it" — and the response applied is the documented one: "restate it as a prediction"
FAIL IF  "Hypothesis is unfalsifiable" reaches the output because "no observation could refute it" was never checked; or it is caught but the response taken is not "restate it as a prediction"
```

## Case 10 — Detects: Cause found, system question skipped

```text
GIVEN    A run of this skill in which the known failure mode is present: Cause found, system question skipped
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the same class returns elsewhere" — and the response applied is the documented one: "ask why it reached production and fix that too"
FAIL IF  "Cause found, system question skipped" reaches the output because "the same class returns elsewhere" was never checked; or it is caught but the response taken is not "ask why it reached production and fix that too"
```

## Case 11 — Detects: Fix cannot be shown to work

```text
GIVEN    A run of this skill in which the known failure mode is present: Fix cannot be shown to work
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no before/after on the reproduction" — and the response applied is the documented one: "the fix is a mitigation; say so"
FAIL IF  "Fix cannot be shown to work" reaches the output because "no before/after on the reproduction" was never checked; or it is caught but the response taken is not "the fix is a mitigation; say so"
```

## Case 12 — Detects: Regression test at the easy level

```text
GIVEN    A run of this skill in which the known failure mode is present: Regression test at the easy level
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the variant recurs" — and the response applied is the documented one: "add it at the level that should have caught it"
FAIL IF  "Regression test at the easy level" reaches the output because "the variant recurs" was never checked; or it is caught but the response taken is not "add it at the level that should have caught it"
```

## Case 13 — Detects: Timeline assembled from memory

```text
GIVEN    A run of this skill in which the known failure mode is present: Timeline assembled from memory
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "deploys and config changes are missing" — and the response applied is the documented one: "build it from logs and records, not recall"
FAIL IF  "Timeline assembled from memory" reaches the output because "deploys and config changes are missing" was never checked; or it is caught but the response taken is not "build it from logs and records, not recall"
```

## Case 14 — Detects: Investigation abandoned silently

```text
GIVEN    A run of this skill in which the known failure mode is present: Investigation abandoned silently
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "nobody knows what was ruled out" — and the response applied is the documented one: "record what is known and what would restart it"
FAIL IF  "Investigation abandoned silently" reaches the output because "nobody knows what was ruled out" was never checked; or it is caught but the response taken is not "record what is known and what would restart it"
```

## Case 15 — Detects: Blame framing

```text
GIVEN    A run of this skill in which the known failure mode is present: Blame framing
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "information is withheld" — and the response applied is the documented one: "analyse the system; people acted on the information they had"
FAIL IF  "Blame framing" reaches the output because "information is withheld" was never checked; or it is caught but the response taken is not "analyse the system; people acted on the information they had"
```

## Case 16 — Avoids: FIXING THE FIRST PLAUSIBLE THING

```text
GIVEN    A situation that invites the anti-pattern "FIXING THE FIRST PLAUSIBLE THING", whose stated consequence is: The most common failure, and invisible in the diff.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "FIXING THE FIRST PLAUSIBLE THING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The most common failure, and invisible in the diff."
FAIL IF  "FIXING THE FIRST PLAUSIBLE THING" appears in the output — that is, "The most common failure, and invisible in the diff."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 17 — Avoids: ONE HYPOTHESIS

```text
GIVEN    A situation that invites the anti-pattern "ONE HYPOTHESIS", whose stated consequence is: Confirmation follows, and the cause survives.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "ONE HYPOTHESIS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Confirmation follows, and the cause survives."
FAIL IF  "ONE HYPOTHESIS" appears in the output — that is, "Confirmation follows, and the cause survives."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 18 — Avoids: UNFALSIFIABLE HYPOTHESES

```text
GIVEN    A situation that invites the anti-pattern "UNFALSIFIABLE HYPOTHESES", whose stated consequence is: "It might be a race" with no observation that would refute it.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "UNFALSIFIABLE HYPOTHESES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It might be a race" with no observation that would refute it."
FAIL IF  "UNFALSIFIABLE HYPOTHESES" appears in the output — that is, "It might be a race" with no observation that would refute it."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 19 — Avoids: ANALYSIS WITHOUT A REPRODUCTION

```text
GIVEN    A situation that invites the anti-pattern "ANALYSIS WITHOUT A REPRODUCTION", whose stated consequence is: Speculation with confidence.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "ANALYSIS WITHOUT A REPRODUCTION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Speculation with confidence."
FAIL IF  "ANALYSIS WITHOUT A REPRODUCTION" appears in the output — that is, "Speculation with confidence."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 20 — Avoids: STOPPING AT THE DEFECT

```text
GIVEN    A situation that invites the anti-pattern "STOPPING AT THE DEFECT", whose stated consequence is: The reason it reached production is a separate cause with a cheaper fix.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "STOPPING AT THE DEFECT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The reason it reached production is a separate cause with a cheaper fix."
FAIL IF  "STOPPING AT THE DEFECT" appears in the output — that is, "The reason it reached production is a separate cause with a cheaper fix."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 21 — Avoids: A FIX NOBODY VERIFIED AGAINST THE CAUSE

```text
GIVEN    A situation that invites the anti-pattern "A FIX NOBODY VERIFIED AGAINST THE CAUSE", whose stated consequence is: A mitigation recorded as a resolution.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "A FIX NOBODY VERIFIED AGAINST THE CAUSE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A mitigation recorded as a resolution."
FAIL IF  "A FIX NOBODY VERIFIED AGAINST THE CAUSE" appears in the output — that is, "A mitigation recorded as a resolution."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 22 — Avoids: REGRESSION TEST AT THE EASIEST LEVEL

```text
GIVEN    A situation that invites the anti-pattern "REGRESSION TEST AT THE EASIEST LEVEL", whose stated consequence is: The next variant is not caught.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "REGRESSION TEST AT THE EASIEST LEVEL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The next variant is not caught."
FAIL IF  "REGRESSION TEST AT THE EASIEST LEVEL" appears in the output — that is, "The next variant is not caught."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 23 — Avoids: TIMELINE FROM MEMORY

```text
GIVEN    A situation that invites the anti-pattern "TIMELINE FROM MEMORY", whose stated consequence is: Deploys, config changes and migrations are the usual cause and are never remembered accurately.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "TIMELINE FROM MEMORY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Deploys, config changes and migrations are the usual cause and are never remembered accurately."
FAIL IF  "TIMELINE FROM MEMORY" appears in the output — that is, "Deploys, config changes and migrations are the usual cause and are never remembered accurately."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 24 — Avoids: OMITTING THE ELIMINATED HYPOTHESES

```text
GIVEN    A situation that invites the anti-pattern "OMITTING THE ELIMINATED HYPOTHESES", whose stated consequence is: The next investigator repeats the work.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "OMITTING THE ELIMINATED HYPOTHESES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The next investigator repeats the work."
FAIL IF  "OMITTING THE ELIMINATED HYPOTHESES" appears in the output — that is, "The next investigator repeats the work."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```

## Case 25 — Avoids: BLAME

```text
GIVEN    A situation that invites the anti-pattern "BLAME", whose stated consequence is: Defensive reports, hidden information, and no systemic fix.
WHEN     the agent applies `root-cause-analysis` in that situation
THEN     "BLAME" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Defensive reports, hidden information, and no systemic fix."
FAIL IF  "BLAME" appears in the output — that is, "Defensive reports, hidden information, and no systemic fix."; or it is absent by accident, with nothing in `root-cause-analysis` having ruled it out
```
