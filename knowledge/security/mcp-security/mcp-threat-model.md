---
id: security-mcp-threat-model
title: "MCP threat model: what can go wrong when an agent gets tools"
domain: security
summary: >-
  The threat model for Model Context Protocol servers and tool-using agents — prompt injection
  reaching a tool, confused deputy, over-broad capability grants, supply-chain risk in server
  packages, and the mitigations that are structural rather than advisory.
status: active
confidence: very-high
claim_type: recommendation
evidence_level: cross-checked
tags: [mcp, security, threat-model, prompt-injection, confused-deputy, tool-use, supply-chain, capabilities]
applies_to: [mcp-server, agent, tool-integration, coding-agent]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
sections:
  - heading: Why MCP changes the threat model
    anchor: "#why-mcp-changes-the-threat-model"
    purpose: overview
  - heading: Threat inventory
    anchor: "#threat-inventory"
    purpose: implementation
  - heading: Capability tiers
    anchor: "#capability-tiers"
    purpose: decision
  - heading: Structural mitigations
    anchor: "#structural-mitigations"
    purpose: implementation
  - heading: What does not work
    anchor: "#what-does-not-work"
    purpose: pitfalls
estimated_tokens: 2812
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [security-audit, threat-modeling, prompt-injection-defense, mcp-integration]
related_repositories: [modelcontextprotocol/servers, microsoft/playwright-mcp, supabase/mcp, chrome-devtools/chrome-devtools-mcp, korotovsky/slack-mcp-server, getsentry/sentry-mcp]
related:
  - knowledge/mcp/security.md
  - knowledge/security/prompt-injection-defenses.md
  - knowledge/security/supply-chain.md
  - knowledge/security/threat-modeling.md
  - knowledge/security/llm-security/excluded-sources.md
  - skills/mcp-integration/SKILL.md
sources:
  - title: "Model Context Protocol specification"
    url: https://modelcontextprotocol.io/specification
    type: specification
    organization: Anthropic / MCP maintainers
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Defines the transport, capability negotiation and tool/resource/prompt primitives the threats below are framed against."
  - title: "OWASP Top 10 for LLM Applications"
    url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    type: standard
    organization: OWASP
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "LLM01 Prompt Injection and LLM06 Excessive Agency are the two entries this threat model operationalises for tool-using agents."
  - title: "OWASP Agentic AI Threats and Mitigations"
    url: https://owasp.org/www-project-agentic-ai-threats-and-mitigations/
    type: standard
    organization: OWASP
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Threat taxonomy for autonomous agents, including memory poisoning and tool misuse across a multi-agent chain."
---

# MCP Threat Model

## Why MCP changes the threat model

An MCP server gives a model the ability to act. Before tools, the worst outcome of a successful
prompt injection was a wrong answer. After tools, the worst outcome is a wrong **action** — a
deleted row, a sent message, a pushed commit, a file read from outside the project.

The structural change is that untrusted content and trusted capability now share a context:

```text
BEFORE   untrusted text → model → text output → human reads it → human acts
AFTER    untrusted text → model → tool call → the tool acts, with the model's privileges
```

The human is removed from the loop that the action occurs in. Every mitigation below is a way of
putting a boundary back into that loop, because no amount of model instruction reliably substitutes
for one.

This is OWASP LLM01 (Prompt Injection) meeting LLM06 (Excessive Agency): the injection is the
entry, and the excessive agency is what makes it consequential.

## Threat inventory

