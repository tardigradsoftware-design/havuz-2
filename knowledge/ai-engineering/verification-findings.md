---
id: ai-engineering-verification-findings
title: "Verification findings: what the 2026-09-15 ingestion actually discovered"
domain: ai-engineering
summary: >-
  The concrete, dated results of verifying 417 seed repositories against the GitHub API — 27 renames,
  5 archived projects, 2 license-null collections, 3 nonexistent slugs, and the aggregator conflict
  that changed how papers are verified in this repository.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: [verification, findings, github-api, renames, archived, license, provenance, audit-trail]
applies_to: [repositories, sources, knowledge, curation]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
sections:
  - heading: Summary
    anchor: "#summary"
    purpose: overview
  - heading: Renames and transfers
    anchor: "#renames-and-transfers"
    purpose: implementation
  - heading: Archived and maintenance-mode projects
    anchor: "#archived-and-maintenance-mode-projects"
    purpose: pitfalls
  - heading: License findings
    anchor: "#license-findings"
    purpose: pitfalls
  - heading: Slugs that do not exist
    anchor: "#slugs-that-do-not-exist"
    purpose: pitfalls
  - heading: The aggregator conflict
    anchor: "#the-aggregator-conflict"
    purpose: examples
  - heading: What this changed
    anchor: "#what-this-changed"
    purpose: decision
estimated_tokens: 2573
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [repository-analysis, evidence-validation, web-research, research-synthesis]
related_repositories: [facebook/react, cli/cli, makeplane/plane, TabbyML/tabby, genkit-ai/genkit, google/adk-js, googleapis/python-genai, protectai/rebuff, sourcegraph/cody-public-snapshot, anthropics/skills, openai/skills, heroku/12factor]
related:
  - knowledge/ai-engineering/source-scoring.md
  - knowledge/ai-engineering/repository-status.md
  - knowledge/research/source-conflict-case-study.md
  - metadata/repositories.json
  - scripts/update/fetch_github_metadata.py
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Every fact in this document was retrieved from this API on 2026-09-15 under an authenticated token at 5000 requests/hour. urllib follows GitHub's 301 redirects automatically, which is how renames were detected."
  - title: "OpenAlex REST API — works endpoint"
    url: https://api.openalex.org/works
    type: official-docs
    organization: OpenAlex
    claim_type: fact
    confidence: medium
    verified_at: 2026-09-15
    note: "Reachable and structurally correct, but returned wrong display titles for two of five arXiv DOIs tested. Documented in the conflict case study."
---

# Verification Findings — 2026-09-15

## Summary

The repository layer of this knowledge base was built by resolving a seed list of 417 slugs against
the GitHub REST API and scoring what came back. The point of recording the findings is that
**verification changed the data** — which is the only evidence that verification happened.

```text
Seeds submitted            417   (418 originally; 3 duplicate slugs collapsed to 1 with aliases)
Resolved successfully      414   (100% of the deduplicated set, after failure resolution)
Detected renames            27   (the seed slug 301-redirected to a different canonical owner/name)
Archived or snapshot         5+  (archived: true, or renamed to a -snapshot/-archive suffix)
license: null                2+  (high-profile collections with no license file)
Slugs that do not exist      3   (plausible names that return 404)
Cached API responses     ~1,903  (.cache/gh — retained so scores are reproducible offline)
```

If the seed list had been trusted instead of resolved, every one of these would have become a
confident, wrong record in the index.

## Renames and transfers

Twenty-seven seeds resolved to a different canonical repository than the one named. GitHub returns
a 301, and `urllib` follows it automatically — so the fetcher records both the seed slug and the
final canonical slug. Selected examples:

| Seed slug | Canonical | Note |
|---|---|---|
| `facebook/react` | `react/react` | organisation transfer |
| `anthropics/anthropic-cookbook` | `anthropics/claude-cookbooks` | renamed |
| `github/gh` | `cli/cli` | moved to its own org |
| `tabby-ml/tabby` | `TabbyML/tabby` | org renamed |
| `plane-so/plane` | `makeplane/plane` | org renamed |
| `firebase/genkit` | `genkit-ai/genkit` | moved to its own org |
| `google/adk-typescript` | `google/adk-js` | renamed |
| `google-gemini/google-genai` | `googleapis/python-genai` | transferred |
| `open-interpreter/open-interpreter` | `openinterpreter/openinterpreter` | org renamed |
| `sourcegraph/cody` | `sourcegraph/cody-public-snapshot` | renamed **and archived** |
| `sentry-experts/mcp` | `getsentry/sentry-mcp` | moved to the vendor org |
| `huggingface/papers` | `huggingface/awesome-papers` | renamed |
| `rebuff-ai/rebuff` | `protectai/rebuff` | acquired, then archived |
| `lmarena-ai/arena-hard-auto` | `lmarena/arena-hard-auto` | org renamed |
| `AgentDeskAI/browser-tools-server` | `AgentDeskAI/browser-tools-mcp` | renamed |
| `slackapi/slack-mcp-server` | `korotovsky/slack-mcp-server` | transferred to an individual |
| `12factor/12factor` | `heroku/12factor` | see the trap below |

**The `12factor` trap.** The slug `12factor/12factor` resolves to `12factor/12factor-br`, a
Brazilian Portuguese translation with three stars. The canonical Twelve-Factor App is
`heroku/12factor` at roughly 3,800 stars. A redirect-following fetcher that records only the
final slug would have scored the translation instead of the original — a 3-star record standing in
for a foundational document. This is why the fetcher records the seed, the final slug and whether
they differ.

## Archived and maintenance-mode projects

