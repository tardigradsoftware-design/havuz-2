---
name: rag-pipeline
version: 1.0.0
description: >-
  Design, build and evaluate a retrieval-augmented generation pipeline: choose chunking from the structure of the content, build hybrid retrieval with reranking, ground generation in what was retrieved, and measure retrieval and end-to-end quality separately.
category: data
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [rag, retrieval, embeddings, chunking, hybrid-search, reranking, evaluation, grounding]
applies_to: [rag, retrieval, search, knowledge-intensive]
priority: 4
requires: []
conflicts_with: []
estimated_tokens: 2461
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
  - title: "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"
    url: https://arxiv.org/abs/1603.09320
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Malkov & Yashunin — the HNSW index behind pgvector, Qdrant and Weaviate defaults; the M / efConstruction / efSearch parameters and the deletion weakness in step 12."
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    url: https://arxiv.org/abs/2005.11401
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Lewis et al. — the grounding premise, and the qualifier that it reduces rather than eliminates hallucination."
  - title: "pgvector"
    url: https://github.com/pgvector/pgvector
    type: github-repository
    organization: "pgvector"
    license: PostgreSQL
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A maintained Postgres extension for vector search; the deployment shape assumed in steps 4, 7 and 12."
related_skills: [data-pipeline, database-optimization, prompt-engineering, evidence-validation, performance-optimization]
related_repositories: []
tests: 9
---
# RAG Pipeline

## Purpose

Build a retrieval-augmented system whose quality is measured rather than assumed. RAG fails in two
places that look like one problem: retrieval returns the wrong content, or generation does not use the
content it was given. They have different causes, different metrics and different fixes, and conflating
them is why most RAG tuning is ineffective.

## When to Use

```text
✓ answers must be grounded in a corpus the model does not contain, or that changes
✓ factual accuracy on domain content is the primary requirement
✓ hallucination on knowledge-intensive questions must be reduced
✓ an existing RAG system is producing plausible wrong answers and needs diagnosis
```

## When NOT to Use

```text
✗ The answer is in the model's weights and is stable. Retrieval adds latency, cost and a failure mode.
✗ The requirement is exact lookup by identifier. That is a database query or a lexical search.
✗ The corpus is tiny enough to fit in context. Put it in context and skip the pipeline.
✗ The task needs reasoning over many documents at once rather than retrieval of a few. That is a
  different architecture — agentic search or a map-reduce over the corpus.
✗ Nothing has been measured. Build the evaluation set before tuning anything.
```

## Workflow

