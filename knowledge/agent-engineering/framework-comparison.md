---
id: agent-engineering-framework-comparison
title: "Agent framework comparison: what they differ on and how to choose"
domain: agent-engineering
summary: >-
  The seven axes on which agent frameworks genuinely differ, the six families they fall into, the selection rules for each, and the traps — choosing by star count, ignoring the archive flag, adopting multi-agent by default.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [agent-frameworks, langgraph, autogen, pydantic-ai, adk, mcp, architecture, selection]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/architecture/build-vs-adopt.md, knowledge/ai-engineering/source-scoring.md, patterns/agents/context-compaction.md]
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Every framework named here is scored in metadata/repositories.json from fields this endpoint returns, retrieved 2026-09-15."
---
# Agent Framework Comparison

## The question this answers

"Which framework should we use?" is usually the wrong first question. The right one is **"do we need
a framework at all, and if so what capability are we buying?"** A framework buys orchestration,
state management, tool integration and observability; it costs a dependency, an abstraction layer
between you and the model API, and a migration when it changes direction.

Every framework here is scored in [`metadata/repositories.json`](../../metadata/repositories.json)
from observable GitHub facts. This document is about *fit*, which scoring cannot decide.

## The seven axes

```text
CONTROL FLOW          Who decides the next step: the graph you define, the model, or a loop you
                      wrote. Graphs give determinism and auditability; model-driven loops give
                      flexibility and unpredictability.
STATE & PERSISTENCE   Where conversation and task state lives, whether it survives a restart,
                      whether you can inspect and repair it. The difference between a demo and a
                      system.
TOOL INTEGRATION      Native tool calling vs an adapter layer vs MCP support. MCP matters more over
                      time because it is the shared protocol across vendors.
OBSERVABILITY         Tracing, token accounting, replay, evaluation hooks. Without traces a
                      misbehaving agent is undiagnosable.
MULTI-AGENT SUPPORT   Handoff, delegation, shared memory, topology. Many projects do not need this
                      and adopt it anyway, paying complexity for nothing.
VENDOR COUPLING       How hard it is to change provider, and whether the framework's value survives
                      that change. Deep coupling is a strategy, not a defect, if it is your vendor.
ABSTRACTION DEPTH     How much is hidden. Deep is fast to start and expensive to debug; thin is slow
                      to start and cheap to reason about.
```

## The families

```text
GRAPH / WORKFLOW        Explicit state machine; you define nodes, edges and transitions, the model
                        fills the nodes. Best when the process is known and must be auditable.
                        langchain-ai/langgraph is the reference implementation.
CONVERSATION-BASED      Multi-agent conversation as the orchestration primitive. Flexible, harder
                        to make deterministic. microsoft/autogen, microsoft/agent-framework.
TYPED / VALIDATED       Agent behaviour as typed structures validated at the boundary. Best when
                        output correctness matters more than process flexibility.
                        pydantic/pydantic-ai.
VENDOR-NATIVE           The provider's own SDK and agent toolkit. Deepest integration with that
                        provider's features, highest coupling. google/adk-python, google/adk-js.
PROTOCOL-FIRST          No framework: MCP servers plus a thin client you own. Maximum control,
                        maximum responsibility. Often right for a single-purpose agent.
BROWSER / COMPUTER-USE  Frameworks whose tools are a browser or a desktop — distinct enough to be
                        its own category. browser-use/browser-use, bytedance/UI-TARS-desktop.
```

## Choosing

```text
GRAPH FRAMEWORK WHEN      the process is known, steps must be auditable, retries and checkpoints
                          matter, or several people will maintain it.
TYPED FRAMEWORK WHEN      structured-output correctness is the main risk — extraction,
                          classification, code generation against a contract.
VENDOR-NATIVE WHEN        you are committed to that vendor and need its newest features before
                          third-party frameworks catch up.
MCP + THIN CLIENT WHEN    the agent does one thing well, you want minimal dependencies, or you are
                          building a tool others consume rather than an agent.
NO FRAMEWORK WHEN         a single loop with tool calling fits in 200 lines you fully understand.
                          More often the right answer than the ecosystem suggests, and easier to
                          debug than any abstraction.
```

## Traps

```text
✗ CHOOSING BY STAR COUNT.       Popularity measures attention and marketing, not fit or
                                maintenance. Two of the most-starred agent-skill collections in this
                                corpus have no license at all — popularity did not make them
                                adoptable.
✗ IGNORING THE ARCHIVE FLAG.    A framework that stopped receiving commits is a migration project
                                waiting to happen. Check status before architecture.
✗ MULTI-AGENT BY DEFAULT.       Most tasks need one agent with good tools and a memory policy.
                                Multi-agent adds coordination cost, non-determinism and debugging
                                surface for a benefit that often does not materialise.
✗ EVALUATING ON THE HELLO-WORLD. Every tutorial looks clean. Build the second and third feature —
                                the ones needing state, retries and error handling — before deciding.
✗ IGNORING OBSERVABILITY.       If you cannot trace a run end to end with token counts and tool
                                calls, you cannot operate it in production. Check before ergonomics.
✗ IGNORING THE 90-DAY WINDOW.   Framework APIs are the fastest-moving category in this repository.
                                A comparison older than one quarter is a historical document.
```

## References

- [`metadata/repositories.json`](../../metadata/repositories.json) — scored records for every framework named
- [`knowledge/ai-engineering/source-scoring.md`](../ai-engineering/source-scoring.md) · [`repository-status.md`](../ai-engineering/repository-status.md) · [`freshness-policy.md`](../ai-engineering/freshness-policy.md)
- [`knowledge/architecture/build-vs-adopt.md`](../architecture/build-vs-adopt.md) — the decision this feeds
- [`skills/repository-analysis/SKILL.md`](../../skills/repository-analysis/SKILL.md) · [`skills/competitive-analysis/SKILL.md`](../../skills/competitive-analysis/SKILL.md) · [`skills/dependency-analysis/SKILL.md`](../../skills/dependency-analysis/SKILL.md)
- [`patterns/agents/context-compaction.md`](../../patterns/agents/context-compaction.md) — framework-independent
