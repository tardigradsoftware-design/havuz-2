---
name: reverse-engineering-public-systems
version: 1.0.0
description: >-
  Infer the architecture of publicly observable systems — from documentation, APIs, job posts,
  patents, talks and observable behaviour — with strict legal and ethical boundaries and explicit
  confidence grading.
category: research
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [reverse-engineering, architecture, inference, competitive-intelligence, ethics, research]
applies_to: [any]
priority: 72
requires: [web-research, evidence-validation]
conflicts_with: []
estimated_tokens: 3128
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Legal and ethical boundaries
    anchor: "#legal-and-ethical-boundaries"
    purpose: overview
  - heading: Evidence classes
    anchor: "#evidence-classes"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Open-source licenses permitting inspection (Apache-2.0, MIT, GPL)"
    url: https://opensource.org/licenses
    type: standard
    organization: Open Source Initiative
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [web-research, evidence-validation, repository-analysis, competitive-analysis, security-audit]
related_repositories: [ossf/scorecard]
tests: 3
---

# Reverse-Engineering Public Systems

## Purpose

Build an accurate model of how a system works using **only what its owners have published or
made observable to any user**, with every inference graded by confidence and every source
cited. Useful for learning architecture, evaluating a vendor, understanding a category, and
diagnosing integration behaviour.

This skill is deliberately narrow. It is analysis of public information — not intrusion, not
circumvention, and not extraction of anything the owner has not offered.

## Legal and ethical boundaries

**These are hard constraints. If an action requires crossing one, stop and do not do it.**

```text
PERMITTED
  □ Reading published documentation, blog posts, engineering talks, papers, patents, changelogs
  □ Reading publicly available source code under its license, and respecting that license's terms
  □ Observing behaviour available to any ordinary user through the intended interface
  □ Reading response headers, published API schemas, error messages your own requests produce
  □ Reading job postings, conference talks, vendor case studies, published architecture diagrams
  □ Reading public filings, standards contributions and public issue trackers
  □ Measuring your own usage: your latency, your quota consumption, your billed units
  □ Forming and publishing hypotheses clearly labelled as inferences

PROHIBITED — do not do these, and do not advise them
  ✗ Accessing any system, endpoint, account or data you are not authorised to access
  ✗ Circumventing authentication, rate limits, access controls, paywalls or license checks
  ✗ Violating a Terms of Service, acceptable-use policy or API agreement
  ✗ Probing, scanning, fuzzing, load-testing or penetrating a third-party system without
    written authorisation (this is unauthorised access in most jurisdictions, regardless of intent)
  ✗ Extracting, reconstructing or republishing model weights, training data, system prompts
    or other proprietary internals — including via "extraction" prompting
  ✗ Using leaked, stolen or inadvertently published internal material, even if it is public.
    This repository excludes such sources by policy; see SECURITY.md
  ✗ Scraping personal data, or scraping in violation of a site's terms or robots directives
  ✗ Social engineering, pretexting or impersonation to obtain information
  ✗ Publishing findings in a way that enables attack (a vulnerability disclosure path exists
    for a reason — use it, and coordinate before publishing)
  ✗ Reproducing copyrighted material beyond quotation for analysis

WHEN UNCERTAIN
  Stop. Ask the owner. Use the disclosure channel. Get written authorisation.
  "It was technically possible" is not permission.
```

Also note: **jurisdiction matters** (CFAA and equivalents, computer-misuse statutes, DMCA
anti-circumvention, GDPR for personal data, contract law for ToS). When the analysis is
commercial, legal review is part of the workflow, not an optional step.

## Evidence classes

Ranked by reliability. Every inference states which class supports it.

