# Test cases — `skill-curation`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Decide what enters the active corpus, at what confidence, and what must be refused. Curation is the control that keeps a growing knowledge base trustworthy: without it, volume rises while average confidence falls, and ev…
WHEN     the agent selects and executes the `skill-curation` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The content is being written for the first time

```text
GIVEN    A task that looks like a match but is the excluded case: Author it, then curate it; self-curation of
WHEN     the agent considers the `skill-curation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The question is whether a claim is true rather than whether it belongs…

```text
GIVEN    A task that looks like a match but is the excluded case: That is
WHEN     the agent considers the `skill-curation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The entry is generated output with no human review

```text
GIVEN    A task that looks like a match but is the excluded case: Generated content is not admitted; it is a draft.
WHEN     the agent considers the `skill-curation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Excluded content admitted

```text
GIVEN    A run in which the known failure mode is present — Excluded content admitted
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is detected by "the policy check was skipped" and the documented response is applied: refuse and record; public reachability is not permission
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Unlicensed content vendored

```text
GIVEN    A run in which the known failure mode is present — Unlicensed content vendored
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is detected by "license: null and a copy in the tree" and the documented response is applied: remove the copy; keep a linked summary with attribution
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Source does not support the claim

```text
GIVEN    A run in which the known failure mode is present — Source does not support the claim
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is detected by "re-reading it does not back the statement" and the documented response is applied: re-grade or remove the claim
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: CURATING BY VOLUME

```text
GIVEN    A situation that invites the anti-pattern: Admitting everything and grading nothing; average confidence falls as the
WHEN     the agent applies `skill-curation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR

```text
GIVEN    A situation that invites the anti-pattern: Popularity does not launder provenance, and
WHEN     the agent applies `skill-curation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