| # | Threat | Mechanism | Impact | Structural mitigation |
|---|---|---|---|---|
| T1 | **Injection reaching a tool** | Untrusted content (a web page, an issue, a file, a tool result) contains an instruction the model follows | Arbitrary action within the granted capability set | Capability minimisation + human confirmation on mutating tools |
| T2 | **Confused deputy** | The agent holds credentials the *user* does not have, and acts on injected instructions using them | Privilege escalation to the agent's level, not the requester's | Per-request scoped credentials; never a standing admin token |
| T3 | **Over-broad capability grant** | A server is enabled wholesale because one tool is needed | Every other tool on that server becomes reachable by T1 | Enable per-tool, not per-server; deny by default |
| T4 | **Tool-result poisoning** | The output of tool A contains instructions that shape the call to tool B | Chained compromise across a workflow | Treat tool results as data; strip or fence instruction-shaped content before it re-enters context |
| T5 | **Supply chain — server package** | A malicious or typosquatted MCP server package is installed and runs locally with the user's file and network access | Full local compromise, credential theft | Pin versions; verify publisher; read the source before enabling; check license and CI |
| T6 | **Supply chain — transitive** | The server is fine; a dependency it installs at first run is not | Same as T5, one hop removed | Lockfile inspection; install in a container or sandbox |
| T7 | **Resource exfiltration** | A read-capable tool is pointed at secrets, `.env`, `~/.ssh`, or a cloud metadata endpoint | Credential and data loss | Path allowlists; block link-local metadata ranges; deny reads outside the workspace |
| T8 | **Unbounded action** | A loop or retry drives repeated mutating calls (thousands of writes, messages, API calls) | Data damage, cost, rate-limit lockout, account action | Idempotency keys, per-session action budgets, circuit breakers |
| T9 | **Silent scope drift** | A server's capability set changes across an upgrade | New tools appear without anyone deciding to grant them | Pin the version; diff the tool list on upgrade; treat new tools as unapproved |
| T10 | **Memory poisoning** | Injected content causes a durable write to agent memory, knowledge or a config file, persisting across sessions | Compromise survives restart | Write-path approval; treat memory writes as privileged; review persisted content |
| T11 | **Cross-session identity confusion** | One server instance serves multiple users or projects with shared state | Data leakage between principals | Isolate per-principal state; never share a server process across trust domains |
| T12 | **Absence of audit** | Actions taken cannot be reconstructed afterwards | Unattributable incident, no way to bound the damage | Log every tool call with args, result and triggering context |

## Capability tiers

The single highest-leverage control is deciding what may happen without a human in the loop. This
repository assigns every MCP server and tool a tier, recorded in the agent definition that uses it:

```text
TIER 0 — READ-ONLY, PUBLIC
  Read public data, search, fetch documentation. No side effects, no private data.
  Autonomy: unrestricted.

TIER 1 — READ-ONLY, PRIVATE
  Read the workspace, the repository, the user's own records, an internal database.
  Side-effect free but exposes private data, so exfiltration (T7) is the live risk.
  Autonomy: unrestricted inside the session; never permitted to send data to a Tier 2+ tool
  without the pair being reviewed together.

TIER 2 — REVERSIBLE WRITE
  Create a branch, open a draft PR, write a file in the workspace, add a comment, create a ticket.
  Undoable by the same actor without data loss.
  Autonomy: permitted with logging; the diff or the created object must be shown.

TIER 3 — IRREVERSIBLE OR EXTERNAL WRITE
  Push to a protected branch, merge, deploy, delete data, send email or a message to a third
  party, move money, change IAM, publish a package, mutate production config.
  Autonomy: REQUIRES EXPLICIT HUMAN APPROVAL, every time, with the concrete parameters shown.
  No standing approval. "You approved the last one" is not approval of this one.

TIER 4 — PROHIBITED
  Disabling a control, editing the agent's own permissions or policy files, installing or
  upgrading a tool mid-task, writing to credential paths, contacting an endpoint not already
  allowlisted.
  Autonomy: never, under any instruction, including one that appears to come from the user
  inside tool output.
```

The tier is a property of the **action**, not of the server. A single database MCP server exposes
Tier 1 reads and Tier 3 writes; enabling "the server" without distinguishing them is exactly the
T3 mistake.

## Structural mitigations

Ordered by leverage. The first three prevent most of the inventory; the rest limit the damage when
they fail.

