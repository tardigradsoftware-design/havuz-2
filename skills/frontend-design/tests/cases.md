# Test cases — `frontend-design`

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
GIVEN    A task inside this skill's stated purpose: Produce an interface that looks **designed** rather than **generated**. The difference is not decoration; it is that every visual property traces to a decision about the content and the user's task.
WHEN     the agent executes `frontend-design` end to end on that task
THEN     and before delivery these specific conditions hold: "Real content inventory with variance (empty/one/many/error)"; "One signature element specific to this product"; "Dark mode designed separately, not inverted"
FAIL IF  "Real content inventory with variance (empty/one/many/error)" is false, or "Dark mode designed separately, not inverted" is false, or "One signature element specific to this product" is false
```

## Case 2 — Declines: Implementing an already-approved design — use frontend-implementation

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Implementing an already-approved design — use frontend-implementation
WHEN     the agent considers `frontend-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Implementing an already-approved design — use frontend-implementation", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Implementing an already-approved design — use frontend-implementation"; or `frontend-design` is declined without naming that exclusion
```

## Case 3 — Declines: Data-dense internal tooling where the answer is "use the component library…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Data-dense internal tooling where the answer is "use the component library defaults"
WHEN     the agent considers `frontend-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Data-dense internal tooling where the answer is "use the component library defaults", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Data-dense internal tooling where the answer is "use the component library defaults"; or `frontend-design` is declined without naming that exclusion
```

## Case 4 — Declines: Anything where the visual system already exists and is documented — extend…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Anything where the visual system already exists and is documented — extend it, don't redesign it
WHEN     the agent considers `frontend-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Anything where the visual system already exists and is documented — extend it, don't redesign it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Anything where the visual system already exists and is documented — extend it, don't redesign it"; or `frontend-design` is declined without naming that exclusion
```

## Case 5 — Detects: PLACEHOLDER DESIGN

```text
GIVEN    A run of this skill in which the known failure mode is present: PLACEHOLDER DESIGN
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "PLACEHOLDER DESIGN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Designing against fake copy; breaks on real content."
FAIL IF  "PLACEHOLDER DESIGN" appears in the work and is reported as complete — specifically "Designing against fake copy; breaks on real content."
```

## Case 6 — Detects: EQUAL-WEIGHT LAYOUT

```text
GIVEN    A run of this skill in which the known failure mode is present: EQUAL-WEIGHT LAYOUT
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "EQUAL-WEIGHT LAYOUT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Three things all trying to be primary."
FAIL IF  "EQUAL-WEIGHT LAYOUT" appears in the work and is reported as complete — specifically "Three things all trying to be primary."
```

## Case 7 — Detects: DECORATION AS FIX

```text
GIVEN    A run of this skill in which the known failure mode is present: DECORATION AS FIX
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "DECORATION AS FIX" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adding gradients/blur/glow to solve a flat composition."
FAIL IF  "DECORATION AS FIX" appears in the work and is reported as complete — specifically "Adding gradients/blur/glow to solve a flat composition."
```

## Case 8 — Detects: TOKEN THEATRY

```text
GIVEN    A run of this skill in which the known failure mode is present: TOKEN THEATRY
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "TOKEN THEATRY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Defining tokens and then hard-coding values in components."
FAIL IF  "TOKEN THEATRY" appears in the work and is reported as complete — specifically "Defining tokens and then hard-coding values in components."
```

## Case 9 — Detects: DESKTOP-ONLY ORDER

```text
GIVEN    A run of this skill in which the known failure mode is present: DESKTOP-ONLY ORDER
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "DESKTOP-ONLY ORDER" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Stacking the desktop hierarchy at 360 px."
FAIL IF  "DESKTOP-ONLY ORDER" appears in the work and is reported as complete — specifically "Stacking the desktop hierarchy at 360 px."
```

## Case 10 — Detects: DEFAULT FOCUS

```text
GIVEN    A run of this skill in which the known failure mode is present: DEFAULT FOCUS
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "DEFAULT FOCUS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Leaving the browser's focus ring on a custom dark surface."
FAIL IF  "DEFAULT FOCUS" appears in the work and is reported as complete — specifically "Leaving the browser's focus ring on a custom dark surface."
```

## Case 11 — Detects: SYSTEM-SWITCHING

```text
GIVEN    A run of this skill in which the known failure mode is present: SYSTEM-SWITCHING
WHEN     the agent executes `frontend-design` and reaches the point where this failure occurs
THEN     "SYSTEM-SWITCHING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Using one spacing scale on the left of the page and another on the right. BLAND OVER-CORRECTION Removing all character after slop detection, leaving nothing memorable."
FAIL IF  "SYSTEM-SWITCHING" appears in the work and is reported as complete — specifically "Using one spacing scale on the left of the page and another on the right. BLAND OVER-CORRECTION Removing all character after slop detection, leaving nothing memorable."
```

## Case 12 — Avoids: Hero + three equal cards + testimonial strip as the default answer to…

```text
GIVEN    A situation that invites the anti-pattern "Hero + three equal cards + testimonial strip as the default answer to "landing page"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Hero + three equal cards + testimonial strip as the default answer to "landing page" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Hero + three equal cards + testimonial strip as the default answer to "landing page" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 13 — Avoids: Gradient text on a headline

