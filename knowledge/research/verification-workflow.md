---
id: research-verification-workflow
title: "The verification workflow: eight steps from retrieval to graded claim"
domain: research
summary: >-
  Why retrieval and verification are separate activities, the eight-step verification procedure, the precedence order for resolving disagreement between sources, and the quarantine-not-delete rule for material that cannot be graded.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [verification, research, evidence, provenance, citations, quarantine, methodology]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-09-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/research/source-conflict-case-study.md, knowledge/ai-engineering/verification-findings.md, knowledge/ai-engineering/source-scoring.md]
sources:
  - title: "arXiv:2305.10601 — Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    url: https://arxiv.org/abs/2305.10601
    type: research-paper
    organization: null
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Verified directly against the primary arXiv abs page on 2026-09-15; used throughout as the worked example of step 1, reaching the primary source rather than a summary of it."
---
# The Verification Workflow

## Why verification is a separate step

Retrieval asks "is this relevant"; verification asks "is this true, current, primary and
corroborated". Collapsing them produces confident citations of things nobody checked — the most
common and most damaging failure in agent research output.

```text
A citation is not evidence.            A URL that resolves proves the page exists.
A well-formatted reference is not      Formatting is trivially generated.
  evidence either.
```

## The eight steps

```text
1. REACH THE PRIMARY SOURCE.     Not a blog citing it, not a summary, not a search snippet. Paper →
                                 the arXiv abs page or publisher. Library → the repository and the
                                 docs for the exact version. Product fact → the vendor's own page.
2. CONFIRM IDENTITY.             Title, authors, identifier, version, date. Aggregators return wrong
                                 titles for valid identifiers — this happened during this
                                 repository's build (see the case study).
3. CHECK THE DATE AGAINST THE
   CLAIM'S SHELF LIFE.           A 2026 framework default has a 90-day window; a complexity result
                                 has none. Recency belongs to the claim, not the publisher.
4. CHECK THE SOURCE'S STANDING.  Who published it, are they the authority, is it archived, is there
                                 a license, are they self-interested. A vendor's performance claim
                                 about its own product is not independent evidence.
5. SEEK ONE INDEPENDENT
   CORROBORATION.                Independent means different provenance, not a different URL. Three
                                 blogs restating one changelog are one source.
6. RECORD WHAT EACH SOURCE
   SUPPORTS.                     Per claim, not per document. A trailing "Sources: [1,2,3]" proves
                                 nothing about which sentence each backs.
7. GRADE AND LABEL.              Assign claim_type and evidence_level. Anything unreachable is
                                 labelled UNVERIFIED and leaves the active index — quarantined, not
                                 deleted, with a note on what would make it gradeable.
8. CONFLICTS ARE RECORDED.       When sources disagree, both are written down with the resolution
                                 rule applied and the reasoning stated. Hiding the minority view
                                 destroys what a later reader needs to re-decide.
```

## Precedence when sources disagree

```text
1. primary source, reached directly, current for the version in question
2. official documentation from the maintainer or standards body
3. peer-reviewed research with published method and data
4. independent corroboration from a second party with no stake in the answer
5. reputable secondary analysis
6. community sources — forums, blogs, Q&A sites
7. model output with no source: labelled GENERATED, never presented as verified
```

Higher wins. Equal rank with genuine disagreement is a conflict, and it is recorded as one.

## Tooling

```bash
python3 scripts/crawl/verify_urls.py             # reachability of every cited URL
python3 scripts/crawl/verify_arxiv_papers.py     # arXiv abs pages, primary source
python3 scripts/update/fetch_github_metadata.py  # repository facts from the GitHub API
python3 scripts/update/check_staleness.py        # expiry and re-verification queue
make validate                                     # schemas, links, policy, dedupe, staleness
```

The run that built this corpus is documented in
[`knowledge/ai-engineering/verification-findings.md`](../ai-engineering/verification-findings.md):
417 seeds resolved, 27 renames detected, 5+ archived projects found, 2 license-null collections
flagged, 3 nonexistent slugs recorded with reasons.

## Quarantine, not deletion

Unverifiable material moves to `metadata/unverified-papers.json` or `experimental/` and leaves the
active retrieval index. Deletion loses the reasoning that prevents the same wrong claim being
re-adopted; silent retention lets an unverified claim be cited as fact.

Current state: 9 papers verified into `metadata/sources-papers.json`, 61 quarantined in
`metadata/pending-paper-candidates.json` because the batch verification endpoint was unreachable
from the build environment. The script is correct and completes in CI, which has network access.
That limitation is recorded rather than papered over.

## References

- [`knowledge/research/source-conflict-case-study.md`](source-conflict-case-study.md) — a real conflict, resolved
- [`knowledge/ai-engineering/verification-findings.md`](../ai-engineering/verification-findings.md) · [`source-scoring.md`](../ai-engineering/source-scoring.md) · [`freshness-policy.md`](../ai-engineering/freshness-policy.md)
- [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md) · [`skills/web-research/SKILL.md`](../../skills/web-research/SKILL.md) · [`skills/research-synthesis/SKILL.md`](../../skills/research-synthesis/SKILL.md)
- [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md) · [`agents/researcher/AGENT.md`](../../agents/researcher/AGENT.md)
- [`workflows/deep-research/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md) · [`workflows/fact-check/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
