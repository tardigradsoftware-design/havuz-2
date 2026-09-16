# Test cases — `context-engineering`

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
GIVEN    A task inside this skill's stated purpose: Treat the model's input window as a **scarce, ordered, budgeted resource** and design it deliberately — instead of appending whatever is available until something breaks. Prompt engineering asks "what words should I use?".
WHEN     the agent executes `context-engineering` end to end on that task
THEN     and before delivery these specific conditions hold: "Written token budget per step class, enforced in code"; "Sub-agent returns are structured and ≥5× smaller than their consumed context"; "Prefix cache stability checked (no volatile content in the cached prefix)"
FAIL IF  "Written token budget per step class, enforced in code" is false, or "Prefix cache stability checked (no volatile content in the cached prefix)" is false, or "Sub-agent returns are structured and ≥5× smaller than their consumed context" is false
```

## Case 2 — Declines: Single-turn tasks with everything already in the prompt

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Single-turn tasks with everything already in the prompt
WHEN     the agent considers `context-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "Single-turn tasks with everything already in the prompt", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Single-turn tasks with everything already in the prompt"; or `context-engineering` is declined without naming that exclusion
```

## Case 3 — Declines: Choosing a model — that is a capability question, not a context question

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Choosing a model — that is a capability question, not a context question
WHEN     the agent considers `context-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "Choosing a model — that is a capability question, not a context question", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Choosing a model — that is a capability question, not a context question"; or `context-engineering` is declined without naming that exclusion
```

## Case 4 — Declines: As an excuse to stuff the window "because tokens are cheap": they are not…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As an excuse to stuff the window "because tokens are cheap": they are not free in accuracy, latency or cost
WHEN     the agent considers `context-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "As an excuse to stuff the window "because tokens are cheap": they are not free in accuracy, latency or cost", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As an excuse to stuff the window "because tokens are cheap": they are not free in accuracy, latency or cost"; or `context-engineering` is declined without naming that exclusion
```

## Case 5 — Detects: CONTEXT FLOOD

```text
GIVEN    A run of this skill in which the known failure mode is present: CONTEXT FLOOD
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "CONTEXT FLOOD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Everything available goes in. Fix: budget + select."
FAIL IF  "CONTEXT FLOOD" appears in the work and is reported as complete — specifically "Everything available goes in. Fix: budget + select."
```

## Case 6 — Detects: SILENT TRUNCATION

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT TRUNCATION
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "SILENT TRUNCATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Provider or code drops the tail. Fix: measure, alert, compact early."
FAIL IF  "SILENT TRUNCATION" appears in the work and is reported as complete — specifically "Provider or code drops the tail. Fix: measure, alert, compact early."
```

## Case 7 — Detects: LOST IN THE MIDDLE

```text
GIVEN    A run of this skill in which the known failure mode is present: LOST IN THE MIDDLE
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "LOST IN THE MIDDLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Critical constraint buried at position 40k. Fix: order policy."
FAIL IF  "LOST IN THE MIDDLE" appears in the work and is reported as complete — specifically "Critical constraint buried at position 40k. Fix: order policy."
```

## Case 8 — Detects: STALE CONTEXT

```text
GIVEN    A run of this skill in which the known failure mode is present: STALE CONTEXT
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "STALE CONTEXT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "An earlier file version still in the window, contradicting the current one. Fix: evict superseded content explicitly."
FAIL IF  "STALE CONTEXT" appears in the work and is reported as complete — specifically "An earlier file version still in the window, contradicting the current one. Fix: evict superseded content explicitly."
```

## Case 9 — Detects: COMPRESSION LOSS

```text
GIVEN    A run of this skill in which the known failure mode is present: COMPRESSION LOSS
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "COMPRESSION LOSS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Summarising away the one number that mattered. Fix: preserve decisions/constraints verbatim; compress only transcripts."
FAIL IF  "COMPRESSION LOSS" appears in the work and is reported as complete — specifically "Summarising away the one number that mattered. Fix: preserve decisions/constraints verbatim; compress only transcripts."
```

## Case 10 — Detects: RETRIEVAL NOISE

