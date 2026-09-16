---
id: source-conflict-case-study
title: "Case study: when a secondary aggregator contradicts the primary source"
domain: research
summary: >-
  A real conflict recorded on 2026-09-15: OpenAlex returned wrong titles for two arXiv DOIs
  (2201.11903 and 2210.03629) while arxiv.org returned the correct ones. This document is the
  worked example for the conflict-resolution policy: never silently pick a winner, record both
  observations, resolve by source precedence, and keep the evidence trail.
status: active
confidence: very-high
claim_type: fact
evidence_level: cross-checked
tags: [verification, conflict-resolution, methodology, arxiv, openalex, citation-integrity]
applies_to: [research, evaluation, ai-engineering]
sections:
  - heading: What happened
    anchor: "#what-happened"
    purpose: overview
  - heading: Evidence log
    anchor: "#evidence-log"
    purpose: references
  - heading: How it was resolved
    anchor: "#how-it-was-resolved"
    purpose: decision
  - heading: Generalised rule
    anchor: "#generalised-rule"
    purpose: pitfalls
  - heading: Checklist
    anchor: "#checklist"
    purpose: checklist
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-09-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    url: https://arxiv.org/abs/2201.11903
    type: research-paper
    organization: Google Brain
    published: 2022-01-28
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Primary source. Fetched directly on 2026-09-15; returned the correct title, author list and version history (v6 2023-01-10)."
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: https://arxiv.org/abs/2210.03629
    type: research-paper
    organization: Princeton University / Google
    published: 2022-10-06
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Primary source. Fetched directly on 2026-09-15; returned the correct title and ICLR camera-ready version history (v3 2023-03-10)."
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    url: https://arxiv.org/abs/2305.10601
    type: research-paper
    published: 2023-05-17
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Third identifier in the same batch; OpenAlex and arXiv agreed here, which is what makes the two disagreements diagnostic rather than systemic."
  - title: "OpenAlex REST API — works endpoint"
    url: https://api.openalex.org/works
    type: official-docs
    organization: OpenAlex
    claim_type: fact
    confidence: medium
    verified_at: 2026-09-15
    note: "The secondary aggregator under test. Queried by DOI filter on 2026-09-15. Reachable and structurally correct, but returned wrong display_title for two of five arXiv DOIs."
---

# Case study: when a secondary aggregator contradicts the primary source

## What happened

While building the research layer of this repository, two independent verification paths were
run against the same two arXiv identifiers on the same day (2026-09-15):

1. **OpenAlex batch DOI lookup** — `api.openalex.org/works?filter=doi:10.48550/arXiv.<id>`
2. **arXiv primary page** — `arxiv.org/abs/<id>`

For three of five identifiers both paths agreed. For two they did not:

| arXiv id | OpenAlex returned title | arXiv returned title |
|---|---|---|
| `2201.11903` | "BNAI, NO-TOKEN, and MIND-UNITY: Pillars of a Systemic Revolution in Artificial Intelligence" | **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (Wei et al., Google; v1 2022-01-28, v6 2023-01-10) |
| `2210.03629` | "Distributing Accountability, Not Capability: Phase Separation and the LLM Workflow Quadrant in Autonomous AI Agent Architectures" | **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al.; v1 2022-10-06, v3 2023-03-10, ICLR camera-ready) |

Corroborating detail that made the arXiv answer obviously correct: OpenAlex reported
`cited_by_count: 4324` for `2201.11903` — consistent with the real Chain-of-Thought paper,
not with an unknown title. The citation graph and the title disagreed *within the same
aggregator record*.

**FACT** (verified 2026-09-15, primary source): `2201.11903` is Chain-of-Thought Prompting
and `2210.03629` is ReAct.

**HYPOTHESIS** (unverified): the aggregator's title metadata was stale, mis-merged, or
overwritten by a metadata-import error. We do not claim to know which.

## Evidence log

```text
2026-09-15  export.arxiv.org/api/query          UNREACHABLE from build sandbox (curl 000)
2026-09-15  api.semanticscholar.org             UNREACHABLE (HTTP 500)
2026-09-15  api.crossref.org                    UNREACHABLE (curl 000)
2026-09-15  api.openalex.org/works?filter=doi:… REACHABLE — 2 of 5 titles mismatched
2026-09-15  arxiv.org/abs/2305.10601            REACHABLE — title/authors/venue confirmed
2026-09-15  arxiv.org/abs/2201.11903            REACHABLE — title/authors/versions confirmed
2026-09-15  arxiv.org/abs/2210.03629            REACHABLE — title/authors/ICLR note confirmed
2026-09-15  web_search (4 queries)              CONFIRMED 2501.12948, 2408.03314,
                                                2311.12983, 2307.03172 against arXiv listings
```

## How it was resolved

Precedence from [`knowledge/ai-engineering/source-scoring.md`](../ai-engineering/source-scoring.md):

```text
official repository / primary publisher  >  academic aggregator  >  blog  >  forum
arxiv.org (the minting authority)        >  OpenAlex (an index)
```

Decision:

1. The arXiv title was recorded as the canonical title.
2. The conflict was **not deleted**. It is recorded in the source's
   `verification.notes` field so a future reader can see that a second path disagreed.
3. `confidence` stayed `very-high` because the primary source was reached directly and
   the corroborating citation count supported it.
4. The remaining 61 candidate papers that could **not** be confirmed against any primary
   source were quarantined in
   [`metadata/pending-paper-candidates.json`](../../metadata/pending-paper-candidates.json)
   with `do_not_cite_until_verified: true` instead of being published with recalled identifiers.

## Generalised rule

When two sources conflict:

```text
1. Identify which one is closer to the minting authority.
2. Check whether either source is internally inconsistent (title vs citation count vs authors).
3. Look for a third independent path (author's own repo, venue proceedings, DOI resolver).
4. Record BOTH observations. Never overwrite the losing claim silently.
5. Set confidence from the strength of the resolution, not from the number of sources:
     2 sources agree, one is primary        → very-high
     2 sources agree, neither is primary    → medium
     sources disagree, resolved by authority → high + conflict note
     sources disagree, unresolved           → conflicting
6. If it cannot be resolved, do not publish the claim. Quarantine it.
```

## Checklist

Use before recording any external citation:

```text
□ Was the primary source (publisher/minting authority) reached directly?
□ Does the record agree with itself (title ↔ authors ↔ year ↔ citation count)?
□ Is there at least one independent corroborating path?
□ If sources disagreed, is the disagreement recorded in verification.notes?
□ If nothing could be confirmed, is the item quarantined rather than published?
□ Is verified_at today's date and not inherited from an earlier run?
```

## References

- arXiv:2201.11903 — <https://arxiv.org/abs/2201.11903> (fetched 2026-09-15)
- arXiv:2210.03629 — <https://arxiv.org/abs/2210.03629> (fetched 2026-09-15)
- arXiv:2305.10601 — <https://arxiv.org/abs/2305.10601> (fetched 2026-09-15)
- OpenAlex Works API — <https://api.openalex.org/works> (queried 2026-09-15)
