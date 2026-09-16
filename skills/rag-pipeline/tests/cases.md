# Test cases — `rag-pipeline`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Build a retrieval-augmented system whose quality is measured rather than assumed. RAG fails in two places that look like one problem: retrieval returns the wrong content, or generation does not use the content it was giv…
WHEN     the agent selects and executes the `rag-pipeline` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The answer is in the model's weights and is stable

```text
GIVEN    A task that looks like a match but is the excluded case: Retrieval adds latency, cost and a failure mode.
WHEN     the agent considers the `rag-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The requirement is exact lookup by identifier

```text
GIVEN    A task that looks like a match but is the excluded case: That is a database query or a lexical search.
WHEN     the agent considers the `rag-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The corpus is tiny enough to fit in context

```text
GIVEN    A task that looks like a match but is the excluded case: Put it in context and skip the pipeline.
WHEN     the agent considers the `rag-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Plausible wrong answers

```text
GIVEN    A run in which the known failure mode is present — Plausible wrong answers
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "retrieval metrics good, faithfulness poor" and the documented response is applied: the generation stage is not using the context; fix grounding and permit refusal
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Good answers on the demo, bad on real queries

```text
GIVEN    A run in which the known failure mode is present — Good answers on the demo, bad on real queries
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "the query set was written from the corpus" and the documented response is applied: rebuild the set from logs
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Exact identifiers not found

```text
GIVEN    A run in which the known failure mode is present — Exact identifiers not found
WHEN     the agent executes `rag-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "vector-only retrieval" and the documented response is applied: add lexical search and hybrid merge
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: VECTOR-ONLY RETRIEVAL

```text
GIVEN    A situation that invites the anti-pattern: Identifiers, negation and exact terms fail silently.
WHEN     the agent applies `rag-pipeline`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: FIXED-CHARACTER CHUNKING

```text
GIVEN    A situation that invites the anti-pattern: Ignores every structural boundary the content has.
WHEN     the agent applies `rag-pipeline`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