```text
GIVEN    A run of this skill in which the known failure mode is present: RETRIEVAL NOISE
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "RETRIEVAL NOISE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Top-k dumps 20 chunks, 2 relevant. Fix: precision metric + reranking."
FAIL IF  "RETRIEVAL NOISE" appears in the work and is reported as complete — specifically "Top-k dumps 20 chunks, 2 relevant. Fix: precision metric + reranking."
```

## Case 11 — Detects: DUPLICATE CONTEXT

```text
GIVEN    A run of this skill in which the known failure mode is present: DUPLICATE CONTEXT
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "DUPLICATE CONTEXT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Same doc included by system prompt, RAG and tool result."
FAIL IF  "DUPLICATE CONTEXT" appears in the work and is reported as complete — specifically "Same doc included by system prompt, RAG and tool result."
```

## Case 12 — Detects: NO ISOLATION

```text
GIVEN    A run of this skill in which the known failure mode is present: NO ISOLATION
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "NO ISOLATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One agent does everything and drowns. Fix: sub-agents with contracts."
FAIL IF  "NO ISOLATION" appears in the work and is reported as complete — specifically "One agent does everything and drowns. Fix: sub-agents with contracts."
```

## Case 13 — Detects: CACHE HOSTILE ORDER

```text
GIVEN    A run of this skill in which the known failure mode is present: CACHE HOSTILE ORDER
WHEN     the agent executes `context-engineering` and reaches the point where this failure occurs
THEN     "CACHE HOSTILE ORDER" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Volatile content at the start destroys prefix caching. Fix: stable prefix, volatile suffix."
FAIL IF  "CACHE HOSTILE ORDER" appears in the work and is reported as complete — specifically "Volatile content at the start destroys prefix caching. Fix: stable prefix, volatile suffix."
```

## Case 14 — Avoids: "The model has 1M tokens so we can include the whole repo"

```text
GIVEN    A situation that invites the anti-pattern "The model has 1M tokens so we can include the whole repo"
WHEN     the agent applies `context-engineering` in that situation
THEN     "The model has 1M tokens so we can include the whole repo" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "The model has 1M tokens so we can include the whole repo" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 15 — Avoids: Re-pasting the entire conversation into every call

```text
GIVEN    A situation that invites the anti-pattern "Re-pasting the entire conversation into every call"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Re-pasting the entire conversation into every call" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Re-pasting the entire conversation into every call" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 16 — Avoids: Summarising a decision until the reason is gone

```text
GIVEN    A situation that invites the anti-pattern "Summarising a decision until the reason is gone"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Summarising a decision until the reason is gone" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Summarising a decision until the reason is gone" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 17 — Avoids: Retrieving top-50 and letting the model sort it out

```text
GIVEN    A situation that invites the anti-pattern "Retrieving top-50 and letting the model sort it out"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Retrieving top-50 and letting the model sort it out" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Retrieving top-50 and letting the model sort it out" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 18 — Avoids: Putting the actual question at the top and 30k tokens of reference below it

```text
GIVEN    A situation that invites the anti-pattern "Putting the actual question at the top and 30k tokens of reference below it"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Putting the actual question at the top and 30k tokens of reference below it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Putting the actual question at the top and 30k tokens of reference below it" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 19 — Avoids: Letting a failing tool call dump its full stack trace into the window five…

```text
GIVEN    A situation that invites the anti-pattern "Letting a failing tool call dump its full stack trace into the window five times"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Letting a failing tool call dump its full stack trace into the window five times" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Letting a failing tool call dump its full stack trace into the window five times" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 20 — Avoids: Compacting only when the API errors

```text
GIVEN    A situation that invites the anti-pattern "Compacting only when the API errors"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Compacting only when the API errors" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Compacting only when the API errors" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```

## Case 21 — Avoids: Handing a sub-agent the parent's full history "for context"

```text
GIVEN    A situation that invites the anti-pattern "Handing a sub-agent the parent's full history "for context"
WHEN     the agent applies `context-engineering` in that situation
THEN     "Handing a sub-agent the parent's full history "for context" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Handing a sub-agent the parent's full history "for context" appears in the output; or it is absent by accident, with nothing in `context-engineering` having ruled it out
```
