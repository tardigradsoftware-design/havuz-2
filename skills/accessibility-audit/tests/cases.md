# Test cases — `accessibility-audit`

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
GIVEN    A task inside this skill's stated purpose: Establish, with evidence, whether people using assistive technology can complete the actual tasks on a page — and produce a remediation list ordered by the barrier's severity, not by how easy it is to fix.
WHEN     the agent executes `accessibility-audit` end to end on that task
THEN     and before delivery these specific conditions hold: "Target level and critical tasks agreed before auditing"; "Colour-independence, motion, target size and drag alternatives verified"; "Regression checks added to CI (axe on states + a11y unit tests on new components)"
FAIL IF  "Target level and critical tasks agreed before auditing" is false, or "Regression checks added to CI (axe on states + a11y unit tests on new components)" is false, or "Colour-independence, motion, target size and drag alternatives verified" is false
```

## Case 2 — Declines: As the only accessibility activity — designing accessibly beats auditing later

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As the only accessibility activity — designing accessibly beats auditing later
WHEN     the agent considers `accessibility-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "As the only accessibility activity — designing accessibly beats auditing later", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As the only accessibility activity — designing accessibly beats auditing later"; or `accessibility-audit` is declined without naming that exclusion
```

## Case 3 — Declines: On a prototype with no users (but keep the token-level decisions correct…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On a prototype with no users (but keep the token-level decisions correct anyway)
WHEN     the agent considers `accessibility-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "On a prototype with no users (but keep the token-level decisions correct anyway)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On a prototype with no users (but keep the token-level decisions correct anyway)"; or `accessibility-audit` is declined without naming that exclusion
```

## Case 4 — Declines: To produce a compliance badge without testing real tasks

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To produce a compliance badge without testing real tasks
WHEN     the agent considers `accessibility-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "To produce a compliance badge without testing real tasks", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To produce a compliance badge without testing real tasks"; or `accessibility-audit` is declined without naming that exclusion
```

## Case 5 — Detects: SCANNER-ONLY AUDIT

```text
GIVEN    A run of this skill in which the known failure mode is present: SCANNER-ONLY AUDIT
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "SCANNER-ONLY AUDIT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reporting axe results as an accessibility audit."
FAIL IF  "SCANNER-ONLY AUDIT" appears in the work and is reported as complete — specifically "Reporting axe results as an accessibility audit."
```

## Case 6 — Detects: OVERLAY WIDGETS

```text
GIVEN    A run of this skill in which the known failure mode is present: OVERLAY WIDGETS
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "OVERLAY WIDGETS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Installing an "accessibility overlay" instead of fixing the code. Overlays frequently conflict with users' own AT and do not achieve conformance; treat as a red flag, not a remediation."
FAIL IF  "OVERLAY WIDGETS" appears in the work and is reported as complete — specifically "Installing an "accessibility overlay" instead of fixing the code. Overlays frequently conflict with users' own AT and do not achieve conformance;"
```

## Case 7 — Detects: ARIA OVER NATIVE

```text
GIVEN    A run of this skill in which the known failure mode is present: ARIA OVER NATIVE
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "ARIA OVER NATIVE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adding ARIA to fix semantics that a native element would provide. First rule of ARIA: don't."
FAIL IF  "ARIA OVER NATIVE" appears in the work and is reported as complete — specifically "Adding ARIA to fix semantics that a native element would provide. First rule of ARIA: don't."
```

## Case 8 — Detects: ALT TEXT THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: ALT TEXT THEATRE
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "ALT TEXT THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "alt="image" on a chart carrying the only copy of a number."
FAIL IF  "ALT TEXT THEATRE" appears in the work and is reported as complete — specifically "alt="image" on a chart carrying the only copy of a number."
```

## Case 9 — Detects: FOCUS INVISIBLE

```text
GIVEN    A run of this skill in which the known failure mode is present: FOCUS INVISIBLE
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "FOCUS INVISIBLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Focus ring removed for aesthetics and never replaced."
FAIL IF  "FOCUS INVISIBLE" appears in the work and is reported as complete — specifically "Focus ring removed for aesthetics and never replaced."
```

## Case 10 — Detects: LIVE-REGION SPAM

```text
GIVEN    A run of this skill in which the known failure mode is present: LIVE-REGION SPAM
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "LIVE-REGION SPAM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "aria-live on a frequently-updating container."
FAIL IF  "LIVE-REGION SPAM" appears in the work and is reported as complete — specifically "aria-live on a frequently-updating container."
```

## Case 11 — Detects: CHECKLIST WITHOUT TASKS

```text
GIVEN    A run of this skill in which the known failure mode is present: CHECKLIST WITHOUT TASKS
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "CHECKLIST WITHOUT TASKS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auditing criteria but never attempting the user's actual journey."
FAIL IF  "CHECKLIST WITHOUT TASKS" appears in the work and is reported as complete — specifically "Auditing criteria but never attempting the user's actual journey."
```

## Case 12 — Detects: ONE AT ONLY

```text
GIVEN    A run of this skill in which the known failure mode is present: ONE AT ONLY
WHEN     the agent executes `accessibility-audit` and reaches the point where this failure occurs
THEN     "ONE AT ONLY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Testing VoiceOver on macOS and assuming Android is fine."
FAIL IF  "ONE AT ONLY" appears in the work and is reported as complete — specifically "Testing VoiceOver on macOS and assuming Android is fine."
```

## Case 13 — Avoids: "We ran Lighthouse and got 100"

```text
GIVEN    A situation that invites the anti-pattern "We ran Lighthouse and got 100"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "We ran Lighthouse and got 100" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "We ran Lighthouse and got 100" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 14 — Avoids: `aria-label="button"` on an unlabelled icon control

```text
GIVEN    A situation that invites the anti-pattern "`aria-label="button"` on an unlabelled icon control"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "`aria-label="button"` on an unlabelled icon control" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`aria-label="button"` on an unlabelled icon control" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 15 — Avoids: A `<div onclick>` styled to look like a button

```text
GIVEN    A situation that invites the anti-pattern "A `<div onclick>` styled to look like a button"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "A `<div onclick>` styled to look like a button" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A `<div onclick>` styled to look like a button" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 16 — Avoids: Placeholder text as the only label

```text
GIVEN    A situation that invites the anti-pattern "Placeholder text as the only label"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "Placeholder text as the only label" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Placeholder text as the only label" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 17 — Avoids: Removing the focus outline with `outline: none` and nothing in its place

```text
GIVEN    A situation that invites the anti-pattern "Removing the focus outline with `outline: none` and nothing in its place"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "Removing the focus outline with `outline: none` and nothing in its place" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Removing the focus outline with `outline: none` and nothing in its place" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 18 — Avoids: An accessibility overlay script presented as compliance

```text
GIVEN    A situation that invites the anti-pattern "An accessibility overlay script presented as compliance"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "An accessibility overlay script presented as compliance" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An accessibility overlay script presented as compliance" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 19 — Avoids: alt="" on an image that contains the only copy of a price

```text
GIVEN    A situation that invites the anti-pattern "alt="" on an image that contains the only copy of a price"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "alt="" on an image that contains the only copy of a price" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "alt="" on an image that contains the only copy of a price" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```

## Case 20 — Avoids: Testing only the marketing page and not the checkout

```text
GIVEN    A situation that invites the anti-pattern "Testing only the marketing page and not the checkout"
WHEN     the agent applies `accessibility-audit` in that situation
THEN     "Testing only the marketing page and not the checkout" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Testing only the marketing page and not the checkout" appears in the output; or it is absent by accident, with nothing in `accessibility-audit` having ruled it out
```
