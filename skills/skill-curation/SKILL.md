---
name: skill-curation
version: 1.0.0
description: >-
  Admit, grade, merge and retire content in the knowledge base: verify provenance and sources, check for duplication and conflict, apply the license and exclusion policy, and decide what enters the active index.
category: meta
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [curation, admission, provenance, deduplication, conflict-resolution, licensing, knowledge-base, meta]
applies_to: [knowledge-base, curation]
priority: 6
requires: []
conflicts_with: []
estimated_tokens: 2456
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: "GitHub"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The license.spdx_id, archived and pushed_at fields that steps 2 and 5 read; license: null is the do-not-redistribute trigger."
  - title: "Open Source Initiative — licenses"
    url: https://opensource.org/licenses
    type: standard
    organization: "Open Source Initiative"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Public availability is not a grant of rights; the license terms govern what may be copied, which is the basis of step 2."
  - title: "JSON Schema Specification, 2020-12 draft"
    url: https://json-schema.org/draft/2020-12/release-notes
    type: specification
    organization: "JSON Schema"
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The schema contract step 10 validates against, with additionalProperties: false."
related_skills: [skill-authoring, evidence-validation, repository-analysis, documentation]
related_repositories: []
tests: 24
---
# Skill Curation

## Purpose

Decide what enters the active corpus, at what confidence, and what must be refused. Curation is the
control that keeps a growing knowledge base trustworthy: without it, volume rises while average
confidence falls, and every retrieved claim carries the same implicit weight as every other.

## When to Use

```text
✓ new content is proposed: a skill, a knowledge article, a repository, a source or a pattern
✓ an existing entry needs re-grading after a source changed or expired
✓ duplication or conflict between entries has been detected
✓ a periodic review of the active index is due
```

## When NOT to Use

```text
✗ The content is being written for the first time. Author it, then curate it; self-curation of
  unreviewed material is a weaker control.
✗ The question is whether a claim is true rather than whether it belongs here. That is
  evidence-validation and fact-checking.
✗ The entry is generated output with no human review. Generated content is not admitted; it is a draft.
✗ A legal question exceeds the policy: escalate rather than decide.
```

## Workflow

