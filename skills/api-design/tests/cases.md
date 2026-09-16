# Test cases — `api-design`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Design an interface whose **first consumer is not its last**, and where adding capability does not break existing callers. An API is a promise made in public;
WHEN     the agent executes `api-design` end to end on that task
THEN     and before delivery these specific conditions hold: "Contract written and reviewed before implementation; linted in CI"; "One error shape (RFC 9457) everywhere, with `type` URIs and `request_id`"; "Changelog maintained per release with migration notes"
FAIL IF  "Contract written and reviewed before implementation; linted in CI" is false, or "Changelog maintained per release with migration notes" is false, or "One error shape (RFC 9457) everywhere, with `type` URIs and `request_id`" is false
```

## Case 2 — Declines: Internal function signatures within one module — apply taste,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Internal function signatures within one module — apply taste, not a specification
WHEN     the agent considers `api-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Internal function signatures within one module — apply taste, not a specification", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Internal function signatures within one module — apply taste, not a specification"; or `api-design` is declined without naming that exclusion
```

## Case 3 — Declines: A one-off script's CLI, unless others will automate against it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A one-off script's CLI, unless others will automate against it
WHEN     the agent considers `api-design` for that task
THEN     the skill is not selected, because this task is the excluded case "A one-off script's CLI, unless others will automate against it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A one-off script's CLI, unless others will automate against it"; or `api-design` is declined without naming that exclusion
```

## Case 4 — Declines: Where an existing platform API dictates the shape — conform to it deliberately

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Where an existing platform API dictates the shape — conform to it deliberately
WHEN     the agent considers `api-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Where an existing platform API dictates the shape — conform to it deliberately", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Where an existing platform API dictates the shape — conform to it deliberately"; or `api-design` is declined without naming that exclusion
```

## Case 5 — Detects: VERB URLS

```text
GIVEN    A run of this skill in which the known failure mode is present: VERB URLS
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "VERB URLS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "/getOrders, /updateUser — the API becomes RPC with extra steps."
FAIL IF  "VERB URLS" appears in the work and is reported as complete — specifically "/getOrders, /updateUser — the API becomes RPC with extra steps."
```

## Case 6 — Detects: GET WITH SIDE EFFECTS

```text
GIVEN    A run of this skill in which the known failure mode is present: GET WITH SIDE EFFECTS
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "GET WITH SIDE EFFECTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Cacheable, prefetchable, and destructive."
FAIL IF  "GET WITH SIDE EFFECTS" appears in the work and is reported as complete — specifically "Cacheable, prefetchable, and destructive."
```

## Case 7 — Detects: INCONSISTENT ERRORS

```text
GIVEN    A run of this skill in which the known failure mode is present: INCONSISTENT ERRORS
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "INCONSISTENT ERRORS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Three error shapes across four services."
FAIL IF  "INCONSISTENT ERRORS" appears in the work and is reported as complete — specifically "Three error shapes across four services."
```

## Case 8 — Detects: FLOAT MONEY

```text
GIVEN    A run of this skill in which the known failure mode is present: FLOAT MONEY
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "FLOAT MONEY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rounding errors in payments. Never."
FAIL IF  "FLOAT MONEY" appears in the work and is reported as complete — specifically "Rounding errors in payments. Never."
```

## Case 9 — Detects: OFFSET PAGINATION

```text
GIVEN    A run of this skill in which the known failure mode is present: OFFSET PAGINATION
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "OFFSET PAGINATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Broken pages under concurrent writes; unusable deep pages."
FAIL IF  "OFFSET PAGINATION" appears in the work and is reported as complete — specifically "Broken pages under concurrent writes; unusable deep pages."
```

