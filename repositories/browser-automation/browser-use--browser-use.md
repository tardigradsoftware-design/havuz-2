---
id: browser-use--browser-use
title: "browser-use/browser-use"
domain: browser-automation
summary: >-
  browser-use/browser-use — ACTIVE, tier S,
  114,702 stars, license MIT, quality 8.62/10, trust 8.51/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "automation", "browser", "browser-automation", "github-repository"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.75, "reproducibility": 10.0, "security": 4.5, "recency": 10.0, "evidence": 8.0}
  quality_score: 8.62
  trust_score: 8.51
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "browser-use/browser-use on GitHub"
    url: https://github.com/browser-use/browser-use
    type: github-repository
    organization: browser-use
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

# browser-use/browser-use

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> Agents that use the browser.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/browser-use/browser-use> |
| Owner | browser-use (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `MIT` |
| Stars | 114,702 (checked 2026-09-15) |
| Forks | 12,609 |
| Open issues | 420 |
| Contributors | 360 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | 0.13.10 (2026-09-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://browser-use.com](https://browser-use.com) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.75 |
| reproducibility | 10.0 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 8.0 |
| **quality_score** (weighted) | **8.62** |
| **trust_score** | **8.51** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | yes |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 14,959 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Agents that must operate a real browser
- Web research automation
- Form filling and multi-step web task completion

**Not recommended for**

- Deterministic test suites where Playwright alone is sufficient
- High-assurance flows without a human gate (payments, account changes)

**Strengths**

- Very high adoption (114k stars verified) and 360 contributors
- MIT license, frequent releases (0.13.10)
- Active sibling projects: browser-harness (self-healing), desktop, bux

**Weaknesses**

- Non-deterministic by nature: the same task can take different paths
- Real browser sessions are a large prompt-injection and data-exfiltration surface
- Token cost per task is high

**Related projects**

- browser-use/browser-harness
- microsoft/playwright-mcp
- browserbase/stagehand
- web-infra-dev/midscene
- ChromeDevTools/chrome-devtools-mcp

## Verification notes

Verified 2026-09-15: ACTIVE, MIT, q=8.62.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug browser-use/browser-use
python3 scripts/generate-index/generate_repository_cards.py --category browser-automation
```
