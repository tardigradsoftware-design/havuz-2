# Test cases — `context-engineering`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Treat the model's input window as a **scarce, ordered, budgeted resource** and design it deliberately — instead of appending whatever is available until something breaks. Prompt engineering asks "what words should I use?…
WHEN     the agent selects and executes the `context-engineering` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Single-turn tasks with everything already in the prompt

```text
GIVEN    A task that looks like a match but is the excluded case: Single-turn tasks with everything already in the prompt
WHEN     the agent considers the `context-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Choosing a model — that is a capability question, not a context questi…

```text
GIVEN    A task that looks like a match but is the excluded case: Choosing a model — that is a capability question, not a context question
WHEN     the agent considers the `context-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As an excuse to stuff the window "because tokens are cheap": they are …

```text
GIVEN    A task that looks like a match but is the excluded case: As an excuse to stuff the window "because tokens are cheap": they are not free in
WHEN     the agent considers the `context-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "The model has 1M tokens so we can include the whole repo"

```text
GIVEN    A situation that invites the anti-pattern: "The model has 1M tokens so we can include the whole repo"
WHEN     the agent applies `context-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Re-pasting the entire conversation into every call

```text
GIVEN    A situation that invites the anti-pattern: Re-pasting the entire conversation into every call
WHEN     the agent applies `context-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
