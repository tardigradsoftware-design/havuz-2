# Changelog

Every notable change to this knowledge base. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the repository uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) at the level of the content corpus: a
**major** version means a schema-breaking or policy-breaking change, a **minor** version means new
content or new capability, and a **patch** version means corrections, re-verification and metadata
refreshes.

Entries are added by the same PR that makes the change. An entry states what changed, why, and — where
a claim changed — what evidence supports the new position. Corrections to previously published claims
are never made silently; they appear here with the old position named.

---

## [1.0.0] — 2026-09-15

Initial public release. Everything below was authored, verified and validated in a single build pass
against live sources on 2026-09-15.

### Added

**Knowledge layer**

- `knowledge/` — 37 articles across nine domains, each with a graded frontmatter record:
  `claim_type`, `evidence_level`, `confidence`, `verified_at`, `expires_at` and a provenance block.
- Nine domain areas populated: `ai-engineering/`, `agent-engineering/`, `frontend/`, `ui-ux/`,
  `animation/`, `testing/`, `security/`, `research/`, `mcp/`, `database/`, `reasoning/`.
- Freshness windows set per claim class in `knowledge/ai-engineering/freshness-policy.md`:
  30 days for security and pricing, 90 for fast-moving tooling, 180 for framework behaviour,
  365 for architecture and theory, and no expiry for mathematics or specifications.
- The scoring model and its hard overrides in `knowledge/ai-engineering/source-scoring.md`:
  eight weighted components computed only from observable GitHub facts, plus overrides that beat the
  score — archived, abandoned, no license, inactive maintainer, experimental, and security-flagged.

**Repository database**

- `metadata/repositories.json` — 414 repositories fetched live from the GitHub REST API on
  2026-09-15, zero fetch failures, each scored, tiered and merged with curated judgement.
- Tier distribution: 214 S, 127 A, 29 B, 16 C, 3 EXPERIMENTAL, 10 ARCHIVED, 15 UNVERIFIED.
- 427 generated cards under `repositories/`, organised into 12 categories, plus a category README
  for each.
- 417 seed repositories deduplicated to 414 records through alias collapse; 27 confirmed renames
  resolved (among them `facebook/react` → `react/react`, `github/gh` → `cli/cli`,
  `tabby-ml/tabby` → `TabbyML/tabby`, `firebase/genkit` → `genkit-ai/genkit`).
- 10 archived repositories flagged rather than scored: including `protectai/rebuff` and
  `sourcegraph/cody-public-snapshot`.
- Every record carries a `license_risk` field. Repositories returning `license: null` from the API —
  including `anthropics/skills` and `openai/skills` — are marked
  `no-license-do-not-redistribute`, which blocks vendoring regardless of score or popularity.

**Skills**

- `skills/` — 50 skills, each a `SKILL.md` with frontmatter, a body within the 2500-token budget, and
  a `tests/cases.md`.
- 333 test cases across the corpus in GIVEN / WHEN / THEN / FAIL IF form, each derived from the
  skill's own purpose, exclusions, failure modes and anti-patterns rather than from a generic
  template.
- Categories covered: agent design, memory, context engineering, prompt engineering, reasoning,
  evaluation, RAG and retrieval, data pipelines, root-cause analysis, code review, refactoring,
  testing, debugging, performance, security, accessibility, design systems, typography, visual
  hierarchy, animation, CRO, copy, AI-slop detection, repository analysis, research, evidence
  validation, synthesis, MCP design, tool design, and skill curation itself.
- `skills/ai-slop-detection/` with two worked before/after examples: a SaaS analytics dashboard
  scored 8/35 → 30/35 with every contrast pairing measured, and a landing-page rewrite scored
  10/40 → 32/40 with each signature removed individually.

**Agents and workflows**

- `agents/` — 12 agent definitions with scoped permissions, handoff contracts and refusal conditions.
- `workflows/` — 11 staged workflows, each with per-stage exit gates, loop budgets, quality gates and
  named failure modes. Includes `deep-research/` (nine stages, saturation-based stopping condition)
  and `research-before-coding/`.

**Prompts and patterns**

- `prompts/research/deep-research-loop.md` — the single-prompt form of the deep-research workflow,
  with the full prompt text machine-readable in frontmatter.
- `prompts/ui-ux/design-direction-brief.md` — produces a design brief, not a visual implementation.
- `patterns/agents/context-compaction.md` — working-memory compaction with durable state, including
  the silent-loss failure mode that makes compaction dangerous.
- `decision-records/` — an ADR template and a decision-matrix template, both usable as-is.

**Sources**

- `indexes/sources-papers.md` — 9 papers verified against their primary arXiv sources, with title,
  authors, identifier and version date confirmed individually.
- 61 further paper candidates quarantined in `pending-paper-candidates.json` rather than published
  unverified.
- The verification finding that drove the quarantine policy: an aggregator API returned **wrong
  titles for valid arXiv identifiers** on two of the papers checked. Identity is therefore always
  confirmed against the primary source.

**Tooling and governance**

- `schemas/` — 17 JSON Schema files governing every content type, with `additionalProperties: false`
  throughout so that a typo in a field name fails validation rather than being silently ignored.
- `scripts/` — validation (`validate_frontmatter.py`, `validate_json.py`, `validate_links.py`,
  `validate_policy.py`), maintenance (`fetch_github_metadata.py`, `check_staleness.py`, `dedupe.py`),
  generation (`extract_registries.py`, `build_index.py`, `generate_repository_cards.py`,
  `update_readme_stats.py`), scoring (`score_skills.py`, `lib/scoring.py`) and crawling
  (`verify_arxiv_papers.py`, `verify_urls.py`).
