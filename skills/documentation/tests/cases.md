# Test cases — `documentation`

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
GIVEN    A task inside this skill's stated purpose: Answer a specific reader's specific question at the moment they have it, in a form they can act on. Documentation fails in two directions: it does not exist, or it exists and is wrong — and wrong documentation is worse than none,
WHEN     the agent executes `documentation` end to end on that task
THEN     and before delivery these specific conditions hold: "Reader and question named per page; one of each"; "ADRs immutable, with context, options, decision, consequences, date, deciders"; "Written to survive isolated retrieval (no cross-section pronouns, self-contained chunks)"
FAIL IF  "Reader and question named per page; one of each" is false, or "Written to survive isolated retrieval (no cross-section pronouns, self-contained chunks)" is false, or "ADRs immutable, with context, options, decision, consequences, date, deciders" is false
```

## Case 2 — Declines: To document code that should be deleted or made self-explanatory

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To document code that should be deleted or made self-explanatory
WHEN     the agent considers `documentation` for that task
THEN     the skill is not selected, because this task is the excluded case "To document code that should be deleted or made self-explanatory", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To document code that should be deleted or made self-explanatory"; or `documentation` is declined without naming that exclusion
```

## Case 3 — Declines: To produce volume: a docs site nobody reads is maintenance debt with extra…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To produce volume: a docs site nobody reads is maintenance debt with extra steps
WHEN     the agent considers `documentation` for that task
THEN     the skill is not selected, because this task is the excluded case "To produce volume: a docs site nobody reads is maintenance debt with extra steps", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To produce volume: a docs site nobody reads is maintenance debt with extra steps"; or `documentation` is declined without naming that exclusion
```

## Case 4 — Declines: As a substitute for a readable API or a good error message

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for a readable API or a good error message
WHEN     the agent considers `documentation` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for a readable API or a good error message", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for a readable API or a good error message"; or `documentation` is declined without naming that exclusion
```

## Case 5 — Detects: TYPE MIXING

```text
GIVEN    A run of this skill in which the known failure mode is present: TYPE MIXING
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "TYPE MIXING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A tutorial that stops to explain architecture; a reference that teaches."
FAIL IF  "TYPE MIXING" appears in the work and is reported as complete — specifically "A tutorial that stops to explain architecture; a reference that teaches."
```

## Case 6 — Detects: UNVERIFIED EXAMPLES

```text
GIVEN    A run of this skill in which the known failure mode is present: UNVERIFIED EXAMPLES
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "UNVERIFIED EXAMPLES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Copied from an older version; fails on the first try."
FAIL IF  "UNVERIFIED EXAMPLES" appears in the work and is reported as complete — specifically "Copied from an older version; fails on the first try."
```

## Case 7 — Detects: NO VERSION SCOPE

```text
GIVEN    A run of this skill in which the known failure mode is present: NO VERSION SCOPE
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "NO VERSION SCOPE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Correct for v2, wrong for v4, undated."
FAIL IF  "NO VERSION SCOPE" appears in the work and is reported as complete — specifically "Correct for v2, wrong for v4, undated."
```

## Case 8 — Detects: README AS PITCH

```text
GIVEN    A run of this skill in which the known failure mode is present: README AS PITCH
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "README AS PITCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adjectives and badges, no quickstart, no "should you not use this"."
FAIL IF  "README AS PITCH" appears in the work and is reported as complete — specifically "Adjectives and badges, no quickstart, no "should you not use this"."
```

## Case 9 — Detects: DUPLICATED FACTS

```text
GIVEN    A run of this skill in which the known failure mode is present: DUPLICATED FACTS
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "DUPLICATED FACTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The same instruction in four places; they drift and contradict."
FAIL IF  "DUPLICATED FACTS" appears in the work and is reported as complete — specifically "The same instruction in four places; they drift and contradict."
```

## Case 10 — Detects: GENERATED-ONLY DOCS

```text
GIVEN    A run of this skill in which the known failure mode is present: GENERATED-ONLY DOCS
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "GENERATED-ONLY DOCS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "API reference with no explanation, how-to or tutorial."
FAIL IF  "GENERATED-ONLY DOCS" appears in the work and is reported as complete — specifically "API reference with no explanation, how-to or tutorial."
```

## Case 11 — Detects: ORPHANED PAGES

