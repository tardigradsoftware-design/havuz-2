# Test cases — `agent-memory-design`

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
GIVEN    A task inside this skill's stated purpose: Give an agent the ability to **not relearn**. Without memory, every session starts from zero, repeats failed experiments, re-derives the same conclusions and re-asks the same questions.
WHEN     the agent executes `agent-memory-design` end to end on that task
THEN     and before delivery these specific conditions hold: "Persistence test applied; over-retention avoided (conclusions, not transcripts)"; "Retrieval scoped narrow-first, ranked by relevance × recency × confidence, capped, logged"; "Privacy review: nothing stored that must not be"
FAIL IF  "Persistence test applied; over-retention avoided (conclusions, not transcripts)" is false, or "Privacy review: nothing stored that must not be" is false, or "Retrieval scoped narrow-first, ranked by relevance × recency × confidence, capped, logged" is false
```

## Case 2 — Declines: Single-session tasks with no carry-over value

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Single-session tasks with no carry-over value
WHEN     the agent considers `agent-memory-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Single-session tasks with no carry-over value", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Single-session tasks with no carry-over value"; or `agent-memory-design` is declined without naming that exclusion
```

## Case 3 — Declines: Where the state fits comfortably in the window — use context-engineering's…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Where the state fits comfortably in the window — use context-engineering's WRITE mechanism (a scratchpad) instead of a memory system
WHEN     the agent considers `agent-memory-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Where the state fits comfortably in the window — use context-engineering's WRITE mechanism (a scratchpad) instead of a memory system", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Where the state fits comfortably in the window — use context-engineering's WRITE mechanism (a scratchpad) instead of a memory system"; or `agent-memory-design` is declined without naming that exclusion
```

## Case 4 — Declines: As a substitute for durable artefacts: code,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for durable artefacts: code, tests and documents beat embeddings whenever they are possible
WHEN     the agent considers `agent-memory-design` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for durable artefacts: code, tests and documents beat embeddings whenever they are possible", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for durable artefacts: code, tests and documents beat embeddings whenever they are possible"; or `agent-memory-design` is declined without naming that exclusion
```

## Case 5 — Declines: Where privacy or regulation forbids retention — then design for no memory,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Where privacy or regulation forbids retention — then design for no memory, explicitly
WHEN     the agent considers `agent-memory-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Where privacy or regulation forbids retention — then design for no memory, explicitly", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Where privacy or regulation forbids retention — then design for no memory, explicitly"; or `agent-memory-design` is declined without naming that exclusion
```

## Case 6 — Detects: TRANSCRIPT HOARDING

```text
GIVEN    A run of this skill in which the known failure mode is present: TRANSCRIPT HOARDING
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "TRANSCRIPT HOARDING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Storing whole sessions. Retrieval drowns; nothing is trusted."
FAIL IF  "TRANSCRIPT HOARDING" appears in the work and is reported as complete — specifically "Storing whole sessions. Retrieval drowns; nothing is trusted."
```

## Case 7 — Detects: SEMANTIC-FOR-EXACT

```text
GIVEN    A run of this skill in which the known failure mode is present: SEMANTIC-FOR-EXACT
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "SEMANTIC-FOR-EXACT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Vector search for version numbers and API names → near-miss retrieval."
FAIL IF  "SEMANTIC-FOR-EXACT" appears in the work and is reported as complete — specifically "Vector search for version numbers and API names → near-miss retrieval."
```

## Case 8 — Detects: DATELESS FACTS

```text
GIVEN    A run of this skill in which the known failure mode is present: DATELESS FACTS
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "DATELESS FACTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Use library X" with no version and no date; wrong forever after."
FAIL IF  "DATELESS FACTS" appears in the work and is reported as complete — specifically "Use library X" with no version and no date; wrong forever after."
```

