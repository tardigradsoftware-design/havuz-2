---
name: context-engineering
version: 1.0.0
description: >-
  Design what an agent sees at each step: what to include, exclude, compress, retrieve, cache and
  evict — so capability is not lost to a badly assembled prompt or an overflowing window.
category: agents
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [context, agents, prompting, rag, memory, token-budget, retrieval]
applies_to: [agents, llm]
priority: 94
requires: [evidence-validation]
conflicts_with: []
estimated_tokens: 2487
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: The context budget
    anchor: "#the-context-budget"
    purpose: implementation
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    organization: Stanford / UC Berkeley / Samaya AI
    published: 2023-07-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Performance is U-shaped over input position: information at the start and end is used far better than information in the middle."
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    url: https://arxiv.org/abs/2201.11903
    type: research-paper
    published: 2022-01-28
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [agent-memory-design, prompt-engineering, web-research, evidence-validation, mcp-integration]
related_repositories: [langchain-ai/langgraph, letta-ai/letta, mem0ai/mem0, thedotmack/claude-mem]
tests: 21
---

# Context Engineering

## Purpose

Treat the model's input window as a **scarce, ordered, budgeted resource** and design it
deliberately — instead of appending whatever is available until something breaks.

Prompt engineering asks "what words should I use?". Context engineering asks "what should
be in the window at step *n*, why, at what cost, and what must be evicted to make room?".
For multi-step agents the second question dominates: most agent failures are context
failures, not reasoning failures.

## When to Use

```text
□ Designing or debugging any multi-step agent, RAG pipeline or tool-using workflow
□ An agent that works on small tasks and fails on large ones
□ Long conversations that degrade, repeat themselves or forget decisions
□ Deciding what to retrieve, how much, and in what order
□ Cost/latency optimisation of an LLM application
□ Designing a compaction or handoff strategy
```

## When NOT to Use

```text
✗ Single-turn tasks with everything already in the prompt
✗ Choosing a model — that is a capability question, not a context question
✗ As an excuse to stuff the window "because tokens are cheap": they are not free in
  accuracy, latency or cost
```

## Inputs

```text
task shape        single-turn | multi-step | long-horizon | multi-agent
window budget     model's context limit minus the output you must reserve
latency/cost cap  what a step may cost
state to carry    decisions, findings, artifacts, constraints, failures
retrieval sources code, docs, KB, memory, tools, web
```

## The context budget

Allocate the window explicitly. A starting allocation (**RECOMMENDATION**, tune per task):

```text
system + role + policies        5–10%    stable → cache it
task definition + constraints   5–10%    stable → cache it
retrieved evidence              20–40%   variable, ordered by relevance
working state (decisions, TODO) 10–20%   grows → must be compacted
recent conversation             15–30%   sliding window
tool results (current step)     10–25%   often the largest; truncate aggressively
reserved output                 10–25%   never let this be squeezed
```

Hard rules:

```text
1. Reserve output space first. Compute the budget from what is left.
2. A step that exceeds 80% of budget must compact before continuing, not after failing.
3. Anything stable goes at the START (cache-friendly and position-favourable).
4. Anything decision-critical goes at the END (position-favourable).
5. Nothing bulky goes in the MIDDLE. "Lost in the Middle" (arXiv:2307.03172) shows
   retrieval accuracy is U-shaped over position.
```

## Workflow

```text
INVENTORY → BUDGET → SELECT → ORDER → COMPRESS → ISOLATE → MONITOR → EVICT → HANDOFF
```

### 1. INVENTORY
List every candidate piece of context with its size and its marginal value:

```text
| item | tokens | needed at which step | value if absent | staleness risk |
```

If you cannot state the cost of an item's absence, it does not belong in the window.

### 2. BUDGET
Set the allocation above against the real model limit. Record it. Enforce it in code,
not in good intentions.

### 3. SELECT
Four mechanisms, in order of preference (cheapest and most reliable first):

```text
WRITE    persist state outside the window: scratchpad, decisions file, TODO list, artifact store
SELECT   retrieve only what this step needs (semantic/keyword/graph search, tool calls)
COMPRESS summarise finished work into its conclusions; keep the conclusion, drop the transcript
ISOLATE  give sub-agents their own windows; return only a structured result to the parent
```

**Do not default to "include everything".** Inclusion is the last resort, not the first.

### 4. ORDER
```text
START   role, policies, stable task definition, output contract
MIDDLE  bulk reference material — least decision-critical, largest
END     the current question, the most recent tool result, the decision needed now
```
Re-assert critical constraints near the end on long runs. Constraints stated once at the
top of a 100k-token conversation will be violated.

### 5. COMPRESS
Compaction triggers (pick and enforce):

```text
token threshold    e.g. compact at 70% of budget
phase boundary     after each completed subtask — cheapest, highest quality point
tool-result age    raw tool output older than N steps → replace with its extracted fact
failure loop       same error twice → replace transcript with "attempted X, failed because Y"
```