```text
CLASS 1 — AUTHORITATIVE PUBLISHED
  official architecture docs, engineering blog posts, published papers, patents,
  conference talks by the team, source code under an OSI license, official API schemas,
  standards contributions
  → supports FACT-level claims about what they state

CLASS 2 — OFFICIAL BUT PROMOTIONAL
  marketing pages, pricing pages, product tours, case studies
  → supports claims about what the vendor SAYS; verify capability claims independently.
    Marketing overstates capability and understates limits

CLASS 3 — OBSERVABLE BY ANY USER
  public response headers, documented error shapes, published status pages, latency and
  throughput of your own authorised usage, visible UI behaviour, public API rate-limit headers
  → supports INFERENCE about implementation, at medium confidence. One observation is an
    anecdote; a controlled series of your own authorised requests is evidence

CLASS 4 — CORROBORATING THIRD-PARTY
  job postings (the strongest accidental signal of a real stack: "we run Kafka on EKS"),
  employee conference talks, engineering podcasts, tech-stack survey sites, dependency
  metadata in published client SDKs, public issue trackers, DNS/TLS certificate transparency
  logs (public by design), CDN and hosting fingerprints visible in headers
  → supports INFERENCE at low-to-medium confidence; requires ≥3 independent corroborations

CLASS 5 — WEAK / UNRELIABLE
  forum speculation, anonymous claims, "a source says", comparison-site marketing,
  AI-summarised content of unknown provenance
  → HYPOTHESIS only. Never published as fact. Never used as the sole support for a conclusion
```

Independence rule: three blog posts restating one vendor talk are **one** source.

## Workflow

```text
SCOPE → LEGAL CHECK → COLLECT → OBSERVE → INFER → CORROBORATE → GRADE → REPORT → DISCLOSE
```

```text
1 SCOPE         Write the question: "How does <product> likely handle multi-tenant isolation?"
                Not "everything about <product>". A bounded question produces a bounded, useful answer.
2 LEGAL CHECK   Confirm every planned method is inside the PERMITTED list and complies with the
                target's terms, the applicable license, and the relevant jurisdiction.
                Record the check. If commercial, get legal review. STOP if any method fails.
3 COLLECT       Class 1 and 2 first: docs, blog, talks, papers, patents, SDK source, API schema,
                changelog. Build a timeline — architecture claims are version-scoped.
4 OBSERVE       Only through your own authorised usage as an ordinary user. Record: what you
                requested, what came back, headers, error shapes, timings, quota behaviour.
                Multiple controlled observations, not one lucky one.
5 INFER         For each question, state the inference, the mechanism it implies, the evidence
                class, and what would falsify it. Prefer the boring explanation: most systems
                use conventional architecture, and exotic inferences need exotic evidence.
6 CORROBORATE   Require ≥2 independent sources for any load-bearing inference; ≥3 for a
                non-obvious one. Look specifically for disconfirming evidence.
7 GRADE         FACT (Class 1 states it) · STRONG INFERENCE (multiple corroborating classes) ·
                INFERENCE (single credible source) · HYPOTHESIS (weak or uncorroborated) ·
                UNKNOWN. Also record the date — architecture claims expire.
8 REPORT        Model → evidence table → inferences with grades → confidence → what would
                change the conclusion → alternatives considered → unknowns → legal basis.
                Label the whole document as an external inference, not as inside knowledge.
9 DISCLOSE      If you found a security weakness in the course of authorised use: do NOT publish.
                Use the vendor's disclosure channel (SECURITY.md, VDP, bug bounty), follow
                coordinated-disclosure norms, and wait for the vendor's timeline.
```

## Report structure

```markdown
# <System> — architecture inference, <date>
Status: EXTERNAL INFERENCE FROM PUBLIC SOURCES — not confirmed by the owner
Legal basis: <methods used, and why each is permitted>

## Model (current best understanding)
<the inferred architecture, with confidence per component>

## Evidence
| # | claim | class | source | publisher | date | verified_at |

## Inferences
### <component>
- Inference: <what>
- Mechanism implied: <why it must work this way>
- Evidence: <classes and sources>
- Confidence: <level>
- Falsified by: <the observation that would prove this wrong>
- Alternatives considered: <other explanations and why they are less likely>

## Unknowns
## Conflicts
## Validity window and re-check trigger
```

