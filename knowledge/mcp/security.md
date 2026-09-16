---
id: mcp-security
title: "MCP server security: the operational checklist for enabling one"
domain: mcp
summary: >-
  The pre-enablement review for an MCP server — publisher verification, source review, capability enumeration, credential scoping, sandboxing and logging — plus the runtime controls that keep a granted capability from becoming an incident.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [mcp, security, tool-use, capabilities, sandboxing, credentials, supply-chain, checklist]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/security/mcp-security/mcp-threat-model.md, knowledge/security/supply-chain.md]
sources:
  - title: "Model Context Protocol specification"
    url: https://modelcontextprotocol.io/specification
    type: specification
    organization: MCP maintainers
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Defines the transport, capability negotiation and tool/resource/prompt primitives this checklist is framed against."
---
# MCP Server Security — Operational Checklist

Companion to [`knowledge/security/mcp-security/mcp-threat-model.md`](../security/mcp-security/mcp-threat-model.md),
which explains the threats and defines the capability tiers. This file is the procedure: what to do
before enabling a server, and what to keep running afterwards.

## Before enabling

```text
□ IDENTIFY THE PUBLISHER.    Who maintains it, are they the canonical owner of the underlying service,
                             is the org verified, how long has it existed. A server named after a
                             well-known product and published by an account created last month is the
                             typosquat case.
□ READ THE SOURCE.           It runs locally with your file and network access. Reviewing it is not
                             optional because it is small — it is possible because it is small. Look
                             for: outbound requests to unexpected hosts, filesystem access outside the
                             stated scope, install scripts, obfuscated code, dynamic evaluation,
                             credential reads.
□ SCORE IT LIKE A DEPENDENCY. License, archived status, pushed_at, CI, tests, issue history. license:
                             null means do-not-redistribute; archived means do-not-depend. See
                             knowledge/ai-engineering/source-scoring.md.
□ PIN THE VERSION.           Exact version plus a lockfile with an integrity hash. Never "latest" for
                             something that executes locally.
□ ENUMERATE THE ACTUAL TOOLS. Start it, list the tools and resources it exposes at runtime, and diff
                             that against the documentation. The runtime surface is the attack surface;
                             the documentation is marketing.
□ ASSIGN A TIER PER TOOL.    Not per server. Read-only public, read-only private, reversible write,
                             irreversible/external write, prohibited. A database server exposes Tier 1
                             reads and Tier 3 writes; enabling "the server" without distinguishing them
                             is the capability-grant mistake.
□ SCOPE THE CREDENTIALS.     Least privilege, for the specific resource and operation, ideally
                             short-lived. Never a standing admin token; never your personal credential.
□ DECIDE THE SANDBOX.        Container or VM with no ambient host filesystem, no host network, no host
                             credentials. Egress allowlisted to the hosts the server legitimately needs.
□ CONFIGURE LOGGING.         Tool name, arguments, result summary, timestamp, and the content that
                             triggered the call. If you cannot reconstruct what happened, you cannot
                             respond to an incident.
□ WRITE THE APPROVAL RULE.   Which tiers require a human, who approves, and where the gate is enforced
                             — outside the model.
```

## At runtime

```text
□ PATH ALLOWLISTS.     Reads confined to the workspace. Deny ~/.ssh, ~/.aws, .env, credential stores
                       and anything outside the declared scope.
□ HOST ALLOWLISTS.     Outbound only to declared hosts. Block link-local metadata ranges
                       unconditionally (169.254.169.254, fd00:ec2::254).
□ ACTION BUDGETS.      Per-session and per-tool limits on mutating calls, with a circuit breaker on
                       repeated failure. Bounds an injection-driven loop.
□ IDEMPOTENCY KEYS.    On every mutating call, so a retry does not double-apply.
□ FENCE TOOL RESULTS.  Content returned by a tool enters context marked as data. Mitigation, not
                       defence — never the only control.
□ WATCH FOR SCOPE DRIFT. On upgrade, re-enumerate the tool list and diff it. A new tool is unapproved
                       until someone approves it.
□ ISOLATE DURABLE WRITES. Anything persisted across sessions — memory, config, a knowledge file —
                       passes a write-path review. Memory poisoning is a persistent compromise, not a
                       transient one.
□ ISOLATE PER PRINCIPAL. Never share one server process across users, tenants or trust domains.
```

## The three questions that catch most mistakes

```text
1. WHAT IS THE WORST THING THIS SERVER CAN DO WITH THE CREDENTIALS I AM ABOUT TO GIVE IT?
   Write it down. If the answer is unacceptable, the grant is wrong — not the prompt, not the model.

2. IF AN INJECTION FULLY CONTROLS THE MODEL FOR ONE TURN, WHAT DOES THIS SERVER ENABLE?
   Assume the injection succeeds. Enumerate reachable tools and their worst-case arguments. Anything
   irreversible must sit behind a human gate the model cannot satisfy alone.

3. CAN I TELL, AFTERWARDS, WHAT IT DID?
   If the audit log cannot answer this, logging is the missing control — and the cheapest one here.
```

## Anti-patterns

```text
✗ Enabling a server because one feature needs one tool.  You granted the whole surface.
✗ Trusting the README's capability list.                 Enumerate at runtime.
✗ Running it with your own credentials.                  Everything you can do is now reachable by
  injection.
✗ "It's read-only, so it's safe."                        Read plus any send path is exfiltration.
✗ Auto-upgrading.                                        The tool list can change silently.
✗ Installing from a recalled package name.               Verify the canonical publisher; typosquats
  here are plausible-sounding.
✗ Treating a high star count as a security property.      Adoption measures attention.
✗ No logging because "nothing sensitive happens here."    You do not know that until you can see it.
```

## References

- [`../security/mcp-security/mcp-threat-model.md`](../security/mcp-security/mcp-threat-model.md) — threat inventory and tier definitions
- [`../security/prompt-injection-defenses.md`](../security/prompt-injection-defenses.md) · [`../security/supply-chain.md`](../security/supply-chain.md) · [`../security/threat-modeling.md`](../security/threat-modeling.md)
- [`../ai-engineering/source-scoring.md`](../ai-engineering/source-scoring.md) — grading a server before enabling it
- [`skills/mcp-integration/SKILL.md`](../../skills/mcp-integration/SKILL.md) · [`skills/security-audit/SKILL.md`](../../skills/security-audit/SKILL.md) · [`skills/threat-modeling/SKILL.md`](../../skills/threat-modeling/SKILL.md)
- [`registry/`](registry/) · [`patterns/mcp/`](../../patterns/mcp/) · [`anti-patterns/`](../../anti-patterns/)
- MCP specification — <https://modelcontextprotocol.io/specification> · OWASP Agentic AI Threats and Mitigations — <https://owasp.org/www-project-agentic-ai-threats-and-mitigations/>
