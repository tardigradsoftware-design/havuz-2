# Test cases — `ai-slop-detection`

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
GIVEN    A task inside this skill's stated purpose: Give an agent a **falsifiable vocabulary** for "this looks AI-generated", and a mechanical path from detection to fix. "Slop" is not a taste judgement.
WHEN     the agent executes `ai-slop-detection` end to end on that task
THEN     and before delivery these specific conditions hold: "Every symptom has an ID, evidence and severity"; "All filler copy replaced with specific, verifiable statements"; "At least one deliberate, non-generic design decision is documented"
FAIL IF  "Every symptom has an ID, evidence and severity" is false, or "At least one deliberate, non-generic design decision is documented" is false, or "All filler copy replaced with specific, verifiable statements" is false
```

## Case 2 — Declines: Internal tools where utility is the only requirement — say so and move on

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Internal tools where utility is the only requirement — say so and move on
WHEN     the agent considers `ai-slop-detection` for that task
THEN     the skill is not selected, because this task is the excluded case "Internal tools where utility is the only requirement — say so and move on", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Internal tools where utility is the only requirement — say so and move on"; or `ai-slop-detection` is declined without naming that exclusion
```

## Case 3 — Declines: Deliberately brutalist, maximalist or expressive designs: apply the craft…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Deliberately brutalist, maximalist or expressive designs: apply the craft checks (contrast, spacing consistency, hierarchy) but not the "restraint" checks
WHEN     the agent considers `ai-slop-detection` for that task
THEN     the skill is not selected, because this task is the excluded case "Deliberately brutalist, maximalist or expressive designs: apply the craft checks (contrast, spacing consistency, hierarchy) but not the "restraint" checks", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Deliberately brutalist, maximalist or expressive designs: apply the craft checks (contrast, spacing consistency,"; or `ai-slop-detection` is declined without naming that exclusion
```

## Case 4 — Declines: As a substitute for accessibility-audit — this skill catches visual smell,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for accessibility-audit — this skill catches visual smell, not WCAG failures
WHEN     the agent considers `ai-slop-detection` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for accessibility-audit — this skill catches visual smell, not WCAG failures", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for accessibility-audit — this skill catches visual smell, not WCAG failures"; or `ai-slop-detection` is declined without naming that exclusion
```

## Case 5 — Declines: On a design system's own primitives: judge the composition,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On a design system's own primitives: judge the composition, not the component library
WHEN     the agent considers `ai-slop-detection` for that task
THEN     the skill is not selected, because this task is the excluded case "On a design system's own primitives: judge the composition, not the component library", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On a design system's own primitives: judge the composition, not the component library"; or `ai-slop-detection` is declined without naming that exclusion
```

## Case 6 — Detects: TASTE-WASHING

```text
GIVEN    A run of this skill in which the known failure mode is present: TASTE-WASHING
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "TASTE-WASHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Declaring something slop without evidence. Fix: symptom ID + file:line."
FAIL IF  "TASTE-WASHING" appears in the work and is reported as complete — specifically "Declaring something slop without evidence. Fix: symptom ID + file:line."
```

## Case 7 — Detects: STYLE CONFORMISM

```text
GIVEN    A run of this skill in which the known failure mode is present: STYLE CONFORMISM
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "STYLE CONFORMISM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Fixing" slop by applying a different cliché (e.g. brutalist-by-default). Fix: derive choices from brand and content, not from a trending aesthetic."
FAIL IF  "STYLE CONFORMISM" appears in the work and is reported as complete — specifically "Fixing" slop by applying a different cliché (e.g. brutalist-by-default). Fix: derive choices from brand and content, not from a trending aesthetic."
```

## Case 8 — Detects: OVER-CORRECTION

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-CORRECTION
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "OVER-CORRECTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Stripping all character until the design is bland. Fix: the goal is deliberate, not minimal. Keep one signature element."
FAIL IF  "OVER-CORRECTION" appears in the work and is reported as complete — specifically "Stripping all character until the design is bland. Fix: the goal is deliberate, not minimal. Keep one signature element."
```

## Case 9 — Detects: TOKEN THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: TOKEN THEATRE
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "TOKEN THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Creating design tokens nobody uses. Fix: grep for hard-coded values after."
FAIL IF  "TOKEN THEATRE" appears in the work and is reported as complete — specifically "Creating design tokens nobody uses. Fix: grep for hard-coded values after."
```

## Case 10 — Detects: SCREENSHOT-ONLY

```text
GIVEN    A run of this skill in which the known failure mode is present: SCREENSHOT-ONLY
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "SCREENSHOT-ONLY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reviewing at 1440 px and missing 360 px. Fix: all required breakpoints."
FAIL IF  "SCREENSHOT-ONLY" appears in the work and is reported as complete — specifically "Reviewing at 1440 px and missing 360 px. Fix: all required breakpoints."
```

## Case 11 — Detects: FIXING SYMPTOMS

```text
GIVEN    A run of this skill in which the known failure mode is present: FIXING SYMPTOMS
WHEN     the agent executes `ai-slop-detection` and reaches the point where this failure occurs
THEN     "FIXING SYMPTOMS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Re-colouring a gradient instead of asking why it exists. Fix: root-cause grouping."
FAIL IF  "FIXING SYMPTOMS" appears in the work and is reported as complete — specifically "Re-colouring a gradient instead of asking why it exists. Fix: root-cause grouping."
```

## Case 12 — Avoids: Adding a gradient to "make it less flat"

```text
GIVEN    A situation that invites the anti-pattern "Adding a gradient to "make it less flat"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Adding a gradient to "make it less flat" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding a gradient to "make it less flat" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 13 — Avoids: Adding a blurred orb behind the hero for "depth"

```text
GIVEN    A situation that invites the anti-pattern "Adding a blurred orb behind the hero for "depth"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Adding a blurred orb behind the hero for "depth" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding a blurred orb behind the hero for "depth" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 14 — Avoids: Three equal feature cards because the content has three items

```text
GIVEN    A situation that invites the anti-pattern "Three equal feature cards because the content has three items"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Three equal feature cards because the content has three items" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Three equal feature cards because the content has three items" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 15 — Avoids: Inter at 400/600 with 16/24/48 px because that is what the template shipped

```text
GIVEN    A situation that invites the anti-pattern "Inter at 400/600 with 16/24/48 px because that is what the template shipped"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Inter at 400/600 with 16/24/48 px because that is what the template shipped" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Inter at 400/600 with 16/24/48 px because that is what the template shipped" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 16 — Avoids: "AI-powered" badge on a form

```text
GIVEN    A situation that invites the anti-pattern "AI-powered" badge on a form"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "AI-powered" badge on a form" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "AI-powered" badge on a form" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 17 — Avoids: Animating the logo on page load

```text
GIVEN    A situation that invites the anti-pattern "Animating the logo on page load"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Animating the logo on page load" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Animating the logo on page load" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 18 — Avoids: Dark mode as a single neon accent on #0a0a0a with glow shadows

```text
GIVEN    A situation that invites the anti-pattern "Dark mode as a single neon accent on #0a0a0a with glow shadows"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Dark mode as a single neon accent on #0a0a0a with glow shadows" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Dark mode as a single neon accent on #0a0a0a with glow shadows" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```

## Case 19 — Avoids: Shipping decorative buttons to fill a layout gap

```text
GIVEN    A situation that invites the anti-pattern "Shipping decorative buttons to fill a layout gap"
WHEN     the agent applies `ai-slop-detection` in that situation
THEN     "Shipping decorative buttons to fill a layout gap" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Shipping decorative buttons to fill a layout gap" appears in the output; or it is absent by accident, with nothing in `ai-slop-detection` having ruled it out
```
