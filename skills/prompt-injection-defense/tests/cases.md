# Test cases — `prompt-injection-defense`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Design so that a successful injection cannot do much. A model has one channel — tokens in, tokens out — so instructions and data are processed by the same mechanism and cannot be reliably separated. Controls that reduce …
WHEN     the agent selects and executes the `prompt-injection-defense` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The model has no tools and no access to private data

```text
GIVEN    A task that looks like a match but is the excluded case: Then the worst outcome is a wrong or
WHEN     the agent considers the `prompt-injection-defense` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The proposal is a denylist, a keyword filter or a hardened system prom…

```text
GIVEN    A task that looks like a match but is the excluded case: Those
WHEN     the agent considers the `prompt-injection-defense` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The system processes only trusted, first-party content with no externa…

```text
GIVEN    A task that looks like a match but is the excluded case: Re-check this
WHEN     the agent considers the `prompt-injection-defense` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Worst case is unacceptable

```text
GIVEN    A run in which the known failure mode is present — Worst case is unacceptable
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is detected by "a tool can delete, send or pay without a gate" and the documented response is applied: remove the capability or add an external gate; do not proceed
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Gate is inside the model

```text
GIVEN    A run in which the known failure mode is present — Gate is inside the model
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is detected by "approval depends on the model deciding to ask" and the documented response is applied: move the gate to a wrapper or policy engine
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Standing admin credential

```text
GIVEN    A run in which the known failure mode is present — Standing admin credential
WHEN     the agent executes `prompt-injection-defense` and reaches the point where this failure occurs
THEN     the failure is detected by "one token for everything" and the documented response is applied: scope per task, short-lived
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL

```text
GIVEN    A situation that invites the anti-pattern: Instruction-following is the exploited capability;
WHEN     the agent applies `prompt-injection-defense`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: DENYLISTS AND KEYWORD FILTERS

```text
GIVEN    A situation that invites the anti-pattern: Evaded by paraphrase, translation, encoding, images, or splitting a
WHEN     the agent applies `prompt-injection-defense`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
