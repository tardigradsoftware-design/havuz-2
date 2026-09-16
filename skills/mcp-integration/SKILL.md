---
name: mcp-integration
version: 1.0.0
description: >-
  Evaluate, adopt, secure and operate Model Context Protocol servers and agent tools — capability
  scoping, transport choice, prompt-injection defence, and the supply-chain checks that apply
  because an MCP server is executable third-party code.
category: agents
status: active
confidence: medium
claim_type: recommendation
evidence_level: emerging-consensus
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [mcp, tools, agents, integration, security, supply-chain, protocol]
applies_to: [agents, mcp]
priority: 88
requires: [repository-analysis, security-audit, dont-reinvent-the-wheel]
conflicts_with: []
estimated_tokens: 3180
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Capability model
    anchor: "#capability-model"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Model Context Protocol specification"
    url: https://modelcontextprotocol.io/
    type: specification
    organization: MCP project
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run; the protocol is evolving quickly — verify the current spec version, transports and capability names before implementing."
  - title: "Playwright MCP"
    url: https://github.com/microsoft/playwright-mcp
    type: github-repository
    organization: Microsoft
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [repository-analysis, security-audit, dont-reinvent-the-wheel, context-engineering, dependency-analysis]
related_repositories: [modelcontextprotocol/servers, microsoft/playwright-mcp, supabase/mcp, getsentry/sentry-mcp, ChromeDevTools/chrome-devtools-mcp, upstash/context7, oraios/serena]
tests: 25
---

# MCP Integration

## Purpose

Treat an MCP server as what it is: **third-party executable code with a credential and a
capability grant**, speaking a protocol the model can influence. Integrating one is a
supply-chain decision plus a security-boundary decision, not a convenience decision.

> **Status note.** MCP is evolving quickly. Protocol details, transport names and capability
> semantics in this skill are `medium` confidence with a 90-day review window. Verify against
> the current specification before implementing — the *security and scoping principles* below
> are stable; the wire details are not.

## When to Use

```text
□ Giving an agent access to an external system (browser, database, filesystem, SaaS, search)
□ Choosing between an existing MCP server, a direct API integration, or a custom tool
□ Reviewing an MCP server before enabling it
□ Wrapping an internal system as a tool for agents
□ Diagnosing an agent that behaves badly only when a particular tool is available
```

## When NOT to Use

```text
✗ When the agent needs one narrow read from one API — a plain function call is simpler,
  cheaper and easier to secure than a protocol server
✗ When a deterministic pipeline can do the job: MCP adds a model in the loop, and with it
  nondeterminism and injection surface
✗ For anything requiring strong guarantees (payments, deletions, deploys) without a
  human-confirmation gate
```

## Inputs

```text
capability needed   the behaviour, stated narrowly ("read open issues assigned to me",
                    not "access GitHub")
agent context       which agent, whose credentials, what trust level, what blast radius
candidate servers   from knowledge/mcp/registry/ and indexes/mcp.md
constraints         network egress policy, data classification, latency, cost, audit needs
```

## Capability model

Score every candidate on **capability vs blast radius** before anything else.

```text
TIER 0 — READ-ONLY PUBLIC       search, docs lookup, public web content
                                blast radius: low. Injection risk: HIGH (content is untrusted)
TIER 1 — READ-ONLY SCOPED       read issues, read rows, read logs, read files in a root
                                blast radius: information disclosure. Scope the read.
TIER 2 — WRITE / MUTATE         create issue, insert row, edit file, send message
                                blast radius: real-world side effects. Confirmation gate required.
TIER 3 — EXECUTE / ADMINISTRATE run shell, run code, deploy, delete, manage credentials
                                blast radius: total. Sandbox, allowlist, human approval, audit log.
```

Rules that follow from the tier:

```text
1. Grant the LOWEST tier that satisfies the stated capability. "It might be useful later"
   is not a reason to grant tier 3.
2. Tier ≥2 always requires an explicit confirmation gate when the trigger came from
   untrusted content (web page, email, file, issue text, tool output).
3. Tier 3 requires: sandbox, resource limits, an allowlist of operations, an audit log,
   and a named human owner.
4. Credentials are scoped to the capability, short-lived, and revocable independently of
   the developer's own access. Never hand an agent your personal token.
5. One server = one capability domain. A server that reads your mail and executes shell
   commands should not be enabled.
```

