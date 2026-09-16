# Test cases — `rag-pipeline`

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
GIVEN    A task inside this skill's stated purpose: Build a retrieval-augmented system whose quality is measured rather than assumed. RAG fails in two places that look like one problem: retrieval returns the wrong content, or generation does not use the content it was given.
WHEN     the agent executes `rag-pipeline` end to end on that task
THEN     the workflow runs in its stated order — "BUILD THE QUERY SET FIRST" through to "WATCH DRIFT"; and before delivery these specific conditions hold: "the query set is built from real queries with known-good documents"; "generation is grounded, cites chunks, and is permitted to refuse"; "drift is re-measured on a schedule"
FAIL IF  "the query set is built from real queries with known-good documents" is false, or "drift is re-measured on a schedule" is false, or the result is delivered before "WATCH DRIFT" has run
```

## Case 2 — Declines: The answer is in the model's weights and is stable.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The answer is in the model's weights and is stable.
WHEN     the agent considers `rag-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Retrieval adds latency, cost and a failure mode."
FAIL IF  the skill is run on a task where "The answer is in the model's weights and is stable.", and the consequence that exclusion states follows — "Retrieval adds latency, cost and a failure mode."; or `rag-pipeline` is declined without naming that exclusion
```

## Case 3 — Declines: The requirement is exact lookup by identifier.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The requirement is exact lookup by identifier.
WHEN     the agent considers `rag-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is a database query or a lexical search."
FAIL IF  the skill is run on a task where "The requirement is exact lookup by identifier.", and the consequence that exclusion states follows — "That is a database query or a lexical search."; or `rag-pipeline` is declined without naming that exclusion
```

## Case 4 — Declines: The corpus is tiny enough to fit in context.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The corpus is tiny enough to fit in context.
WHEN     the agent considers `rag-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Put it in context and skip the pipeline."
FAIL IF  the skill is run on a task where "The corpus is tiny enough to fit in context.", and the consequence that exclusion states follows — "Put it in context and skip the pipeline."; or `rag-pipeline` is declined without naming that exclusion
```

## Case 5 — Declines: The task needs reasoning over many documents at once rather than retrieval of…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The task needs reasoning over many documents at once rather than retrieval of a few.
WHEN     the agent considers `rag-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is a different architecture — agentic search or a map-reduce over the corpus."
FAIL IF  the skill is run on a task where "The task needs reasoning over many documents at once rather than retrieval of a few.", and the consequence that exclusion states follows — "That is a different architecture — agentic search or a map-reduce over the corpus."; or `rag-pipeline` is declined without naming that exclusion
```

## Case 6 — Declines: Nothing has been measured.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing has been measured.
WHEN     the agent considers `rag-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Build the evaluation set before tuning anything."
FAIL IF  the skill is run on a task where "Nothing has been measured.", and the consequence that exclusion states follows — "Build the evaluation set before tuning anything."; or `rag-pipeline` is declined without naming that exclusion
```

## Case 7 — Detects: Plausible wrong answers

```text
GIVEN    A run of this skill in which the known failure mode is present: Plausible wrong answers
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "retrieval metrics good, faithfulness poor" — and the response applied is the documented one: "the generation stage is not using the context; fix grounding and permit refusal"
FAIL IF  "Plausible wrong answers" reaches the output because "retrieval metrics good, faithfulness poor" was never checked; or it is caught but the response taken is not "the generation stage is not using the context; fix grounding and permit refusal"
```

## Case 8 — Detects: Good answers on the demo, bad on real queries

```text
GIVEN    A run of this skill in which the known failure mode is present: Good answers on the demo, bad on real queries
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the query set was written from the corpus" — and the response applied is the documented one: "rebuild the set from logs"
FAIL IF  "Good answers on the demo, bad on real queries" reaches the output because "the query set was written from the corpus" was never checked; or it is caught but the response taken is not "rebuild the set from logs"
```

## Case 9 — Detects: Exact identifiers not found

```text
GIVEN    A run of this skill in which the known failure mode is present: Exact identifiers not found
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "vector-only retrieval" — and the response applied is the documented one: "add lexical search and hybrid merge"
FAIL IF  "Exact identifiers not found" reaches the output because "vector-only retrieval" was never checked; or it is caught but the response taken is not "add lexical search and hybrid merge"
```

## Case 10 — Detects: Right document retrieved, wrong chunk

```text
GIVEN    A run of this skill in which the known failure mode is present: Right document retrieved, wrong chunk
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "chunks too large or too small" — and the response applied is the documented one: "re-tune chunk size and add context enrichment"
FAIL IF  "Right document retrieved, wrong chunk" reaches the output because "chunks too large or too small" was never checked; or it is caught but the response taken is not "re-tune chunk size and add context enrichment"
```

## Case 11 — Detects: Fewer than k results after filtering

```text
GIVEN    A run of this skill in which the known failure mode is present: Fewer than k results after filtering
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "post-filtering" — and the response applied is the documented one: "filter before the ANN search"
FAIL IF  "Fewer than k results after filtering" reaches the output because "post-filtering" was never checked; or it is caught but the response taken is not "filter before the ANN search"
```

## Case 12 — Detects: Recall degraded after an upgrade

```text
GIVEN    A run of this skill in which the known failure mode is present: Recall degraded after an upgrade
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "index trained or built on old data" — and the response applied is the documented one: "rebuild and re-measure"
FAIL IF  "Recall degraded after an upgrade" reaches the output because "index trained or built on old data" was never checked; or it is caught but the response taken is not "rebuild and re-measure"
```

## Case 13 — Detects: Results changed after a model swap

```text
GIVEN    A run of this skill in which the known failure mode is present: Results changed after a model swap
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "index not re-embedded" — and the response applied is the documented one: "re-embed; record the model version with the index"
FAIL IF  "Results changed after a model swap" reaches the output because "index not re-embedded" was never checked; or it is caught but the response taken is not "re-embed; record the model version with the index"
```

## Case 14 — Detects: Latency blew the budget

```text
GIVEN    A run of this skill in which the known failure mode is present: Latency blew the budget
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "reranker over too many candidates" — and the response applied is the documented one: "cap the rerank input at 50-100"
FAIL IF  "Latency blew the budget" reaches the output because "reranker over too many candidates" was never checked; or it is caught but the response taken is not "cap the rerank input at 50-100"
```

## Case 15 — Detects: Fabricated answers on unanswerable questions

```text
GIVEN    A run of this skill in which the known failure mode is present: Fabricated answers on unanswerable questions
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "refusal not permitted or not rewarded" — and the response applied is the documented one: "make "not in the context" an explicit, evaluated output"
FAIL IF  "Fabricated answers on unanswerable questions" reaches the output because "refusal not permitted or not rewarded" was never checked; or it is caught but the response taken is not "make "not in the context" an explicit, evaluated output"
```

## Case 16 — Detects: No ablation, so nobody knows what helps

```text
GIVEN    A run of this skill in which the known failure mode is present: No ablation, so nobody knows what helps
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "changes made one at a time without comparison" — and the response applied is the documented one: "run the ablation matrix and record it"
FAIL IF  "No ablation, so nobody knows what helps" reaches the output because "changes made one at a time without comparison" was never checked; or it is caught but the response taken is not "run the ablation matrix and record it"
```

## Case 17 — Avoids: VECTOR-ONLY RETRIEVAL

```text
GIVEN    A situation that invites the anti-pattern "VECTOR-ONLY RETRIEVAL", whose stated consequence is: Identifiers, negation and exact terms fail silently.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "VECTOR-ONLY RETRIEVAL" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Identifiers, negation and exact terms fail silently."
FAIL IF  "VECTOR-ONLY RETRIEVAL" appears in the output — that is, "Identifiers, negation and exact terms fail silently."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 18 — Avoids: FIXED-CHARACTER CHUNKING

