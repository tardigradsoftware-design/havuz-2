---
id: chromedevtools--chrome-devtools-mcp
title: "ChromeDevTools/chrome-devtools-mcp"
domain: mcp-servers
summary: >-
  ChromeDevTools/chrome-devtools-mcp — ACTIVE, tier S,
  52,413 stars, license Apache-2.0, quality 8.15/10, trust 7.28/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["browser", "devtools", "github-repository", "mcp", "mcp-servers", "official"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 6.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.54, "reproducibility": 9.0, "security": 6.0, "recency": 10.0, "evidence": 7.0}
  quality_score: 8.15
  trust_score: 7.28
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "ChromeDevTools/chrome-devtools-mcp on GitHub"
    url: https://github.com/ChromeDevTools/chrome-devtools-mcp
    type: github-repository
    organization: ChromeDevTools
    license: Apache-2.0
    license_risk: none
    confidence: high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# ChromeDevTools/chrome-devtools-mcp

🟢 ACTIVE · tier **S** · production-grade · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Chrome DevTools for coding agents

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/ChromeDevTools/chrome-devtools-mcp> |
| Owner | ChromeDevTools (Organization) |
| Official upstream | no |
| Language | TypeScript |
| License | `Apache-2.0` |
| Stars | 52,413 (checked 2026-09-21) |
| Forks | 4,384 |
| Open issues | 122 |
| Contributors | 128 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | chrome-devtools-mcp-v1.9.0 (2026-09-08) |
| Archived | no |
| Fork | no |
| Homepage | [https://developer.chrome.com/docs/devtools/agents](https://developer.chrome.com/docs/devtools/agents) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 6.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.54 |
| reproducibility | 9.0 |
| security | 6.0 |
| recency | 10.0 |
| evidence | 7.0 |
| **quality_score** (weighted) | **8.15** |
| **trust_score** | **7.28** |

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
| examples | no |
| security md | yes |
| changelog | yes |
| contributing | yes |
| root entries | yes |
| README size | 6,445 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Performance tracing, network inspection and console debugging from an agent
- Frontend debugging workflows that need real DevTools data

**Not recommended for**

- Cross-browser testing (Chrome-only)
- Environments where a full browser profile is unacceptable

**Strengths**

- Official Chrome DevTools team project, Apache-2.0
- Very high adoption for an MCP server (52k stars verified)
- Pushed on the verification date

**Weaknesses**

- Chrome-only
- Exposes runtime page state, so treat page content as untrusted input

**Related projects**

- microsoft/playwright-mcp
- AgentDeskAI/browser-tools-mcp
- GoogleChrome/lighthouse

## Verification notes

Discovered via topic:mcp-server search on 2026-09-15 and verified the same day.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug ChromeDevTools/chrome-devtools-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
