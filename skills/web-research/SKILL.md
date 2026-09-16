---
name: web-research
version: 1.0.0
description: >-
  Run a structured multi-source web investigation: search, open, compare, cross-check,
  extract, cite, rank and summarise — never deciding from a single result.
category: research
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [research, web, search, citation, verification, evidence]
applies_to: [any]
priority: 88
requires: []
conflicts_with: []
estimated_tokens: 2066
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Ranking
    anchor: "#ranking"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: Anti-Patterns
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: References
    anchor: "#references"
    purpose: references
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "GAIA: a benchmark for General AI Assistants"
    url: https://arxiv.org/abs/2311.12983
    type: research-paper
    organization: Meta AI / Hugging Face
    published: 2023-11-24
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Browsing plus tool use is required for real-world assistant questions; humans 92% vs GPT-4+plugins 15% at publication."
related_skills: [research-before-code, evidence-validation, research-synthesis, competitive-analysis]
related_repositories: [assafelovic/gpt-researcher, exa-labs/exa-mcp-server, firecrawl/firecrawl-mcp-server, browser-use/browser-use]
tests: 19
---

# Web Research

## Purpose

Answer a question with an **evidence set**, not with an impression. The unit of output
is a ranked, dated, cited claim list with explicit confidence and an explicit statement
of what remains unknown.

## When to Use

```text
□ Any factual question whose answer is not inside the current codebase
□ Comparing libraries, services, pricing, quotas or API shapes
□ Checking whether a project is still maintained, archived, renamed or forked
□ Establishing the current state of a fast-moving ecosystem
□ Investigating an error message that may be version-specific
```

## When NOT to Use

```text
✗ Questions answerable from the repository itself — read the code first
✗ Questions answerable from this knowledge base — check indexes/topics.md first
✗ Opinion questions dressed as fact questions ("what's the best framework?") —
  use competitive-analysis and answer with tradeoffs, not a verdict
✗ Anything requiring authenticated access you do not have
```

## Inputs

```text
question       one sentence, answerable, with a checkable success condition
scope          what is in and out (versions, dates, geographies, ecosystems)
budget         max sources to open, max time; a research task without a budget never ends
decision       what decision the answer will drive (this determines required confidence)
```

## Workflow

```text
FRAME → SEARCH → OPEN → EXTRACT → CROSS-CHECK → RANK → CITE → SUMMARISE → STATE UNKNOWN
```

### 1. FRAME
Rewrite the question so a yes/no or a specific value is the answer.
Bad: "How does Next.js caching work?" Good: "In Next.js <version>, is a `fetch` inside a
Server Component cached by default, and how is that opt-out expressed?"

### 2. SEARCH
Generate ≥4 distinct query formulations. Vary them by:

```text
exact API/term        "unstable_cache" site:nextjs.org
error string          verbatim, in quotes
version-scoped        next.js 15 route handler revalidate default
negative              next.js caching changed breaking
source-scoped         site:github.com/vercel/next.js issue revalidate
```

Do not accept the first query's results. Ranking is optimised for engagement, not correctness.

### 3. OPEN
Open at least: the **official docs for the target version**, the **official repository**
(README, CHANGELOG, relevant issues/PRs), and **one independent source**.
Record the URL, the date on the page (not the date you found it), and the publisher.

### 4. EXTRACT
Pull the specific sentence, code block or table cell that answers the question. Quote it.
Note the version and date it applies to. Discard everything else — extraction is not summarising
a page, it is capturing the load-bearing fragment.

### 5. CROSS-CHECK
For every load-bearing claim, find a second independent source.

```text
agree                  → confidence high / very-high
disagree               → confidence conflicting; write the conflict up (see below)
only one source exists → confidence medium, and say explicitly that it is single-sourced
```

Independence means different *provenance*, not different URLs. Three blogs quoting the
same changelog are one source.

