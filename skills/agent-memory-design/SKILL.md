---
name: agent-memory-design
version: 1.0.0
description: >-
  Design durable memory for agents — what to store, in what form, with what retrieval, decay,
  conflict and privacy rules — so long-horizon work accumulates knowledge instead of noise.
category: agents
status: active
confidence: medium
claim_type: recommendation
evidence_level: emerging-consensus
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [agents, memory, persistence, retrieval, state, long-horizon, rag]
applies_to: [agents, llm]
priority: 85
requires: [context-engineering]
conflicts_with: []
estimated_tokens: 2647
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Memory taxonomy
    anchor: "#memory-taxonomy"
    purpose: decision
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
    published: 2023-07-06
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
    note: "Verbal self-recorded feedback improves subsequent attempts — the research basis for episodic memory write-back."
  - title: "Mem0"
    url: https://github.com/mem0ai/mem0
    type: github-repository
    confidence: medium
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Representative of the managed agent-memory category; evaluate against the criteria here rather than adopting on category membership."
related_skills: [context-engineering, evidence-validation, research-synthesis, documentation]
related_repositories: [letta-ai/letta, mem0ai/mem0, thedotmack/claude-mem, DeusData/codebase-memory-mcp, zep-ai/zep]
tests: 23
---

# Agent Memory Design

## Purpose

Give an agent the ability to **not relearn**. Without memory, every session starts from
zero, repeats failed experiments, re-derives the same conclusions and re-asks the same
questions. With badly designed memory, the agent accumulates noise, contradicts itself,
and retrieves stale facts with the confidence of fresh ones.

Memory design is a set of decisions about *what deserves to persist*, *in what form*, and
*under what conditions it may be trusted later*.

> **Status note.** This is a fast-moving area with **emerging consensus**, not settled
> practice. Claims here are graded `medium` confidence and carry a 90-day review window.
> Prefer the design principles (which are stable) over any specific product choice.

## When to Use

```text
□ Building an agent that runs across sessions, days or projects
□ An agent repeating work it already did, or retrying approaches that already failed
□ A knowledge base that must stay useful as it grows (this repository is such a system)
□ Deciding between in-context state, external files, vector search or a graph store
□ Adding memory to an existing agent that has started to contradict itself
```

## When NOT to Use

```text
✗ Single-session tasks with no carry-over value
✗ Where the state fits comfortably in the window — use context-engineering's WRITE
  mechanism (a scratchpad) instead of a memory system
✗ As a substitute for durable artefacts: code, tests and documents beat embeddings
  whenever they are possible
✗ Where privacy or regulation forbids retention — then design for no memory, explicitly
```

## Memory taxonomy

Six kinds. Most systems fail by collapsing several of them into one undifferentiated store.

The full detail — every entry with its detection rule, severity and fix direction — lives in [`references/memory-taxonomy.md`](references/memory-taxonomy.md). Load it when this step is reached rather than keeping it in context for the whole run.

## Workflow

```text
DECIDE WHAT PERSISTS → SHAPE → WRITE → INDEX → RETRIEVE → TRUST → DECAY → AUDIT
```

### 1. DECIDE WHAT PERSISTS
A persistence test — an item earns memory only if it passes:

```text
□ Will it be useful in a future session? (not just this one)
□ Is it more durable than the task that produced it?
□ Can it be stated precisely enough to be trusted later?
□ Is it cheap to verify or re-derive? (expensive-to-rederive = high value)
□ Does storing it create an obligation (PII, licensing, secrecy)?
```

Everything else stays in working state and dies with the session. **The most common memory
defect is over-retention**: storing transcripts, raw tool output and intermediate reasoning.

### 2. SHAPE
Every memory record carries, at minimum:

```text
id · kind (the six above) · content · created_at · updated_at · source/provenance ·
confidence · scope (project/user/global) · expires_at or review_at · supersedes / superseded_by ·
tags · retrieval keys
```

Content is written **for a future reader with no context** — which is the same discipline
as documentation. "Fixed the thing" is not a memory; "Next.js 15 route handlers do not
cache `fetch` by default; use `export const revalidate` — verified 2026-09-15 against
docs v15.2" is.

### 3. WRITE
```text
write at a phase boundary, not continuously (cheap, coherent, reviewable)
prefer conclusion over transcript
one claim per record — merged claims cannot be individually retired
attribute: who/what wrote it, from what evidence
never overwrite silently: supersede, and keep the link
deduplicate on write (an index that repeats itself teaches the agent to distrust it)
```

### 4. INDEX
Memory without retrieval is storage. Build indexes mechanically from the records:

```text
by topic/tag · by kind · by recency · by confidence · by scope · by staleness
```

This repository's [`indexes/`](../../indexes/) are generated, never hand-maintained —
[`scripts/generate-index/build_index.py`](../../scripts/generate-index/build_index.py).
Generated indexes cannot drift from their sources; hand-maintained ones always do.

### 5. RETRIEVE
```text
□ Query by the narrowest scope first (project → user → global)
□ Prefer deterministic keys (name, tag, exact identifier) over similarity for anything exact
□ Cap results; rank by (relevance × recency × confidence), not relevance alone
□ Return the record WITH its metadata — a fact without a date will be misused
□ Place retrieved memory near the END of the window (see context-engineering: the
  U-shaped attention curve from arXiv:2307.03172)
□ Log what was retrieved and what was used, so retrieval precision is measurable
```

