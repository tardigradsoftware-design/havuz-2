---
id: microsoft--agent-framework
title: "microsoft/agent-framework"
domain: agent-frameworks
summary: >-
  microsoft/agent-framework — ACTIVE, tier S,
  13,532 stars, license MIT, quality 8.46/10, trust 8.29/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-frameworks", "enterprise", "framework", "github-repository", "microsoft"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.61, "reproducibility": 7.0, "security": 7.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.46
  trust_score: 8.29
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "microsoft/agent-framework on GitHub"
    url: https://github.com/microsoft/agent-framework
    type: github-repository
    organization: microsoft
    license: MIT
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# microsoft/agent-framework

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/microsoft/agent-framework> |
| Owner | microsoft (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 13,532 (checked 2026-09-15) |
| Forks | 2,323 |
| Open issues | 612 |
| Contributors | 253 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | dotnet-1.21.0 (2026-09-11) |
| Archived | no |
| Fork | no |
| Homepage | [https://aka.ms/agent-framework](https://aka.ms/agent-framework) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.61 |
| reproducibility | 7.0 |
| security | 7.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.46** |
| **trust_score** | **8.29** |

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
| README size | 13,336 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- New enterprise agent systems on .NET or Python
- Teams that need Microsoft-supported lifecycle and security patching
- Migrating off AutoGen or Semantic Kernel

**Not recommended for**

- Projects that need a minimal, dependency-light Python agent loop
- Teams standardising on the LangChain ecosystem

**Strengths**

- Actively developed by Microsoft with 253 contributors (verified)
- Successor to both AutoGen and Semantic Kernel
- First-class multi-agent workflows, threading and observability
- MIT license

**Weaknesses**

- Younger than the frameworks it replaces, so fewer community answers
- Enterprise orientation adds ceremony for small scripts

**Related projects**

- microsoft/autogen
- microsoft/semantic-kernel
- microsoft/mcp

## Verification notes

Verified 2026-09-15: ACTIVE, release dotnet-1.21.0, MIT.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug microsoft/agent-framework
python3 scripts/generate-index/generate_repository_cards.py --category agent-frameworks
```
