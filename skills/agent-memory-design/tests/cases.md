# Test cases — `agent-memory-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Give an agent the ability to **not relearn**. Without memory, every session starts from zero, repeats failed experiments, re-derives the same conclusions and re-asks the same questions. With badly designed memory, the ag…
WHEN     the agent selects and executes the `agent-memory-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Single-session tasks with no carry-over value

```text
GIVEN    A task that looks like a match but is the excluded case: Single-session tasks with no carry-over value
WHEN     the agent considers the `agent-memory-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Where the state fits comfortably in the window — use context-engineeri…

```text
GIVEN    A task that looks like a match but is the excluded case: Where the state fits comfortably in the window — use context-engineering's WRITE
WHEN     the agent considers the `agent-memory-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a substitute for durable artefacts: code, tests and documents beat …

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for durable artefacts: code, tests and documents beat embeddings
WHEN     the agent considers the `agent-memory-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Embedding the entire conversation history "so the agent remembers ever…

```text
GIVEN    A situation that invites the anti-pattern: Embedding the entire conversation history "so the agent remembers everything"
WHEN     the agent applies `agent-memory-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A `memory.json` with one growing string per session

```text
GIVEN    A situation that invites the anti-pattern: A `memory.json` with one growing string per session
WHEN     the agent applies `agent-memory-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
