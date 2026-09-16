---
id: openai--skills
title: "openai/skills"
domain: agent-skills
summary: >-
  openai/skills — ACTIVE, tier UNVERIFIED,
  27,255 stars, license NONE, quality 6.56/10, trust 4.77/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: medium
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "github-repository", "openai", "skills"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 4.15, "reproducibility": 1.0, "security": 2.5, "recency": 9.92, "evidence": 2.0}
  quality_score: 6.56
  trust_score: 4.77
  tier: UNVERIFIED
  maturity: early
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "openai/skills on GitHub"
    url: https://github.com/openai/skills
    type: github-repository
    organization: openai
    license: NONE
    confidence: medium
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# openai/skills

🟢 ACTIVE · tier **UNVERIFIED** · early · confidence **medium**

> Skills Catalog for Codex

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/openai/skills> |
| Owner | openai (Organization) |
| Official upstream | yes |
| Language | Python |
| License | `NONE` |
| Stars | 27,255 (checked 2026-09-15) |
| Forks | 1,823 |
| Open issues | 297 |
| Contributors | 35 |
| Last push | 2026-09-08 (6 days before verification) |
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
| documentation | 4.15 |
| reproducibility | 1.0 |
| security | 2.5 |
| recency | 9.92 |
| evidence | 2.0 |
| **quality_score** (weighted) | **6.56** |
| **trust_score** | **4.77** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | no |
| examples | no |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 1,840 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-15) and must be
re-checked against your own constraints._

**Recommended for**

- Comparing OpenAI's skill cataloguing approach with Anthropic's
- Understanding cross-vendor skill portability

**Not recommended for**

- Assuming it is the current recommended distribution channel without checking OpenAI's docs
- Vendoring content: no license detected

**Strengths**

- Useful for studying skill taxonomy and catalogue structure
- 35 contributors, recent activity

**Weaknesses**

- No license detected by GitHub on 2026-09-15
- Small README (1.8 KB) relative to its star count - the substance lives elsewhere
- No releases

**Related projects**

- anthropics/skills
- google-gemini/gemini-skills
- openai/codex

## Verification notes

NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only. The brief asked whether this repository is deprecated. Verified 2026-09-15: it is NOT archived and received a push 6 days before verification, so it is live - but its low documentation volume means it should be treated as a catalogue pointer, not a knowledge source. Check OpenAI's official docs for the currently recommended skill mechanism before building on it.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug openai/skills
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
