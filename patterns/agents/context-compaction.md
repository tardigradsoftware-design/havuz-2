---
id: pattern-agent-context-compaction
name: "Context compaction"
domain: agents
problem: >-
  A long-running agent task exhausts its context window. Truncating loses the information the task
  depends on; summarising naively loses the specific details — identifiers, decisions, exact values —
  that cannot be reconstructed from a paraphrase; and continuing without intervention fails outright.
solution: >-
  Compact deliberately and early: separate durable state from conversation, write decisions and facts
  to external storage as they occur, summarise the transcript against a fixed schema that preserves
  identifiers and open questions, keep recent turns verbatim, and reload from the durable store on
  demand rather than carrying everything.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
maturity: established
tags: [agents, context-window, compaction, memory, long-running-tasks, summarisation, llm]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
when_to_use:
  - a task will run longer than one context window can hold
  - an agent must resume after a restart or across sessions
  - tool output is large and only part of it is relevant later
  - cost or latency scales with context length and the budget is fixed
when_not_to_use:
  - the task fits comfortably in one window with room to spare — compaction adds a lossy step and a
    failure mode for no benefit
  - the content is a verbatim record that must not be paraphrased (a legal transcript, an audit log,
    source code being edited) — store it externally and reference it, do not summarise it
  - the model's own long-context capability is being relied on as the mechanism; see the tradeoffs,
    a large window is not a substitute for state management
forces:
  - "Fidelity: a compacted summary must retain what the task cannot proceed without."
  - "Cost and latency: context length is paid for on every turn, so carrying everything is expensive."
  - "Position: attention over a long input is unevenly distributed, so where information sits matters."
  - "Recoverability: a compacted state must be resumable after a crash, not only at a clean boundary."
  - "Determinism: two compactions of the same transcript should produce equivalent states, or debugging becomes impossible."
consequences:
  positive:
    - "Tasks run unbounded in duration at bounded cost."
    - "State survives a restart or a crash, because durable state is written before the model call."
    - "The agent can explain what it has done from a compact, structured record."
  negative:
    - "Compaction is lossy and the loss is silent — a dropped identifier surfaces later as a wrong action, not as an error."
    - "A second model call per compaction adds cost, latency, and a component that can itself fail or hallucinate."
    - "The summary schema, retention rules and durable store become load-bearing artifacts that need tests."
  neutral:
    - "The transcript is no longer the record of the task; the durable state is. Debugging moves to the store."
tradeoffs:
  - "Summarise versus externalise: summarising saves tokens and loses detail; writing to a store keeps detail and costs a retrieval step. Use both — summarise the narrative, externalise the facts."
  - "Compact early versus compact late: early compaction keeps cost low and risks discarding something not yet known to matter; late compaction preserves options and produces a worse summary under pressure."
  - "Model-generated versus deterministic compaction: a model summarises well and unpredictably; a deterministic extractor is reliable and only keeps what it was told to keep."
alternatives:
  - "Truncation — drop the oldest turns. Cheapest, and loses exactly the decisions made earliest, which are usually the constraints."
  - "A larger context window — defers the problem and pays for it every turn; attention over long inputs is unevenly distributed."
  - "Sliding window with pinned system content — keeps the instructions and drops the middle; better than plain truncation, still loses task history."
  - "Retrieval over the transcript — store everything, retrieve on demand. Works when the agent knows what to ask for, which it often does not mid-task."
  - "Checkpointing to durable state — write structured task state at defined points and restart from the checkpoint rather than the transcript."
anti_pattern: >-
  Summarising the whole transcript into free prose at the moment the window fills, with no schema, no
  external store and no test. The summary reads well, the agent continues confidently, and the specific
  identifiers, file paths, decision rationale and open questions it needed are gone. The failure appears
  much later as an incorrect action and cannot be traced to the compaction.
related_skills: [agent-memory-design, context-engineering, prompt-engineering, reasoning-strategies]
related_repositories: [langchain-ai/langgraph, anthropics/claude-code, thedotmack/claude-mem]
related:
  - type: related
    target: knowledge/agent-engineering/framework-comparison.md
    note: "State and persistence are a framework selection axis; this pattern is what the framework provides or omits."
  - type: related
    target: knowledge/reasoning/public-reasoning-research.md
    note: "Test-time compute scaling is the cost side of carrying a long context."
  - type: implements
    target: skills/agent-memory-design/SKILL.md
    note: "This pattern is the working-memory half of the memory taxonomy."
  - type: related
    target: skills/context-engineering/SKILL.md
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    published: 2023-07-06
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "U-shaped performance over input position — models use the beginning and the end of a long context better than the middle. This is why the pattern keeps recent turns verbatim and places the compacted summary before them rather than interleaving it."
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    claim_type: fact
    confidence: high
    verified_at: 2026-09-15
    note: "Self-recorded verbal feedback improves performance on later attempts — the research basis for writing decisions and lessons to durable state during compaction rather than discarding them with the transcript."
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: https://arxiv.org/abs/2210.03629
    type: research-paper
    published: 2022-10-06
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Interleaved reasoning and observation is the loop whose history grows without bound and therefore needs compaction; verified against the primary arXiv abs page on 2026-09-15."
---

# Context Compaction

## Context

An agent loop accumulates history: the task, every reasoning step, every tool call and every tool
result. Tool results dominate — one file read or one search response can exceed the entire reasoning
transcript. Growth is monotonic and the window is not, so a task of any length reaches the boundary.

What happens at the boundary is a design decision that most implementations make by accident.

## The pattern

Three separations, applied together:

