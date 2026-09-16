# Test cases — `debugging`

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
GIVEN    A task inside this skill's stated purpose: Find the **root cause**, not the nearest place to put a `try`. Debugging is a search problem with a hypothesis-driven strategy;
WHEN     the agent executes `debugging` end to end on that task
THEN     and before delivery these specific conditions hold: "Automated reproduction exists and is recorded"; "Root cause established at least to "why was it not caught"; "Lesson filed in gotchas/ or failure-modes/"
FAIL IF  "Automated reproduction exists and is recorded" is false, or "Lesson filed in gotchas/ or failure-modes/" is false, or "Root cause established at least to "why was it not caught" is false
```

## Case 2 — Declines: A known, understood defect with an agreed fix — implement it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A known, understood defect with an agreed fix — implement it
WHEN     the agent considers `debugging` for that task
THEN     the skill is not selected, because this task is the excluded case "A known, understood defect with an agreed fix — implement it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A known, understood defect with an agreed fix — implement it"; or `debugging` is declined without naming that exclusion
```

## Case 3 — Declines: A feature request described as a bug

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A feature request described as a bug
WHEN     the agent considers `debugging` for that task
THEN     the skill is not selected, because this task is the excluded case "A feature request described as a bug", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A feature request described as a bug"; or `debugging` is declined without naming that exclusion
```

## Case 4 — Declines: Cosmetic preference changes

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Cosmetic preference changes
WHEN     the agent considers `debugging` for that task
THEN     the skill is not selected, because this task is the excluded case "Cosmetic preference changes", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Cosmetic preference changes"; or `debugging` is declined without naming that exclusion
```

## Case 5 — Detects: SYMPTOM PATCHING

```text
GIVEN    A run of this skill in which the known failure mode is present: SYMPTOM PATCHING
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "SYMPTOM PATCHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Catching the exception, adding a null check, retrying forever. The cause survives and returns in a new shape."
FAIL IF  "SYMPTOM PATCHING" appears in the work and is reported as complete — specifically "Catching the exception, adding a null check, retrying forever. The cause survives and returns in a new shape."
```

## Case 6 — Detects: SHOTGUN DEBUGGING

```text
GIVEN    A run of this skill in which the known failure mode is present: SHOTGUN DEBUGGING
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "SHOTGUN DEBUGGING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Changing five things at once; the bug "goes away" and nobody knows why."
FAIL IF  "SHOTGUN DEBUGGING" appears in the work and is reported as complete — specifically "Changing five things at once; the bug "goes away" and nobody knows why."
```

## Case 7 — Detects: UNREPRODUCED FIX

```text
GIVEN    A run of this skill in which the known failure mode is present: UNREPRODUCED FIX
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "UNREPRODUCED FIX" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Declaring success without a repro. This is a guess with a commit message."
FAIL IF  "UNREPRODUCED FIX" appears in the work and is reported as complete — specifically "Declaring success without a repro. This is a guess with a commit message."
```

## Case 8 — Detects: BLAME THE FRAMEWORK

```text
GIVEN    A run of this skill in which the known failure mode is present: BLAME THE FRAMEWORK
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "BLAME THE FRAMEWORK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Assuming a widely-used library is wrong before checking your usage. Check your call first; then the version; then the issue tracker."
FAIL IF  "BLAME THE FRAMEWORK" appears in the work and is reported as complete — specifically "Assuming a widely-used library is wrong before checking your usage. Check your call first; then the version; then the issue tracker."
```