```text
GIVEN    A situation that invites the anti-pattern "FIXED-CHARACTER CHUNKING", whose stated consequence is: Ignores every structural boundary the content has.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "FIXED-CHARACTER CHUNKING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Ignores every structural boundary the content has."
FAIL IF  "FIXED-CHARACTER CHUNKING" appears in the output — that is, "Ignores every structural boundary the content has."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 19 — Avoids: POST-FILTERING AFTER THE ANN SEARCH

```text
GIVEN    A situation that invites the anti-pattern "POST-FILTERING AFTER THE ANN SEARCH", whose stated consequence is: Returns fewer than k and biases recall.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "POST-FILTERING AFTER THE ANN SEARCH" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Returns fewer than k and biases recall."
FAIL IF  "POST-FILTERING AFTER THE ANN SEARCH" appears in the output — that is, "Returns fewer than k and biases recall."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 20 — Avoids: TUNING WITHOUT AN EVALUATION SET

```text
GIVEN    A situation that invites the anti-pattern "TUNING WITHOUT AN EVALUATION SET", whose stated consequence is: Every decision is then aesthetic.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "TUNING WITHOUT AN EVALUATION SET" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Every decision is then aesthetic."
FAIL IF  "TUNING WITHOUT AN EVALUATION SET" appears in the output — that is, "Every decision is then aesthetic."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 21 — Avoids: ONE END-TO-END METRIC

```text
GIVEN    A situation that invites the anti-pattern "ONE END-TO-END METRIC", whose stated consequence is: It cannot tell you which stage failed.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "ONE END-TO-END METRIC" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It cannot tell you which stage failed."
FAIL IF  "ONE END-TO-END METRIC" appears in the output — that is, "It cannot tell you which stage failed."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 22 — Avoids: CHANGING THE EMBEDDING MODEL WITHOUT RE-EMBEDDING