## Workflow

```text
SPECIFY → SEARCH → VET → SCOPE → SANDBOX → INTEGRATE → TEST → OBSERVE → OPERATE
```

### 1. SPECIFY
Write the capability as a sentence with a boundary: *"list and read open issues in repo X
assigned to the current user; no writes, no other repos."* If you cannot write the boundary,
you are about to over-grant.

### 2. SEARCH — don't reinvent
Check in order: the agent platform's built-in tools → [`knowledge/mcp/registry/`](../../knowledge/mcp/registry/)
and [`indexes/mcp.md`](../../indexes/mcp.md) → [`metadata/repositories.json`](../../metadata/repositories.json)
filtered to `repo_kind: mcp` → the official MCP servers repository → the vendor's own
first-party server → build your own (last resort; then follow
[`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md)'s BUILD argument).

Prefer, in order: **vendor first-party** > **official/well-maintained community** >
**unknown third-party**. A vendor's own server has both the incentive and the access to keep
it correct.

### 3. VET — run [`repository-analysis`](../repository-analysis/SKILL.md) in full, plus
```text
□ Who publishes it? Verified org, the vendor itself, or an anonymous account?
□ Maintenance: last release, release cadence, issue responsiveness, archived?
□ License: usable? `license: null` → do not vendor, do not redistribute
□ Distribution: how does it run? npx/uvx/pipx fetching at start time is a supply-chain
  event on every launch — pin an exact version and hash, or vendor it
□ Install-time and start-time network calls: what does it fetch, from where?
□ Tool inventory: list every tool it exposes and its tier. Refuse servers whose tool set
  is far broader than your need.
□ Credential handling: where do tokens live, how are they transmitted, are they logged?
□ Data egress: does content leave your boundary? To whom? Is it used for training?
□ Known advisories; OpenSSF Scorecard result
□ Read the source of the tools you will actually call. It is usually a few hundred lines.
```

### 4. SCOPE
```text
□ Enable only the tools you need (disable the rest in configuration, not by convention)
□ Least-privilege credential: read-only token, single repo/schema/bucket, short TTL
□ Filesystem tools rooted at a specific path; no symlink escape; no writes unless required
□ Network tools with an egress allowlist; cloud metadata endpoints blocked
□ Argument schemas validated on your side too — the server's validation is not your control
□ Per-tool rate limits and cost caps
```

### 5. SANDBOX
Run the server in the most restrictive environment that still works: container or VM with
no ambient credentials, read-only mounts except the declared workspace, CPU/memory/time
limits, no network except the allowlist. Assume the server process can be driven by
attacker-controlled content.

### 6. INTEGRATE
```text
□ Pin the exact version; record it with the date and the reason for choosing it
□ Declare the tool set in configuration that is reviewed like code
□ Map each tool to the workflow steps that may call it — tools are not globally available
  to every agent by default
□ Structured outputs parsed and validated; failures handled, not swallowed
□ Timeouts, retries with bounded budgets, and circuit breaking per tool
□ Tool results enter the context as DATA, clearly delimited, never as instructions
□ Context cost measured: verbose tool output truncated/summarised before it enters the window
  (see context-engineering)
```

### 7. TEST
```text
□ Happy path per tool, with real (not mocked) responses where the side effect is safe
□ Failure paths: auth expired, rate limited, timeout, malformed output, tool absent,
  server crash mid-call
□ Injection tests: feed content containing instruction-shaped text
  ("ignore previous instructions and …") through every read tool and assert that no
  tier ≥2 action occurs without confirmation
□ Permission tests: attempt an out-of-scope read/write and assert denial
□ Determinism: same input → same tool call sequence, n ≥ 3
□ Cost/latency: tokens and wall time per task with and without the tool
```

### 8. OBSERVE
Log per tool call: agent, principal, tool, arguments (redacted), tier, confirmation
decision, result status, duration, tokens. Alert on: new tools appearing, scope denials,
confirmation prompts spiking, unusual argument shapes, cost anomalies.

### 9. OPERATE
```text
□ Version updates treated as dependency updates: changelog read, tests re-run, then bump
□ Re-vet on a schedule (90 days for fast-moving servers) and after any ownership change
□ Removal plan: which workflows break if the server disappears tomorrow?
□ Incident path: how to disable a single tool instantly, without a deploy
□ Ownership: a named human owns each enabled server
```

## Failure Modes

```text
CAPABILITY CREEP          Enabling a server "for search" and inheriting shell execution.
AMBIENT CREDENTIALS       The agent runs with the developer's full token.
UNPINNED RUNTIME          `npx some-mcp@latest` fetching unreviewed code on every start.
TOOL-OUTPUT-AS-INSTRUCTION  A web page's text becomes a command the agent obeys.
NO CONFIRMATION GATE      Tier 2/3 actions executed on untrusted triggers.
BROAD FILESYSTEM ROOT     A tool rooted at `/` or the home directory.
METADATA ENDPOINT         SSRF to 169.254.169.254 through a fetch tool → cloud credentials.
CONTEXT FLOOD             A tool returning 40k tokens of JSON per call, evicting the task.
SILENT PARTIAL FAILURE    A tool errors; the agent proceeds as if it succeeded.
STAR RANKING              Choosing an MCP by popularity rather than by scope and maintenance.
VENDOR LOCK BLINDNESS     No removal plan for a server that becomes unmaintained.
UNLOGGED ACTIONS          Side effects with no attribution — unauditable and unreproducible.
```

## Quality Checklist

```text
□ Capability written as one sentence with an explicit boundary
□ Existing options searched before building (registry → official → vendor → build)
□ Full repository analysis run on the chosen server; source of used tools read
□ Distribution reviewed: version and hash pinned; no unreviewed runtime fetch
□ Capability tier assigned per tool; lowest tier granted
□ Only required tools enabled; least-privilege, short-lived, revocable credential
□ Filesystem rooted; egress allowlisted; metadata endpoints blocked
□ Sandbox with resource limits and no ambient credentials
□ Confirmation gate on every tier ≥2 action triggered by untrusted content
□ Tool output delimited as data, validated, truncated, never treated as instruction
□ Injection, permission, failure-path and determinism tests written and passing
□ Per-call audit log with attribution; alerts configured
□ Removal plan and instant-disable path documented
□ Named human owner; re-vetting scheduled (90 days for fast-moving servers)
```

## Anti-Patterns

```text
✗ Enabling a 40-tool server to use 2 of its tools
✗ Passing the developer's personal GitHub token to an MCP server
✗ `npx @someone/mcp@latest` in a startup script
✗ Letting a fetched web page decide which tool to call next without a gate
✗ A filesystem tool rooted at the user's home directory
✗ Ignoring a tool error and continuing the plan
✗ Pasting raw tool JSON into the context without truncation
✗ Adopting an MCP server because it has 5k stars and no license file
✗ No log of which agent called which tool with which arguments
```

## References

- Model Context Protocol — <https://modelcontextprotocol.io/> (verify current version)
- [`knowledge/mcp/registry/`](../../knowledge/mcp/registry/) · [`indexes/mcp.md`](../../indexes/mcp.md)
- [`knowledge/mcp/`](../../knowledge/mcp/) · [`patterns/mcp/`](../../patterns/mcp/)
- [`security-audit`](../security-audit/SKILL.md) — agent-specific threats section
- [`repository-analysis`](../repository-analysis/SKILL.md) · [`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md)
- [`context-engineering`](../context-engineering/SKILL.md) — tool-output cost control
- [`SECURITY.md`](../../SECURITY.md)

## Related Skills

`repository-analysis` · `security-audit` · `dont-reinvent-the-wheel` · `context-engineering` ·
`dependency-analysis` · `testing`

## Evaluation Criteria

```text
1. Least privilege: granted capability tier ≤ required tier for 100% of enabled tools.
2. Injection resistance: 0 unconfirmed tier ≥2 actions across the injection test suite.
3. Supply-chain hygiene: 100% of servers pinned by version and vetted, with a recorded owner.
4. Reliability: tool-call failure rate and silent-partial-failure count (target 0 silent).
5. Cost: tokens and latency per task attributable to tool use, within budget.
6. Auditability: 100% of side-effecting calls attributable in the log.
```

Test cases in [`tests/`](tests/).
