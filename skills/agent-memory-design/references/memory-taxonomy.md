---
id: memory-taxonomy
title: "The six kinds of agent memory and how to store each"
domain: agent-engineering
summary: >-
  Procedural, semantic, episodic, working, preferential and relational memory — form, retrieval and decay rules for each, plus the storage-choice comparison — extracted from the skill so the skill body stays inside its context budget.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [reference, agent-engineering]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [agent-memory-design]
---

# The six kinds of agent memory and how to store each

Reference material for [`agent-memory-design`](../SKILL.md), extracted so the skill body stays
within its context budget. Load this file only when the step that needs it is reached.


Six kinds. Most systems fail by collapsing several of them into one undifferentiated store.

```text
1 PROCEDURAL      how to do things: skills, workflows, playbooks, tool-usage rules
                  form: structured documents with frontmatter, versioned, reviewed
                  retrieval: by name/tag/applicability, deterministic
                  decay: on review date; superseded versions archived, never deleted
                  THIS REPOSITORY'S PRIMARY FORM — skills/, workflows/, patterns/

2 SEMANTIC        facts about the world: library versions, API shapes, benchmark numbers
                  form: claim + source + date + confidence (never a bare fact)
                  retrieval: by topic/entity; keyword beats embedding for exact identifiers
                  decay: aggressive — version-scoped facts expire with the version

3 EPISODIC        what happened: sessions, attempts, decisions, outcomes
                  form: timestamped records with goal → action → result → lesson
                  retrieval: by similarity to the current situation, and by recency
                  decay: summarise old episodes into lessons; keep the lesson, drop the transcript

4 WORKING         the current task's state: plan, TODO, open questions, artifacts produced
                  form: a single mutable document, human-readable, in the repo or session store
                  retrieval: always in context (this is not really "memory", it is state)
                  decay: at task end — promote lessons to episodic/procedural, discard the rest

5 PREFENTIAL      user and project preferences: style, conventions, rejections, tone
                  form: explicit statements with provenance ("user said X on <date>")
                  retrieval: always loaded for that user/project — small enough to be permanent
                  decay: only on explicit reversal; a reversed preference must be recorded,
                         not silently overwritten

6 RELATIONAL      entities and their connections: repos↔skills↔papers↔tools↔people
                  form: typed links (this repository's indexes/ are exactly this)
                  retrieval: traversal; "what else touches X"
                  decay: link rot is the risk — verify targets on a schedule
```

## Storage choice

```text
FILES IN A GIT REPO   best default for procedural, semantic, preferential, relational.
                      Versioned, reviewable, diffable, greppable, portable, no infra.
                      Cost: no semantic search; retrieval must be index-driven.
STRUCTURED DB         semantic claims with metadata filters (date, confidence, scope).
                      Cost: schema rigidity; needs a validation pipeline.
VECTOR STORE          episodic similarity search over large corpora.
                      Cost: opaque, embedding-model-dependent, poor at exact identifiers,
                      and retrieval quality silently degrades as the corpus grows.
GRAPH STORE           relational queries with multi-hop traversal.
                      Cost: highest operational complexity; only worth it above ~10⁵ edges.
```

**Default to files + generated indexes.** Add vector search only when a measured retrieval
failure justifies it, and keep the files as the source of truth so the index can be rebuilt.
