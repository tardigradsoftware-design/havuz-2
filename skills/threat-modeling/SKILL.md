---
name: threat-modeling
version: 1.0.0
description: >-
  Produce a threat model from a data-flow diagram: enumerate trust boundaries, apply STRIDE plus the agent-specific threat classes, prioritise by likelihood and impact, and record every mitigation, acceptance and test.
category: security
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [security, threat-modeling, stride, data-flow, risk, agents, review]
applies_to: [any]
priority: 3
requires: []
conflicts_with: []
estimated_tokens: 2175
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
  - heading: "Inputs"
    anchor: "#inputs"
    purpose: implementation
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
  - title: "OWASP Top 10 for LLM Applications"
    url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    type: standard
    organization: "OWASP"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "LLM01 Prompt Injection and LLM06 Excessive Agency are the entries that make agent threat modeling differ from classical STRIDE; they drive step 3 and the structural-mitigation rule in step 7."
  - title: "OWASP Agentic AI Threats and Mitigations"
    url: https://owasp.org/www-project-agentic-ai-threats-and-mitigations/
    type: standard
    organization: "OWASP"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Threat taxonomy for autonomous agents including memory poisoning and tool misuse across a multi-agent chain."
  - title: "Microsoft — Threat Modeling Tool and STRIDE"
    url: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool
    type: official-docs
    organization: "Microsoft"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "The STRIDE-per-element enumeration procedure in step 2."
related_skills: [security-audit, prompt-injection-defense, ai-safety-evaluation, architecture-design, code-review]
related_repositories: []
tests: 9
---
# Threat Modeling

## Purpose

Answer in writing, before building: what can go wrong, who would want it to, what it would cost, and
what is being done about it. Skipping this does not remove the threats; it removes the record of which
ones were accepted. The output is a threat register with dispositions, not a diagram.

## When to Use

```text
✓ a new system, service or integration is being designed
✓ an existing system is gaining a new data store, a new external dependency or a new tool grant
✓ a security review is required before launch or before handling a new data class
✓ an incident revealed a threat nobody had enumerated
```

## When NOT to Use

```text
✗ The data flows are unknown. A threat model against a vague description produces vague threats. Draw
  the diagram first.
✗ The goal is compliance evidence rather than risk reduction. Produce the artifact the standard asks
  for, and model separately — conflating them yields a document that satisfies nobody.
✗ A penetration test or an audit is what is needed. Those verify controls against a live system; this
  enumerates threats against a design. They are complements.
✗ The system is unchanged since the last model. Revisit on change, not on a calendar.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| Data-flow diagram | yes | processes, data stores, external entities, and every trust boundary |
| Data inventory | yes | what data exists, its sensitivity, where it is stored and where it leaves |
| Authentication and authorisation model | yes | who the principals are and how access is enforced |
| Deployment topology | yes | what runs where, network boundaries, third parties |
| For agent systems: the tool inventory | yes | every tool, its arguments and its capability tier |

## Workflow

```text
1. DRAW THE DATA FLOWS AND MARK THE BOUNDARIES.   Processes, data stores, external entities, and every
   crossing of a trust boundary: process↔store, inside↔outside the network, user↔system, tenant↔tenant,
   agent↔tool, model↔untrusted content, development↔production, human↔automated action. The crossing is
   the unit of analysis, because that is where threats concentrate.

2. ENUMERATE WITHOUT FILTERING.   Apply all six STRIDE categories to every element and every boundary:
   Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.
   Volume first, triage second. The mechanical pass surfaces what intuition skips — repudiation and
   denial of service are the two most commonly missed.

3. ADD THE AGENT-SPECIFIC CLASSES.   STRIDE under-covers LLM systems. Add: prompt injection, excessive
   agency, confused deputy, memory poisoning, model/tool/dataset supply chain, data leakage into logs
   and traces, and non-determinism (a passing test is not evidence of safety).

4. FOR EACH THREAT, STATE THE MECHANISM AND THE IMPACT.   Not "injection possible" but "an attacker who
   controls a fetched web page can cause the agent to call the send-email tool with an arbitrary
   recipient, because the tool is granted without an approval gate". A threat without a mechanism cannot
   be mitigated or tested.

5. PRIORITISE BY LIKELIGENCE × IMPACT.   Be honest about likelihood: a threat requiring physical access
   and a targeted attacker is not equivalent to one reachable by any anonymous request. Record the
   scores, not just the rank, so a reviewer can dispute the inputs rather than the conclusion.

