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

## [1.1.0] — 2026-09-16

Corrections from the pre-merge review of 1.0.0 ([`REVIEW-REPORT.md`](REVIEW-REPORT.md),
35 findings against commit `32720b8`). This release fixes the three critical findings
and the first high-priority one. No data was invented and no confidence was raised:
every grading change moves a claim **down** to what its evidence supports.

### Fixed — C-1: the skill test corpus was a template

**What was wrong.** 333 cases shared only **4 distinct `FAIL IF` strings** — every
failure condition in the corpus was one of four sentences, identical across
`accessibility-audit`, `rag-pipeline` and `threat-modeling` alike. `THEN` had 45
distinct values, of which 3 covered 87%. Only the `GIVEN` line was skill-specific.
The suite could detect a skill being selected when it should not have been, and
nothing else. `skills/AGENTS.md` rule 3 prohibited this in terms.

**What changed.** `scripts/generate-index/generate_skill_tests.py` now derives all
four clauses from each skill's own body:

| Case kind | Derived from |
|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items |
| Declines | each `When NOT to Use` exclusion, with the alternative it names |
| Detects | each `Failure Modes` entry, with its own detection signal and documented response |
| Avoids | each `Anti-Patterns` entry, with the consequence that entry states |

`THEN` and `FAIL IF` quote that material verbatim, so assertions differ per skill by
construction rather than by rewording. Both parsers handle the two `Failure Modes`
shapes in the corpus (14 skills use a `Failure | Detection | Response` table, 36 use
an aligned `NAME  description` block).

**Measured result.** 1,108 cases across 50 skills (17–26 each, up from 333):

| Clause | Before | After |
|---|---|---|
| distinct `GIVEN` | 332 / 333 | 1,092 / 1,108 |
| distinct `THEN` | 45 / 333 (ratio 0.135) | **1,106 / 1,108 (ratio 0.998)** |
| distinct `FAIL IF` | **4 / 333 (ratio 0.012)** | **1,108 / 1,108 (ratio 1.000)** |
| max skills sharing one `FAIL IF` | 50 | **1** |

The two remaining duplicate `THEN` values are two skills that genuinely list the same
anti-pattern ("logging the full request body on an auth endpoint"); the assertion is
shared because the guidance is. `WHEN` stays at 199 distinct values by design — it
names the act of applying a particular skill, so ~4 values per skill is correct.

**The guarantee is enforced, not asserted.** The generator measures its own output and
refuses to write unless `THEN` and `FAIL IF` distinctness are both ≥ 0.95 and no
`FAIL IF` is shared by more than one skill. `--check` runs the same gates for CI.

**Corrected alongside:** `README.md` claimed skills *"are graded by their
`test_pass_rate` in frontmatter"*. No skill has that field and none has been executed
by a harness. The section now states that the cases are **authored specifications, not
executed results**, and that no pass rate exists or should be inferred.

### Fixed — C-2: evidence level now caps confidence, corpus-wide

**What was wrong.** `README.md` stated that `evidence_level: practitioner-experience`
or `model-generated` *"cannot claim `confidence: high`"*. **59 governed documents did
exactly that.** The review counted 28 because it measured `skills/*/SKILL.md` only;
the rule applies to everything with graded frontmatter.

**The single rule adopted**, derived from the `evidenceLevel` descriptions already in
`schemas/common.defs.json` — not invented for this fix:

| `evidence_level` | Maximum `confidence` |
|---|---|
| `verified-github-api`, `verified-official-docs`, `verified-paper`, `verified-benchmark-run` | `very-high` |
| `cross-checked` | `high` |
| `single-source`, `emerging-consensus`, `practitioner-experience` | `medium` |
| `model-generated` | `low` |

Defined once as `CONFIDENCE_CAP` in `scripts/lib/frontmatter.py`, documented in
`README.md`, and enforced as a **hard error** by `validate_frontmatter.py` — so CI now
fails on any future violation rather than warning.

**59 records corrected, all downward:**

| Change | Count | Directories |
|---|---|---|
| `practitioner-experience` + `high` → `medium` | 50 | skills, agents, workflows, knowledge, prompts, decision-records |
| `cross-checked` + `very-high` → `high` | 6 | knowledge |
| `practitioner-experience` + `very-high` → `medium` | 2 | knowledge |
| `emerging-consensus` + `high` → `medium` | 1 | knowledge |

By directory: skills 33, knowledge 10, agents 7, workflows 5, decision-records 2,
prompts 2. `evidence_level` was **never** raised to justify a confidence — that is the
specific failure the rule exists to prevent. Frontmatter warnings fell from 6 to 1 as
a side effect, since five of the six were "confidence high with no sources".

### Fixed — C-3: documentation no longer asserts an evaluation suite that does not exist

