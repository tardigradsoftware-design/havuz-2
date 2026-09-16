---
id: security-excluded-sources
title: "Excluded sources: what this knowledge base will never contain, and why"
domain: security
summary: >-
  The exclusion policy for leaked system prompts, private model internals, proprietary weights and
  other improperly obtained material — including two high-star public repositories that are
  explicitly named as excluded, the reasoning, and how the policy is enforced mechanically.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [security, policy, ethics, exclusions, leaked-prompts, model-internals, provenance, legal]
applies_to: [knowledge, sources, repositories, skills, evaluations, research-archive]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-09-15
sections:
  - heading: The rule
    anchor: "#the-rule"
    purpose: overview
  - heading: Named exclusions
    anchor: "#named-exclusions"
    purpose: implementation
  - heading: What is still permitted
    anchor: "#what-is-still-permitted"
    purpose: decision
  - heading: Why popularity does not override this
    anchor: "#why-popularity-does-not-override-this"
    purpose: pitfalls
  - heading: Enforcement
    anchor: "#enforcement"
    purpose: validation
estimated_tokens: 1999
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [evidence-validation, repository-analysis, security-audit, web-research, reverse-engineering-public-systems]
related:
  - SECURITY.md
  - knowledge/security/supply-chain.md
  - knowledge/security/threat-modeling.md
  - scripts/validate/validate_policy.py
  - skills/reverse-engineering-public-systems/SKILL.md
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Star counts for the excluded repositories were retrieved on 2026-09-15 and are recorded here to document that the exclusion was made with full knowledge of their popularity."
  - title: "Open Source Initiative — licenses"
    url: https://opensource.org/licenses
    type: standard
    organization: Open Source Initiative
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Public availability is not a grant of rights; license terms govern what may be copied."
---

# Excluded Sources

## The rule

**This repository will not contain, vendor, summarise in usable form, link as an instruction
source, or build upon:**

```text
✗ leaked, extracted or inadvertently published system prompts of commercial products
✗ private, confidential or proprietary model internals — weights, activation traces, training
  data, tokeniser internals, RLHF datasets, evaluation sets marked private
✗ material obtained by circumventing an access control, a paywall, a rate limit, a terms-of-service
  restriction or a license check
✗ credentials, tokens, API keys or session material of any kind, however obtained
✗ personal data collected without a lawful basis
✗ unpatched vulnerability detail about a third-party system published outside coordinated
  disclosure
```

The rule applies **regardless of public reachability**. Material that has leaked onto the public
internet is still leaked; the leak is the defect, not the accessibility. "Anyone can find it" is a
statement about the internet, not about permission.

## Named exclusions

Two repositories are excluded by name so that the decision is auditable and is not silently
reversed by a future contributor or agent who notices they are popular and missing.

```text
asgeirtj/system_prompts_leaks
  Observed 2026-09-15: ~67,100 stars
  Content: system prompts of commercial AI products, collected without the operators' consent.
  Decision: EXCLUDED. Not ingested, not linked as an instruction source, not summarised in a form
  usable as a prompt. May be referenced in this policy file as an example of the category.

elder-plinius/CL4R1T4S
  Observed 2026-09-15: ~49,900 stars
  Content: extracted system prompts and jailbreak transcripts targeting commercial assistants.
  Decision: EXCLUDED on the same basis.
```

Both are recorded with their star counts deliberately. The point of recording the number is to make
the tradeoff explicit and visible: these are among the most-starred repositories in their category,
and this knowledge base still does not use them. A future reader who wonders whether the omission
was an oversight has the answer.

Star counts carry `stars_checked_at: 2026-09-15` and are snapshots, not durable facts.

### Also excluded, for different reasons

```text
Repositories returning license: null (no license file)
  Not an ethical exclusion — a legal one. Reference and link are fine; vendoring, copying and
  redistribution are not. Two prominent agent-skill collections fall in this class and are marked
  license_risk: no-license-do-not-redistribute in metadata/repositories.json.

Archived repositories
  Not excluded — reclassified. Marked ARCHIVED, citable as prior art, never recommended as a
  live dependency.

Nonexistent repositories
  Several plausible-sounding slugs in the original seed list do not exist (for example an
  "OpenAgentSafety" repository under a well-known org, and a GAIA benchmark repository — GAIA is
  distributed through Hugging Face, not GitHub). These are recorded as resolution failures rather
  than silently dropped, so the absence is explained rather than mysterious.
```