6. DISPOSITION EVERY THREAT.   Mitigate, transfer, accept or avoid. "Accept" is a legitimate answer and
   must be written with the reason, the owner and the date it must be revisited. An undispositioned
   threat is an unmanaged one.

7. DESIGN THE MITIGATIONS AS STRUCTURE, NOT ADVICE.   Prefer removing capability over instructing
   caution; a gate outside the model over a rule inside the prompt; a scoped short-lived credential over
   a standing token. A mitigation that depends on a component behaving correctly while that component is
   under attack is not a mitigation.

8. WRITE A TEST FOR EVERY TESTABLE MITIGATION.   A control nobody tests is a wish. Adversarial cases
   belong in the evaluation suite with a known correct behaviour.

9. RECORD THE FOUR ARTIFACTS.   The annotated data-flow diagram, the threat register, the acceptance log,
   and the test plan. A model without them did not happen.

10. SET THE REVISIT TRIGGER.   Not a date — a condition: a new integration, a new data store, a new tool
   grant, a new data class, or an incident. Write it into the register.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Modeled services instead of flows | no boundary crossings in the diagram | redraw around data movement; boxes hide the crossings |
| Mitigations before enumeration | "we use TLS" appears with no threat attached | return to step 2; the control answers a question nobody asked |
| Threats without mechanisms | register entries are one word ("injection") | expand each to actor, path, action and impact |
| No disposition | threats listed, nothing decided | disposition every row; unaccepted risk is unmanaged risk |
| Acceptance without owner or date | "accepted" with no follow-up | add an owner and a revisit date, or mitigate |
| Mitigations that depend on the model | "the prompt tells it not to" | move the control outside the model: capability removal, a wrapper gate, a policy check |
| No tests | mitigations asserted, never verified | add adversarial cases to the evaluation suite |
| Model never revisited | diagram predates three integrations | add the revisit trigger to the register |

## Quality Checklist

```text
□ the data-flow diagram exists with boundaries marked
□ all six STRIDE categories were applied to every element and boundary
□ agent-specific classes were considered where a model is involved
□ every threat states actor, mechanism, action and impact
□ likelihood and impact scores are recorded, not just a rank
□ every threat has a disposition, and every acceptance has a reason, an owner and a date
□ mitigations are structural rather than advisory wherever possible
□ every testable mitigation has a test
□ all four artifacts are written down
□ the revisit trigger is stated
```

## Anti-Patterns

```text
✗ STARTING WITH CONTROLS.   A list of technologies in use is not a threat model.
✗ MODELING THE ORG CHART.   Service boxes without data flows hide every crossing.
✗ TREATING "ACCEPT" AS FAILURE.   Written acceptance with a date is the mature outcome; silent
  acceptance is the failure.
✗ ONE-TIME EXERCISE.   The model must be revisited when the diagram changes.
✗ MITIGATIONS WITHOUT OWNERS.   Nobody owns it, nobody schedules it.
✗ ASSUMING THE MODEL IS A TRUST BOUNDARY.   It is not. Instructions to a model are not a control
  boundary; capability removal and external gates are.
✗ THREAT INFLATION.   Listing 200 threats nobody will disposition produces a document that is ignored.
  Depth on the reachable ones beats breadth on the theoretical.
✗ NO ARTIFACTS.   A meeting where threats were discussed is not a threat model.
```

## References

- [`knowledge/security/threat-modeling.md`](../../knowledge/security/threat-modeling.md) — the method and boundary taxonomy in full
- [`knowledge/security/mcp-security/mcp-threat-model.md`](../../knowledge/security/mcp-security/mcp-threat-model.md) — agent tool threats and capability tiers
- [`knowledge/security/prompt-injection-defenses.md`](../../knowledge/security/prompt-injection-defenses.md) · [`knowledge/security/supply-chain.md`](../../knowledge/security/supply-chain.md)
- [`skills/prompt-injection-defense/SKILL.md`](../prompt-injection-defense/SKILL.md) · [`skills/security-audit/SKILL.md`](../security-audit/SKILL.md) · [`skills/ai-safety-evaluation/SKILL.md`](../ai-safety-evaluation/SKILL.md)
- [`workflows/security-audit/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md) · [`agents/security-engineer/AGENT.md`](../../agents/researcher/AGENT.md)
- STRIDE — <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool> · OWASP LLM Top 10 — <https://owasp.org/www-project-top-10-for-large-language-model-applications/> · OWASP Agentic AI Threats — <https://owasp.org/www-project-agentic-ai-threats-and-mitigations/>