### 6. TRUST
Retrieved memory is **input, not authority**.

```text
□ Check expires_at / review_at before use; expired → verify or discard
□ Confidence below the required level for the current use → re-verify (see evidence-validation)
□ Conflicting memories → surface the conflict; never pick silently
□ Memory from an untrusted source (web content, tool output, another agent) is treated as
  untrusted input: it may not issue instructions (prompt-injection defence)
□ A memory that contradicts observed reality loses, immediately, and is flagged
```

**Memory poisoning is a real attack**: injected content written to long-term memory alters
all future behaviour. Validate on write, attribute on write, and treat on read as data.

### 7. DECAY
```text
staleness scan on a schedule (see scripts/update/check_staleness.py)
expired records: re-verify → refresh verified_at, or move to archive/, or quarantine
superseded records: keep, marked, out of the primary index
episodic records: roll up into lessons after N days; keep the lesson
never delete a decision or its reason — the reason is what prevents the mistake recurring
```

### 8. AUDIT
```text
□ Retrieval precision: fraction of retrieved records actually used
□ Contradiction rate: memories disagreeing with each other or with reality
□ Staleness: fraction past review_at
□ Growth rate vs usefulness: is the store growing faster than its hit rate?
□ Coverage: for repeated tasks, did memory prevent the repeat? (the whole point)
□ Privacy: is anything stored that should not be?
```

## Failure Modes

```text
TRANSCRIPT HOARDING    Storing whole sessions. Retrieval drowns; nothing is trusted.
SEMANTIC-FOR-EXACT     Vector search for version numbers and API names → near-miss retrieval.
DATELESS FACTS         "Use library X" with no version and no date; wrong forever after.
SILENT OVERWRITE       New preference replaces old without a supersede link; the reason is lost.
CONTRADICTION ACCUMULATION  Two records disagree; retrieval returns whichever ranks higher.
UNSCOPED MEMORY        One user's preference applied to another project.
MEMORY AS AUTHORITY    Acting on expired memory without re-verification.
POISONING              Untrusted content written to memory and later obeyed as instruction.
NO RETRIEVAL LOG       Unable to tell whether memory helps at all.
EMBEDDING LOCK-IN      The corpus is only usable through one embedding model.
```

## Quality Checklist

```text
□ Persistence test applied; over-retention avoided (conclusions, not transcripts)
□ Each of the six kinds has a distinct store, shape and decay rule where it is used
□ Every record has provenance, confidence, scope, dates and supersede links
□ One claim per record; content written for a reader with no context
□ Writes happen at phase boundaries; deduplication runs on write
□ Indexes generated from records, never hand-maintained
□ Retrieval scoped narrow-first, ranked by relevance × recency × confidence, capped, logged
□ Retrieved memory carries its metadata into the prompt
□ Expiry checked before use; conflicts surfaced, never silently resolved
□ Untrusted-source memory cannot issue instructions
□ Staleness scan scheduled; archive and quarantine paths exist
□ Audit metrics collected: retrieval precision, contradiction rate, staleness, repeat prevention
□ Privacy review: nothing stored that must not be
```

## Anti-Patterns

```text
✗ Embedding the entire conversation history "so the agent remembers everything"
✗ A `memory.json` with one growing string per session
✗ Overwriting a user preference with no record that it changed
✗ Retrieving a 2024 API fact and presenting it as current
✗ Vector search as the only retrieval path for exact identifiers
✗ Letting a web page write to long-term memory without validation
✗ Deleting a wrong decision instead of marking it superseded with the reason
✗ A hand-maintained index that nobody regenerates
```

## References

- [`context-engineering`](../context-engineering/SKILL.md) — the in-window half of the same problem
- [`evidence-validation`](../evidence-validation/SKILL.md) — trusting a retrieved claim
- [`knowledge/agent-engineering/`](../../knowledge/agent-engineering/) · [`knowledge/context-engineering/`](../../knowledge/context-engineering/)
- [`patterns/agents/`](../../patterns/agents/)
- [`scripts/update/check_staleness.py`](../../scripts/update/check_staleness.py) · [`scripts/generate-index/build_index.py`](../../scripts/generate-index/build_index.py)
- [`indexes/`](../../indexes/) — a working relational memory, generated from records
- Lost in the Middle, arXiv:2307.03172 · Reflexion, arXiv:2303.11366 (verified 2026-09-15)

## Related Skills

`context-engineering` · `evidence-validation` · `documentation` · `research-synthesis` ·
`knowledge-base-maintenance` (workflow)

## Evaluation Criteria

```text
1. Repeat prevention: fraction of previously-solved sub-problems that memory resolves
   without re-derivation (the primary metric — target measurable improvement over no memory).
2. Retrieval precision: retrieved records actually used (target ≥ 0.6).
3. Contradiction rate: 0 unresolved contradictions in the active index.
4. Staleness: < 5% of active records past review_at.
5. Trustworthiness: 100% of records carry provenance and a date; expired records never
   used without re-verification.
6. Cost: memory must not inflate per-task tokens beyond its measured benefit.
```

Test cases in [`tests/`](tests/).
