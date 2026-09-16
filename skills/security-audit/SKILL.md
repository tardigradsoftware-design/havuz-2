---
name: security-audit
version: 1.0.0
description: >-
  Structured security review of application code, agent systems, dependencies and data flows —
  with findings graded by exploitability and blast radius, and every recommendation traceable to a
  named standard.
category: security
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [security, audit, threat-model, owasp, supply-chain, agents, review]
applies_to: [any]
priority: 95
requires: [evidence-validation, code-review]
conflicts_with: []
estimated_tokens: 3257
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Threat model
    anchor: "#threat-model"
    purpose: implementation
  - heading: Audit checklist
    anchor: "#audit-checklist"
    purpose: checklist
  - heading: Agent-specific threats
    anchor: "#agent-specific-threats"
    purpose: implementation
  - heading: Severity model
    anchor: "#severity-model"
    purpose: decision
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "OWASP Top Ten"
    url: https://owasp.org/www-project-top-ten/
    type: standard
    organization: OWASP
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run; confirm the current edition year before citing specific item IDs."
  - title: "OWASP ASVS — Application Security Verification Standard"
    url: https://owasp.org/www-project-application-security-verification-standard/
    type: standard
    organization: OWASP
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
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
related_skills: [code-review, dependency-analysis, evidence-validation, testing, api-design]
related_repositories: [ossf/scorecard, aquasecurity/trivy, protectai/rebuff, semgrep/semgrep]
tests: 21
---

# Security Audit

## Purpose

Find the defects that matter, in the order they matter, with a recommendation an engineer
can execute today. A security audit is not a list of everything that could theoretically go
wrong; it is a ranked set of **exploitable** conditions in **this** system, each mapped to a
control from a named standard.

Two rules that override everything else in this skill:

```text
1. Never hand-roll a security primitive. Escalate or adopt (see dont-reinvent-the-wheel).
2. Never publish, vendor or train on leaked system prompts, private model internals or
   proprietary weights. This repository excludes such material by policy
   (see SECURITY.md and knowledge/security/).
```

## When to Use

```text
□ Before any release that touches auth, sessions, payments, PII, file upload or admin surfaces
□ Adding an agent, tool integration, MCP server or any code-execution path
□ Adding a dependency, especially one that runs at install time
□ After an incident, as the preventive half of the post-mortem
□ Periodically on production systems (recommended: per major release + quarterly)
□ When exposing an internal service to a broader network
```

## When NOT to Use

```text
✗ As a substitute for a penetration test on a system where one is required
✗ On code with no attack surface (a pure local script with no inputs) — say so and skip
✗ To generate a long list of theoretical findings with no exploitability analysis:
  that produces alert fatigue and hides the real issue
```

## Inputs

```text
system description   components, data flows, trust boundaries, deployment topology
data classification  what is public / internal / confidential / regulated (PII, PHI, PCI)
attack surface       every entry point: HTTP routes, queues, webhooks, file uploads,
                     CLI, agent tools, MCP servers, CI, package registry, admin UI
identity model       who and what authenticates; how authorisation is decided
threat actors        who benefits from breaking this, and with what resources
compliance scope     obligations that apply (GDPR, HIPAA, PCI DSS, SOC 2 …)
```

## Threat model

Do this before reading code. Ten minutes here saves hours of unfocused grepping.

```text
1. DIAGRAM the data flows and mark every TRUST BOUNDARY (user→app, app→db, service→service,
   agent→tool, tool→filesystem, CI→registry).
2. For each boundary, enumerate what crosses it and whether it is validated.
3. Apply STRIDE per boundary:
     Spoofing            can the actor be impersonated? (authn)
     Tampering           can data in transit or at rest be modified? (integrity)
     Repudiation         can actions be denied? (audit log completeness)
     Information disclosure  can secrets/PII leak? (logging, errors, responses)
     Denial of service   can the resource be exhausted? (rate limits, quotas, timeouts)
     Elevation of privilege  can a role be exceeded? (authz checks per operation)
4. Rank threats by (likelihood × impact) and keep the top N as the audit scope.
5. For each retained threat, write the expected CONTROL. The audit is then a check of
   whether the control exists, is correct, and cannot be bypassed.
```

## Audit checklist

