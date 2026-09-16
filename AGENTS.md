# AGENTS.md

Instructions for AI coding agents working **on** this repository.
If you are an agent working **with** this repository as a knowledge source, read
[`README.md` → "Quick start for AI agents"](README.md#quick-start-for-ai-agents) first.

---

## 1. What this repository is

An AI Engineering Intelligence Repository: skill registry + repository database +
MCP registry + research archive + evaluation library, designed to be consumed
programmatically by other agents.

**It is a data product, not a documentation site.** Two consequences:

1. Structure is part of the contract. Moving a file, renaming an `id`, or changing
   a frontmatter key can break retrieval for downstream agents.
2. Every assertion must be attributable. "X is the best framework" is not a
   statement this repository makes without a source, a date and a confidence level.

---

## 2. Build / test / validate commands

```bash
# setup
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt

# validate everything (this is what CI runs)
make validate

# individual checks
python3 scripts/validate/validate_frontmatter.py      # YAML frontmatter + schema conformance
python3 scripts/validate/validate_json.py             # metadata/*.json parse + schema
python3 scripts/validate/validate_links.py --internal # referenced paths exist
python3 scripts/validate/validate_links.py --external # external URLs resolve (network)
python3 scripts/validate/validate_policy.py           # secrets, private-reasoning, license policy
python3 scripts/deduplicate/dedupe.py --report        # near-duplicate content

# regenerate derived artifacts (never hand-edit these)
python3 scripts/update/fetch_github_metadata.py       # needs GITHUB_TOKEN
python3 scripts/crawl/verify_arxiv_papers.py
python3 scripts/generate-index/build_index.py         # metadata/index.json + indexes/*.md
python3 scripts/generate-index/generate_repository_cards.py
python3 scripts/generate-index/update_readme_stats.py
python3 scripts/score/score_skills.py
python3 scripts/update/check_staleness.py
```

There is no application to run and no dev server. "Tests" here means validators
plus the evaluation suite in [`evaluations/`](evaluations/).

---

## 3. Directory contract

| Path | Rule |
|---|---|
| `metadata/*.json` | **GENERATED.** Never hand-edit. Regenerate with `scripts/`. |
| `indexes/*.md` | **GENERATED.** Never hand-edit. |
| `repositories/**/*.md` | **GENERATED** from `metadata/repositories.json`. Curated prose goes in the `notes`, `recommended_for`, `strengths`, `weaknesses` fields of `scripts/update/seeds.json` or in `knowledge/`. |
| `skills/<name>/SKILL.md` | Hand-authored. Frontmatter must match `schemas/skill.schema.json`. |
| `knowledge/**/*.md` | Hand-authored. Frontmatter must match `schemas/knowledge.schema.json`. |
| `agents/<name>/AGENT.md` | Hand-authored. Matches `schemas/agent.schema.json`. |
| `workflows/<name>/WORKFLOW.md` | Hand-authored. Matches `schemas/workflow.schema.json`. |
| `patterns/**/*.md` | Hand-authored. Matches `schemas/pattern.schema.json`. |
| `prompts/**/*.md` | Hand-authored. Matches `schemas/prompt.schema.json`. |
| `experimental/**` | Quarantine. Unvalidated and AI-generated content lives here and nowhere else. |
| `research-archive/YYYY/MM/` | Dated research runs. Append-only; never rewrite history. |
| `.cache/` | Local API cache. Gitignored. Never commit. |

---

## 4. Authoring rules

### 4.1 Every document starts with frontmatter

```yaml
---
id: kebab-case-unique-id
title: Human readable title
domain: frontend            # must be a value from schemas/knowledge.schema.json
summary: >-
  Two or three sentences. This is what a retriever shows before the agent
  decides to read the body, so it must be self-sufficient.
status: active
confidence: high            # very-high | high | medium | low | unverified | conflicting
claim_type: recommendation  # fact | recommendation | experiment | opinion | hypothesis | unknown
evidence_level: cross-checked
tags: [frontend, nextjs, performance]
updated: 2026-09-15
verified_at: 2026-09-15
sources:
  - title: ...
    url: https://...
    type: official-docs
    confidence: high
    verified_at: 2026-09-15
---
```

### 4.2 Write in semantic chunks

Retrievers pull sections, not files. Use these headings where they apply so the
chunk map in frontmatter (`sections:`) is meaningful:

```text
## Overview            ## When to use         ## Implementation
## Pitfalls            ## Examples            ## Validation
## References          ## Decision            ## Checklist
```

Keep each chunk self-contained: no "as above", no unresolved pronouns referring to
a previous section.

### 4.3 Token budget

```text
SKILL.md body            ≤ 2,500 tokens   (put the rest in references/)
knowledge article        ≤ 3,000 tokens
AGENT.md                 ≤ 1,500 tokens
pattern card             ≤ 1,200 tokens
README in any folder     ≤ 800 tokens
```

If content exceeds the budget, split it into `references/<topic>.md` and link.
Progressive disclosure is a hard requirement, not a style preference.

### 4.4 INPUT → PROCESS → OUTPUT → VALIDATION

Skills must be executable procedures. This shape is required:

```markdown
## Inputs
- <what the agent must have before starting>

## Workflow
1. <step> — exit gate: <observable condition>
2. ...

## Outputs
- <artifact, with its required shape>

## Validation
- <check that proves the output is correct>
```

Advice without a validation step is not a skill; move it to `knowledge/`.

### 4.5 Fact vs opinion

Label every non-obvious assertion. Use the `claim_type` field and inline markers:

```markdown
**FACT** (source: …, verified 2026-09-15): Microsoft AutoGen's repository has had
no push in 153 days and Microsoft's Agent Framework is the actively developed successor.

**RECOMMENDATION**: prefer Agent Framework for new .NET/Python agent work.

**HYPOTHESIS** (untested here): …
```

Never let a `model-generated` statement sit next to a verified fact without a marker.

### 4.6 Conflicts are surfaced, not resolved silently

```markdown
### Conflict: does X hold?
- Source A (official docs, 2026-08-01) says: …
- Source B (maintainer blog, 2026-09-02) says: …
- Difference: …
- Likely explanation: …
- Current recommendation: … (confidence: medium)
```

Set `confidence: conflicting` on the record.

### 4.7 Citations

```markdown
Per the Playwright MCP README[^1] …

[^1]: microsoft/playwright-mcp, verified 2026-09-15, Apache-2.0,
      https://github.com/microsoft/playwright-mcp
```

A URL alone is not a citation. Include: what it is, when it was checked, and its license.

### 4.8 Duplication

One concept lives in exactly one place. Everything else links to it.

```markdown
React best practices → see knowledge/frontend/react/best-practices.md
```

`scripts/deduplicate/dedupe.py` flags overlap above a similarity threshold.
Fix by extracting the shared content and linking, not by deleting one copy at random.

---

## 5. Collection ethics — hard limits

**Never add to this repository:**

```text
✗ private or extracted chain-of-thought
✗ leaked, extracted or reverse-engineered system prompts
✗ credentials, API keys, tokens, cookies, session secrets
✗ private repository content or internal proprietary model instructions
✗ hacked, scraped-without-consent or exfiltrated datasets
✗ personal data, private enterprise information
```

If you find such material while researching, **record the exclusion and the reason**
in [`knowledge/security/llm-security/excluded-sources.md`](knowledge/security/llm-security/excluded-sources.md).
Do not copy the content, do not summarise it in a way that reproduces it, and do
not link to it as a recommended resource.

Collect instead: public reasoning research, open models, published techniques,
public datasets, model cards, open evaluation results.

---

## 6. Adding a GitHub repository

```text
1. Add { slug, category, tier, tags, repo_kind?, note? } to scripts/update/seeds.json
2. Run: python3 scripts/update/fetch_github_metadata.py --slug <owner/name>
3. If it 404s: run scripts/update/resolve_failed_seeds.py — do NOT guess a replacement
4. Check metadata/fetch-report.json for: renamed, archived, no_license, stale
5. Run: python3 scripts/generate-index/generate_repository_cards.py
6. Add curated judgement (recommended_for, not_recommended_for, strengths,
   weaknesses, related_projects) via scripts/update/curation.json
7. Run: make validate && make index
```

Never write `stars`, `license`, `pushed_at`, `archived` or any date by hand.
They come from the API and carry `stars_checked_at`.

---

## 7. Adding a skill

```text
skills/<name>/
├── SKILL.md          frontmatter + the 12 required sections
├── references/       deep material, loaded on demand
├── examples/         worked input → output pairs
├── checklists/       short, printable verification lists
└── tests/
    ├── test-001.md   GIVEN / WHEN / THEN / FAIL IF
    └── README.md     how to run them and record results
```

Required `SKILL.md` sections:

```text
Purpose · When to Use · When NOT to Use · Inputs · Required Context · Workflow
Research Phase · Planning Phase · Implementation Phase · Validation Phase
Failure Modes · Quality Checklist · Examples · Anti-Patterns · References
Related Skills · Evaluation Criteria
```

Then register dependencies:

```yaml
requires: [research-before-code, evidence-validation]
conflicts_with: []
priority: 60
```

Priority resolves conflicts: **higher `priority` wins → then `authority` of sources →
then scope specificity (a Next.js-specific skill beats a generic frontend skill) →
then `verified_at` recency.**

---

## 8. Git conventions

```text
Branch:  arena/01a0a577-havuz-2   (this session is pinned to it)
Commit:  feat(skills): add ai-slop-detection validation phase
         fix(metadata): re-verify stale repository records
         docs(knowledge): document context compression tradeoffs
         chore(ci): add freshness gate
Never:   commit .cache/, credentials, or generated files that were hand-edited
Always:  run `make validate` before committing
```

---

## 9. Definition of done for any change

```text
□ Frontmatter complete and schema-valid
□ Every external claim cited with url + verified_at + license
□ No duplication of existing content (linked instead)
□ Generated files regenerated, not hand-edited
□ New skill has ≥3 test cases; new resource has a score
□ Stale records touched by this change were re-verified
□ `make validate` passes locally
□ CHANGELOG.md updated under Added / Updated / Deprecated / Removed / Security
□ experimental/ content was not promoted to core without evidence + human review
```

---

## 10. Agent behaviour creed

```text
DON'T GUESS.                              RESEARCH FIRST.
DON'T COPY RANDOMLY.                      VERIFY FIRST.
DON'T TRUST STARS ALONE.                  EVALUATE QUALITY.
DON'T USE OUTDATED INFORMATION.           CHECK RECENCY.
DON'T HALLUCINATE SOURCES.                CITE THEM.
DON'T OVERLOAD CONTEXT.                   RETRIEVE PROGRESSIVELY.
DON'T REINVENT MATURE SOLUTIONS.          SEARCH FIRST.
DON'T TREAT AI OUTPUT AS FACT.            VALIDATE IT.
DON'T ADD UNVERIFIED KNOWLEDGE TO CORE.   USE EXPERIMENTAL FIRST.
DON'T HIDE CONFLICTING INFORMATION.       SURFACE THE CONFLICT.
DON'T COLLECT PRIVATE MODEL INTERNALS.    USE PUBLIC, LEGAL, REPRODUCIBLE RESEARCH.
BUILD KNOWLEDGE THAT MAKES FUTURE AGENTS BETTER.
```

---

## 11. Nested AGENTS.md

Sub-directories may add a narrower `AGENTS.md` that overrides this file within its
scope. Precedence: **nearest file wins**, then this root file. Any nested file must
state which rules it overrides and why.

Current nested instruction files:

- [`skills/AGENTS.md`](AGENTS.md) — skill authoring specifics
- [`metadata/AGENTS.md`](AGENTS.md) — generated-file contract
- [`experimental/AGENTS.md`](AGENTS.md) — quarantine rules
