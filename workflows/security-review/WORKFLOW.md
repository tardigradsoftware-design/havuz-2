---
name: security-review
version: 1.0.0
description: >-
  Threat-model, audit and remediate — covering application code, data flows, supply chain, CI/CD and
  the agent/tool/MCP surface that conventional checklists miss, with every finding backed by a
  concrete exploit path.
trigger: >-
  Before any release touching auth, sessions, payments, PII, file upload or admin surfaces; when
  adding an agent, tool integration, MCP server or any code-execution path; when adding a dependency
  that runs at install time; after a security incident; and periodically on production systems.
not_for: >-
  Code with no attack surface (a local script with no external inputs) — record that and skip; as a
  substitute for an authorised penetration test where one is contractually required; as a way to
  generate a long list of theoretical findings, which produces alert fatigue and hides the real issue.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [security, threat-model, audit, supply-chain, agents, workflow, compliance]
confidence: high
claim_type: recommendation
evidence_level: cross-checked
estimated_duration: half a day for a focused change review; days for a full system audit
stages:
  - id: 1
    name: Scope and classify
    goal: Establish what is in scope, what data is involved, and who benefits from breaking it.
    skill: security-audit
    agent: security-reviewer
    inputs: [system description, data classification, compliance scope, deployment topology]
    outputs: [scope statement, data classification map, threat-actor list, compliance obligations]
    exit_gate: Every entry point is enumerated — HTTP routes, webhooks, queues, uploads, CLI, agent tools, MCP servers, CI, admin UI — and every data class is mapped to where it is stored, processed and logged.
    on_gate_failure: Widen the enumeration. A missed entry point is a missed finding, and the miss is invisible in the report.
  - id: 2
    name: Threat model
    goal: Diagram data flows, mark trust boundaries, apply STRIDE per boundary and rank the resulting threats.
    skill: security-audit
    inputs: [scope statement, data classification map, architecture documentation]
    outputs: [data-flow diagram with trust boundaries, STRIDE enumeration per boundary, ranked threat list with expected controls]
    exit_gate: Every trust boundary has a STRIDE pass, and every retained threat names the control expected to mitigate it — the audit then checks whether that control exists, is correct, and cannot be bypassed.
    max_loops: 2
    on_gate_failure: Return to stage 1; an incomplete boundary map produces an incomplete threat list.
  - id: 3
    name: Read the code
    goal: Audit injection and input handling, authn and sessions, authz at object and function level, secrets and configuration, data protection, and availability and abuse.
    skill: security-audit
    inputs: [codebase or diff, ranked threat list, expected controls]
    outputs: [findings with file:line locations, conditions and evidence per checklist area]
    exit_gate: Every checklist area has been grepped across the whole codebase rather than sampled, and each item either cites a location or records "not present".
    max_loops: 3
    on_gate_failure: Complete the sweep. A sampled audit reports the defects it happened to look at.
  - id: 4
    name: Supply chain
    goal: Review dependencies, build and CI/CD for the risks that live outside the application code.
    skill: dependency-analysis
    inputs: [lockfiles, dependency graph, CI workflows, registry configuration, container images]
    outputs: [advisory triage at resolved versions with reachability, install-time script review, provenance and signing status, CI credential posture, license risk]
    exit_gate: Advisories are triaged at the RESOLVED version with a reachability judgement, install-time scripts are reviewed or disabled, CI credentials are least-privilege and short-lived, and no workflow grants production access to pull-request code.
    max_loops: 2
    on_gate_failure: Block the release for unresolved critical advisories with a reachable path; record accepted risks with owner, expiry and compensating control.
  - id: 5
    name: Agent, tool and MCP surface
    goal: Audit the attack surface that conventional checklists miss, whenever agents or tool integrations exist.
    skill: mcp-integration
    inputs: [agent inventory, tool and MCP configuration, credential scopes, capability grants]
    outputs: [per-tool capability tier, injection test results, permission test results, egress and filesystem boundary verification, audit-log attribution check]
    exit_gate: Every tool has an assigned capability tier at or below what its use requires; filesystem tools are rooted; egress is allowlisted with cloud metadata endpoints blocked; tier-2-or-above actions require confirmation when triggered by untrusted content; and every side-effecting call is attributable in a log.
    max_loops: 2
    on_gate_failure: Disable the over-scoped tool. Capability creep is not mitigated by documentation.
  - id: 6
    name: Injection and abuse testing
    goal: Attempt the attacks the threat model predicts, in an authorised environment only.
    skill: security-audit
    inputs: [ranked threats, test environment, written authorisation]
    outputs: [test results per threat, with reproduction steps for anything that succeeded]
    exit_gate: Every high-ranked threat has been exercised in an environment the reviewer is authorised to test, and results are recorded whether they confirm or refute the control.
    max_loops: 2
    on_gate_failure: Do not test. Escalate for authorisation, or convert the item into a code-reading finding with its limitation stated. Testing a third-party system without authorisation is prohibited by this workflow.
  - id: 7
    name: Grade and report
    goal: Rank findings by exploitability times blast radius, each with a standard reference, a remediation and a verification test.
    skill: security-audit
    agent: security-reviewer
    inputs: [all findings from stages 3-6]
    outputs: [findings report — severity, location, condition, exploit path, impact, standard, remediation with code sketch, verification test]
    exit_gate: Every finding above INFO has a concrete exploit path, severity is derived from exploitability times blast radius rather than from category prestige, and every finding names the test that proves its remediation.
    max_loops: 2
    on_gate_failure: Downgrade findings without an exploit path to INFO and state why. Eighty theoretical findings hide the one that matters.
  - id: 8
    name: Remediate
    goal: Fix in severity order, using trusted implementations rather than hand-rolled primitives.
    inputs: [findings report, release schedule]
    outputs: [remediation commits, one per finding or per coherent group, each referencing the finding]
    exit_gate: All CRITICAL findings are fixed before release; HIGH findings are fixed or carry an accepted-risk entry with owner, expiry and compensating control; no security primitive is hand-rolled.
    max_loops: 3
    on_gate_failure: Block the release for unfixed CRITICAL findings, or escalate for a written risk acceptance. Never hand-roll crypto, token signing, password storage or payment flows — adopt or escalate.
  - id: 9
    name: Verify remediation
    goal: Run each finding's verification test and confirm the failure mode is now impossible rather than merely unlikely.
    skill: testing
    agent: qa-engineer
    inputs: [remediation commits, verification tests]
    outputs: [verification results per finding, added regression tests, re-scan results]
    exit_gate: Every remediated finding's verification test passes, regression tests are committed, and a re-scan of the affected area produces no new findings.
    max_loops: 2
    on_gate_failure: Reopen the finding. A claimed fix that was not verified is not a fix.
  - id: 10
    name: Harden and record
    goal: Close the systemic gaps the findings revealed and make the audit repeatable.
    skill: security-audit
    agent: skill-curator
    inputs: [findings, root causes, accepted risks]
    outputs: [CI security gates, lint rules for the defect classes found, threat-model update, failure-modes entries, accepted-risk register, next-audit date]
    exit_gate: Each defect class that produced a finding has a preventive gate in CI or in lint, the threat model reflects the current system, accepted risks are registered with expiry dates, and the next audit is scheduled.
    on_gate_failure: File at minimum the accepted-risk register and the next-audit date; a finding fixed without a gate will recur.
