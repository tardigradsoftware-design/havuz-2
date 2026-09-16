---
id: langchain-ai--langgraph
title: "langchain-ai/langgraph"
domain: agent-frameworks
summary: >-
  langchain-ai/langgraph — ACTIVE, tier S,
  41,696 stars, license MIT, quality 8.35/10, trust 8.13/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "framework", "github-repository", "orchestration", "stateful"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.53, "reproducibility": 8.5, "security": 4.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.35
  trust_score: 8.13
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "langchain-ai/langgraph on GitHub"
    url: https://github.com/langchain-ai/langgraph
    type: github-repository
    organization: langchain-ai
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# langchain-ai/langgraph

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> Build resilient agents.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/langchain-ai/langgraph> |
| Owner | langchain-ai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 41,696 (checked 2026-09-15) |
| Forks | 7,044 |
| Open issues | 787 |
| Contributors | 279 |
| Last push | 2026-09-14 (0 days before verification) |
| Latest release | sdk==0.4.4 (2026-08-27) |
| Archived | no |
| Fork | no |
| Homepage | https://docs.langchain.com/oss/python/langgraph/ |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.53 |
| reproducibility | 8.5 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.35** |
| **trust_score** | **8.13** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | yes |
| examples | yes |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 6,395 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Stateful, multi-step agents that must survive restarts
- Human-in-the-loop approval gates
- Cyclic graphs where a linear chain is not enough
- Durable long-running workflows with checkpointing

**Not recommended for**

- A single tool call with no state
- Teams that want a typed-Python-first API with minimal abstraction
- Prototypes where the graph definition costs more than the logic

**Strengths**

- Explicit graph + checkpoint model gives durable, resumable agents
- Native human-in-the-loop interrupts
- Large ecosystem and integration surface (279 contributors verified)
- Strong observability via LangSmith

**Weaknesses**

- Graph boilerplate for simple tasks
- Abstraction changes between major versions have historically required migration work
- Debugging a graph is harder than debugging a function

**Related projects**

- langchain-ai/langchain
- pydantic/pydantic-ai
- temporalio/temporal

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, q=8.35.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug langchain-ai/langgraph
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