## What is still permitted

The exclusion is narrow, and being precise about its edges prevents it from being used as an
excuse to avoid research:

```text
✓ published research papers, including papers that analyse or critique commercial systems
✓ official documentation, model cards, capability and safety disclosures published by the vendor
✓ vendor engineering blogs, talks, patents and standards contributions
✓ open-source implementations under a usable license, with the license respected
✓ observable behaviour available to any ordinary user through the intended interface
✓ a system's OWN published prompt guidance — many vendors document their prompt format
✓ analysis and criticism of leaked material where the analysis does not reproduce the material
  (describing that a leak exists and what category it belongs to is permitted; republishing the
  text is not)
✓ coordinated-disclosure security research on systems you own or are authorised to test
```

The distinction throughout is **provenance and permission**, not subject matter. Security research
on agent systems is encouraged; obtaining the research material improperly is not.

## Why popularity does not override this

The scoring model in [`source-scoring.md`](../../ai-engineering/source-scoring.md) weights adoption at 15%. It would be
possible to construct a rule where sufficiently high adoption outweighs a provenance defect. That
rule is explicitly rejected here, for three reasons:

```text
1. IT INVERTS THE INCENTIVE.  If popularity launders provenance, the fastest path to legitimacy
   for improperly obtained material is to make it popular. A knowledge base that rewards that is
   participating in it.

2. THE RISK IS NOT PROPORTIONAL TO POPULARITY.  A widely-mirrored leaked prompt is not safer to
   use than a narrowly-shared one; it is more likely to have been noticed and acted upon.

3. THE UTILITY IS LOW.  Leaked prompts are snapshots of a moving target, are usually incomplete,
   and describe a system's configuration rather than its capability. The legitimate alternative —
   published model cards, vendor documentation and reproducible public research — is more durable
   and more useful for engineering decisions.
```

So the exclusion is implemented as a **hard override**, applied before scoring, in the same layer
as `license: null` and `archived: true`. It cannot be outvoted by any component.

## Enforcement

The policy is mechanical, not aspirational.

```bash
make validate-policy        # scripts/validate/validate_policy.py
```

What the validator does:

```text
□ greps every governed file for the excluded repository slugs and for known leaked-prompt
  filenames, and fails on any hit outside this policy document
□ rejects any artifact whose sources block cites an excluded source
□ flags repository records whose license is null and whose card does not carry the
  no-license-do-not-redistribute marker
□ flags code files that reference a no-license repository, requiring confirmation that nothing
  was copied (these surface as warnings with an explicit human-check prompt, because a mention
  in a comment is legitimate while an import is not)
□ runs in CI on every pull request; a contribution cannot merge over it
```

Contributions arriving through the issue templates are checked at admission by the
[`skill-curator`](../../../agents/skill-curator/AGENT.md) agent, whose `refuses_when` clause includes
this policy verbatim. The admission path is stage 5 of
[`workflows/knowledge-base-maintenance`](../../../workflows/knowledge-base-maintenance/WORKFLOW.md).

## References

- [`SECURITY.md`](../../../SECURITY.md) — the repository's security and disclosure policy
- [`knowledge/ai-engineering/source-scoring.md`](../../ai-engineering/source-scoring.md) — hard overrides including this one
- [`knowledge/security/supply-chain.md`](../supply-chain.md) · [`knowledge/security/threat-modeling.md`](../threat-modeling.md)
- [`skills/reverse-engineering-public-systems/SKILL.md`](../../../skills/reverse-engineering-public-systems/SKILL.md) — the permitted/prohibited boundary in detail
- [`skills/evidence-validation/SKILL.md`](../../../skills/evidence-validation/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../../../skills/repository-analysis/SKILL.md)
- [`scripts/validate/validate_policy.py`](../../../scripts/validate/validate_policy.py) — the executable form
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) — what contributors may and may not submit
