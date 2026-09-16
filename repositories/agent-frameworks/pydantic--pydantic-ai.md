---
id: pydantic--pydantic-ai
title: "pydantic/pydantic-ai"
domain: agent-frameworks
summary: >-
  pydantic/pydantic-ai — ACTIVE, tier S,
  19,956 stars, license MIT, quality 8.92/10, trust 9.01/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "framework", "github-repository", "python", "structured-output"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 8.25, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.5}
  quality_score: 8.92
  trust_score: 9.01
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "pydantic/pydantic-ai on GitHub"
    url: https://github.com/pydantic/pydantic-ai
    type: github-repository
    organization: pydantic
    license: MIT
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# pydantic/pydantic-ai

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> How Python does AI. Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/pydantic/pydantic-ai> |
| Owner | pydantic (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 19,956 (checked 2026-09-15) |
| Forks | 2,717 |
| Open issues | 884 |
| Contributors | 476 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v2.43.0 (2026-09-12) |
| Archived | no |
| Fork | no |
| Homepage | https://pydantic.dev/pydantic-ai |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 8.25 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.5 |
| **quality_score** (weighted) | **8.92** |
| **trust_score** | **9.01** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | yes |
| ci | yes |
| examples | yes |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 20,943 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Python agents that must return validated structured output
- Type-safe tool definitions
- Declarative agent specification and dependency injection
- Teams already using Pydantic and FastAPI

**Not recommended for**

- .NET or Java shops
- Multi-agent systems needing a durable graph runtime out of the box

**Strengths**

- Model-agnostic with a typed, Pydantic-native API
- First-class structured outputs, tools, MCP client support, web search, code execution and sub-agents
- Declarative agent definition with typed dependencies
- Very high contributor count for its age (476 verified) and frequent releases (v2.43.0)

**Weaknesses**

- Python only
- Younger ecosystem than LangChain's

**Related projects**

- langchain-ai/langgraph
- modelcontextprotocol/python-sdk
- colinhacks/zod

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, q=8.92, trust 8.x - one of the strongest scores in the registry.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug pydantic/pydantic-ai
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