quality_gates:
  - Threat model drawn with trust boundaries before any code was read.
  - STRIDE applied per boundary; every retained threat names its expected control.
  - All entry points enumerated, including agent tools, MCP servers and CI.
  - Code swept across all seven checklist areas, whole-codebase rather than sampled.
  - Advisories triaged at resolved versions with a reachability judgement.
  - Install-time scripts reviewed; CI credentials least-privilege; no PR code with production access.
  - Agent/tool/MCP surface audited whenever it exists, with capability tiers assigned.
  - No unauthorised testing of any third-party system, at any stage.
  - 100% of findings above INFO carry a concrete exploit path.
  - Severity from exploitability times blast radius, never from category prestige.
  - Every finding has a remediation and a verification test; remediations are verified.
  - No security primitive hand-rolled anywhere in the remediation.
  - Secret scanning covers git history, not only the working tree.
  - Accepted risks recorded with owner, expiry and compensating control.
  - No leaked system prompts, private model internals or proprietary weights used, vendored or reproduced.
artifacts:
  - scope and data classification map
  - threat model with STRIDE enumeration and ranked threats
  - code-audit findings per checklist area
  - supply-chain and CI/CD report
  - agent/tool/MCP capability and injection test report
  - graded findings report with remediations and verification tests
  - accepted-risk register
  - CI security gates and lint rules added
  - next-audit date
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "OWASP Top Ten"
    url: https://owasp.org/www-project-top-ten/
    type: standard
    organization: OWASP
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run; confirm the current edition before citing specific item IDs."
  - title: "OWASP ASVS"
    url: https://owasp.org/www-project-application-security-verification-standard/
    type: standard
    organization: OWASP
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "NIST AI Risk Management Framework"
    url: https://www.nist.gov/itl/ai-risk-management-framework
    type: standard
    organization: NIST
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run; verify current version before quoting control identifiers."
related: [skills/security-audit/SKILL.md, agents/security-reviewer/AGENT.md, SECURITY.md, patterns/security/]
---