**What was wrong.** `README.md` stated *"The repository itself **is benchmarked** in
`evaluations/knowledge-base/` with a 40-task suite run in two arms … comparing success
rate, time, token usage, code quality, bug count, security issues and architecture
quality."* `AGENTS.md` repeated it. `evaluations/` holds **0 content files** and
`evaluations/knowledge-base/` does not exist as a path. `CHANGELOG.md` already said the
suite was "specified but not built", so the repository contradicted itself.

**What changed.** Both documents now state plainly: *"Not measured. No effectiveness
claim is made."* The suite is described as specified-but-not-built, the non-existent
path is gone, and the future plan is separated from present fact. `AGENTS.md` now
distinguishes the three things "tests" could mean here — validators (exist, enforced in
CI), skill test cases (authored, not executed), and the effectiveness suite (not built).

**New check.** `validate_links.py --internal` now asserts that every repository path
named in prose in `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md` and
`CHANGELOG.md` actually exists — backticked spans as well as link targets, since prose
paths are rarely links. 101 paths checked. Documented naming conventions
(`research-archive/YYYY/MM/`) are exempt via a placeholder-segment list, and tokens
whose first segment is not a real top-level entry are ignored, which keeps GitHub slugs
and package names out of the check without an allowlist.

**The check immediately found three more false claims**, all now corrected:

- `README.md` listed `scripts/score/score_sources.py` in its automation table. That
  script has never existed; the row is replaced with the five generators that do.
- `CHANGELOG.md` referenced `indexes/sources-papers.md`, which `build_index.py` does
  not produce. Corrected to `metadata/sources-papers.json`, the file that exists.
- `sources/papers/README.md` referenced the same non-existent index (fixed pre-commit).

### Fixed — H-1: the MCP registry no longer guesses authentication

**What was wrong.** `generate_mcp_registry.py` documented that capability fields the
GitHub API cannot report *"are NOT guessed"*, and correctly left five of them empty —
then inferred the sixth:

```python
"authentication": "mixed" if rec.get("official") else None,
```

**28 of 35 records** asserted `authentication: mixed` on the sole evidence that the
owner appears in a hand-maintained organisation list. Authentication is the field an
integrator acts on, and `official` says who owns a repository, not how its server
authenticates. The guarantee was the valuable part of that generator, and one field
quietly voided it.

**What changed.** The inference is removed. `authentication` is now absent from all
35 records and from all 35 markdown entries, which is the honest representation: the
schema's enum has no `unknown` member, and absence plus
`capability_evidence: unverified` says exactly what is known. Entries document how to
fill it in — read the project's own docs, then set `capability_evidence` to
`readme-reviewed` or `verified` and date it.

**The guarantee is now enforced.** `assert_no_guesses()` fails the generator if any
entry with `capability_evidence: unverified` carries a populated capability field
(`transport`, `tools`, `resources`, `prompts`, `permissions`, `authentication`,
`recommended_for`). Verified by negative test: injecting `authentication: "mixed"` or
`tools: ["read_file"]` into a clean corpus is caught and reported with the offending
repository named.

**Verified after the fix:** 35/35 records — `authentication` absent, `transport`,
`tools`, `resources`, `prompts`, `permissions`, `recommended_for` and
`not_recommended_for` all empty, `capability_evidence: unverified` on every entry.

### CI

`generated-drift` now regenerates with both new generators and runs their gates as
named steps — *MCP registry asserts no unobservable capability* and *Skill test cases
are skill-specific* — so each generator's guarantee is checked on every push and pull
request rather than resting on its docstring. `update_readme_stats.py` was added to the
regeneration list, since the statistics block was previously regenerated only by hand.

### Still open from the review

Recorded rather than closed, per this repository's own rule on unstated gaps. The
review's remaining findings are untouched by this release:

- **High:** H-2 nine schema fields lost between the registry markdown and `tools.json`,
  including the archived server's `not_recommended_for` warning; H-3 the `UNVERIFIED`
  tier names the wrong property (all 15 records have `fetch_ok: true`; the real
  condition is "no license detected"); H-4 `SECURITY.md`'s hard exclusions have no
  enforcement path in code; H-5 the license override warns only on source-code files
  in a repository whose vendoring risk is markdown; H-6 GitHub API descriptions are
  rendered into cards as markdown with no sanitisation, an injection surface in a
  corpus built to be read by agents; H-7 MCP `category` assigned by unanchored
  substring match — both official SDKs are labelled `ci-cd` because `'ci'` appears
  inside "offi**ci**al"; H-8 five of the "35 MCP servers" are SDKs, a testing tool, a
  registry and a catalog.
- **Medium/Low:** the scoring model's saturated adoption component (94% of records at
  the ceiling), inconsistent component ceilings (theoretical maximum 9.30, which is why
  51.7% of the corpus reaches tier S), `days_since_push` driving three components, the
  `.cache/gh/` reproducibility claim that is not committed, and 20 further items. These
  are grouped in the report as one major-version scoring revision, to be done before the
  corpus grows.

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

- `metadata/sources-papers.json` — 9 papers verified against their primary arXiv sources, with title,
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