- `indexes/` — 13 generated indexes covering 428 entries.
- `.github/workflows/kb-ci.yml` — six CI jobs running the full validation suite on every PR.
- `Makefile` with the same targets, so local and CI runs are identical.
- Five issue templates, plus Dependabot configuration.
- `AGENTS.md` at the root: the operating contract for any agent working in this repository.
- `SECURITY.md` with the exclusion policy, and `CONTRIBUTING.md` with the contribution workflow.
- Dual licensing: `LICENSE` (CC BY-SA 4.0) for content, `LICENSE-CODE` (MIT) for scripts and schemas.

### Security and exclusion decisions

- Two high-popularity repositories were **excluded from ingestion by policy**, not by score:
  `asgeirtj/system_prompts_leaks` (≈67,100 stars) and `elder-plinius/CL4R1T4S` (≈49,900 stars).
  Both distribute leaked or extracted system prompts. They are recorded as explicit exclusions in
  `SECURITY.md` and in `knowledge/security/llm-security/excluded-sources.md`, and must never be
  vendored, summarised in detail, or treated as evidence.
- The exclusion is recorded rather than the repositories being omitted silently, so that a later
  contributor does not rediscover them and add them in good faith.
- No private, stolen or improperly obtained model internals are present anywhere in this repository.
  All research content derives from public, legally obtainable sources.
- A GitHub personal access token pasted into the build conversation was **not** used, stored or
  written into any file, environment variable or git configuration. All metadata was fetched with the
  sandbox's own credentials. The user was advised to revoke it.

### Verification notes

- Star counts, licenses, archival status and push dates were read from the GitHub REST API on
  2026-09-15 and are accurate as of that date. Approximately 1,900 API responses are cached under
  `.cache/gh/` so that the corpus can be re-audited against the exact data it was built from.
- `EleutherAI/OpenAgentSafety` was checked and **does not exist** on GitHub (404). It is recorded as
  absent rather than listed as unverified.
- The GAIA benchmark was checked and is **not hosted on GitHub**; it lives on Hugging Face. It is
  therefore not in the repository database, which covers GitHub-hosted projects.
- `export.arxiv.org/api/query` was unreachable from the build environment by both HTTP client and
  page fetch, so batch paper verification was not possible. Papers were verified individually against
  `arxiv.org/abs/` pages, which is why only 9 are published as verified and 61 remain quarantined.
- OpenAlex returned incorrect titles for some arXiv DOIs and is **not trusted without cross-check**.
  Where sources disagree, the primary source wins and the conflict is recorded.

### Known gaps at release

Recorded rather than hidden, per the repository's own policy on unstated gaps:

- `patterns/` holds 1 pattern. The taxonomy and the template exist; the corpus does not. Domains with
  empty pattern directories: frontend, backend, database, mcp, security, architecture, animation,
  testing, ui, data.
- `anti-patterns/`, `failure-modes/` and `gotchas/` are scaffolded but empty. Failure modes are
  currently documented inside each skill and workflow rather than as standalone records.
- `evaluations/`, `datasets/` and `models/` are scaffolded but empty. The 40-task evaluation suite
  described in the README is specified but not yet built.
- `prompts/` holds 2 prompts across 9 categories. Seven categories are scaffolded and empty.
- `experimental/` and `research-archive/` are scaffolded but empty.
- 7 validation warnings remain, all of the class "reference file with `confidence: high` and no
  `sources[]`". These are deliberately uncorrected rather than silently downgraded: each needs either
  a citation or a confidence reduction decided by a human, not a script.
- Identity distinctiveness on the dashboard example scores 3/5 by design; removing slop produces a
  competent neutral interface, and a distinctive identity is a separate act of design that was not
  attempted.

### Schema changes made during the build

Recorded because they change what content is expressible, and because two of them were made to fit
structured content rather than to loosen a constraint:

- `agent.schema.json` — added `version`, `estimated_tokens`, `handoff_contract`, `quality_gates`
  (string **or** structured object with `gate`/`checked_by`/`on_failure`), `refusal_conditions`,
  `escalation`, `related_skills`, `related_repositories`, `supersedes`, `superseded_by` and
  `sections`.
- `workflow.schema.json` — added `estimated_tokens`, `estimated_duration`, `claim_type`,
  `evidence_level`, `related_skills`, `related_repositories`, `supersedes`, `superseded_by` and
  `sections`; widened `quality_gates` and `artifacts` to accept structured objects alongside strings.
- `pattern.schema.json` — added `version`, bringing it in line with every other content schema.

Each change was made because the structured form carries information a plain string cannot — who
checks a gate, and what happens when it fails — and each preserves the original string form so that
existing content stays valid.

---

## Versioning policy

| Change | Version bump |
|---|---|
| A field removed or renamed in any schema; a policy reversed | **major** |
| A new schema field, content type, skill, workflow, agent or domain | **minor** |
| Re-verification, metadata refresh, corrected claim, fixed link, typo | **patch** |

Metadata refreshes are expected to be frequent and are always patch-level: re-running
`fetch_github_metadata.py` changes star counts and push dates, which changes scores and tiers, and
none of that is a content decision.

[1.0.0]: https://github.com/tardigradsoftware-design/havuz-2/releases/tag/v1.0.0