## Failure Modes

```text
BOUNDARY DRIFT         "Just one more request to that endpoint" — how permitted becomes prohibited.
TOS BLINDNESS          Scraping or automating against terms that forbid it.
MARKETING AS ARCHITECTURE  Repeating a product page's claims as technical facts.
EXOTIC INFERENCE BIAS  Assuming a novel design because the ordinary one is less interesting.
SINGLE-OBSERVATION PROOF One latency measurement presented as an architectural fact.
ECHO CHAMBER           Three blogs restating one talk counted as corroboration.
UNDATED MODEL          A 2022 architecture claim presented as current.
WEIGHT/PROMPT EXTRACTION Attempting to recover proprietary model internals — prohibited here,
                       and prohibited by this repository's policy.
LEAKED-MATERIAL USE    Citing stolen or inadvertently published internals because they are reachable.
PUBLISHING A VULNERABILITY  Disclosing a weakness publicly instead of through the vendor's channel.
UNQUALIFIED REPORT      Presenting inference as inside knowledge, with no confidence grades.
```

## Quality Checklist

```text
□ Question scoped narrowly; "everything about X" rejected
□ Legal and ethical check recorded; every method inside the PERMITTED list
□ Terms of service, license and jurisdiction reviewed; legal review obtained if commercial
□ No probing, scanning, circumvention, extraction or unauthorised access performed or advised
□ No leaked, stolen or proprietary-internals material used, even if publicly reachable
□ Class 1 and 2 sources collected with dates; a version timeline built
□ Observations limited to your own authorised usage, controlled and repeated
□ Every inference states its mechanism, evidence class, and falsifier
□ ≥2 independent corroborations per load-bearing inference (≥3 if non-obvious)
□ Disconfirming evidence sought and recorded
□ Confidence graded per claim; the whole document labelled external inference
□ Boring/conventional explanations considered before exotic ones
□ Validity window and re-check trigger stated
□ Any security weakness routed to coordinated disclosure, never published
```

## Anti-Patterns

```text
✗ Scanning a third-party host to "see what's running"
✗ Automating requests in violation of the site's terms or rate limits
✗ Prompting a model to reveal its system prompt or training data
✗ Citing a leaked internal document because it is on the public internet
✗ "The marketing page says 99.99%, so their infrastructure must be multi-region active-active"
✗ One curl timing presented as proof of a caching layer
✗ Publishing an unpatched vulnerability as a blog post
✗ An inference report with no confidence grades and no evidence table
```

## References

- [`web-research`](../web-research/SKILL.md) · [`evidence-validation`](../evidence-validation/SKILL.md)
- [`repository-analysis`](../repository-analysis/SKILL.md) · [`competitive-analysis`](../competitive-analysis/SKILL.md)
- [`security-audit`](../security-audit/SKILL.md) — for systems you own or are authorised to test
- [`SECURITY.md`](../../SECURITY.md) — this repository's exclusion policy for leaked material
- [`knowledge/security/`](../../knowledge/security/) · [`research-archive/`](../../research-archive/)
- [`decision-records/`](../../decision-records/) — record the legal-basis decision

## Related Skills

`web-research` · `evidence-validation` · `repository-analysis` · `competitive-analysis` ·
`research-synthesis` · `security-audit`

## Evaluation Criteria

```text
1. Boundary compliance: 0 methods outside the PERMITTED list; 100% of reports carry a legal basis.
2. Evidence grading: 100% of claims carry a class, a source, a date and a confidence level.
3. Corroboration: ≥2 independent sources per load-bearing inference.
4. Falsifiability: every inference names what would disprove it.
5. Predictive accuracy: where later confirmed by the owner, the model matched (tracked over time).
6. Disclosure discipline: 100% of discovered weaknesses routed to coordinated disclosure.
```

Test cases in [`tests/`](tests/).