## Case 9 — Detects: ENVIRONMENT BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: ENVIRONMENT BLINDNESS
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "ENVIRONMENT BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Fixing local, shipping to prod, where the config differs."
FAIL IF  "ENVIRONMENT BLINDNESS" appears in the work and is reported as complete — specifically "Fixing local, shipping to prod, where the config differs."
```

## Case 10 — Detects: LOG STARVATION

```text
GIVEN    A run of this skill in which the known failure mode is present: LOG STARVATION
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "LOG STARVATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Not enough observability to see the boundary. Fix the instrumentation."
FAIL IF  "LOG STARVATION" appears in the work and is reported as complete — specifically "Not enough observability to see the boundary. Fix the instrumentation."
```

## Case 11 — Detects: FLAKE NORMALISATION

```text
GIVEN    A run of this skill in which the known failure mode is present: FLAKE NORMALISATION
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "FLAKE NORMALISATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Re-running until green. Flakes are timing bugs with a low reproduction rate."
FAIL IF  "FLAKE NORMALISATION" appears in the work and is reported as complete — specifically "Re-running until green. Flakes are timing bugs with a low reproduction rate."
```

## Case 12 — Detects: ROOT-CAUSE STOPPING

```text
GIVEN    A run of this skill in which the known failure mode is present: ROOT-CAUSE STOPPING
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "ROOT-CAUSE STOPPING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Answering only "why did it fail", never "why was it not caught"."
FAIL IF  "ROOT-CAUSE STOPPING" appears in the work and is reported as complete — specifically "Answering only "why did it fail", never "why was it not caught"."
```

## Case 13 — Detects: ATTEMPT AMNESIA

```text
GIVEN    A run of this skill in which the known failure mode is present: ATTEMPT AMNESIA
WHEN     the agent executes `debugging` and reaches the point where this failure occurs
THEN     "ATTEMPT AMNESIA" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Retrying a hypothesis already disproved (an agent-specific failure)."
FAIL IF  "ATTEMPT AMNESIA" appears in the work and is reported as complete — specifically "Retrying a hypothesis already disproved (an agent-specific failure)."
```

## Case 14 — Avoids: `try { … } catch { /* ignore */ }`

```text
GIVEN    A situation that invites the anti-pattern "`try { … } catch { /* ignore */ }`"
WHEN     the agent applies `debugging` in that situation
THEN     "`try { … } catch { /* ignore */ }`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`try { … } catch { /* ignore */ }`" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 15 — Avoids: Adding `await sleep(500)` to fix a race

```text
GIVEN    A situation that invites the anti-pattern "Adding `await sleep(500)` to fix a race"
WHEN     the agent applies `debugging` in that situation
THEN     "Adding `await sleep(500)` to fix a race" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding `await sleep(500)` to fix a race" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 16 — Avoids: Re-running CI until it passes

```text
GIVEN    A situation that invites the anti-pattern "Re-running CI until it passes"
WHEN     the agent applies `debugging` in that situation
THEN     "Re-running CI until it passes" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Re-running CI until it passes" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 17 — Avoids: "Works on my machine" as a conclusion rather than a clue

```text
GIVEN    A situation that invites the anti-pattern "Works on my machine" as a conclusion rather than a clue"
WHEN     the agent applies `debugging` in that situation
THEN     "Works on my machine" as a conclusion rather than a clue" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Works on my machine" as a conclusion rather than a clue" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 18 — Avoids: Rewriting the module instead of finding the defect

```text
GIVEN    A situation that invites the anti-pattern "Rewriting the module instead of finding the defect"
WHEN     the agent applies `debugging` in that situation
THEN     "Rewriting the module instead of finding the defect" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Rewriting the module instead of finding the defect" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 19 — Avoids: Fixing three bugs in one commit

```text
GIVEN    A situation that invites the anti-pattern "Fixing three bugs in one commit"
WHEN     the agent applies `debugging` in that situation
THEN     "Fixing three bugs in one commit" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Fixing three bugs in one commit" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```

## Case 20 — Avoids: Downgrading a dependency to avoid reading its changelog

```text
GIVEN    A situation that invites the anti-pattern "Downgrading a dependency to avoid reading its changelog"
WHEN     the agent applies `debugging` in that situation
THEN     "Downgrading a dependency to avoid reading its changelog" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Downgrading a dependency to avoid reading its changelog" appears in the output; or it is absent by accident, with nothing in `debugging` having ruled it out
```
