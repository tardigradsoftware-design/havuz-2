---
id: security-threat-modeling
title: "Threat modeling for agent systems"
domain: security
summary: >-
  The four-question threat-modeling method, trust boundaries as the unit of analysis, STRIDE per element, the agent-specific threat classes STRIDE misses, and the four artifacts that prove a model happened.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [threat-modeling, stride, security, agents, data-flow, risk]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/security/mcp-security/mcp-threat-model.md, knowledge/security/prompt-injection-defenses.md, knowledge/security/supply-chain.md]
sources:
  - title: "OWASP Top 10 for LLM Applications"
    url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    type: standard
    organization: OWASP
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "LLM01 Prompt Injection and LLM06 Excessive Agency are the entries that make agent threat modeling differ from classical STRIDE."
---
# Threat Modeling

## The method

Threat modeling answers, in writing and before building: **what can go wrong, who would want it to
go wrong, what would it cost, and what are we doing about it.** Skipping it does not remove the
threats; it removes the record of which ones were accepted.

```text
1. WHAT ARE WE BUILDING?      Data-flow diagram: processes, data stores, external entities, and
                              every trust boundary a crossing occurs at. No diagram, no model —
                              threats cannot be enumerated against a vague description.
2. WHAT CAN GO WRONG?         Enumerate per element and per boundary. Volume first, triage second.
3. WHAT ARE WE DOING ABOUT IT? Every threat gets one of: mitigate, transfer, accept, avoid.
                              "Accept" is legitimate and must be written down with a reason, an
                              owner and a date.
4. DID WE DO A GOOD JOB?      Is every boundary examined? Is every accept reasoned? Is every
                              mitigation testable?
```

## Trust boundaries

Threats concentrate at crossings, so the crossing is the unit of analysis:

```text
process ↔ data store          privilege of the process vs sensitivity of the data
inside ↔ outside the network  the internet-facing surface
user ↔ system                 authentication and authorisation
tenant ↔ tenant               isolation in multi-tenant systems
agent ↔ tool                  the MCP boundary
model ↔ untrusted content     prompt injection — a boundary models do not enforce
development ↔ production      CI, secrets, artifact provenance
human ↔ automated action      approval gates on irreversible operations
```

## STRIDE per element

| Threat | Property violated | Question |
|---|---|---|
| **S**poofing | Authentication | Can an actor claim an identity that is not theirs? |
| **T**ampering | Integrity | Can data or code be modified in transit or at rest? |
| **R**epudiation | Non-repudiation | Can an actor deny an action because it is not logged? |
| **I**nformation disclosure | Confidentiality | Can data reach someone unauthorised? |
| **D**enial of service | Availability | Can the service be made unusable or ruinously expensive? |
| **E**levation of privilege | Authorisation | Can an actor act above their granted level? |

Apply all six to every element and every boundary. The mechanical pass surfaces what intuition
skips — repudiation and denial of service are the two most often missed.

## Agent-specific additions

STRIDE under-covers LLM and agent systems. Add:

```text
PROMPT INJECTION            Untrusted content issuing instructions. Treat as a given; control the
                            blast radius rather than trying to prevent it.
EXCESSIVE AGENCY            The model can do more than the task requires. Removing capability is
                            the highest-leverage mitigation available.
CONFUSED DEPUTY             The agent holds credentials the requester does not, and acts on
                            injected instructions using them.
MEMORY POISONING            An injection persists across sessions via memory, config or data.
SUPPLY CHAIN — MODEL/TOOL   A malicious or compromised dependency, MCP server or dataset.
DATA LEAKAGE                Sensitive data reaching a model, a log, a trace or an evaluation set.
NON-DETERMINISM             Same input, different actions — so a passing test is not evidence of
                            safety. Requires distributional evaluation.
```

## Prioritisation

Score likelihood × impact, then rank. Be honest about likelihood: a threat needing physical access
and a targeted attacker is not equivalent to one reachable by any anonymous request. Record the
score, not just the rank, so a reviewer can dispute the inputs rather than the conclusion.

```text
CRITICAL    mitigate before shipping; blocks release
HIGH        mitigate this iteration; written acceptance with an owner and a date if deferred
MEDIUM      track; mitigate when the area is next touched
LOW         accept with a one-line reason
```

## Outputs

A model without these four artifacts did not happen:

```text
1. the data-flow diagram with boundaries marked
2. the threat register — one row per threat with category, score and disposition
3. the acceptance log — what was accepted, by whom, why, and when to revisit
4. the test plan — every testable mitigation gets a test, or it is a wish
```

## Anti-patterns

```text
✗ Modeling services instead of data flows. Boxes hide the crossings where threats live.
✗ Starting with mitigations. "We use TLS" answers a question nobody asked yet.
✗ Treating "accept" as failure. Unaccepted risk is unmanaged risk; written acceptance with a date
  is the mature outcome.
✗ A one-time exercise. Revisit whenever the diagram changes: a new integration, store or tool grant.
✗ Mitigations without owners. Nobody owns it, nobody schedules it.
✗ Assuming the model is a boundary. It is not — see prompt-injection-defenses.md.
```

## References

- [`knowledge/security/mcp-security/mcp-threat-model.md`](mcp-security/mcp-threat-model.md) · [`prompt-injection-defenses.md`](prompt-injection-defenses.md) · [`supply-chain.md`](supply-chain.md)
- [`skills/threat-modeling/SKILL.md`](../../skills/threat-modeling/SKILL.md) · [`skills/security-audit/SKILL.md`](../../skills/security-audit/SKILL.md) · [`workflows/security-audit/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
- STRIDE — <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool> · OWASP LLM Top 10 · OWASP Agentic AI Threats and Mitigations — <https://owasp.org/www-project-agentic-ai-threats-and-mitigations/>
