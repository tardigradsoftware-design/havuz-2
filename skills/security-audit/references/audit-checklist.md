---
id: audit-checklist
title: "The full application security audit checklist by control area"
domain: security
summary: >-
  The complete audit checklist across injection, authentication, authorisation, secrets, data, supply chain and availability, extracted from the skill so the skill body stays inside its context budget.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [reference, security]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [security-audit]
---

# The full application security audit checklist by control area

Reference material for [`security-audit`](../SKILL.md), extracted so the skill body stays
within its context budget. Load this file only when the step that needs it is reached.


## Injection & input handling
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

## Authentication & sessions
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

## Authorisation
```text
□ Every operation checks authorisation server-side; client-side hiding is not a control
□ Object-level authorisation (IDOR): ownership checked on every access by ID
□ Function-level authorisation: admin routes gated by role, not by absence of a link
□ Deny by default; allowlists over blocklists
□ Multi-tenant isolation enforced at the data layer (e.g. Postgres RLS), not only in queries
□ Mass assignment: input schemas explicit; no blind object binding
```

## Secrets & configuration
```text
□ No secret in the repository, including history (scan it, do not assume)
□ Secrets from a manager or environment; rotation documented and tested
□ Default credentials removed; debug/admin endpoints disabled in production
□ Error responses do not disclose stack traces, versions, or internal paths
□ Security headers present and correct: CSP (with a real policy), HSTS, X-Content-Type-Options,
  Referrer-Policy, frame-ancestors; permissions-policy where relevant
□ CORS: explicit origins, credentials only where required, no wildcard-with-credentials
□ TLS enforced; certificate validation not disabled anywhere (grep for `verify=False`,
  `rejectUnauthorized: false`, `InsecureSkipVerify`)
```

## Data
```text
□ Data classified; storage locations known; encryption at rest for confidential classes
□ PII minimised, retained on a schedule, deletable on request
□ Logging excludes secrets, full tokens, passwords, card numbers, and unmasked PII
□ Backups access-controlled and restoration tested
□ Third-party data flows documented (subprocessors)
```

## Supply chain
```text
□ Dependency inventory complete, including transitive and build-time dependencies
□ Known CVEs scanned in CI; findings triaged, not just reported
□ Lockfiles committed; installs reproducible; integrity hashes enabled
□ No dependency pinned to a mutable tag or a git branch in production
□ Install-time scripts (postinstall) reviewed or disabled for untrusted packages
□ Typosquatting check on every new dependency name
□ Maintainer and repository identity verified for new dependencies (OpenSSF Scorecard)
□ Archived/unmaintained dependencies flagged and replaced or accepted with a written risk
□ CI/CD: least-privilege tokens, no `pull_request_target` with checkout of PR code,
  required reviews on workflows, artefact provenance where available
```

## Availability & abuse
```text
□ Rate limits per actor and per endpoint; quotas on expensive operations
□ Timeouts on every outbound call; retries with jitter and a bounded budget
□ Request/response size limits; upload size and type limits with server-side validation
□ Pagination bounds enforced; no unbounded query
□ Circuit breaking for dependencies; graceful degradation defined
□ Cost-exhaustion paths identified (anything an anonymous user can trigger expensively)
```