### Injection & input handling
```text
□ Every SQL/NoSQL/LDAP/OS-command/LDAP/path/query uses parameterised or allowlisted construction
□ No string concatenation into a query anywhere (grep, do not sample)
□ Output encoding matched to context: HTML, attribute, JS, URL, CSS — each different
□ File paths validated against an allowlist root; no user-controlled traversal; symlinks refused
□ Deserialisation of untrusted data disabled or type-restricted
□ Template injection: user input never reaches a template compiler or eval-like function
□ SSRF: outbound URLs validated against an allowlist; metadata endpoints (169.254.169.254) blocked
□ Regex DoS: no unbounded nested quantifiers on user input
```

### Authentication & sessions
```text
□ Password storage via a memory-hard KDF (Argon2id / scrypt) with per-user salt — never MD5/SHA1/bcrypt-truncated
□ MFA available for privileged accounts; recovery codes handled safely
□ Session identifiers high-entropy, rotated on privilege change, server-side revocable
□ Cookie flags: Secure, HttpOnly, SameSite appropriate to the flow
□ Token expiry, audience, issuer and signature all verified — not just the signature
□ Password reset and email-change tokens single-use, short-lived, and non-enumerable
□ Rate limiting on auth endpoints; lockout that does not itself enable DoS
□ No credential in URLs, logs, error messages, or client-side storage
```

The full detail — every entry with its detection rule, severity and fix direction — lives in [`references/audit-checklist.md`](references/audit-checklist.md). Load it when this step is reached rather than keeping it in context for the whole run.

## Agent-specific threats

Agent systems add attack surface that traditional checklists miss. Audit these explicitly:

```text
PROMPT INJECTION (direct and indirect)
  □ Untrusted content (web pages, emails, files, tool output, issue text) is never
    treated as instruction. It is data, and it is delimited as data.
  □ High-risk actions (send, delete, pay, deploy, execute, exfiltrate) require explicit
    human confirmation when the trigger came from untrusted content.
  □ Tool output is not re-interpreted as a system-level directive.

TOOL / MCP ABUSE
  □ Each tool has a documented capability and the narrowest scope that satisfies it.
  □ Filesystem tools are rooted and allowlisted; no path escape; no symlink following
    outside the root.
  □ Network tools have an egress allowlist; cloud metadata endpoints blocked.
  □ Execution tools are sandboxed, resource-limited, and time-limited.
  □ MCP servers are treated as third-party dependencies: identity, license, maintenance
    and CVE status checked before adoption (see knowledge/mcp/registry/).
  □ Credentials handed to tools are scoped, short-lived and revocable.

PERMISSION & IDENTITY
  □ The agent runs with least privilege, never the developer's full credentials.
  □ Actions are attributable: an audit log records which agent, which tool, which
    arguments, which principal, and the outcome.
  □ No ambient authority: an agent acting on a user's behalf cannot exceed that user's
    permissions (confused-deputy check on every tool call).

DATA EXFILTRATION
  □ Outbound channels are enumerated; secrets and PII cannot reach a model provider,
    a log aggregator, or a web request without a recorded decision.
  □ Redaction applied before logging model I/O.

MEMORY POISONING
  □ Long-term memory writes are validated and attributable; a poisoned memory cannot
    silently alter future behaviour.
  □ Memory content is treated as untrusted input when re-read.

OUTPUT INTEGRITY
  □ Generated code passes the same review, tests and scanning as human code.
  □ Generated content that reaches users is sanitised (it can carry injection payloads).

RESOURCE EXHAUSTION
  □ Loop, depth and cost caps on every agent; a runaway agent cannot exhaust budget.
```

## Severity model

Grade on **exploitability × blast radius**, not on how scary the category sounds.

```text
CRITICAL   unauthenticated remote exploitation, or leads to full system/tenant compromise,
           data exfiltration at scale, or RCE.            → fix before ship; block release
HIGH       authenticated exploitation with broad impact, or unauthenticated with narrow
           impact; secret exposure; authz bypass.          → fix this sprint
MEDIUM     requires specific conditions or a privileged actor; meaningful but bounded impact.
                                                                → scheduled fix
LOW        defence-in-depth gap; no demonstrated exploit path.  → backlog
INFO       hardening suggestion; not a defect.               → optional
```

Every finding is reported as:

```markdown
### [SEVERITY] <title>
- Location: <file:line / endpoint / component>
- Condition: <what is true today>
- Exploit path: <concrete steps an attacker takes — no path means downgrade to INFO>
- Impact: <what the attacker gains; whose data; what breaks>
- Standard: <OWASP / ASVS / CWE reference>
- Remediation: <the specific change, with a code sketch where useful>
- Verification: <the test or check that proves it is fixed>
- Accepted risk: <if not fixed — who accepted, until when, with what compensating control>
```

A finding without an exploit path is not a finding. Downgrade it and say why.

## Failure Modes

```text
CHECKLIST THEATRE     Marking items without reading the code. Fix: cite file:line per item.
THEORETICAL FLOOD     80 LOW findings hiding 1 CRITICAL. Fix: exploitability required.
SCANNER AS AUDIT      Treating SAST/dependency output as the answer. Fix: triage every hit.
FALSE NEGATIVE COMFORT "The scanner found nothing." Scanners miss logic and authz bugs —
                      the majority of real incidents.
SCOPE DRIFT           Auditing the framework instead of the application's use of it.
HISTORY BLINDNESS     Checking the working tree but not git history for secrets.
AGENT BLINDNESS       Auditing the web app and ignoring the agent that can execute code.
FIX WITHOUT PROOF     Remediation claimed, never verified by the stated test.
```

## Quality Checklist

```text
□ Threat model drawn with trust boundaries before code was read
□ STRIDE applied per boundary; retained threats have an expected control
□ Injection, authn, authz, secrets, data, supply chain and availability checklists run
□ Agent/tool/MCP threats audited if any agent or tool integration exists
□ Every finding has location, condition, exploit path, impact, standard, remediation, verification
□ Severity assigned from exploitability × blast radius, not from category
□ Findings ranked; CRITICAL blocks release
□ Secret scanning includes git history
□ Dependency and CI/CD supply chain reviewed, including install-time scripts
□ Accepted risks recorded with owner, expiry and compensating control
□ Remediations re-verified with the stated test
□ No security primitive hand-rolled; escalation used where one was needed
```

## Anti-Patterns

```text
✗ Client-side "admin only" rendering as an authorisation control
✗ `WHERE user_id = ?` present on one query and absent on its three siblings
✗ A JWT verified for signature but not for `exp`, `aud` or `iss`
✗ `verify=False` "temporarily" in production HTTP clients
✗ Secrets in `.env` committed to the repository, then deleted in a later commit
✗ Logging the full request body on an auth endpoint
✗ An agent with `shell: true` and no allowlist, triggered by inbound email content
✗ A wildcard CORS origin combined with credentialed requests
✗ "We use a framework, so injection is impossible"
✗ Vendoring a leaked system prompt as a research reference
```

## References

- OWASP Top Ten — <https://owasp.org/www-project-top-ten/>
- OWASP ASVS — <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Cheat Sheets — <https://cheatsheetseries.owasp.org/>
- OpenSSF Scorecard — <https://github.com/ossf/scorecard> (Apache-2.0, verified 2026-09-15)
- NIST AI RMF — <https://www.nist.gov/itl/ai-risk-management-framework>
- [`SECURITY.md`](../../SECURITY.md) — this repository's policy, including the leaked-prompt exclusion
- [`workflows/security-review/`](../../workflows/security-review/) · [`patterns/security/`](../../patterns/security/)
- [`anti-patterns/`](../../anti-patterns/) · [`knowledge/security/`](../../knowledge/security/)
- [`dependency-analysis`](../dependency-analysis/SKILL.md) · [`mcp-integration`](../mcp-integration/SKILL.md)

## Related Skills

`code-review` · `dependency-analysis` · `evidence-validation` · `testing` · `api-design` ·
`mcp-integration` · `deployment`

## Evaluation Criteria

```text
1. Recall against a seeded-defect benchmark: fraction of planted vulnerabilities found
   (target ≥ 0.8 for CRITICAL/HIGH).
2. Precision: fraction of reported findings confirmed real by a human reviewer (target ≥ 0.7).
3. Exploit-path completeness: 100% of findings include a concrete exploit path or are downgraded.
4. Actionability: a developer can implement the remediation without further questions.
5. Agent coverage: if tools/MCP exist, 100% of the agent-specific section is audited.
6. Time to first CRITICAL finding — earlier is better.
```

Test cases in [`tests/`](tests/).
