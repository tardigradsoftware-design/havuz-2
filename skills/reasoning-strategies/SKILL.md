---
name: reasoning-strategies
version: 1.0.0
description: >-
  Choose and apply a reasoning strategy to a task from its structure: direct answer, decomposition, retrieval-grounded reasoning, verification loops, self-consistency and search — with the cost of each and the evidence for when each helps.
category: agent-engineering
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [reasoning, chain-of-thought, decomposition, self-consistency, verification, task-shape, compute-budget]
applies_to: [any]
priority: 4
requires: []
conflicts_with: []
estimated_tokens: 2552
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Inputs"
    anchor: "#inputs"
    purpose: implementation
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    url: https://arxiv.org/abs/2201.11903
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Wei et al. — verified against the primary arXiv abs page on 2026-09-15 (v6, 2023-01-10). Establishes the effect and its scale dependence, which is why step 7 forbids adding it by default."
  - title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    url: https://arxiv.org/abs/2203.11171
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Wang et al. — the sampling-and-vote procedure in step 5 and its linear cost."
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    url: https://arxiv.org/abs/2305.10601
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Yao et al. (NeurIPS 2023) — verified against the primary source. The search strategy in step 6 and its cost."
  - title: "Language Models Do Not Always Say What They Think"
    url: https://arxiv.org/abs/2305.04388
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: high
    verified_at: 2026-09-15
    note: "Turpin et al. — unfaithful explanations; the basis for step 11, not using stated reasoning as an audit trail."
related_skills: [prompt-engineering, context-engineering, evidence-validation, web-research, research-synthesis]
related_repositories: []
tests: 9
---
# Reasoning Strategies

## Purpose

Match the reasoning strategy to the structure of the task and pay for only as much of it as the task
needs. The strategies differ by orders of magnitude in cost, and the popular default — always ask the
model to think step by step — is measurably neutral or negative on some models and tasks. Choosing is an
engineering decision with a compute budget attached.

## When to Use

```text
✓ a task is failing and the failure looks like a reasoning failure rather than a knowledge or format one
✓ a new task class is being built and its strategy must be chosen deliberately
✓ accuracy can be traded against latency or cost and the trade needs quantifying
✓ a reasoning-heavy pipeline is being debugged and the failure point must be localised
```

## When NOT to Use

```text
✗ The model lacks the information. That is a retrieval problem; a strategy will not supply facts.
✗ The output format is the problem. Fix the format with a schema and validation.
✗ The task is a single deterministic operation. Call a function.
✗ There is no evaluation set. Without one, strategy selection is aesthetic and the cost is real.
✗ The correct behaviour is to refuse or escalate. Strategy choice does not substitute for a boundary.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| The task, with real examples | yes | including the failures, not only the successes |
| Verifiability | yes | can a correct answer be checked cheaply and mechanically? |
| Step structure | yes | is the answer one step, a chain, a branching search, or a lookup plus computation? |
| Compute budget | yes | latency and cost ceiling per task, stated before choosing |
| Evaluation set | yes | with known-correct answers, to compare strategies on |

## Workflow

```text
1. CLASSIFY THE TASK BY STRUCTURE.   This determines the candidate strategies more than any other
   property:
     - LOOKUP                       the answer is a fact. Retrieval, not reasoning.
     - SINGLE-STEP TRANSFORMATION     one operation on given input. Direct answer; a chain adds latency
                                      and can introduce error.
     - MULTI-STEP WITH ONE PATH       each step depends on the previous. Decomposition, explicitly
                                      ordered.
     - MULTI-STEP WITH BRANCHING      several candidate paths, some dead ends. Search with evaluation of
                                      intermediate states.
     - OPEN-ENDED GENERATION          many acceptable answers. Constraints and examples, not search.
     - VERIFIABLE COMPUTATION         a checker exists (tests, arithmetic, a compiler). Generate and
                                      verify, iterating on failure.

2. ASK WHETHER THE ANSWER IS CHEAPLY VERIFIABLE.   This is the highest-leverage question available.
   When verification is cheap and mechanical, generate-and-verify beats every reasoning-only strategy,
   because the verifier supplies a signal the model cannot. When it is not, you are paying for a
   plausible answer and should budget accordingly.

3. START WITH THE CHEAPEST STRATEGY THAT FITS THE STRUCTURE.   Direct answer first. Add decomposition
   only if the task has genuine multi-step structure. Add sampling or search only if the branch space is
   real and the verifier or evaluator can choose between branches.

4. DECOMPOSE EXPLICITLY WHEN THE TASK IS MULTI-STEP.   Have the model state the sub-goals before solving
   them, one at a time, carrying each result forward. Make the intermediate results visible — they are
   where failures localise, and an invisible chain cannot be debugged.

5. USE SELF-CONSISTENCY WHERE CORRECTNESS IS VERIFIABLE AND CHEAP.   Sample several independent attempts
   and take a majority vote over final answers, or select with the verifier. One of the most reliable
   interventions available; the cost is linear and predictable in the number of samples. It requires that
   the answers be comparable — free-form prose is not.

6. USE SEARCH ONLY WHEN BRANCHING IS REAL AND EVALUABLE.   Tree search over reasoning branches with
   lookahead helps on tasks needing exploration, at one to two orders of magnitude more model calls.
   Before adopting it, check how much of the gain self-consistency gets more cheaply — much of what
   looks like search benefit is additional sampling.

