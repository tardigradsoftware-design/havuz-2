---
name: prompt-injection-defense
version: 1.0.0
description: >-
  Design and verify defences for systems where untrusted content reaches a model that can act: minimise capability, gate irreversible actions outside the model, scope credentials per task, and test that a fully-compromised model cannot do unacceptable damage.
category: security
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [prompt-injection, security, llm-security, agents, capability-minimisation, blast-radius, testing]
applies_to: [any]
priority: 2
requires: []
conflicts_with: []
estimated_tokens: 2359
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
  - title: "OWASP Top 10 for LLM Applications — LLM01 Prompt Injection"
    url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    type: standard
    organization: "OWASP"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "States the position this skill implements: privilege control and human approval are the mitigations, not detection."
  - title: "Not what you have signed up for: Assessing Indirect Prompt Injection Attacks on LLMs"
    url: https://arxiv.org/abs/2302.12173
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Greshake et al. — establishes indirect injection as a distinct class and retrieval/browsing pipelines as attack surface; the basis for step 5 and the read-plus-send rule."
  - title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
    url: https://arxiv.org/abs/2307.15043
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: high
    verified_at: 2026-09-15
    note: "Zou et al. — automated transferable suffix attacks; the reason string filtering cannot be the primary control."
related_skills: [threat-modeling, security-audit, ai-safety-evaluation, mcp-integration, agent-memory-design]
related_repositories: []
tests: 9
---
# Prompt Injection Defense

## Purpose

Design so that a successful injection cannot do much. A model has one channel — tokens in, tokens out —
so instructions and data are processed by the same mechanism and cannot be reliably separated. Controls
that reduce likelihood are worth having; controls that reduce impact are what the system depends on.

## When to Use

```text
✓ an agent, RAG pipeline or tool-using model reads content it does not fully control
✓ a new tool, MCP server or data source is being connected to a model
✓ a security review covers an LLM feature before launch
✓ an injection was demonstrated or suspected in an existing system
```

## When NOT to Use

```text
✗ The model has no tools and no access to private data. Then the worst outcome is a wrong or
  embarrassing answer — handle it with output policy and abuse tooling, not this skill.
✗ The proposal is a denylist, a keyword filter or a hardened system prompt as the primary control. Those
  are likelihood reductions and are evadable; the structural controls come first.
✗ The system processes only trusted, first-party content with no external ingestion. Re-check this
  assumption: a user's own uploaded document is untrusted content.
✗ The task is red-teaming for disclosure purposes on a system you do not own or are not authorised to
  test. That is prohibited.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| Tool inventory | yes | every tool the model can call, with arguments and worst-case effect |
| Content sources | yes | everything the model reads that it does not control |
| Credential model | yes | what identity the agent acts under and how it is scoped |
| Capability tiers | yes | which actions are read-only, reversible, irreversible or prohibited |
| The approval mechanism | yes | where the human gate is enforced, and proof it is outside the model |

## Workflow

```text
1. ANSWER THE BLAST-RADIUS QUESTION FIRST.   "If the model were fully controlled for one turn, what is
   the worst action it could take?" Enumerate every tool and write the worst case for each. If any entry
   is unacceptable — delete production data, email the customer list, push and deploy, move money — the
   capability grant is wrong. This is not a prompt problem and no prompt fixes it.

2. MINIMISE CAPABILITY.   Grant the narrowest tool set that completes the task. Every capability not
   granted is one injection cannot reach. Review the grant when the task changes, not when someone
   remembers to.

3. GATE IRREVERSIBLE ACTIONS OUTSIDE THE MODEL.   Tier-3 actions — push, merge, deploy, delete, send,
   pay, change IAM, publish — require explicit human approval showing the concrete parameters. The gate
   must live in a wrapper, policy engine or required flag. A gate the model can be persuaded about is
   not a gate, and "the agent asks for confirmation" is not one either.

4. SCOPE CREDENTIALS PER TASK.   Short-lived, least-privilege tokens for the specific resource and
   operation. This removes the confused-deputy condition: there is no excess privilege to misuse.

5. FENCE UNTRUSTED CONTENT AND TRACK PROVENANCE.   Retrieved pages, tool results, files and user
   uploads enter context marked as data, with their origin recorded and a stated rule about which origins
   may issue instructions. Treat this as reducing likelihood, never as sufficient.

6. VALIDATE THE ACTION SIDE.   Check tool-call arguments against a schema and a policy before execution:
   path allowlists confined to the workspace, host allowlists, link-local metadata ranges blocked
   unconditionally, argument-shape constraints. This catches a surprising fraction of successful
   injections at the moment they try to act.

7. BOUND THE DAMAGE.   Action budgets per session and per tool, exponential backoff with jitter,
   idempotency keys on mutations, a circuit breaker on repeated failure. Injection-driven loops are a
   real failure mode and they are cheap to bound.