# Workflow: Security Review

```text
1 SCOPE → 2 THREAT MODEL → 3 READ THE CODE → 4 SUPPLY CHAIN → 5 AGENT/MCP SURFACE
  → 6 TEST (authorised only) → 7 GRADE → 8 REMEDIATE → 9 VERIFY → 10 HARDEN
```

## Two rules that override everything

```text
1. NO UNAUTHORISED TESTING.  Stage 6 requires written authorisation for the environment under
   test. If it is absent, the stage is skipped and the item becomes a code-reading finding with
   its limitation stated. "It was technically possible" is not permission.
2. NO HAND-ROLLED PRIMITIVES.  Crypto, token signing, password storage and payment flows are
   adopted from trusted implementations or escalated to a human. Stage 8 refuses to merge a
   hand-rolled one, however correct it looks.
```

## Why the threat model comes first

Reading code without a threat model produces a checklist report: everything that could
theoretically go wrong, ranked by how scary the category sounds. Modelling the boundaries first
produces the opposite: a short list of controls that must exist, each checked for existence,
correctness and bypassability. The second list finds the defects that matter.

## Scaling the workflow

```text
CHANGE REVIEW (per PR)   stages 3, 4 (diff scope), 7, 9 — the full audit runs on a schedule
PRE-RELEASE              all stages, scoped to the release's attack surface
FULL SYSTEM AUDIT        all stages, all entry points, with stage 6 under authorisation
AGENT-ONLY REVIEW        stages 1, 2, 5, 7, 8, 9, 10 — the agent surface is the system
POST-INCIDENT            stages 1, 2, 6, 7, 8, 9, 10 plus a post-mortem; the preventive half
                         of the incident response
```

## Failure modes specific to this workflow

```text
CHECKLIST THEATRE      Items marked complete with no file:line evidence anywhere in the report.
SCANNER AS AUDIT       SAST and dependency output pasted as findings. Scanners cannot see logic
                       or authorisation defects, which are the majority of real incidents.
AGENT BLINDNESS        The web app audited while the agent with shell access and a broad
                       credential is not — stage 5 skipped because "it's just a tool".
THEORETICAL FLOOD      Eighty LOW findings and one buried CRITICAL. Exploit path or INFO.
FIX WITHOUT PROOF      Stage 9 skipped under release pressure; the finding recurs.
NO GATE                Stage 10 skipped; the same defect class returns in the next release.
LEAKED MATERIAL        Citing a publicly reachable leaked prompt or private weight as evidence.
                       Prohibited by policy regardless of reachability — see SECURITY.md.
```

## References

- [`skills/security-audit/SKILL.md`](../../skills/security-audit/SKILL.md) — the full checklist
- [`skills/dependency-analysis/SKILL.md`](../../skills/dependency-analysis/SKILL.md) · [`skills/mcp-integration/SKILL.md`](../../skills/mcp-integration/SKILL.md)
- [`agents/security-reviewer/AGENT.md`](../../agents/security-reviewer/AGENT.md)
- [`SECURITY.md`](../../SECURITY.md) — policy, including the leaked-material exclusion
- [`patterns/security/`](../../patterns/security/) · [`knowledge/security/`](../../knowledge/security/)
- OWASP Top Ten · OWASP ASVS · OWASP Cheat Sheets · OpenSSF Scorecard · NIST AI RMF