```text
1. BUILD THE QUERY SET FIRST.   100-500 real queries with the documents that should answer them, ideally
   from logs. Real queries — not queries written while looking at the corpus, which produces a set the
   system trivially passes. Without this set every later decision is aesthetic.

2. CHUNK BY STRUCTURE, NOT BY CHARACTER COUNT.   Respect headings, paragraphs and function boundaries.
   200-800 tokens is the common working range; the right size follows the content's density. A chunk that
   ends mid-sentence embeds badly, and a chunk covering three topics matches none of them well.

3. ENRICH EACH CHUNK BEFORE EMBEDDING.   Prepend the document title, section path and governing metadata.
   "Section 4.2 of the Postgres runbook" plus the body embeds far better than the body alone, because the
   vector carries the topic the body assumes. For code, chunk by symbol with its signature; for tables,
   keep the header row; for APIs, keep the endpoint with its parameters.

4. STORE FILTERABLE METADATA AND FILTER BEFORE SEARCHING.   Tenant, document type, date, version, access
   level. Post-filtering after an ANN search returns fewer than k results and biases recall.

5. BUILD HYBRID RETRIEVAL, NOT VECTOR-ONLY.   BM25 or full-text for exact terms, identifiers, code symbols
   and rare tokens; vectors for paraphrase and conceptual similarity. Merge with Reciprocal Rank Fusion,
   which needs no score calibration between two systems with different score distributions. Vector-only
   retrieval is plausible and wrong on exactly the queries where precision matters most.

6. ADD A CROSS-ENCODER RERANKER.   Pass the top 50-100 merged candidates through it. A cross-encoder reads
   query and document together and is far more accurate than a bi-encoder similarity, and far too slow to
   run over the corpus. This is the largest quality-per-latency gain available after fixing chunking.

7. MATCH THE DISTANCE METRIC TO THE MODEL.   Most modern text embeddings are trained for cosine; Euclidean
   on unnormalised vectors from such a model degrades results for a reason invisible in the scores.
   L2-normalise at ingest and the choice stops mattering.

8. SET k FROM MEASURED RECALL.   Not from a template. k=3 is too small when chunking is fine-grained.
   Increase k until Recall@k stops improving, then let the reranker and the context budget decide.

9. GROUND THE GENERATION.   Instruct the model to answer only from the retrieved context, to cite the
   chunk each claim comes from, and to say when the context does not contain the answer. "I don't know"
   must be a permitted and rewarded output — a system that must answer produces fabrication.

10. MEASURE RETRIEVAL AND GENERATION SEPARATELY.   Retrieval: Recall@k, MRR, nDCG@k. Generation:
   faithfulness (is every claim supported by the retrieved context), answer relevance, and refusal
   correctness on unanswerable questions. A retrieval improvement that does not move the end answer is not
   an improvement, and an end-to-end score cannot tell you which stage to fix.

11. ABLATE.   Flat versus ANN index, chunk sizes, with and without reranking, lexical-only versus
   vector-only versus hybrid. Report each number with the query set, the configuration and the date.

12. HANDLE THE OPERATIONAL CASES.   New and updated documents re-embedded incrementally; deletions
   propagated (ANN indexes often mark-and-rebuild, so a churning index degrades); the embedding model
   version recorded with the index, because changing the model means re-embedding everything and vectors
   from two models are not comparable; retrieval latency and cost budgeted alongside generation.

13. WATCH DRIFT.   New documents change the distribution and a quantised or IVF index trained on old data
   degrades. Re-measure on a schedule, not only at launch.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Plausible wrong answers | retrieval metrics good, faithfulness poor | the generation stage is not using the context; fix grounding and permit refusal |
| Good answers on the demo, bad on real queries | the query set was written from the corpus | rebuild the set from logs |
| Exact identifiers not found | vector-only retrieval | add lexical search and hybrid merge |
| Right document retrieved, wrong chunk | chunks too large or too small | re-tune chunk size and add context enrichment |
| Fewer than k results after filtering | post-filtering | filter before the ANN search |
| Recall degraded after an upgrade | index trained or built on old data | rebuild and re-measure |
| Results changed after a model swap | index not re-embedded | re-embed; record the model version with the index |
| Latency blew the budget | reranker over too many candidates | cap the rerank input at 50-100 |
| Fabricated answers on unanswerable questions | refusal not permitted or not rewarded | make "not in the context" an explicit, evaluated output |
| No ablation, so nobody knows what helps | changes made one at a time without comparison | run the ablation matrix and record it |

## Quality Checklist

```text
□ the query set is built from real queries with known-good documents
□ chunking follows the content's structure, with context enrichment before embedding
□ filterable metadata is stored and applied before the vector search
□ retrieval is hybrid: lexical plus vector, merged with RRF
□ a cross-encoder reranker runs over a bounded candidate set
□ the distance metric matches the embedding model's training objective
□ k was chosen from measured recall, not from a template
□ generation is grounded, cites chunks, and is permitted to refuse
□ retrieval and generation are measured separately, with the metrics named
□ the ablation matrix was run and recorded
□ incremental updates, deletions and re-embedding are handled
□ the embedding model version is recorded with the index
□ latency and cost are budgeted alongside quality
□ drift is re-measured on a schedule
```

## Anti-Patterns

```text
✗ VECTOR-ONLY RETRIEVAL.   Identifiers, negation and exact terms fail silently.
✗ FIXED-CHARACTER CHUNKING.   Ignores every structural boundary the content has.
✗ POST-FILTERING AFTER THE ANN SEARCH.   Returns fewer than k and biases recall.
✗ TUNING WITHOUT AN EVALUATION SET.   Every decision is then aesthetic.
✗ ONE END-TO-END METRIC.   It cannot tell you which stage failed.
✗ CHANGING THE EMBEDDING MODEL WITHOUT RE-EMBEDDING.   The index becomes noise.
✗ RECORDING THE MODEL VERSION NOWHERE.   Six months later nobody knows whether the index matches the code.
✗ A SYSTEM THAT MUST ANSWER.   Fabrication is the designed outcome.
✗ TRUSTING THE VENDOR'S RECALL NUMBER.   Recall is data-dependent; measure against a flat index on your
  corpus.
✗ RAG FOR A CORPUS THAT FITS IN CONTEXT.   Added latency, cost and a failure mode for no benefit.
```

## References

- [`knowledge/data-engineering/vector-search.md`](../../knowledge/data-engineering/vector-search.md) — index families, chunking and hybrid retrieval in detail
- [`knowledge/evaluation/llm-judge-validation.md`](../../knowledge/evaluation/llm-judge-validation.md) — scoring faithfulness and answer relevance
- [`knowledge/databases/indexing-strategy.md`](../../knowledge/databases/indexing-strategy.md) — pgvector inherits Postgres vacuum and memory behaviour
- [`knowledge/reasoning/public-reasoning-research.md`](../../knowledge/reasoning/public-reasoning-research.md) — what retrieval augmentation does and does not establish
- [`skills/data-pipeline/SKILL.md`](../data-pipeline/SKILL.md) · [`skills/prompt-engineering/SKILL.md`](../prompt-engineering/SKILL.md) · [`skills/database-optimization/SKILL.md`](../database-optimization/SKILL.md) · [`skills/performance-optimization/SKILL.md`](../performance-optimization/SKILL.md)
- [`agents/researcher/AGENT.md`](../../agents/researcher/AGENT.md) · [`workflows/deep-research/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
- pgvector — <https://github.com/pgvector/pgvector> · Malkov & Yashunin arXiv:1603.09320 · Lewis et al. arXiv:2005.11401