```text
1. CHECK THE EXCLUSION POLICY FIRST.   Refuse outright, before any quality assessment: leaked or
   extracted system prompts, private model internals, material obtained by circumventing an access
   control, credentials of any kind, personal data without a lawful basis, unpatched third-party
   vulnerability detail outside coordinated disclosure. Public reachability does not change this — the
   leak is the defect, not the accessibility. Record the refusal and the reason so the decision is not
   re-litigated.

2. CHECK THE LICENSE BEFORE THE CONTENT.   license: null means do-not-redistribute: reference and link
   with attribution, never vendor or copy. Record license_risk on the entry. For derived content, confirm
   the upstream license permits it and that attribution is present.

3. VERIFY PROVENANCE.   content_class (original, derived, curated, generated), generated_by, and
   human_reviewed. Reach every cited source and confirm it supports the claim attached to it. A source
   that does not support the claim is a defect regardless of the claim's truth.

4. GRADE THE CLAIM, NOT THE AUTHOR.   Assign claim_type (fact, recommendation, experiment, opinion,
   hypothesis) and evidence_level from what was actually verified. confidence: high or very-high requires
   sources. Anything that could not be reached is labelled UNVERIFIED and quarantined — it leaves the
   active index rather than being deleted, with a note on what would make it gradeable.

5. SET THE FRESHNESS WINDOW FROM THE CLAIM.   30 days for pricing and quotas; 90 for framework APIs, MCP,
   model capability and browser behaviour; 6 months for stable library APIs; 12 months for
   specifications, language semantics and design principles; no expiry for mathematical results and
   published findings, which change by retraction rather than by time. Halve the window for a volatile
   subject or a load-bearing claim.

6. SEARCH FOR DUPLICATION.   Same procedure under a different name, same fact in two domains, two entries
   describing one repository under different slugs. Prefer merging with an alias over keeping both; a
   duplicate pair eventually diverges and then both are wrong.

7. RESOLVE CONFLICTS BY PRECEDENCE, AND RECORD THEM.   Primary source reached directly > official
   documentation > peer-reviewed research > independent corroboration > reputable secondary analysis >
   community sources > unsourced model output. Independence means different provenance, not different
   URLs. When two sources of equal rank genuinely disagree, record both with the reasoning — do not
   silently drop the minority view.

8. CHECK THE ENTRY'S CONNECTIONS.   related_skills resolve to real skills, related_repositories to real
   records, internal links resolve, and the sections map matches the headings. A broken link is a
   retrieval failure, not a cosmetic one.

9. DECIDE THE DISPOSITION.   Admit to the active index; admit as experimental; quarantine as unverified;
   merge into an existing entry; supersede with a link from the old entry; or refuse with a recorded
   reason. Every disposition is written down.

10. VALIDATE MECHANICALLY.   Frontmatter against the schema, links, JSON records, policy, dedupe and
   staleness. Curation judgement is not a substitute for the validators, and the validators are not a
   substitute for judgement.

11. REGENERATE THE DERIVED VIEWS.   Indexes and cards are generated from the metadata layer; a hand-edited
   index is overwritten on the next run. Edit the data or the curation file, then regenerate.

12. RECORD THE DECISION.   What was admitted, at what grade, what was refused and why, what was merged,
   and the date. Curated judgements are the only place human opinion enters the score, so they are dated
   and attributed for that reason.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Excluded content admitted | the policy check was skipped | refuse and record; public reachability is not permission |
| Unlicensed content vendored | license: null and a copy in the tree | remove the copy; keep a linked summary with attribution |
| Source does not support the claim | re-reading it does not back the statement | re-grade or remove the claim |
| Unreachable source admitted as verified | the URL was never reached | quarantine as UNVERIFIED with a re-grade note |
| Duplicate entries diverge | two entries, different content | merge with an alias; keep one authoritative version |
| Conflict resolved silently | the minority source disappeared | record both with the precedence reasoning |
| Window set from the source's prestige | a 2026 framework default given 12 months | set the window from the claim class |
| Broken internal links | validator reports them | fix before admitting; a broken link is a retrieval failure |
| Index hand-edited | overwritten on regeneration | edit the data or curation file, then regenerate |
| Disposition not recorded | nobody knows why an entry is absent | record refusals with reasons |

## Quality Checklist

```text
□ the exclusion policy was checked before quality
□ the license permits what was done with the content, and license_risk is recorded where relevant
□ provenance fields are complete and human review is stated
□ every cited source was reached and supports its claim
□ claim_type, evidence_level and confidence reflect what was verified
□ the freshness window was set from the claim class, not the source's prestige
□ duplication was searched for and merges were preferred over duplicates
□ conflicts were resolved by precedence and recorded, including the minority view
□ related references and internal links resolve
□ a disposition was chosen and written down
□ all validators pass with zero errors
□ derived views were regenerated, not hand-edited
```

## Anti-Patterns

```text
✗ CURATING BY VOLUME.   Admitting everything and grading nothing; average confidence falls as the
  corpus grows.
✗ SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR.   Popularity does not launder provenance, and
  a leaked prompt is excluded at any star count.
✗ TREATING license: null AS A LOW SCORE.   It is a hard override: reference only, never redistribute.
✗ DELETING UNVERIFIABLE CONTENT.   Quarantine keeps the reasoning that prevents the same wrong claim
  being re-adopted; deletion loses it.
✗ HIDING A CONFLICT.   Suppressing the minority view destroys what a later reader needs to re-decide.
✗ GRADING THE PUBLISHER INSTEAD OF THE CLAIM.   A prestigious source can carry an unverified claim.
✗ SETTING THE WINDOW FROM PRESTIGE.   Recency is a property of the claim, not the publisher.
✗ HAND-EDITING GENERATED FILES.   The change is silently lost on the next regeneration.
✗ NO RECORDED REFUSALS.   The same content is proposed again next quarter.
```

## References

- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md) — the model and its hard overrides
- [`knowledge/ai-engineering/freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md) — the windows applied in step 5
- [`knowledge/ai-engineering/repository-status.md`](../../knowledge/ai-engineering/repository-status.md) — status classifications
- [`knowledge/research/verification-workflow.md`](../../knowledge/research/verification-workflow.md) · [`source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md) — the exclusion policy in full
- [`skills/evidence-validation/SKILL.md`](../evidence-validation/SKILL.md) · [`skills/skill-authoring/SKILL.md`](../skill-authoring/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../repository-analysis/SKILL.md)
- [`agents/skill-curator/AGENT.md`](../../agents/skill-curator/AGENT.md) · [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md) · [`workflows/knowledge-base-maintenance/WORKFLOW.md`](../../workflows/knowledge-base-maintenance/WORKFLOW.md)
- [`scripts/validate/`](../../scripts/validate/) · [`scripts/deduplicate/dedupe.py`](../../scripts/deduplicate/dedupe.py) · [`scripts/update/curation.json`](../../scripts/update/curation.json)