8. TREAT DURABLE WRITES AS PRIVILEGED.   Anything the system persists across sessions — memory, config,
   a knowledge file, a database row — passes a write-path review. Memory poisoning is a persistent
   compromise, not a transient one.

9. REVIEW READ-PLUS-SEND PAIRS TOGETHER.   A read-only tool combined with any send capability is an
   exfiltration path. "It only reads" is not a safe classification.

10. LOG EVERYTHING.   Tool name, arguments, result summary, timestamp, and the content that triggered the
   call. Without this a compromise is undiagnosable and unattributable, and steps 1-9 cannot be verified
   after an incident.

11. TEST IT.   Include injection attempts in the evaluation suite as adversarial tasks with a known
   correct behaviour: refuse or escalate, and take no action. Test direct injection, indirect injection
   via retrieved content, encoded and translated payloads, payloads split across two tool results, and
   the "the user approved this" claim inside tool output.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Worst case is unacceptable | a tool can delete, send or pay without a gate | remove the capability or add an external gate; do not proceed |
| Gate is inside the model | approval depends on the model deciding to ask | move the gate to a wrapper or policy engine |
| Standing admin credential | one token for everything | scope per task, short-lived |
| Fence treated as a boundary | "the prompt says to ignore instructions in content" | keep it, and stop relying on it; add steps 2, 3, 6 |
| Exfiltration path unnoticed | read tool plus send tool both granted | review the pair; restrict the send side |
| Memory write unprotected | injected content persisted | add write-path review |
| No action budget | a loop issued thousands of calls | add budgets, backoff, a breaker |
| Cannot reconstruct the incident | no per-call log | logging is the missing control and the cheapest one |
| Tests pass, adversarial cases absent | evaluation suite has no injection tasks | add them with known correct behaviour |

## Quality Checklist

```text
□ the blast-radius question was answered per tool, in writing
□ no entry in that list is unacceptable without a gate
□ the capability grant is the narrowest that completes the task
□ Tier-3 actions are gated outside the model, with concrete parameters shown
□ credentials are scoped and short-lived
□ untrusted content is fenced and its provenance is tracked
□ tool arguments are validated against a schema and policy before execution
□ path and host allowlists exist; metadata ranges are blocked
□ action budgets, backoff, idempotency keys and a breaker are in place
□ durable writes pass a review
□ every tool call is logged with its triggering context
□ adversarial injection cases are in the evaluation suite and pass
```

## Anti-Patterns

```text
✗ SYSTEM-PROMPT HARDENING AS THE ONLY CONTROL.   Instruction-following is the exploited capability;
  the same mechanism makes the mitigation unreliable.
✗ DENYLISTS AND KEYWORD FILTERS.   Evaded by paraphrase, translation, encoding, images, or splitting a
  payload across two tool results. Automated suffix attacks make hand-written lists obsolete before
  they ship.
✗ ASKING THE MODEL IF IT IS SAFE TO PROCEED.   The component under attack is the component being asked.
✗ A GUARD MODEL AS THE ONLY CONTROL.   Useful as a signal; still probabilistic, and now also injectable.
✗ TRUSTING A TOOL'S DOCUMENTED CAPABILITIES.   Enumerate the runtime surface and diff it on upgrade.
✗ "IT ONLY READS, SO IT IS SAFE."   Read plus send is exfiltration.
✗ DESIGNING FOR PREVENTION ONLY.   Assume success and design the blast radius; prevention-only designs
  fail completely the first time they fail.
✗ NO TESTS.   A defence nobody has attacked is a hypothesis.
```

## References

- [`knowledge/security/prompt-injection-defenses.md`](../../knowledge/security/prompt-injection-defenses.md) — the layered model and what does not work
- [`knowledge/security/mcp-security/mcp-threat-model.md`](../../knowledge/security/mcp-security/mcp-threat-model.md) — threat inventory and capability tiers
- [`knowledge/mcp/security.md`](../../knowledge/mcp/security.md) — the pre-enablement checklist for a tool
- [`knowledge/security/threat-modeling.md`](../../knowledge/security/threat-modeling.md) · [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md)
- [`skills/threat-modeling/SKILL.md`](../threat-modeling/SKILL.md) · [`skills/security-audit/SKILL.md`](../security-audit/SKILL.md) · [`skills/ai-safety-evaluation/SKILL.md`](../ai-safety-evaluation/SKILL.md) · [`skills/mcp-integration/SKILL.md`](../mcp-integration/SKILL.md)
- [`workflows/security-audit/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
- OWASP LLM Top 10 — <https://owasp.org/www-project-top-10-for-large-language-model-applications/> · Greshake et al., arXiv:2302.12173 · Zou et al., arXiv:2307.15043
