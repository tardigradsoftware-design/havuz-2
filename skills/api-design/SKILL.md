---
name: api-design
version: 1.0.0
description: >-
  Design interfaces that stay compatible as they grow — resource modelling, HTTP semantics,
  versioning, error contracts, pagination, idempotency and the schema-first workflow.
category: backend
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [api, rest, openapi, http, contracts, versioning, backend, design]
applies_to: [backend, api, web]
priority: 85
requires: []
conflicts_with: []
estimated_tokens: 2769
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Design rules
    anchor: "#design-rules"
    purpose: implementation
  - heading: Error contract
    anchor: "#error-contract"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "OpenAPI Specification"
    url: https://spec.openapis.org/oas/latest.html
    type: specification
    organization: OpenAPI Initiative / Linux Foundation
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Not fetched in this run; confirm the current version (3.1.x) before depending on specific fields."
  - title: "RFC 9110 — HTTP Semantics"
    url: https://www.rfc-editor.org/rfc/rfc9110
    type: specification
    organization: IETF
    published: 2022-06-01
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "RFC 9457 — Problem Details for HTTP APIs"
    url: https://www.rfc-editor.org/rfc/rfc9457
    type: specification
    organization: IETF
    published: 2023-07-01
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Obsoletes RFC 7807."
related_skills: [backend-engineering, database-design, documentation, security-audit, testing]
related_repositories: [OAI/OpenAPI-Specification, stoplightio/spectral, fern-api/fern, speakeasy-api/speakeasy]
tests: 6
---

# API Design

## Purpose

Design an interface whose **first consumer is not its last**, and where adding capability
does not break existing callers. An API is a promise made in public; the cost of a bad one
is paid by everyone who integrates, forever.

Optimise for: predictability, compatibility, and the caller's error path. Almost every API
complaint is one of those three.

## When to Use

```text
□ Designing any HTTP/gRPC/GraphQL/event interface consumed by someone else
□ Adding an endpoint to a public or cross-team API
□ Reviewing a contract before it is published
□ Deciding how to change an API without breaking callers
```

## When NOT to Use

```text
✗ Internal function signatures within one module — apply taste, not a specification
✗ A one-off script's CLI, unless others will automate against it
✗ Where an existing platform API dictates the shape — conform to it deliberately
```

## Design rules

### Resources & URLs
```text
nouns, not verbs:        /orders, /orders/{id}, /orders/{id}/items
collection then item:    plural, consistent, lowercase, hyphenated
no file extensions:      content type comes from Accept / Content-Type
nest only for real containment, max depth 2:  /orders/{id}/items   (not /users/{u}/orders/{o}/items/{i})
non-CRUD actions:        POST /orders/{id}:cancel  or a subresource POST /orders/{id}/cancellations
                         — never GET with side effects
filters/sorting/paging:  query parameters, documented and bounded:
                         ?status=open&sort=-created_at&page[cursor]=…&page[limit]=50
sparse fields:           ?fields[order]=id,status,total
```

### HTTP semantics (RFC 9110)
```text
GET     safe, cacheable, idempotent — no body semantics, no mutation
POST    create or non-idempotent action; returns 201 + Location for creation
PUT     full replace, idempotent
PATCH   partial update — use JSON Merge Patch (RFC 7386) or JSON Patch (RFC 6902), not an ad-hoc shape
DELETE  idempotent removal; 204 or 200 with a resource
200/201/204 success · 202 accepted-for-async · 304 not-modified
400 malformed · 401 unauthenticated · 403 forbidden (authenticated, not permitted) ·
404 not found (also for "exists but not visible to you") · 409 conflict/state ·
412 precondition · 415 media type · 422 semantically invalid · 429 rate limited ·
5xx your fault, never the caller's
Use 422 vs 400 deliberately: 400 = cannot parse; 422 = parsed, but violates a rule.
```

### Idempotency & safety
```text
□ Every mutating endpoint either is idempotent or accepts an Idempotency-Key header
□ Key semantics documented: scope, TTL, replay behaviour (returns the original response)
□ Retries are safe by design — callers WILL retry on timeout
□ Conditional requests supported on mutable resources: ETag + If-Match / If-None-Match
□ Optimistic concurrency preferred over long-held locks
```

### Pagination
```text
□ Cursor-based by default for anything that can change under the reader; offset only for
  stable, small, admin-style listings (offset breaks on insert/delete and on deep pages)
□ Response envelope carries: data, next cursor, prev cursor (optional), and total only if cheap
□ page[limit] bounded server-side with a documented maximum; reject absurd values
□ Stable sort order guaranteed, with a tiebreaker on a unique field
```

### Versioning & compatibility
```text
Choose ONE strategy and document it:
  URL path      /v1/orders            — obvious, cache-friendly, easy to route
  Header        Accept: application/vnd.api.v2+json — cleaner URLs, harder to debug
  Non-versioned + additive-only      — best when you can commit to never breaking

Compatible (allowed at any time):
  + new endpoint, + new optional field, + new enum value (only if callers are told to
    tolerate unknown values), + new optional header, wider input range, faster responses

Breaking (requires a version or a deprecation cycle):
  − removed/renamed field or endpoint, type change, narrower input, new required field,
  changed error shape, changed semantics of an existing field, new enum value where callers
  switch exhaustively, changed auth

Deprecation cycle: announce → Deprecation + Sunset headers → dual support for a stated
window → removal. Every breaking change is documented in a changelog with a migration note.
```