```text
GIVEN    A situation that invites the anti-pattern "CHANGING THE EMBEDDING MODEL WITHOUT RE-EMBEDDING", whose stated consequence is: The index becomes noise.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "CHANGING THE EMBEDDING MODEL WITHOUT RE-EMBEDDING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The index becomes noise."
FAIL IF  "CHANGING THE EMBEDDING MODEL WITHOUT RE-EMBEDDING" appears in the output — that is, "The index becomes noise."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 23 — Avoids: RECORDING THE MODEL VERSION NOWHERE

```text
GIVEN    A situation that invites the anti-pattern "RECORDING THE MODEL VERSION NOWHERE", whose stated consequence is: Six months later nobody knows whether the index matches the code.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "RECORDING THE MODEL VERSION NOWHERE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Six months later nobody knows whether the index matches the code."
FAIL IF  "RECORDING THE MODEL VERSION NOWHERE" appears in the output — that is, "Six months later nobody knows whether the index matches the code."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 24 — Avoids: A SYSTEM THAT MUST ANSWER

```text
GIVEN    A situation that invites the anti-pattern "A SYSTEM THAT MUST ANSWER", whose stated consequence is: Fabrication is the designed outcome.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "A SYSTEM THAT MUST ANSWER" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Fabrication is the designed outcome."
FAIL IF  "A SYSTEM THAT MUST ANSWER" appears in the output — that is, "Fabrication is the designed outcome."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 25 — Avoids: TRUSTING THE VENDOR'S RECALL NUMBER

```text
GIVEN    A situation that invites the anti-pattern "TRUSTING THE VENDOR'S RECALL NUMBER", whose stated consequence is: Recall is data-dependent; measure against a flat index on your corpus.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "TRUSTING THE VENDOR'S RECALL NUMBER" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Recall is data-dependent; measure against a flat index on your corpus."
FAIL IF  "TRUSTING THE VENDOR'S RECALL NUMBER" appears in the output — that is, "Recall is data-dependent; measure against a flat index on your corpus."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```

## Case 26 — Avoids: RAG FOR A CORPUS THAT FITS IN CONTEXT

```text
GIVEN    A situation that invites the anti-pattern "RAG FOR A CORPUS THAT FITS IN CONTEXT", whose stated consequence is: Added latency, cost and a failure mode for no benefit.
WHEN     the agent applies `rag-pipeline` in that situation
THEN     "RAG FOR A CORPUS THAT FITS IN CONTEXT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Added latency, cost and a failure mode for no benefit."
FAIL IF  "RAG FOR A CORPUS THAT FITS IN CONTEXT" appears in the output — that is, "Added latency, cost and a failure mode for no benefit."; or it is absent by accident, with nothing in `rag-pipeline` having ruled it out
```