`archived: true` caps the maintenance component at 0 and forces tier `ARCHIVED` regardless of the
computed score. Discovered during this run:

```text
protectai/rebuff                    archived; last push 2024-08-07 — a prompt-injection scanner
                                      from a vendor that was subsequently acquired
sourcegraph/cody-public-snapshot    archived; last push 2025-08-01 — the name itself signals it
                                      is a frozen public snapshot of a product that went closed
lmnr-ai/index                       archived
bigcode-project/bigcodebench        archived
bytebot-ai/bytebot                  archived
```

Each is retained in the index — an archived project is legitimate prior art and a legitimate
reference — but each card carries the `ARCHIVED` tier and the correct handling: **cite as history,
never adopt as a dependency.** The distinction matters most for `rebuff`, which is a security tool;
an unmaintained security dependency is worse than none, because it supplies confidence without
coverage.

## License findings

Two of the most prominent agent-skill collections in the ecosystem return `license: null`:

```text
anthropics/skills    ~176,000 stars, license: null
openai/skills        license: null
```

Both are excellent references and neither is redistributable. Every card for them carries
`license_risk: no-license-do-not-redistribute`, and the policy validator warns on any code file
that references them, prompting an explicit confirmation that nothing was copied.

This finding drove the hard-override design in [`source-scoring.md`](source-scoring.md). A model
that expressed "no license" as a reduced number would let a 176k-star unlicensed collection
outscore a 2k-star Apache-2.0 project — which is exactly backwards for an adoption decision.

## Slugs that do not exist

Three plausible seeds return 404 and are recorded as resolution failures rather than dropped:

```text
EleutherAI/OpenAgentSafety    does not exist. EleutherAI publishes lm-evaluation-harness and
                              related projects; no such safety repository was found under the org.
gaia-benchmark/GAIA           does not exist on GitHub. The GAIA benchmark is distributed through
                              Hugging Face, not as a GitHub repository under that org.
microsoft/generativeai-for-beginners
                              404. The correct slug is microsoft/generative-ai-for-beginners —
                              a single hyphen, and the kind of error that is trivially invented
                              by a model recalling the name.
```

Recording failures matters as much as recording successes. An agent that searches for GAIA on
GitHub, finds nothing, and concludes the benchmark does not exist has made a worse error than one
that finds a record saying "distributed via Hugging Face, not on GitHub".

## The aggregator conflict

Paper verification was attempted two ways on the same day: the OpenAlex API (batch DOI lookup) and
`arxiv.org/abs/` pages (primary source, fetched individually).

For three of five identifiers they agreed. For two they did not:

```text
arXiv 2201.11903
  OpenAlex: "BNAI, NO-TOKEN, and MIND-UNITY: Pillars of a Systemic Revolution in AI"
  arXiv:    "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al.)

arXiv 2210.03629
  OpenAlex: "Distributing Accountability, Not Capability: Phase Separation and the LLM Workflow
             Quadrant in Autonomous AI Agent Architectures"
  arXiv:    "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al.)
```

The arXiv answers were corroborated by OpenAlex's own metadata for the same records — a
`cited_by_count` of 4,324 for 2201.11903 is consistent with Chain-of-Thought and absurd for the
title OpenAlex returned. So the conflict was internally diagnosable, and the primary source won.

Full write-up: [`knowledge/research/source-conflict-case-study.md`](../research/source-conflict-case-study.md).

## What this changed

Findings are only worth recording if they change behaviour. These did:

```text
1. Primary source always wins.   arxiv.org/abs is authoritative for arXiv papers. OpenAlex is
                                 used for citation counts and metadata, never for titles without
                                 cross-check. scripts/crawl/verify_arxiv_papers.py encodes this.

2. Seeds record their resolution. Every repository record keeps the seed slug, the final slug and
                                 a flag for whether they differed, so a redirect can never silently
                                 substitute a different project.

3. Duplicate seeds were collapsed. Three slugs each appeared twice in the seed list (supabase/mcp,
                                 getsentry/sentry-mcp, microsoft/OmniParser). They are now one
                                 record each with an aliases field — 418 seeds, 414 records, and the
                                 difference is explained rather than mysterious.

4. License null became a hard override, not a score deduction.

5. archived became a tier, not a low number.

6. Nonexistent slugs are recorded with the reason and the correct alternative where one exists.

7. The API cache is retained. .cache/gh holds ~1,903 responses so that scores are reproducible
                                 offline and a re-run can be diffed against the data it used.
```

## Re-verification

This document is dated 2026-09-15 with a 90-day window, because the underlying facts (star counts,
archive flags, license presence, push dates) are volatile. Re-run:

```bash
make fetch-repos      # re-resolves all seeds and refreshes observable facts
make validate         # confirms the refreshed records still satisfy every schema and policy
```

The findings above are a snapshot of what verification found on that date. The **method** does not
expire; the numbers do.

## References

- [`knowledge/ai-engineering/source-scoring.md`](source-scoring.md) · [`knowledge/ai-engineering/repository-status.md`](repository-status.md)
- [`knowledge/research/source-conflict-case-study.md`](../research/source-conflict-case-study.md)
- [`metadata/repositories.json`](../../metadata/repositories.json) — the 414 scored records
- [`scripts/update/fetch_github_metadata.py`](../../scripts/update/fetch_github_metadata.py) · [`scripts/update/seeds.json`](../../scripts/update/seeds.json)
- [`scripts/crawl/verify_arxiv_papers.py`](../../scripts/crawl/verify_arxiv_papers.py)
- [`knowledge/security/llm-security/excluded-sources.md`](../security/llm-security/excluded-sources.md)