A compaction record must preserve, at minimum:

```text
decisions made + why  ·  constraints discovered  ·  artifacts and their paths  ·
open questions  ·  failures already tried (so they are not retried)  ·  current goal
```

What may be dropped: raw file dumps, verbose tool output already acted on, exploration
dead ends (keep one line: "tried X — no"), restatements of the system prompt.

### 6. ISOLATE
Sub-agents get a narrow window and a narrow job; they return **structured findings only**.
This is the single most effective defence against context collapse in long tasks. Rule:
a sub-agent's return should be smaller than the context it consumed by at least 5×,
otherwise isolation bought nothing.

### 7. MONITOR
Track per step: tokens in, tokens out, cache hit rate, retrieval precision (fraction of
retrieved items actually used), number of constraint violations, repeats of already-tried
actions. Degradation shows up as repeats and constraint violations before it shows up as
wrong answers.

### 8. EVICT
Explicit eviction policy, not silent truncation:

```text
never evict      task definition, output contract, security policies, decisions
evict last       constraints discovered from failures, current goal
evict first      raw tool output already summarised, superseded file contents,
                 exploratory transcripts
```
Silent truncation is a defect: the agent then acts on a partial instruction it believes
is complete.

### 9. HANDOFF
When passing to another agent, phase or human, produce a handoff document — not a
transcript. Minimum: goal, state, decisions, artifacts, open risks, next action, what
was already tried.

## Failure Modes

```text
CONTEXT FLOOD         Everything available goes in. Fix: budget + select.
SILENT TRUNCATION     Provider or code drops the tail. Fix: measure, alert, compact early.
LOST IN THE MIDDLE    Critical constraint buried at position 40k. Fix: order policy.
STALE CONTEXT         An earlier file version still in the window, contradicting the current one.
                      Fix: evict superseded content explicitly.
COMPRESSION LOSS      Summarising away the one number that mattered.
                      Fix: preserve decisions/constraints verbatim; compress only transcripts.
RETRIEVAL NOISE       Top-k dumps 20 chunks, 2 relevant. Fix: precision metric + reranking.
DUPLICATE CONTEXT     Same doc included by system prompt, RAG and tool result.
NO ISOLATION          One agent does everything and drowns. Fix: sub-agents with contracts.
CACHE HOSTILE ORDER   Volatile content at the start destroys prefix caching.
                      Fix: stable prefix, volatile suffix.
```

## Quality Checklist

```text
□ Written token budget per step class, enforced in code
□ Output space reserved before input is assembled
□ Every included item has a stated cost-of-absence
□ Stable content at the start; decision-critical content at the end; nothing bulky in the middle
□ Compaction trigger defined and tested at a real phase boundary
□ Compaction preserves decisions, constraints, artifacts, failures-tried, open questions
□ Sub-agent returns are structured and ≥5× smaller than their consumed context
□ Eviction policy explicit; no silent truncation
□ Retrieval precision measured, not assumed
□ Constraint re-assertion scheduled for long runs
□ Handoff document produced for every phase/agent boundary
□ Prefix cache stability checked (no volatile content in the cached prefix)
```

## Anti-Patterns

```text
✗ "The model has 1M tokens so we can include the whole repo"
✗ Re-pasting the entire conversation into every call
✗ Summarising a decision until the reason is gone
✗ Retrieving top-50 and letting the model sort it out
✗ Putting the actual question at the top and 30k tokens of reference below it
✗ Letting a failing tool call dump its full stack trace into the window five times
✗ Compacting only when the API errors
✗ Handing a sub-agent the parent's full history "for context"
```

## References

- Lost in the Middle — arXiv:2307.03172 (verified 2026-09-15)
- Chain-of-Thought — arXiv:2201.11903 (verified 2026-09-15)
- Reflexion — arXiv:2303.11366 (verified 2026-09-15)
- [`knowledge/context-engineering/`](../../knowledge/context-engineering/)
- [`agent-memory-design`](../agent-memory-design/SKILL.md)
- [`patterns/agents/context-compaction.md`](../../patterns/agents/context-compaction.md)
- [`prompts/system/`](../../prompts/system/)

## Related Skills

`agent-memory-design` · `evidence-validation` · `web-research` · `mcp-integration` ·
`project-planning`

## Evaluation Criteria

```text
1. Task success at scale: success rate on long-horizon tasks vs short ones (target: <10% drop).
2. Constraint retention: fraction of stated constraints still honoured at step N (target ≥0.95).
3. Repeat rate: fraction of already-tried actions retried after compaction (target 0).
4. Retrieval precision: retrieved items actually used (target ≥0.6).
5. Cost per successful task, and tokens per step vs the declared budget.
```

Test cases in [`tests/`](tests/).