7. DO NOT ADD CHAIN-OF-THOUGHT BY DEFAULT.   The original result is scale-dependent, was largely driven
   by few-shot exemplars, and is reported as neutral or negative on models trained with reinforcement
   learning for reasoning, which produce their own chains unprompted. Measure it on your task with your
   model. Do not carry a 2022 result forward as a default.

8. BUDGET TEST-TIME COMPUTE EXPLICITLY.   Accuracy improves monotonically with inference compute across
   several independent lines of work, which makes compute a design variable rather than a constraint to
   minimise. State the budget, measure the accuracy/compute curve for the task, and choose the point on
   it. A strategy comparison without a stated budget is not a comparison.

9. GROUND ANY TASK THAT NEEDS EXTERNAL FACTS.   Retrieve first, then reason over what was retrieved, with
   the sources attached to the claims. Reasoning over parametric memory produces confident fabrication on
   knowledge-intensive questions.

10. LOCALISE THE FAILURE IN THE CHAIN, NOT THE ANSWER.   When a multi-step result is wrong, find the first
   incorrect intermediate step. A failure at step 2 has a different fix from a failure at step 6, and the
   final answer cannot tell you which.

11. DO NOT TREAT STATED REASONING AS AN AUDIT TRAIL.   Whether the generated chain reflects the
   computation that produced the answer is contested, and evidence shows irrelevant added features can
   bias the answer without appearing in the chain. Log inputs, outputs, tool calls, model version and
   prompt hash; treat reasoning text as a debugging aid.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Strategy chosen by fashion | cost is high and accuracy is not | re-measure the cheapest strategy that fits the structure |
| CoT added by default | neutral or negative delta on a reasoning-tuned model | remove it; keep only measured interventions |
| Chain produced, answer still wrong | failure not localised | find the first incorrect intermediate step |
| Self-consistency on free-form output | votes are not comparable | constrain the answer format so votes can be counted |
| Search where sampling suffices | cost rose far more than accuracy | ablate: sampling-only versus search |
| Reasoning over parametric memory | confident fabrication | retrieve first and ground the claims |
| No compute budget stated | strategy comparisons are meaningless | state latency and cost ceilings before comparing |
| Reasoning text used as an audit trail | the chain does not explain the action | log the actual inputs, outputs and tool calls |

## Quality Checklist

```text
□ the task structure was classified before a strategy was chosen
□ verifiability was assessed, and generate-and-verify used where it applies
□ the cheapest fitting strategy was tried first
□ intermediate results are visible for multi-step tasks
□ every strategy change was measured against the evaluation set
□ the compute budget is stated, and the accuracy/compute point was chosen deliberately
□ CoT was measured on this model and task, not assumed
□ external facts are retrieved and grounded, with sources attached to claims
□ the first incorrect intermediate step was identified for any failure
□ inputs, outputs and tool calls are logged; stated reasoning is not relied on as evidence
```

## Anti-Patterns

```text
✗ ALWAYS THINK STEP BY STEP.   The default that the evidence does not support across models and tasks.
✗ REASONING INSTEAD OF RETRIEVAL.   Asking a model to reason its way to a fact it does not have produces
  confident fabrication.
✗ SEARCH BY DEFAULT.   One to two orders of magnitude more calls, much of the benefit available from
  cheaper sampling.
✗ INVISIBLE INTERMEDIATE STEPS.   A failure that cannot be localised cannot be fixed.
✗ SELF-CONSISTENCY ON UNSTRUCTURED OUTPUT.   Majority voting requires comparable answers.
✗ NO COMPUTE BUDGET.   Then the strategy is chosen by preference and the cost is discovered in
  production.
✗ TRUSTING THE STATED REASONING.   It may be post-hoc; it is not an audit trail.
✗ ONE STRATEGY FOR ALL TASK CLASSES.   Structure differs; so should the strategy.
✗ CARRYING A 2022 RESULT FORWARD UNMEASURED.   Reasoning behaviour changed with RL training.
```

## References

- [`knowledge/reasoning/public-reasoning-research.md`](../../knowledge/reasoning/public-reasoning-research.md) — the graded evidence behind every choice here
- [`knowledge/evaluation/llm-judge-validation.md`](../../knowledge/evaluation/llm-judge-validation.md) — scoring open-ended reasoning output
- [`knowledge/data-engineering/vector-search.md`](../../knowledge/data-engineering/vector-search.md) — the retrieval side of grounded reasoning
- [`skills/prompt-engineering/SKILL.md`](../prompt-engineering/SKILL.md) · [`skills/context-engineering/SKILL.md`](../context-engineering/SKILL.md) · [`skills/evidence-validation/SKILL.md`](../evidence-validation/SKILL.md) · [`skills/debugging/SKILL.md`](../debugging/SKILL.md)
- [`patterns/agents/context-compaction.md`](../../patterns/agents/context-compaction.md) · [`prompts/research/deep-research-loop.md`](../../prompts/research/deep-research-loop.md)
- Wei et al. arXiv:2201.11903 · Wang et al. arXiv:2203.11171 · Yao et al. arXiv:2305.10601 · Yao et al. arXiv:2210.03629 · Turpin et al. arXiv:2305.04388