## Case 10 — Detects: SILENT BREAKING CHANGE

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT BREAKING CHANGE
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "SILENT BREAKING CHANGE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A field's meaning changes with no version and no changelog."
FAIL IF  "SILENT BREAKING CHANGE" appears in the work and is reported as complete — specifically "A field's meaning changes with no version and no changelog."
```

## Case 11 — Detects: ENUM TRAP

```text
GIVEN    A run of this skill in which the known failure mode is present: ENUM TRAP
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "ENUM TRAP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Adding an enum value crashes exhaustive client switches."
FAIL IF  "ENUM TRAP" appears in the work and is reported as complete — specifically "Adding an enum value crashes exhaustive client switches."
```

## Case 12 — Detects: UNDOCUMENTED LIMITS

```text
GIVEN    A run of this skill in which the known failure mode is present: UNDOCUMENTED LIMITS
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "UNDOCUMENTED LIMITS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rate limits discovered by hitting them."
FAIL IF  "UNDOCUMENTED LIMITS" appears in the work and is reported as complete — specifically "Rate limits discovered by hitting them."
```

## Case 13 — Detects: SCHEMA-LAST

```text
GIVEN    A run of this skill in which the known failure mode is present: SCHEMA-LAST
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "SCHEMA-LAST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Implementation first, spec generated afterwards, spec then ignored."
FAIL IF  "SCHEMA-LAST" appears in the work and is reported as complete — specifically "Implementation first, spec generated afterwards, spec then ignored."
```

## Case 14 — Detects: NO IDEMPOTENCY

```text
GIVEN    A run of this skill in which the known failure mode is present: NO IDEMPOTENCY
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "NO IDEMPOTENCY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Duplicate orders on every retry."
FAIL IF  "NO IDEMPOTENCY" appears in the work and is reported as complete — specifically "Duplicate orders on every retry."
```

## Case 15 — Detects: LEAKY ABSTRACTION

```text
GIVEN    A run of this skill in which the known failure mode is present: LEAKY ABSTRACTION
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "LEAKY ABSTRACTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Internal table/column names in the public contract — impossible to change later."
FAIL IF  "LEAKY ABSTRACTION" appears in the work and is reported as complete — specifically "Internal table/column names in the public contract — impossible to change later."
```

## Case 16 — Detects: AUTH AS AFTERTHOUGHT

```text
GIVEN    A run of this skill in which the known failure mode is present: AUTH AS AFTERTHOUGHT
WHEN     the agent executes `api-design` and reaches the point where this failure occurs
THEN     "AUTH AS AFTERTHOUGHT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Endpoints secured by obscurity; missing object-level authorisation (IDOR)."
FAIL IF  "AUTH AS AFTERTHOUGHT" appears in the work and is reported as complete — specifically "Endpoints secured by obscurity; missing object-level authorisation (IDOR)."
```

## Case 17 — Avoids: `GET /api/deleteUser?id=1`

```text
GIVEN    A situation that invites the anti-pattern "`GET /api/deleteUser?id=1`"
WHEN     the agent applies `api-design` in that situation
THEN     "`GET /api/deleteUser?id=1`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`GET /api/deleteUser?id=1`" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 18 — Avoids: Returning `200 OK` with `{"error": "not found"}`

```text
GIVEN    A situation that invites the anti-pattern "Returning `200 OK` with `{"error": "not found"}`"
WHEN     the agent applies `api-design` in that situation
THEN     "Returning `200 OK` with `{"error": "not found"}`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Returning `200 OK` with `{"error": "not found"}`" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 19 — Avoids: `amount: 19.99` as a float

```text
GIVEN    A situation that invites the anti-pattern "`amount: 19.99` as a float"
WHEN     the agent applies `api-design` in that situation
THEN     "`amount: 19.99` as a float" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`amount: 19.99` as a float" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 20 — Avoids: `page=10000&per_page=100000`

```text
GIVEN    A situation that invites the anti-pattern "`page=10000&per_page=100000`"
WHEN     the agent applies `api-design` in that situation
THEN     "`page=10000&per_page=100000`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`page=10000&per_page=100000`" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 21 — Avoids: Renaming `customer_id` to `client_id` in place

```text
GIVEN    A situation that invites the anti-pattern "Renaming `customer_id` to `client_id` in place"
WHEN     the agent applies `api-design` in that situation
THEN     "Renaming `customer_id` to `client_id` in place" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Renaming `customer_id` to `client_id` in place" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 22 — Avoids: A different error envelope per microservice

```text
GIVEN    A situation that invites the anti-pattern "A different error envelope per microservice"
WHEN     the agent applies `api-design` in that situation
THEN     "A different error envelope per microservice" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A different error envelope per microservice" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 23 — Avoids: Documenting an API by pasting example responses with no field definitions

```text
GIVEN    A situation that invites the anti-pattern "Documenting an API by pasting example responses with no field definitions"
WHEN     the agent applies `api-design` in that situation
THEN     "Documenting an API by pasting example responses with no field definitions" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Documenting an API by pasting example responses with no field definitions" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```

## Case 24 — Avoids: Requiring clients to guess that an unknown enum value means "other"

```text
GIVEN    A situation that invites the anti-pattern "Requiring clients to guess that an unknown enum value means "other"
WHEN     the agent applies `api-design` in that situation
THEN     "Requiring clients to guess that an unknown enum value means "other" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Requiring clients to guess that an unknown enum value means "other" appears in the output; or it is absent by accident, with nothing in `api-design` having ruled it out
```