## Case 9 — Detects: SILENT OVERWRITE

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT OVERWRITE
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "SILENT OVERWRITE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "New preference replaces old without a supersede link; the reason is lost."
FAIL IF  "SILENT OVERWRITE" appears in the work and is reported as complete — specifically "New preference replaces old without a supersede link; the reason is lost."
```

## Case 10 — Detects: CONTRADICTION ACCUMULATION

```text
GIVEN    A run of this skill in which the known failure mode is present: CONTRADICTION ACCUMULATION
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "CONTRADICTION ACCUMULATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Two records disagree; retrieval returns whichever ranks higher."
FAIL IF  "CONTRADICTION ACCUMULATION" appears in the work and is reported as complete — specifically "Two records disagree; retrieval returns whichever ranks higher."
```

## Case 11 — Detects: UNSCOPED MEMORY

```text
GIVEN    A run of this skill in which the known failure mode is present: UNSCOPED MEMORY
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "UNSCOPED MEMORY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One user's preference applied to another project."
FAIL IF  "UNSCOPED MEMORY" appears in the work and is reported as complete — specifically "One user's preference applied to another project."
```

## Case 12 — Detects: MEMORY AS AUTHORITY

```text
GIVEN    A run of this skill in which the known failure mode is present: MEMORY AS AUTHORITY
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "MEMORY AS AUTHORITY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Acting on expired memory without re-verification."
FAIL IF  "MEMORY AS AUTHORITY" appears in the work and is reported as complete — specifically "Acting on expired memory without re-verification."
```

## Case 13 — Detects: POISONING

```text
GIVEN    A run of this skill in which the known failure mode is present: POISONING
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "POISONING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Untrusted content written to memory and later obeyed as instruction."
FAIL IF  "POISONING" appears in the work and is reported as complete — specifically "Untrusted content written to memory and later obeyed as instruction."
```

## Case 14 — Detects: NO RETRIEVAL LOG

```text
GIVEN    A run of this skill in which the known failure mode is present: NO RETRIEVAL LOG
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "NO RETRIEVAL LOG" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Unable to tell whether memory helps at all."
FAIL IF  "NO RETRIEVAL LOG" appears in the work and is reported as complete — specifically "Unable to tell whether memory helps at all."
```

## Case 15 — Detects: EMBEDDING LOCK-IN

```text
GIVEN    A run of this skill in which the known failure mode is present: EMBEDDING LOCK-IN
WHEN     the agent executes `agent-memory-design` and reaches the point where this failure occurs
THEN     "EMBEDDING LOCK-IN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The corpus is only usable through one embedding model."
FAIL IF  "EMBEDDING LOCK-IN" appears in the work and is reported as complete — specifically "The corpus is only usable through one embedding model."
```

## Case 16 — Avoids: Embedding the entire conversation history "so the agent remembers everything"

```text
GIVEN    A situation that invites the anti-pattern "Embedding the entire conversation history "so the agent remembers everything"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Embedding the entire conversation history "so the agent remembers everything" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Embedding the entire conversation history "so the agent remembers everything" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 17 — Avoids: A `memory.json` with one growing string per session

```text
GIVEN    A situation that invites the anti-pattern "A `memory.json` with one growing string per session"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "A `memory.json` with one growing string per session" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A `memory.json` with one growing string per session" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 18 — Avoids: Overwriting a user preference with no record that it changed

```text
GIVEN    A situation that invites the anti-pattern "Overwriting a user preference with no record that it changed"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Overwriting a user preference with no record that it changed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Overwriting a user preference with no record that it changed" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 19 — Avoids: Retrieving a 2024 API fact and presenting it as current

```text
GIVEN    A situation that invites the anti-pattern "Retrieving a 2024 API fact and presenting it as current"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Retrieving a 2024 API fact and presenting it as current" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Retrieving a 2024 API fact and presenting it as current" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 20 — Avoids: Vector search as the only retrieval path for exact identifiers

```text
GIVEN    A situation that invites the anti-pattern "Vector search as the only retrieval path for exact identifiers"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Vector search as the only retrieval path for exact identifiers" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Vector search as the only retrieval path for exact identifiers" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 21 — Avoids: Letting a web page write to long-term memory without validation

```text
GIVEN    A situation that invites the anti-pattern "Letting a web page write to long-term memory without validation"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Letting a web page write to long-term memory without validation" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Letting a web page write to long-term memory without validation" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 22 — Avoids: Deleting a wrong decision instead of marking it superseded with the reason

```text
GIVEN    A situation that invites the anti-pattern "Deleting a wrong decision instead of marking it superseded with the reason"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "Deleting a wrong decision instead of marking it superseded with the reason" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Deleting a wrong decision instead of marking it superseded with the reason" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```

## Case 23 — Avoids: A hand-maintained index that nobody regenerates

```text
GIVEN    A situation that invites the anti-pattern "A hand-maintained index that nobody regenerates"
WHEN     the agent applies `agent-memory-design` in that situation
THEN     "A hand-maintained index that nobody regenerates" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A hand-maintained index that nobody regenerates" appears in the output; or it is absent by accident, with nothing in `agent-memory-design` having ruled it out
```