### Schemas & contracts
```text
□ Schema-first: write the OpenAPI/protobuf document, review it, then implement
□ Lint the contract in CI (Spectral or equivalent) — style rules enforced mechanically
□ Every field has: type, required/optional, format, bounds, example, description
□ Date-time in RFC 3339 UTC; money as integer minor units + currency code (never a float);
  identifiers as opaque strings even when they look numeric
□ Nullable vs absent distinguished; default values documented
□ Unknown fields: state whether the server ignores or rejects them (be strict on input
  you define, tolerant on output you consume — and document which you chose)
□ Generate clients and server stubs from the contract; hand-written clients drift
□ Contract tests on both sides of every integration
```

### Async & long operations
```text
□ Anything over ~a few hundred ms returns 202 with an operation resource; poll or webhook
□ Operation resource exposes state, progress, result and error, with the same error contract
□ Webhooks: signed, retried with backoff, idempotent on the receiver, documented events,
  a test endpoint, and versioned payloads
□ Rate limits published in headers (RateLimit-* per the IETF draft) with 429 + Retry-After
```

## Error contract

One shape, everywhere, per **RFC 9457 (Problem Details)**:

```json
{
  "type": "https://api.example.com/errors/insufficient-stock",
  "title": "Insufficient stock",
  "status": 422,
  "detail": "Requested 12 units of SKU-8841; 3 available.",
  "instance": "/orders/ord_01H...",
  "errors": [
    { "field": "items[0].quantity", "code": "max_available", "limit": 3 }
  ],
  "request_id": "req_9f2c..."
}
```

Rules:

```text
1. `type` is a stable, documented URI — the machine-readable identity of the error.
   Callers branch on it, never on `title` or `detail` prose.
2. Every error carries `request_id` so support can find the trace.
3. Field-level errors are enumerable and include the constraint that was violated.
4. Never leak internals: no stack traces, no SQL, no internal hostnames, no framework errors.
5. The error catalogue is published and versioned like the rest of the API.
6. 4xx must be actionable: the caller can fix it from the response alone.
   If they cannot, the message is wrong.
7. Same shape for gateway, auth and rate-limit errors — one contract, no exceptions.
```

## Failure Modes

```text
VERB URLS               /getOrders, /updateUser — the API becomes RPC with extra steps.
GET WITH SIDE EFFECTS   Cacheable, prefetchable, and destructive.
INCONSISTENT ERRORS     Three error shapes across four services.
FLOAT MONEY             Rounding errors in payments. Never.
OFFSET PAGINATION       Broken pages under concurrent writes; unusable deep pages.
SILENT BREAKING CHANGE  A field's meaning changes with no version and no changelog.
ENUM TRAP               Adding an enum value crashes exhaustive client switches.
UNDOCUMENTED LIMITS     Rate limits discovered by hitting them.
SCHEMA-LAST             Implementation first, spec generated afterwards, spec then ignored.
NO IDEMPOTENCY          Duplicate orders on every retry.
LEAKY ABSTRACTION       Internal table/column names in the public contract — impossible to change later.
AUTH AS AFTERTHOUGHT    Endpoints secured by obscurity; missing object-level authorisation (IDOR).
```

## Quality Checklist

```text
□ Contract written and reviewed before implementation; linted in CI
□ Resources are nouns; nesting ≤2; actions expressed correctly
□ HTTP methods, status codes and semantics match RFC 9110
□ Every mutating endpoint idempotent or Idempotency-Key aware
□ Conditional requests (ETag/If-Match) on mutable resources
□ Cursor pagination with bounded limits and a stable sort tiebreaker
□ One versioning strategy chosen, documented and enforced
□ Compatibility rules published; deprecation uses Deprecation/Sunset headers + a window
□ One error shape (RFC 9457) everywhere, with `type` URIs and `request_id`
□ Error catalogue published; 4xx responses actionable without support
□ Types correct: RFC 3339 UTC datetimes, integer minor-unit money, opaque string IDs
□ Every field documented with type, bounds, example, required/optional
□ Clients and stubs generated from the contract; contract tests on both sides
□ Rate limits and quotas published in headers; 429 + Retry-After
□ Object-level authorisation on every ID-addressed resource
□ No internal identifiers or storage details in the public surface
□ Changelog maintained per release with migration notes
```

## Anti-Patterns

```text
✗ `GET /api/deleteUser?id=1`
✗ Returning `200 OK` with `{"error": "not found"}`
✗ `amount: 19.99` as a float
✗ `page=10000&per_page=100000`
✗ Renaming `customer_id` to `client_id` in place
✗ A different error envelope per microservice
✗ Documenting an API by pasting example responses with no field definitions
✗ Requiring clients to guess that an unknown enum value means "other"
```

## References

- RFC 9110 HTTP Semantics — <https://www.rfc-editor.org/rfc/rfc9110>
- RFC 9457 Problem Details — <https://www.rfc-editor.org/rfc/rfc9457> (obsoletes RFC 7807)
- OpenAPI Specification — <https://spec.openapis.org/oas/latest.html>
- [`backend-engineering`](../backend-engineering/SKILL.md) · [`database-design`](../database-design/SKILL.md)
- [`documentation`](../documentation/SKILL.md) · [`security-audit`](../security-audit/SKILL.md)
- [`patterns/backend/`](../../patterns/backend/) · [`knowledge/backend/`](../../knowledge/backend/)
- [`evaluations/`](../../evaluations/) — contract-design tasks

## Related Skills

`backend-engineering` · `database-design` · `documentation` · `security-audit` · `testing` ·
`migration`

## Evaluation Criteria

```text
1. Compatibility: zero unplanned breaking changes per year.
2. Predictability: a new consumer guesses the shape of an unlisted endpoint correctly.
3. Self-service: integrators complete a first successful call from the docs alone.
4. Error actionability: fraction of 4xx resolved by the caller without contacting support.
5. Contract coverage: 100% of endpoints defined in the linted schema; clients generated.
6. Performance: pagination and field-selection keep payload sizes bounded at scale.
```

Test cases in [`tests/`](tests/).
