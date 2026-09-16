# Test cases — `visual-design-research`

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
GIVEN    A task inside this skill's stated purpose: Replace "make it look good" with a **written, defensible visual direction** derived from real references. Design quality is mostly a research problem: agents produce generic output because they skip the step where a human designer would…
WHEN     the agent executes `visual-design-research` end to end on that task
THEN     and before delivery these specific conditions hold: "Intended impression written before collecting"; "Design Direction Brief complete, including explicit rejections"; "A third party could rebuild the direction from the brief alone"
FAIL IF  "Intended impression written before collecting" is false, or "A third party could rebuild the direction from the brief alone" is false, or "Design Direction Brief complete, including explicit rejections" is false
```

## Case 2 — Declines: A brand book already exists — read it, do not research around it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A brand book already exists — read it, do not research around it
WHEN     the agent considers `visual-design-research` for that task
THEN     the skill is not selected, because this task is the excluded case "A brand book already exists — read it, do not research around it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A brand book already exists — read it, do not research around it"; or `visual-design-research` is declined without naming that exclusion
```

## Case 3 — Declines: Extending an existing product surface: research the product, not the internet

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Extending an existing product surface: research the product, not the internet
WHEN     the agent considers `visual-design-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Extending an existing product surface: research the product, not the internet", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Extending an existing product surface: research the product, not the internet"; or `visual-design-research` is declined without naming that exclusion
```

## Case 4 — Declines: Purely functional internal tooling

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Purely functional internal tooling
WHEN     the agent considers `visual-design-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Purely functional internal tooling", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Purely functional internal tooling"; or `visual-design-research` is declined without naming that exclusion
```

## Case 5 — Declines: When the deadline allows no research: say so,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the deadline allows no research: say so, pick the safest conventional direction, and record that it was unresearched
WHEN     the agent considers `visual-design-research` for that task
THEN     the skill is not selected, because this task is the excluded case "When the deadline allows no research: say so, pick the safest conventional direction, and record that it was unresearched", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the deadline allows no research: say so, pick the safest conventional direction, and record that it was unresearched"; or `visual-design-research` is declined without naming that exclusion
```

## Case 6 — Detects: MOODBOARD WITHOUT ANALYSIS

```text
GIVEN    A run of this skill in which the known failure mode is present: MOODBOARD WITHOUT ANALYSIS
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "MOODBOARD WITHOUT ANALYSIS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Pretty pictures, zero extracted decisions."
FAIL IF  "MOODBOARD WITHOUT ANALYSIS" appears in the work and is reported as complete — specifically "Pretty pictures, zero extracted decisions."
```

## Case 7 — Detects: SINGLE-POOL RESEARCH

```text
GIVEN    A run of this skill in which the known failure mode is present: SINGLE-POOL RESEARCH
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "SINGLE-POOL RESEARCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Only looking at competitors → you will look like a competitor."
FAIL IF  "SINGLE-POOL RESEARCH" appears in the work and is reported as complete — specifically "Only looking at competitors → you will look like a competitor."
```

## Case 8 — Detects: AWWARD-WASHING

```text
GIVEN    A run of this skill in which the known failure mode is present: AWWARD-WASHING
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "AWWARD-WASHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Copying expressive agency sites into a data-dense tool."
FAIL IF  "AWWARD-WASHING" appears in the work and is reported as complete — specifically "Copying expressive agency sites into a data-dense tool."
```

## Case 9 — Detects: DIFFERENTIATOR MAXIMALISM

```text
GIVEN    A run of this skill in which the known failure mode is present: DIFFERENTIATOR MAXIMALISM
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "DIFFERENTIATOR MAXIMALISM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Five deliberate deviations → incoherence, not character."
FAIL IF  "DIFFERENTIATOR MAXIMALISM" appears in the work and is reported as complete — specifically "Five deliberate deviations → incoherence, not character."
```

## Case 10 — Detects: GAP CHASING

```text
GIVEN    A run of this skill in which the known failure mode is present: GAP CHASING
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "GAP CHASING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Choosing a position because it is empty, not because it fits."
FAIL IF  "GAP CHASING" appears in the work and is reported as complete — specifically "Choosing a position because it is empty, not because it fits."
```

## Case 11 — Detects: COPYING SURFACE

```text
GIVEN    A run of this skill in which the known failure mode is present: COPYING SURFACE
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "COPYING SURFACE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Replicating a specific visual without its underlying system."
FAIL IF  "COPYING SURFACE" appears in the work and is reported as complete — specifically "Replicating a specific visual without its underlying system."
```

## Case 12 — Detects: BRIEF DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: BRIEF DRIFT
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "BRIEF DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Designing tokens that the brief does not support."
FAIL IF  "BRIEF DRIFT" appears in the work and is reported as complete — specifically "Designing tokens that the brief does not support."
```

## Case 13 — Detects: NO ANTI-REFERENCES

```text
GIVEN    A run of this skill in which the known failure mode is present: NO ANTI-REFERENCES
WHEN     the agent executes `visual-design-research` and reaches the point where this failure occurs
THEN     "NO ANTI-REFERENCES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Nothing to steer away from, so defaults creep back in."
FAIL IF  "NO ANTI-REFERENCES" appears in the work and is reported as complete — specifically "Nothing to steer away from, so defaults creep back in."
```

## Case 14 — Avoids: "Let's do a dark, minimal, modern look" with no references and no reasoning

```text
GIVEN    A situation that invites the anti-pattern "Let's do a dark, minimal, modern look" with no references and no reasoning"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "Let's do a dark, minimal, modern look" with no references and no reasoning" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Let's do a dark, minimal, modern look" with no references and no reasoning" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```

## Case 15 — Avoids: A moodboard of 40 screenshots and no written analysis

```text
GIVEN    A situation that invites the anti-pattern "A moodboard of 40 screenshots and no written analysis"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "A moodboard of 40 screenshots and no written analysis" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A moodboard of 40 screenshots and no written analysis" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```

## Case 16 — Avoids: Choosing an aesthetic because a competitor does not have it

```text
GIVEN    A situation that invites the anti-pattern "Choosing an aesthetic because a competitor does not have it"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "Choosing an aesthetic because a competitor does not have it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Choosing an aesthetic because a competitor does not have it" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```

## Case 17 — Avoids: Naming an aesthetic ("brutalist", "glassmorphism") instead of describing…

```text
GIVEN    A situation that invites the anti-pattern "Naming an aesthetic ("brutalist", "glassmorphism") instead of describing decisions"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "Naming an aesthetic ("brutalist", "glassmorphism") instead of describing decisions" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Naming an aesthetic ("brutalist", "glassmorphism") instead of describing decisions" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```

## Case 18 — Avoids: Copying a reference's colour palette while ignoring its density and type…

```text
GIVEN    A situation that invites the anti-pattern "Copying a reference's colour palette while ignoring its density and type decisions"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "Copying a reference's colour palette while ignoring its density and type decisions" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Copying a reference's colour palette while ignoring its density and type decisions" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```

## Case 19 — Avoids: Skipping anti-references, then shipping a gradient hero

```text
GIVEN    A situation that invites the anti-pattern "Skipping anti-references, then shipping a gradient hero"
WHEN     the agent applies `visual-design-research` in that situation
THEN     "Skipping anti-references, then shipping a gradient hero" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Skipping anti-references, then shipping a gradient hero" appears in the output; or it is absent by accident, with nothing in `visual-design-research` having ruled it out
```
