# Test cases — `design-systems`

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
GIVEN    A task inside this skill's stated purpose: Move consistency from a review activity to a structural property. A design system is not a component library; it is the **decision layer** (tokens) plus the **implementation layer** (components) plus the **rules** for how they compose,
WHEN     the agent executes `design-systems` end to end on that task
THEN     and before delivery these specific conditions hold: "Audit completed with counts; the case for the system is quantified"; "Layout primitives documented separately from components"; "Adoption metric tracked and published"
FAIL IF  "Audit completed with counts; the case for the system is quantified" is false, or "Adoption metric tracked and published" is false, or "Layout primitives documented separately from components" is false
```

## Case 2 — Declines: A single page, a prototype, a one-off landing site — use tokens lightly,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single page, a prototype, a one-off landing site — use tokens lightly, skip governance
WHEN     the agent considers `design-systems` for that task
THEN     the skill is not selected, because this task is the excluded case "A single page, a prototype, a one-off landing site — use tokens lightly, skip governance", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A single page, a prototype, a one-off landing site — use tokens lightly, skip governance"; or `design-systems` is declined without naming that exclusion
```

## Case 3 — Declines: Before any design exists: a system codifies decisions, it does not make them

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Before any design exists: a system codifies decisions, it does not make them
WHEN     the agent considers `design-systems` for that task
THEN     the skill is not selected, because this task is the excluded case "Before any design exists: a system codifies decisions, it does not make them", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Before any design exists: a system codifies decisions, it does not make them"; or `design-systems` is declined without naming that exclusion
```

## Case 4 — Declines: As a substitute for shipping: an unpublished component nobody uses is worse…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for shipping: an unpublished component nobody uses is worse than none
WHEN     the agent considers `design-systems` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for shipping: an unpublished component nobody uses is worse than none", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for shipping: an unpublished component nobody uses is worse than none"; or `design-systems` is declined without naming that exclusion
```

## Case 5 — Detects: TWO-TIER COLLAPSE

```text
GIVEN    A run of this skill in which the known failure mode is present: TWO-TIER COLLAPSE
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "TWO-TIER COLLAPSE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Skipping semantic tokens; components bind to palette values. Fix: lint against tier-1 usage in components."
FAIL IF  "TWO-TIER COLLAPSE" appears in the work and is reported as complete — specifically "Skipping semantic tokens; components bind to palette values. Fix: lint against tier-1 usage in components."
```

## Case 6 — Detects: TOKEN PROLIFERATION

```text
GIVEN    A run of this skill in which the known failure mode is present: TOKEN PROLIFERATION
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "TOKEN PROLIFERATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A token per screen. Fix: additions need a proposal and a reuse check."
FAIL IF  "TOKEN PROLIFERATION" appears in the work and is reported as complete — specifically "A token per screen. Fix: additions need a proposal and a reuse check."
```

## Case 7 — Detects: UNENFORCED SYSTEM

```text
GIVEN    A run of this skill in which the known failure mode is present: UNENFORCED SYSTEM
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "UNENFORCED SYSTEM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Tokens exist; hard-coded values keep arriving. Fix: CI + lint."
FAIL IF  "UNENFORCED SYSTEM" appears in the work and is reported as complete — specifically "Tokens exist; hard-coded values keep arriving. Fix: CI + lint."
```

## Case 8 — Detects: ZOMBIE LIBRARY

```text
GIVEN    A run of this skill in which the known failure mode is present: ZOMBIE LIBRARY
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "ZOMBIE LIBRARY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Beautiful components nobody uses. Fix: adoption metric, and build the system from real screens rather than in isolation."
FAIL IF  "ZOMBIE LIBRARY" appears in the work and is reported as complete — specifically "Beautiful components nobody uses. Fix: adoption metric, and build the system from real screens rather than in isolation."
```

## Case 9 — Detects: VERSIONING BY VIBES

```text
GIVEN    A run of this skill in which the known failure mode is present: VERSIONING BY VIBES
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "VERSIONING BY VIBES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Renaming tokens without deprecation breaks every consumer. DARK MODE AS INVERSION Filter-based dark mode with broken contrast and elevation."
FAIL IF  "VERSIONING BY VIBES" appears in the work and is reported as complete — specifically "Renaming tokens without deprecation breaks every consumer. DARK MODE AS INVERSION Filter-based dark mode with broken contrast and elevation."
```

## Case 10 — Detects: OVER-ABSTRACTION

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-ABSTRACTION
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "OVER-ABSTRACTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Configurable components with 40 props. Fix: closed variant sets."
FAIL IF  "OVER-ABSTRACTION" appears in the work and is reported as complete — specifically "Configurable components with 40 props. Fix: closed variant sets."
```

## Case 11 — Detects: DOCUMENTATION DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: DOCUMENTATION DRIFT
WHEN     the agent executes `design-systems` and reaches the point where this failure occurs
THEN     "DOCUMENTATION DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Docs describe a version that no longer exists. Fix: publish from code."
FAIL IF  "DOCUMENTATION DRIFT" appears in the work and is reported as complete — specifically "Docs describe a version that no longer exists. Fix: publish from code."
```

## Case 12 — Avoids: `--blue-500` used in a component instead of `--action-primary-bg`

```text
GIVEN    A situation that invites the anti-pattern "`--blue-500` used in a component instead of `--action-primary-bg`"
WHEN     the agent applies `design-systems` in that situation
THEN     "`--blue-500` used in a component instead of `--action-primary-bg`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`--blue-500` used in a component instead of `--action-primary-bg`" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 13 — Avoids: A `<Button variant="custom" style={{...}} />` escape hatch

```text
GIVEN    A situation that invites the anti-pattern "A `<Button variant="custom" style={{...}} />` escape hatch"
WHEN     the agent applies `design-systems` in that situation
THEN     "A `<Button variant="custom" style={{...}} />` escape hatch" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A `<Button variant="custom" style={{...}} />` escape hatch" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 14 — Avoids: Building the system for six months before shipping a single screen with it

```text
GIVEN    A situation that invites the anti-pattern "Building the system for six months before shipping a single screen with it"
WHEN     the agent applies `design-systems` in that situation
THEN     "Building the system for six months before shipping a single screen with it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Building the system for six months before shipping a single screen with it" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 15 — Avoids: Two "Button" components in the same codebase

```text
GIVEN    A situation that invites the anti-pattern "Two "Button" components in the same codebase"
WHEN     the agent applies `design-systems` in that situation
THEN     "Two "Button" components in the same codebase" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Two "Button" components in the same codebase" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 16 — Avoids: Renaming a token in the same commit that removes the old one

```text
GIVEN    A situation that invites the anti-pattern "Renaming a token in the same commit that removes the old one"
WHEN     the agent applies `design-systems` in that situation
THEN     "Renaming a token in the same commit that removes the old one" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Renaming a token in the same commit that removes the old one" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 17 — Avoids: Documenting components with screenshots of a design file that has since…

```text
GIVEN    A situation that invites the anti-pattern "Documenting components with screenshots of a design file that has since changed"
WHEN     the agent applies `design-systems` in that situation
THEN     "Documenting components with screenshots of a design file that has since changed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Documenting components with screenshots of a design file that has since changed" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```

## Case 18 — Avoids: Dark mode via `filter: invert(1)`

```text
GIVEN    A situation that invites the anti-pattern "Dark mode via `filter: invert(1)`"
WHEN     the agent applies `design-systems` in that situation
THEN     "Dark mode via `filter: invert(1)`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Dark mode via `filter: invert(1)`" appears in the output; or it is absent by accident, with nothing in `design-systems` having ruled it out
```