### 6. RANK
See [Ranking](#ranking).

### 7. CITE
Every claim gets: `claim — source (type, publisher, page date, verified_at)`.

### 8. SUMMARISE
Answer the framed question in 1–3 sentences, then the evidence table, then tradeoffs.

### 9. STATE UNKNOWN
List what you could not establish. An answer without an unknown-list is an overconfident answer.

## Ranking

Source precedence (highest wins on conflict):

```text
1  official organisation statement / spec / standard
2  official repository (source code, CHANGELOG, maintainer reply in an issue)
3  official documentation for the exact version in question
4  peer-reviewed paper or preprint from the originating team
5  academic or institutional publication
6  maintainer-authored documentation or blog
7  established open-source project's own docs
8  high-quality community repository with tests and CI
9  practitioner blog with reproducible code
10 forum / social discussion
```

Tie-breakers, in order: **specificity to the version** → recency → reproducibility
(does it include runnable code?) → author's demonstrated proximity to the code.

A high-ranking but *stale* source loses to a lower-ranking *current* one for
version-specific questions. A high-ranking *current* source always wins for
behavioural questions.

## Conflict format

```markdown
### Conflict: <question>
- Source A (<type>, <publisher>, <date>): "<quote>"
- Source B (<type>, <publisher>, <date>): "<quote>"
- Difference: <precise statement of what disagrees>
- Likely explanation: <version drift / scope difference / one is wrong / marketing vs implementation>
- Current recommendation: <what to do> (confidence: <level>)
- How to settle it definitively: <the experiment or primary source that would end the debate>
```

Never silently pick a side.

## Failure Modes

```text
FIRST-RESULT BIAS     The top hit becomes the answer. Fix: ≥3 opened sources, ≥2 independent.
ENGAGEMENT RANKING    Assuming search order reflects correctness. Fix: rank by precedence yourself.
UNDATED DOCS          Reading v4 docs while installing v6. Fix: record the doc's version.
ECHO CHAMBER          Three blogs restating one changelog counted as three sources.
SNIPPET RESEARCH      Answering from the search snippet without opening the page.
INFINITE RESEARCH     No budget, no stopping rule. Fix: declare budget in FRAME.
HALLUCINATED URL      Citing a plausible-looking URL that was never fetched.
                      Fix: never write a URL you did not open; the validator greps for this.
SILENT UNCERTAINTY    Presenting medium-confidence findings as settled.
```

## Quality Checklist

```text
□ Question framed to a checkable answer
□ ≥4 distinct query formulations run
□ Official docs for the correct version opened
□ Official repository (README/CHANGELOG/issues) opened
□ ≥1 independent corroborating source per load-bearing claim
□ Every citation has URL + publisher + page date + verified_at
□ Conflicts written up in the conflict format, not resolved silently
□ Unknowns listed explicitly
□ Budget respected and stated
□ Output would let someone else re-run the search and reach the same conclusion
```

## Anti-Patterns

```text
✗ Citing a URL that was never fetched
✗ "According to the documentation" with no link and no version
✗ Treating an AI-written medium.com post as a primary source
✗ Answering "what's best" with a single product name
✗ Ignoring the CHANGELOG when the question is about a behaviour change
✗ Stopping at the first source that agrees with the initial hypothesis
```

## References

- [`evidence-validation`](../evidence-validation/SKILL.md) — grading a source after finding it
- [`research-synthesis`](../research-synthesis/SKILL.md) — combining multiple investigations
- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md)
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md) — a real conflict recorded on 2026-09-15
- [`prompts/research/deep-research-loop.md`](../../prompts/research/deep-research-loop.md)
- GAIA benchmark, arXiv:2311.12983 (verified 2026-09-15)

## Related Skills

`research-before-code` · `evidence-validation` · `research-synthesis` · `competitive-analysis` ·
`repository-analysis`

## Evaluation Criteria

```text
1. Citation validity: 100% of cited URLs resolve and contain the quoted claim.
2. Independence: ≥2 distinct provenances per load-bearing claim.
3. Version accuracy: the answer is correct for the version actually in the lockfile.
4. Unknown honesty: a human reviewer finds no unstated assumption presented as fact.
5. Reproducibility: another agent given the report can re-run the searches and agree.
```

Test cases in [`tests/`](tests/).
