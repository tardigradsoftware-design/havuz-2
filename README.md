# havuz-2 — AI Engineering Intelligence Repository

A **machine-readable, continuously verified external memory layer** for AI coding agents,
research agents and IDE agents.

This is not an awesome-list, not a prompt dump and not a README collection. It is a
**curated evidence base**: every claim carries a source, every source carries a
verification date, and every resource carries a computed quality and trust score.
An agent that reads this repository should make *better decisions*, not just have
*more files*.

> **Design rule #1 — quality over quantity.** A single verified, scored, tested
> skill is worth more than a hundred unvetted links.
> **Design rule #2 — evidence over assumption.** If it cannot be sourced, it is
> marked `model-generated` and quarantined in [`experimental/`](experimental/).
> **Design rule #3 — proven pattern over invention.** Before writing new code an
> agent should find the mature library, the official spec or the proven pattern.

---

## Contents

- [What problem this solves](#what-problem-this-solves)
- [Repository map](#repository-map)
- [Quick start for humans](#quick-start-for-humans)
- [Quick start for AI agents](#quick-start-for-ai-agents)
- [How information is curated](#how-information-is-curated)
- [Scoring: quality vs trust](#scoring-quality-vs-trust)
- [Staleness and expiration](#staleness-and-expiration)
- [How skills are tested](#how-skills-are-tested)
- [Validation & CI](#validation--ci)
- [Automation](#automation)
- [Security & collection ethics](#security--collection-ethics)
- [Current state](#current-state)
- [Contributing](#contributing)
- [License](#license)

---

## What problem this solves

When you tell a coding agent *"build a SaaS dashboard with Next.js, TypeScript and
Supabase"*, the agent normally falls back on:

1. whatever is inside its training cutoff,
2. whatever it can guess confidently,
3. whatever single web result it happened to open first.

The failure modes are predictable and expensive:

| Failure mode | Consequence |
|---|---|
| Outdated framework knowledge | Deprecated APIs, wrong auth patterns, removed config keys |
| Reinventing mature solutions | Hand-rolled auth/ORM/queues instead of maintained libraries |
| Hallucinated sources | Cited repos, papers and packages that do not exist |
| Single-source decisions | Choosing a tool from one blog post, no cross-check |
| Star-count reasoning | "Most stars = best" — ignores archived, abandoned and farmed repos |
| AI-slop UI output | Generic gradients, glassmorphism, fake metrics, inconsistent spacing |
| Context overload | Dumping the whole repo into the prompt and degrading the answer |
| No validation | Nothing measures whether the guidance actually helped |

This repository attacks each of those directly:

| Layer | Directory | Answers the question |
|---|---|---|
| **Skill registry** | [`skills/`](skills/) | *How should this task be executed?* |
| **Agent roles** | [`agents/`](agents/) | *Who is responsible, and what is their output contract?* |
| **Workflows** | [`workflows/`](workflows/) | *What is the gated sequence of steps?* |
| **Knowledge base** | [`knowledge/`](knowledge/) | *What is known about this domain?* |
| **Repository database** | [`repositories/`](repositories/) + [`metadata/repositories.json`](metadata/repositories.json) | *Which project should I use, and is it still alive?* |
| **MCP registry** | [`knowledge/mcp/`](knowledge/mcp/) + [`metadata/tools.json`](metadata/tools.json) | *Which tools can the agent safely be given?* |
| **Patterns** | [`patterns/`](patterns/) | *What is the proven solution shape?* |
| **Prompts** | [`prompts/`](prompts/) | *What instruction has been evaluated?* |
| **Evaluations** | [`evaluations/`](evaluations/) | *Did it actually work?* |
| **Failure knowledge** | [`anti-patterns/`](anti-patterns/), [`failure-modes/`](failure-modes/), [`gotchas/`](gotchas/) | *What should I refuse to do?* |
| **Research archive** | [`sources/`](sources/), [`research-archive/`](research-archive/) | *What does the public research say?* |
| **Decision records** | [`decision-records/`](decision-records/) | *Why was this tradeoff made?* |

---

## Repository map

```text
havuz-2/
├── README.md                     ← you are here
├── AGENTS.md                     ← read this first if you are an agent
├── CONTRIBUTING.md               ← quality gate for new content
├── SECURITY.md                   ← reporting + collection ethics
├── CHANGELOG.md                  ← Added / Updated / Deprecated / Removed / Security
│
├── knowledge/                    ← domain knowledge, written as semantic chunks
│   ├── ai-engineering/           ← agentic coding, knowledge-base design, source scoring
│   ├── agent-engineering/        ← harnesses, memory, self-improvement
│   ├── context-engineering/      ← packing, compression, progressive disclosure
│   ├── prompt-engineering/       ← techniques that survive evaluation
│   ├── reasoning/                ← public reasoning research & methods
│   ├── frontend/ ui-ux/ motion/  ← the web engineering core of this KB
│   ├── backend/ databases/ devops/ infrastructure/
│   ├── security/                 ← web + LLM + agent + MCP security
│   ├── testing/ debugging/ performance/ accessibility/ seo/ architecture/
│   ├── evaluation/ mcp/ browser-automation/ computer-use/ research/
│   └── data-engineering/ multi-agent/ agent-skills/ coding/ misc/
│
├── skills/                       ← SKILL.md + references/ examples/ checklists/ tests/
├── agents/                       ← role definitions with output contracts
├── workflows/                    ← gated multi-skill procedures
├── patterns/                     ← named solutions with tradeoffs
├── prompts/                      ← evaluated prompt templates
├── evaluations/                  ← benchmarks + the internal task suite
├── datasets/                     ← public datasets (never private reasoning traces)
├── models/                       ← model cards, capabilities, limitations
├── repositories/                 ← human-readable cards, one folder per category
├── sources/                      ← papers / docs / blogs / discussions
├── decision-records/             ← ADRs and technology-selection matrices
├── anti-patterns/ failure-modes/ gotchas/    ← failure knowledge
├── research-archive/             ← dated research runs (YYYY/MM)
├── experimental/                 ← quarantined, unvalidated, AI-generated
│
├── metadata/                     ← GENERATED machine-readable registries
│   ├── repositories.json         ← 418 GitHub repos, live-verified
│   ├── tools.json                ← MCP + agent tool registry
│   ├── sources.json              ← consolidated source registry
│   ├── skills.json               ← skill registry extracted from frontmatter
│   ├── evaluations.json          ← evaluation registry
│   ├── index.json                ← flat retrieval index for RAG / vector ingest
│   ├── fetch-report.json         ← audit trail of the last GitHub fetch
│   └── graph.json                ← knowledge-graph edges
│
├── schemas/                      ← JSON Schema for every record type
├── scripts/                      ← crawl / validate / update / score / dedupe / index
├── indexes/                      ← human-readable generated indexes
└── .github/workflows/            ← CI: schema, frontmatter, links, freshness, duplicates
```

Two invariants hold across the whole tree:

- **Generated files are never hand-edited.** `metadata/*.json` and `indexes/*.md`
  are produced by `scripts/`. Hand-edit them and CI fails.
- **Human-authored files carry YAML frontmatter** validated against `schemas/`.

---

## Quick start for humans

```bash
git clone https://github.com/tardigradsoftware-design/havuz-2.git
cd havuz-2
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt

make validate          # schema + frontmatter + links + duplicates
make refresh-github    # re-verify all repository metadata (needs GITHUB_TOKEN)
make index             # regenerate metadata/index.json + indexes/*.md
make stale             # list everything past its expires_at
make score             # re-score skills and sources
```

Read in this order: [`AGENTS.md`](AGENTS.md) → [`indexes/topics.md`](indexes/topics.md)
→ the skill you need → its `references/`.

---

## Quick start for AI agents

**Do not read this repository top to bottom.** Use progressive disclosure:

```text
STEP 1  indexes/topics.md            → which domains apply to my task?        (~1k tokens)
STEP 2  metadata/index.json          → filter by tag/domain/kind               (query, don't read)
STEP 3  skills/<name>/SKILL.md       → frontmatter + Purpose + When to Use     (~800 tokens)
STEP 4  skills/<name>/               → only the section you need
STEP 5  metadata/repositories.json   → pick the tool: filter tier/status/kind
STEP 6  gotchas/ + anti-patterns/    → what will break
STEP 7  execute, then validate against the skill's checklist
```

Machine-readable entry points:

| File | Use it for |
|---|---|
| [`metadata/index.json`](metadata/index.json) | Single flat retrieval index; one entry per embeddable chunk |
| [`metadata/repositories.json`](metadata/repositories.json) | Tool selection: `tier`, `status`, `quality_score`, `trust_score`, `license_risk` |
| [`metadata/tools.json`](metadata/tools.json) | MCP registry entries incl. `registry_kind`, `permissions` and `security.risk_level` |
| [`metadata/skills.json`](metadata/skills.json) | Skill lookup incl. `requires`, `conflicts_with`, `priority` |
| [`metadata/sources.json`](metadata/sources.json) | Citations with `confidence` and `verified_at` |
| [`metadata/graph.json`](metadata/graph.json) | Relationship traversal (skill → uses → framework → mcp → repo) |

**Agent tool-selection rule** (applies whenever you choose a library):

```text
1. Filter metadata/repositories.json by category + tags.
2. Drop status in {ARCHIVED, ABANDONED} unless the task is explicitly historical.
3. Drop license_risk == "no-license-do-not-redistribute" if you intend to vendor code.
4. Sort by trust_score, then quality_score.
5. Prefer official == true for anything touching auth, payments or infra.
6. Read notes: they contain verified move/deprecation/maintenance warnings.
7. If the top candidate is MAINTENANCE, look for a successor before adopting.
```

---

## How information is curated

Intake follows a fixed pipeline. Nothing skips the gate.

```text
DISCOVER → VERIFY → SCORE → CLASSIFY → CATEGORIZE → DEDUPE → LICENSE CHECK → CURATE
```

**Source precedence** (higher wins on conflict):

```text
1. Official organization          7. Established open-source project
2. Official GitHub repository     8. High-quality community repository
3. Official documentation         9. Blog / article
4. Research paper                10. Forum / social discussion
5. Academic institution
6. Maintainer-authored docs
```

**Verification checklist** — run before anything is admitted (`scripts/validate/`):

1. Does the URL resolve?
2. Does the repository actually exist (not a 404, not a squatter)?
3. Is it archived?
4. When was the last commit?
5. Is there a license? Which one?
6. Who maintains it?
7. Stars / forks / contributor count?
8. Is there a security policy?
9. Is there documentation?
10. Is it reproducible (tests, CI, releases, examples)?
11. Does an independent source corroborate it?
12. Does the content actually do what it claims?

Findings that fail verification are **recorded, not deleted** — see
[`metadata/fetch-report.json`](metadata/fetch-report.json) and
[`knowledge/ai-engineering/verification-findings.md`](knowledge/ai-engineering/verification-findings.md).

---

## Scoring: quality vs trust

Two different numbers, because they answer different questions.

- **`quality_score`** — *how good is this thing?*
- **`trust_score`** — *how safe is it to act on without a human double-check?*

An archived project can score well on quality and poorly on trust. A brand-new
project with 200 stars can be high-trust for a narrow claim and low-quality overall.

Weights (see [`knowledge/ai-engineering/source-scoring.md`](knowledge/ai-engineering/source-scoring.md)):

```text
Authority        20%     Documentation      10%
Maintenance      15%     Reproducibility    10%
Adoption         15%     Security           10%
                         Recency            10%
                         Evidence           10%
```

Every component is computed from **observable signals**, never from opinion:

| Component | Signals used |
|---|---|
| Authority | owner is the official org, org vs user account, has homepage, topic coverage, fork penalty |
| Maintenance | days since push, contributor count, release recency, open-issue ratio, archived flag |
| Adoption | log-scaled stars + log-scaled forks + contributor diversity (star farming cannot dominate) |
| Documentation | README presence & size, `docs/`, homepage, CONTRIBUTING, CHANGELOG, description |
| Reproducibility | license strength, tests dir, CI workflows, releases, examples, Makefile/Dockerfile |
| Security | SECURITY.md, official owner, license redistribution risk, archived (no patches), staleness |
| Recency | linear decay on days since push (≈0 at 2 years) |
| Evidence | tests, CI, releases, contributor count, examples, homepage |

Tier mapping: `S ≥ 8.0`, `A ≥ 7.0`, `B ≥ 5.8`, `C ≥ 4.3`, else `EXPERIMENTAL`.
Overrides, in precedence order: `UNVERIFIED` if the GitHub fetch failed, `ARCHIVED` if
archived, `NO-LICENSE` if no license file is detected; a non-SPDX custom license caps the
tier at `A`.

`NO-LICENSE` and `UNVERIFIED` are not interchangeable and were once conflated here:

| Tier | What it says | What it does **not** say |
|---|---|---|
| `NO-LICENSE` | the metadata **was** verified, and verification found no published license — legally unsafe to redistribute | nothing about the record's reliability; it is fully trustworthy |
| `UNVERIFIED` | the metadata **could not** be verified — the fetch failed or the repository is unresolvable | nothing about the license; every other field on such a record is also suspect |

An agent that reads `UNVERIFIED` should re-fetch or discard the record. An agent that reads
`NO-LICENSE` should trust the record and refuse to vendor it. `validate_json.py` enforces
both directions, so a record cannot claim either label without the fact behind it.

### Status of this model: implemented and reproducible, **not** validated

The weights and thresholds above are a documented engineering judgement. They are reproducible —
`scripts/lib/scoring.py` is the single implementation, every component is stored alongside the
total, and two runs on the same data produce the same number — but **nobody has measured whether
they predict usefulness**. No outcome data exists to calibrate against: the 40-task effectiveness
suite that would produce some is specified and not built, and `evaluations/` holds seven scaffolded
domain READMEs and **zero evaluation records** (`metadata/evaluations.json` is an empty list;
[`indexes/evaluations.md`](indexes/evaluations.md) reports 0).

So these figures should be read as *"a defensible, inspectable ordering"* and not as *"a
validated quality metric"*. Nothing in this repository claims otherwise, and a tier is a signal
to check, not a verdict to obey.

Two things are deliberately unresolved and tracked rather than quietly settled:

- **The bands live only in code.** `knowledge/ai-engineering/source-scoring.md` explains the
  model's required properties and its hard overrides but does not restate the numeric
  thresholds, so the document and the implementation cannot be compared by reading them. That is
  an open documentation finding, not a disagreement about the values — the thresholds in this
  README are the ones `scoring.py` implements.
- **Revision is planned major-version work.** Re-weighting the model changes every tier in the
  corpus at once, which is a breaking change for anything that has cached a tier. It is therefore
  scheduled as a `MAJOR` version change with its own validation run, and was explicitly out of
  scope for the Phase 5 review fixes. The Phase 5 work corrected what the tiers *mean*
  (`NO-LICENSE` versus `UNVERIFIED`) without touching how they are computed.

---

## Staleness and expiration

Every record carries `verified_at` and `expires_at`. TTLs by resource kind
(`scripts/lib/scoring.py::expires_for`):

```text
model information              21 days      benchmark            90 days
github tool / mcp / framework  45–60 days   official docs        90 days
blog                          120 days      dataset             180 days
research paper                365 days      specification       365 days
```

`make stale` lists everything past expiry; CI opens a tracking issue when the
count crosses a threshold. Expired ≠ wrong. Expired means **re-verify before acting**.

---

## How skills are tested

Every skill has its own generated test cases at `skills/<skill>/tests/cases.md`, built from
that skill's own body text by
[`scripts/generate-index/generate_skill_tests.py`](scripts/generate-index/generate_skill_tests.py).
Each case uses a fixed four-clause format:

```text
GIVEN    <initial state / input>
WHEN     <the agent applies the skill>
THEN     <observable, checkable outcome>
FAIL IF  <the specific slop or error that means the skill did not work>
```

Four kinds of case are produced, each from a different section of the skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry | the failure is caught by that entry's own detection signal and answered by its own documented response |
| Avoids | each `Anti-Patterns` entry | the anti-pattern is absent for the consequence that entry states |

`THEN` and `FAIL IF` quote the skill's own wording, so a case asserts something
different for every skill by construction rather than by rewording. The generator
measures this and refuses to write output that is generic: distinctness of `THEN`
and `FAIL IF` across the corpus must be at least 0.95, and no single `FAIL IF` may
be shared by more than one skill. Current measurement: **1,108 cases across 50
skills, 1,108 distinct `FAIL IF` strings, at most one skill per `FAIL IF`.**

**These cases are authored specifications, not executed results.** No skill has been
run against its cases by a measured harness, so no `test_pass_rate` is recorded
anywhere and none should be inferred. A case states what would prove the skill
failed; it is not evidence that the skill passes.

### Grading rule: evidence caps confidence

One rule applies corpus-wide, and
[`scripts/validate/validate_frontmatter.py`](scripts/validate/validate_frontmatter.py)
enforces it as a hard error:

| `evidence_level` | Maximum `confidence` |
|---|---|
| `verified-github-api`, `verified-official-docs`, `verified-paper`, `verified-benchmark-run` | `very-high` |
| `cross-checked` | `high` |
| `single-source`, `emerging-consensus`, `practitioner-experience` | `medium` |
| `model-generated` | `low` |

A claim may never be stronger than the evidence that established it. Confidence is
only ever **downgraded** to meet the cap; raising `evidence_level` to match a
confidence is the failure this rule exists to prevent. The table is defined once, in
[`scripts/lib/frontmatter.py`](scripts/lib/frontmatter.py) as `CONFIDENCE_CAP`,
derived from the `evidenceLevel` descriptions in
[`schemas/common.defs.json`](schemas/common.defs.json).

### Is the knowledge base itself effective?

**Not measured. No effectiveness claim is made.**

A 40-task, two-arm suite — `without-kb` versus `with-kb`, comparing success rate,
time, token usage, code quality, bug count, security issues and architecture
quality — is **specified but not built**. It is recorded as a gap in
[`CHANGELOG.md`](CHANGELOG.md), and [`evaluations/`](evaluations/) currently holds
scaffolded directory READMEs and no content. When it is built it will live under
`evaluations/` and this section will be replaced with results — not before. Until
then the honest statement is that this repository's guidance is graded, cited and
cross-referenced, and that nobody has measured whether it helps.

---

## Validation & CI

`.github/workflows/kb-ci.yml` runs on every push and pull request:

```text
validate-yaml         every frontmatter block parses
validate-schemas      every record matches its JSON Schema
validate-links        internal references exist; external links resolve (retry + allowlist)
validate-duplicates   near-duplicate content is flagged, not silently merged
validate-freshness    records past expires_at are reported
validate-policy       no secrets, no private reasoning traces, no unlicensed vendored code
markdown-lint         consistent heading structure for chunking
```

Broken external links do not hard-fail the build on the first occurrence —
transient outages are real. The link checker retries, keeps a known-flaky
allowlist, and only fails after repeated failure across runs.

---

## Automation

| Script | Purpose |
|---|---|
| `scripts/update/fetch_github_metadata.py` | Re-verify every repo against the GitHub API |
| `scripts/update/resolve_failed_seeds.py` | Resolve renamed/moved slugs instead of guessing |
| `scripts/update/check_staleness.py` | Report records past `expires_at` |
| `scripts/crawl/verify_arxiv_papers.py` | Confirm papers by title search (never stores recalled IDs) |
| `scripts/crawl/verify_urls.py` | HEAD/GET-check every external URL |
| `scripts/score/score_skills.py` | Recompute skill quality/trust/tier |
| `scripts/generate-index/generate_mcp_registry.py` | Build `knowledge/mcp/registry/` from verified repo metadata; `--check` proves no drift |
| `scripts/generate-index/generate_skill_tests.py` | Build `skills/*/tests/cases.md` from each skill's own body; refuses to write generic assertions |
| `scripts/generate-index/extract_registries.py` | Emit `metadata/*.json` registries from the governed markdown |
| `scripts/generate-index/update_readme_stats.py` | Refresh the corpus statistics block below |
| `scripts/deduplicate/dedupe.py` | Detect overlapping content across files |
| `scripts/validate/*.py` | Schema, frontmatter, link, policy validators |
| `scripts/generate-index/build_index.py` | Emit `metadata/index.json` + `indexes/*.md` |
| `scripts/generate-index/generate_repository_cards.py` | Emit human-readable repo cards from metadata |

---

## Security & collection ethics

**This repository never collects or redistributes:**

```text
✗ private chain-of-thought          ✗ leaked / extracted system prompts
✗ stolen credentials, API keys      ✗ tokens, cookies, session secrets
✗ private repository content        ✗ internal proprietary model instructions
✗ hacked or exfiltrated datasets    ✗ personal data or private enterprise information
```

Public reasoning *research* is actively collected instead — open models, published
techniques, public datasets, verifier and reward-model research, test-time compute,
search-based reasoning. See [`knowledge/reasoning/public-reasoning-research.md`](knowledge/reasoning/public-reasoning-research.md)
and the exclusion policy in [`knowledge/security/llm-security/excluded-sources.md`](knowledge/security/llm-security/excluded-sources.md).

Report a vulnerability per [`SECURITY.md`](SECURITY.md).

---

## Current state

<!-- KB:STATS:BEGIN -->
_Generated 2026-09-16 by `scripts/generate-index/update_readme_stats.py`. Do not edit by hand._

### Corpus

| Layer | Count | Where |
|---|---|---|
| Skills | **50** | [`skills/`](skills/) |
| Agent roles | **12** | [`agents/`](agents/) |
| Workflows | **11** | [`workflows/`](workflows/) |
| Knowledge articles | **72** | [`knowledge/`](knowledge/) |
| Patterns | **1** | [`patterns/`](patterns/) |
| Failure knowledge (anti-patterns, failure modes, gotchas) | **0** | [`anti-patterns/`](anti-patterns/) · [`failure-modes/`](failure-modes/) · [`gotchas/`](gotchas/) |
| Decision records | **2** | [`decision-records/`](decision-records/) |
| Verified GitHub repositories | **414** | [`indexes/repositories.md`](indexes/repositories.md) |
| MCP servers | **26** | [`indexes/mcp.md`](indexes/mcp.md) |
| MCP registry entries (incl. 9 that are not servers) | **35** | [`indexes/mcp.md`](indexes/mcp.md) |
| Research sources (incl. 9 verified papers) | **9** | [`indexes/research.md`](indexes/research.md) |
| Evaluations & benchmarks | **0** | [`indexes/evaluations.md`](indexes/evaluations.md) |
| Model cards | **0** | [`models/`](models/) |
| Datasets | **0** | [`datasets/`](datasets/) |
| Prompt templates | **2** | [`indexes/prompts.md`](indexes/prompts.md) |
| Skill test cases | **1108** | `skills/*/tests/` |
| Quarantined / experimental | **62** | [`experimental/`](experimental/) · `metadata/pending-paper-candidates.json` |
| Retrieval index entries | **608** | [`metadata/index.json`](metadata/index.json) |

### Verification status of the repository database

All **414** repositories were verified against the GitHub REST API. Aggregate adoption tracked: **16,143,095 stars** across 12 categories.

| Maintenance status | Count | | Tier | Count |
|---|---|---|---|---|
| ACTIVE | 296 | | S | 214 |
| STABLE | 82 | | A | 127 |
| MAINTENANCE | 19 | | B | 29 |
| EXPERIMENTAL |  | | C | 16 |
| ARCHIVED | 10 | | EXPERIMENTAL | 3 |
| ABANDONED | 7 | | ARCHIVED | 10 |
| UNKNOWN |  | | NO-LICENSE | 15 |
|  |  | | UNVERIFIED |  |
|  |  | | DEPRECATED |  |

### Findings the verification run produced

- **26 repositories have moved.** Every one was recorded with its new slug; hard-coded URLs to the old paths silently break agents.
- **10 are archived** — read-only, no security patches, successor required.
- **15 have no detectable license** — flagged `license_risk: no-license-do-not-redistribute`; they are referenced, never vendored.
- **19 are in maintenance mode** (>120 days without a push) and **7 are abandoned** (>365 days), excluding published research artifacts, which are classified `STABLE` on purpose.
- **61 candidate research papers are quarantined** because no primary source could confirm them from the build environment. They are excluded from the retrieval index.

### Top 10 by trust score

| Repository | Stars | Tier | Status | Trust |
|---|---|---|---|---|
| [`Arize-ai/phoenix`](https://github.com/Arize-ai/phoenix) | 11,469 | A | ACTIVE | 9.47 |
| [`camel-ai/camel`](https://github.com/camel-ai/camel) | 17,721 | S | ACTIVE | 9.45 |
| [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | 58,790 | A | ACTIVE | 9.4 |
| [`openai/openai-python`](https://github.com/openai/openai-python) | 31,623 | S | ACTIVE | 9.38 |
| [`github/gh-aw`](https://github.com/github/gh-aw) | 5,137 | S | ACTIVE | 9.27 |
| [`lobehub/lobehub`](https://github.com/lobehub/lobehub) | 82,498 | A | ACTIVE | 9.22 |
| [`calcom/cal.diy`](https://github.com/calcom/cal.diy) | 48,481 | S | ACTIVE | 9.2 |
| [`OpenRLHF/OpenRLHF`](https://github.com/OpenRLHF/OpenRLHF) | 10,005 | S | ACTIVE | 9.2 |
| [`OpenAdaptAI/OpenAdapt`](https://github.com/OpenAdaptAI/OpenAdapt) | 1,725 | S | ACTIVE | 9.16 |
| [`mermaid-js/mermaid`](https://github.com/mermaid-js/mermaid) | 90,253 | S | ACTIVE | 9.14 |

### Categories

| Category | Repositories |
|---|---|
| `developer-tools` | 81 |
| `frontend` | 54 |
| `agent-skills` | 42 |
| `evaluation` | 38 |
| `mcp-servers` | 35 |
| `agent-frameworks` | 33 |
| `browser-automation` | 29 |
| `reasoning-research` | 26 |
| `ai` | 24 |
| `backend` | 21 |
| `databases` | 17 |
| `instructions-standards` | 14 |

`mcp-servers` above is a **repository-corpus category** from the seed list, not a count of MCP servers. The registry's own split — **26 servers** and **9 entries that are not servers**, out of 35 — is in the layer table above and in [`indexes/mcp.md`](indexes/mcp.md). The two numbers measure different things and are not expected to agree.
<!-- KB:STATS:END -->

---

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version:

```text
1. Search first. Duplicate knowledge is a defect.
2. Cite everything. An uncited claim is an opinion, and must be labelled as one.
3. Fill the frontmatter completely. Incomplete metadata blocks curation.
4. New AI-generated content goes to experimental/, not to core.
5. Add a test case with every skill.
6. State conflicts instead of hiding them.
```

Issue templates: new resource · new skill · new research finding · correction · staleness report.

---

## License

Content is licensed [CC BY 4.0](LICENSE); code under `scripts/` is licensed MIT
([LICENSE-CODE](LICENSE-CODE)). Third-party material is **referenced, not vendored** —
each record links to its upstream license. Repositories whose license could not be
detected are flagged `license_risk: no-license-do-not-redistribute` and are never copied.