```text
1. NARRATIVE vs FACTS.     The conversation is a narrative; the task's facts are data. Compact the
                           narrative, externalise the facts. A summary that contains a file path, an
                           identifier, a decision or an exact value is storing data in a lossy format.

2. DURABLE vs EPHEMERAL.   Durable state — the goal, decisions made, files changed, open questions,
                           constraints discovered — lives outside the transcript, written as it occurs
                           rather than reconstructed at the end. Ephemeral state — intermediate tool
                           output, explored-and-rejected paths — can be dropped once its conclusion is
                           recorded.

3. RECENT vs DISTANT.      Keep the last N turns verbatim: they carry the immediate reasoning and
                           precise references. Everything older is represented by the compacted summary.
                           Do not interleave them — attention over position is uneven, and a summary
                           buried in the middle is the least reliably used content in the window.
```

## Structure

```text
┌──────────────────────────────────────────────────────────────┐
│ SYSTEM / ROLE                                  (pinned)      │
├──────────────────────────────────────────────────────────────┤
│ TASK STATE (durable, structured, rewritten on compaction)     │
│   goal · constraints discovered · decisions + rationale       │
│   artifacts touched (exact paths, identifiers)                │
│   current position in the plan · next action                  │
│   open questions · what has been ruled out and why            │
├──────────────────────────────────────────────────────────────┤
│ COMPACTED HISTORY (schema-fixed summary of turns 1..n-k)      │
│   what was tried, what was learned, what failed and why       │
├──────────────────────────────────────────────────────────────┤
│ RECENT TURNS (last k, verbatim)                               │
└──────────────────────────────────────────────────────────────┘
        ↕ written to and read from an external store
```

The task-state block is structured, not prose. Structured state can be validated, diffed between runs
and tested; prose state cannot, and its omissions are invisible.

## Implementation

```text
TRIGGER        compact at a fixed fraction of the window — 60-75% — not at 100%. Compacting under
               pressure produces the worst possible summary at the moment the most depends on it.
               Also compact at natural boundaries: after a stage completes, after a decision, before a
               long operation.

WHAT TO WRITE  Before summarising anything, write the durable facts out: every identifier, path,
               decision with its reason, constraint discovered, and the current plan position. These
               are extracted deterministically where possible — from tool-call arguments and results,
               not from a model's recollection of them.

WHAT TO SUMMARISE  The narrative: what was attempted, what was learned, what was ruled out and why.
               "Ruled out and why" is the highest-value content in a summary, because it prevents the
               agent from repeating a failed approach after the evidence for rejecting it is gone.

WHAT TO DROP   Raw tool output whose conclusion has been recorded. Verbose intermediate reasoning whose
               result is in the task state. Duplicated content. Explored paths that led nowhere, once
               the fact that they led nowhere is recorded.

WHAT TO KEEP VERBATIM  The last k turns. Any content the current step depends on precisely: an error
               message being debugged, a code block being edited, an exact quote being checked.

RELOAD ON DEMAND  Compacted-away detail is not deleted; it is externalised. The agent retrieves it when
               a step needs it, which converts an unbounded context into a bounded one plus a store.

RECOVERABILITY  Write the durable state before the model call that might exhaust the window, so a crash
               mid-turn loses the turn and not the task.
```

## Failure modes

| Failure | Detection | Response |
|---|---|---|
| An identifier lost in summarisation | a later step references a path or ID that does not exist | extract identifiers deterministically into task state; never let them exist only in prose |
| The agent repeats a failed approach | the same rejected action appears again after compaction | the summary schema must include "ruled out and why" as a required field |
| Compaction at 100% produces a bad summary | the first post-compaction step regresses | trigger at 60-75%, and at stage boundaries |
| The summary is placed mid-context | adherence to earlier constraints drops | pin task state early, keep recent turns last, do not interleave |
| Durable state drifts from reality | task state says a file is unchanged when it was edited | write state from observed tool results, not from the model's account of them |
| Compaction itself fails or hallucinates | the post-compaction state contradicts the transcript | validate the summary against the extracted facts; keep the transcript until the summary is verified |
| Unbounded growth of the durable store | the store itself exceeds what can be reloaded | the store needs its own retention and retrieval policy, not just an append |
| Two runs compact differently | the same task produces different outcomes | make the extraction deterministic where possible, and record the summary schema version |

## Testing it

```text
□ run a task longer than one window and assert it completes without losing a stated constraint
□ assert every identifier introduced before compaction is still resolvable after it
□ assert an approach ruled out before compaction is not retried after it
□ crash the run mid-turn and assert it resumes from durable state
□ compact the same transcript twice and diff the task state
□ measure cost and latency per turn before and after compaction, and report both against the fidelity
  loss — compaction that saves tokens and fails the task is a regression
```

## References

- [`skills/agent-memory-design/SKILL.md`](../../skills/agent-memory-design/SKILL.md) — the memory taxonomy this pattern implements the working-memory part of
- [`skills/agent-memory-design/references/memory-taxonomy.md`](../../skills/agent-memory-design/references/memory-taxonomy.md) · [`skills/context-engineering/SKILL.md`](../../skills/context-engineering/SKILL.md)
- [`knowledge/agent-engineering/framework-comparison.md`](../../knowledge/agent-engineering/framework-comparison.md) — state and persistence as a framework selection axis
- [`knowledge/reasoning/public-reasoning-research.md`](../../knowledge/reasoning/public-reasoning-research.md) — test-time compute and the cost side of long context
- [`patterns/agents/`](.) · [`failure-modes/`](../../failure-modes/) · [`anti-patterns/`](../../anti-patterns/)
- Liu et al., "Lost in the Middle" — arXiv:2307.03172 · Shinn et al., "Reflexion" — arXiv:2303.11366 · Yao et al., "ReAct" — arXiv:2210.03629