```text
GIVEN    A situation that invites the anti-pattern "Gradient text on a headline"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Gradient text on a headline" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Gradient text on a headline" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 14 — Avoids: A blurred orb behind the hero

```text
GIVEN    A situation that invites the anti-pattern "A blurred orb behind the hero"
WHEN     the agent applies `frontend-design` in that situation
THEN     "A blurred orb behind the hero" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A blurred orb behind the hero" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 15 — Avoids: 4 px here, 18 px there, 22 px somewhere else

```text
GIVEN    A situation that invites the anti-pattern "4 px here, 18 px there, 22 px somewhere else"
WHEN     the agent applies `frontend-design` in that situation
THEN     "4 px here, 18 px there, 22 px somewhere else" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "4 px here, 18 px there, 22 px somewhere else" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 16 — Avoids: Six font sizes none of which come from a scale

```text
GIVEN    A situation that invites the anti-pattern "Six font sizes none of which come from a scale"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Six font sizes none of which come from a scale" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Six font sizes none of which come from a scale" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 17 — Avoids: Four saturated accent colours

```text
GIVEN    A situation that invites the anti-pattern "Four saturated accent colours"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Four saturated accent colours" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Four saturated accent colours" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 18 — Avoids: `backdrop-blur` on the navbar, the cards and the modal

```text
GIVEN    A situation that invites the anti-pattern "`backdrop-blur` on the navbar, the cards and the modal"
WHEN     the agent applies `frontend-design` in that situation
THEN     "`backdrop-blur` on the navbar, the cards and the modal" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`backdrop-blur` on the navbar, the cards and the modal" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 19 — Avoids: Icons from two different sets with different stroke weights

```text
GIVEN    A situation that invites the anti-pattern "Icons from two different sets with different stroke weights"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Icons from two different sets with different stroke weights" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Icons from two different sets with different stroke weights" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 20 — Avoids: A "Trusted by 10,000+ teams" strip with no named teams

```text
GIVEN    A situation that invites the anti-pattern "A "Trusted by 10,000+ teams" strip with no named teams"
WHEN     the agent applies `frontend-design` in that situation
THEN     "A "Trusted by 10,000+ teams" strip with no named teams" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A "Trusted by 10,000+ teams" strip with no named teams" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 21 — Avoids: Animating the hero on load for no reason

```text
GIVEN    A situation that invites the anti-pattern "Animating the hero on load for no reason"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Animating the hero on load for no reason" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Animating the hero on load for no reason" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```

## Case 22 — Avoids: Designing the happy path only

```text
GIVEN    A situation that invites the anti-pattern "Designing the happy path only"
WHEN     the agent applies `frontend-design` in that situation
THEN     "Designing the happy path only" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Designing the happy path only" appears in the output; or it is absent by accident, with nothing in `frontend-design` having ruled it out
```
