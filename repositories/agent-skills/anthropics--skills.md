---
id: anthropics--skills
title: "anthropics/skills"
domain: agent-skills
summary: >-
  anthropics/skills — ACTIVE, tier UNVERIFIED,
  176,456 stars, license NONE, quality 6.94/10, trust 5.24/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "anthropic", "github-repository", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 3.96, "reproducibility": 3.0, "security": 2.5, "recency": 9.95, "evidence": 4.0}
  quality_score: 6.94
  trust_score: 5.24
  tier: UNVERIFIED
  maturity: early
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "anthropics/skills on GitHub"
    url: https://github.com/anthropics/skills
    type: github-repository
    organization: anthropics
    license: NONE
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anthropics/skills

🟢 ACTIVE · tier **UNVERIFIED** · early · confidence **medium**

> Public repository for Agent Skills

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anthropics/skills> |
| Owner | anthropics (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NONE` |
| Stars | 176,456 (checked 2026-09-15) |
| Forks | 20,886 |
| Open issues | 1,232 |
| Contributors | 15 |
| Last push | 2026-09-10 (4 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 3.96 |
| reproducibility | 3.0 |
| security | 2.5 |
| recency | 9.95 |
| evidence | 4.0 |
| **quality_score** (weighted) | **6.94** |
| **trust_score** | **5.24** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 5,552 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Reference for the SKILL.md format and progressive disclosure
- Understanding how a vendor structures first-party skills

**Not recommended for**

- Copying or redistributing its content: GitHub detected NO license file on 2026-09-15
- Vendoring any file from it into this repository

**Strengths**

- Canonical example of the skill format from the vendor that popularised it
- Very high adoption (176k stars verified)
- Actively maintained

**Weaknesses**

- No license detected by GitHub - default copyright applies, so redistribution is not permitted
- No releases, so there is no stable version to pin

**Related projects**

- openai/skills
- google-gemini/gemini-skills
- VoltAgent/awesome-agent-skills

## Verification notes

NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only. Verified 2026-09-15: license NONE. Reference and link only; never vendor.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anthropics/skills
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