```text
GIVEN    A run of this skill in which the known failure mode is present: ORPHANED PAGES
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "ORPHANED PAGES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Written once, never linked, never found."
FAIL IF  "ORPHANED PAGES" appears in the work and is reported as complete — specifically "Written once, never linked, never found."
```

## Case 12 — Detects: CHANGELOG AS GIT LOG

```text
GIVEN    A run of this skill in which the known failure mode is present: CHANGELOG AS GIT LOG
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "CHANGELOG AS GIT LOG" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "fix stuff", "update" — useless to someone upgrading."
FAIL IF  "CHANGELOG AS GIT LOG" appears in the work and is reported as complete — specifically "fix stuff", "update" — useless to someone upgrading."
```

## Case 13 — Detects: ADR REWRITING

```text
GIVEN    A run of this skill in which the known failure mode is present: ADR REWRITING
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "ADR REWRITING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Editing an accepted decision so the reasoning is lost."
FAIL IF  "ADR REWRITING" appears in the work and is reported as complete — specifically "Editing an accepted decision so the reasoning is lost."
```

## Case 14 — Detects: DOC ROT

```text
GIVEN    A run of this skill in which the known failure mode is present: DOC ROT
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "DOC ROT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No owner, no review date, no staleness scan."
FAIL IF  "DOC ROT" appears in the work and is reported as complete — specifically "No owner, no review date, no staleness scan."
```

## Case 15 — Detects: AGENT-HOSTILE PROSE

```text
GIVEN    A run of this skill in which the known failure mode is present: AGENT-HOSTILE PROSE
WHEN     the agent executes `documentation` and reaches the point where this failure occurs
THEN     "AGENT-HOSTILE PROSE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "As mentioned earlier" — retrieved in isolation, it means nothing."
FAIL IF  "AGENT-HOSTILE PROSE" appears in the work and is reported as complete — specifically "As mentioned earlier" — retrieved in isolation, it means nothing."
```

## Case 16 — Avoids: "Simply run the following command" — for a reader who has never seen the tool

```text
GIVEN    A situation that invites the anti-pattern "Simply run the following command" — for a reader who has never seen the tool"
WHEN     the agent applies `documentation` in that situation
THEN     "Simply run the following command" — for a reader who has never seen the tool" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Simply run the following command" — for a reader who has never seen the tool" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 17 — Avoids: A README whose first paragraph is three adjectives

```text
GIVEN    A situation that invites the anti-pattern "A README whose first paragraph is three adjectives"
WHEN     the agent applies `documentation` in that situation
THEN     "A README whose first paragraph is three adjectives" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A README whose first paragraph is three adjectives" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 18 — Avoids: An example whose output was never observed

```text
GIVEN    A situation that invites the anti-pattern "An example whose output was never observed"
WHEN     the agent applies `documentation` in that situation
THEN     "An example whose output was never observed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An example whose output was never observed" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 19 — Avoids: Documentation without a version or a date

```text
GIVEN    A situation that invites the anti-pattern "Documentation without a version or a date"
WHEN     the agent applies `documentation` in that situation
THEN     "Documentation without a version or a date" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Documentation without a version or a date" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 20 — Avoids: A CHANGELOG entry reading "various fixes"

```text
GIVEN    A situation that invites the anti-pattern "A CHANGELOG entry reading "various fixes"
WHEN     the agent applies `documentation` in that situation
THEN     "A CHANGELOG entry reading "various fixes" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A CHANGELOG entry reading "various fixes" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 21 — Avoids: Rewriting an ADR instead of superseding it

```text
GIVEN    A situation that invites the anti-pattern "Rewriting an ADR instead of superseding it"
WHEN     the agent applies `documentation` in that situation
THEN     "Rewriting an ADR instead of superseding it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Rewriting an ADR instead of superseding it" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 22 — Avoids: The same installation instructions in six files

```text
GIVEN    A situation that invites the anti-pattern "The same installation instructions in six files"
WHEN     the agent applies `documentation` in that situation
THEN     "The same installation instructions in six files" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "The same installation instructions in six files" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```

## Case 23 — Avoids: "See above" in a document designed to be retrieved in chunks

```text
GIVEN    A situation that invites the anti-pattern "See above" in a document designed to be retrieved in chunks"
WHEN     the agent applies `documentation` in that situation
THEN     "See above" in a document designed to be retrieved in chunks" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "See above" in a document designed to be retrieved in chunks" appears in the output; or it is absent by accident, with nothing in `documentation` having ruled it out
```
