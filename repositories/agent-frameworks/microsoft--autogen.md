---
id: microsoft--autogen
title: "microsoft/autogen"
domain: agent-frameworks
summary: >-
  microsoft/autogen — MAINTENANCE, tier A,
  60,994 stars, license CC-BY-4.0, quality 7.72/10, trust 7.71/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "framework", "github-repository", "maintenance-candidate", "microsoft"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 6.0, "adoption": 10.0, "documentation": 8.23, "reproducibility": 6.55, "security": 7.0, "recency": 7.9, "evidence": 5.5}
  quality_score: 7.72
  trust_score: 7.71
  tier: A
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "microsoft/autogen on GitHub"
    url: https://github.com/microsoft/autogen
    type: github-repository
    organization: microsoft
    license: CC-BY-4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# microsoft/autogen

🟡 MAINTENANCE · tier **A** · maintenance-mode · confidence **very-high**

> A programming framework for agentic AI

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/autogen> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `CC-BY-4.0` |
| Stars | 60,994 (checked 2026-09-15) |
| Forks | 9,213 |
| Open issues | 1,065 |
| Contributors | 444 |
| Last push | 2026-04-15 (153 days before verification) |
| Latest release | python-v0.7.5 (2025-09-30) |
| Archived | no |
| Fork | no |
| Homepage | https://microsoft.github.io/autogen/ |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 6.0 |
| adoption | 10.0 |
| documentation | 8.23 |
| reproducibility | 6.55 |
| security | 7.0 |
| recency | 7.9 |
| evidence | 5.5 |
| **quality_score** (weighted) | **7.72** |
| **trust_score** | **7.71** |

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
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 20,790 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Understanding the origin of multi-agent conversation patterns
- Reading historical research context

**Not recommended for**

- New production agent systems
- Long-term dependency in a 2026+ roadmap

**Strengths**

- Established the multi-agent conversation abstraction that most later frameworks copied
- Very large contributor base (444 verified)
- Extensive published research and examples

**Weaknesses**

- No push in 153 days as of 2026-09-15 (verified)
- Microsoft's active investment moved to microsoft/agent-framework
- Conversation-centric model makes durable state and checkpointing awkward

**Related projects**

- microsoft/agent-framework
- microsoft/semantic-kernel
- camel-ai/camel

## Verification notes

No push in 153 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting. Verified 2026-09-15: microsoft/autogen is in maintenance mode. Microsoft recommends microsoft/agent-framework for new work. Do not start a new project on AutoGen; migrate existing ones deliberately. MAINTENANCE

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/autogen
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