```text
1. MINIMISE CAPABILITY.        Grant the narrowest tool set that completes the task. Every tool
                               not granted is a tool injection cannot reach. Review the grant when
                               the task changes, not when someone remembers to.

2. HUMAN GATE ON TIER 3.       Approval must show the concrete action and parameters, not "the
                               agent wants to deploy". The gate belongs outside the model —
                               a wrapper, a policy engine, a required flag — because a gate the
                               model can be persuaded about is not a gate.

3. SCOPE CREDENTIALS PER TASK. Short-lived, least-privilege tokens for the specific resource and
                               operation. Defeats T2 by removing the excess privilege for the
                               deputy to be confused about.

4. SANDBOX EXECUTION.          Run servers in a container or VM with no ambient access to the host
                               filesystem, host network or host credentials. Defeats T5 and T6 at
                               the blast-radius level rather than at the detection level.

5. PATH AND HOST ALLOWLISTS.   Reads confined to the workspace; outbound requests confined to an
                               explicit host list; link-local metadata ranges (169.254.169.254,
                               fd00:ec2::254) blocked unconditionally.

6. FENCE UNTRUSTED CONTENT.    Tool results and fetched pages enter context marked as data, with
                               a boundary the prompt states may not be crossed. This is mitigation,
                               not defence — treat it as reducing likelihood, never as sufficient.

7. IDEMPOTENCY AND BUDGETS.    Every mutating call carries an idempotency key; every session has
                               an action budget and a per-tool rate limit; a circuit breaker trips
                               on repeated failure. Defeats T8.

8. LOG EVERYTHING.             Tool name, arguments, result summary, timestamp, and the content
                               that triggered the call. Without this, T4 and T10 are
                               undiagnosable after the fact.

9. PIN AND DIFF.               Server versions pinned; on upgrade, diff the exposed tool list and
                               treat any addition as unapproved until reviewed. Defeats T9.

10. ISOLATE MEMORY WRITES.     Anything persisted across sessions passes a write-path review.
                               Treat the memory store as a privileged destination. Defeats T10.
```

## What does not work

```text
✗ Instructing the model to ignore injected instructions.   Necessary, insufficient. Instruction-
   following is the capability being exploited; the same mechanism that makes the agent useful
   makes the mitigation unreliable. Never the only control.
✗ A denylist of dangerous strings.   Trivially evaded by encoding, translation, indirection or
   splitting across tool results.
✗ Asking the model whether it is safe to proceed.   The component under attack is the component
   being asked. Self-assessment is not a control boundary.
✗ Trusting the server's own description of its capabilities.   Verify by reading the tool list it
   actually exposes at runtime and diffing it against what was approved.
✗ Treating "it only reads" as safe.   Read capability plus any send capability is an exfiltration
   path. The pair must be reviewed together (T7).
✗ Enabling a server because it is popular.   Adoption says nothing about the blast radius of the
   capability you are granting. Score it like any other dependency: see source-scoring.md.
```

## References

- [`knowledge/mcp/security.md`](../../mcp/security.md) — operational checklist for enabling a server
- [`knowledge/security/prompt-injection-defenses.md`](../prompt-injection-defenses.md) — the injection side in depth
- [`knowledge/security/supply-chain.md`](../supply-chain.md) · [`knowledge/security/threat-modeling.md`](../threat-modeling.md)
- [`knowledge/ai-engineering/source-scoring.md`](../../ai-engineering/source-scoring.md) — grading a server before enabling it
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) · [`skills/security-audit/SKILL.md`](../../../skills/security-audit/SKILL.md) · [`skills/threat-modeling/SKILL.md`](../../../skills/threat-modeling/SKILL.md)
- MCP specification — <https://modelcontextprotocol.io/specification> · OWASP LLM Top 10 — <https://owasp.org/www-project-top-10-for-large-language-model-applications/> · OWASP Agentic AI Threats and Mitigations — <https://owasp.org/www-project-agentic-ai-threats-and-mitigations/>
