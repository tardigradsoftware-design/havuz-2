---
id: data-engineering-vector-search
title: "Vector search: embeddings, indexes and the retrieval decisions that matter"
domain: data-engineering
summary: >-
  What embedding retrieval does and does not provide, the ANN index families and their parameters, chunking as the dominant quality lever, hybrid retrieval with reranking, and the evaluation that separates a working RAG system from a plausible one.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [vector-search, embeddings, rag, ann, hnsw, ivf, chunking, hybrid-search, retrieval, evaluation]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: []
sources:
  - title: "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"
    url: https://arxiv.org/abs/1603.09320
    type: research-paper
    organization: Yandex
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Malkov & Yashunin — the HNSW paper behind the default index in pgvector, Qdrant, Weaviate and most managed vector offerings; the M / efConstruction / efSearch parameters below are its parameters."
---
# Vector Search

## What it provides, and what it does not

Embedding retrieval finds content **semantically near** a query in the space a particular model
produces. Genuinely useful, and frequently oversold.

```text
IT PROVIDES      synonym and paraphrase tolerance — "how do I stop the server" finds "shutdown
                 procedure"
                 retrieval without an exact-match vocabulary, useful when query language and document
                 language differ
                 a ranking signal that can be combined with others

IT DOES NOT      understand the query. Similarity is not relevance, and confidently irrelevant results
                 are the normal failure mode.
                 handle negation, comparison, counting or "everything except".
                 handle exact identifiers well. Error codes, SKUs, function names, CVE IDs and version
                 strings are lexical problems; BM25 beats embeddings on them.
                 handle freshness. The index contains what was ingested; nothing about recency or
                 authority is in the vector.
                 remain stable across embedding models. Vectors from two models are not comparable;
                 changing the model means re-embedding everything.
```

Consequence: retrieval built on vectors alone is plausible and wrong on exactly the queries where
precision matters most. **Hybrid retrieval is the baseline design, not an optimisation.**

## Index families

```text
FLAT / EXHAUSTIVE   exact nearest neighbour, O(n) per query. Correct, and the only option below
                    roughly 100k vectors or when recall must be 1.0. Always benchmark against it
                    before believing an ANN index's recall number.

HNSW                a navigable small-world graph. Near-logarithmic query time, recall tunable close
                    to 1.0, memory-hungry (the graph lives in RAM), cheap incremental inserts. The
                    default in pgvector, Qdrant, Weaviate and Milvus.
                      M                 edges per node (typ. 16). Higher = better recall, more memory,
                                        slower build.
                      efConstruction    search width during build (typ. 64-200). Higher = better graph,
                                        slower build. Set once; changing it means rebuilding.
                      efSearch          search width at query time (typ. 40-200). Higher = better
                                        recall, higher latency. Tunable per query — the recall/latency
                                        dial.
                    Deletions are the weak point: many implementations mark and periodically rebuild,
                    so a heavily-churning index degrades.

IVF                 inverted file — cluster the space, search the nearest clusters. Lower memory than
                    HNSW, faster build, requires training, and recall drops sharply if nprobe is too
                    low or the distribution shifts after training. Good for very large, relatively
                    static corpora.

PQ / SQ             quantisation to cut memory and raise throughput, at a recall cost. Product
                    quantisation is lossy in a way that is hard to predict; scalar quantisation
                    (fp32 → int8) is usually the better first choice. Re-measure recall after.

DISK-BASED          DiskANN and similar keep the graph on NVMe, for corpora that do not fit in RAM.
                    Higher and less predictable latency than in-memory HNSW.
```

**Distance metric must match the model's training objective.** Most modern text embeddings are trained
for cosine similarity; Euclidean on unnormalised vectors from such a model gives worse results for a
reason invisible in the scores. If vectors are L2-normalised, cosine and inner product are equivalent
and Euclidean is a monotone transform of them — normalise once at ingest and the choice stops mattering.

## Chunking: the dominant quality lever

More retrieval-quality variance comes from chunking than from the index or the model.

```text
SIZE                too small → context lost, a matching chunk does not answer; too large → diluted
                    vectors, several topics averaged into one point that matches none well. 200-800
                    tokens is the common working range; the right number follows the content's
                    density, not a default.
BOUNDARIES          respect structure — headings, paragraphs, function boundaries. Never a fixed
                    character count. A chunk ending mid-sentence embeds badly.
OVERLAP             10-20% prevents an answer straddling a boundary from being lost. It also
                    duplicates content in results — deduplicate by document and section before
                    presenting.
CONTEXT ENRICHMENT  prepend the document title, section path and governing metadata to the chunk text
                    before embedding. "Section 4.2 of the Postgres runbook" plus the body embeds far
                    better than the body alone, because the vector now carries the topic the body
                    assumes.
STRUCTURED CHUNKS   code: chunk by symbol with signature and docstring. Tables: keep the header row
                    and caption. APIs: keep an endpoint with its parameters. Splitting these by
                    character count destroys exactly what makes them retrievable.
PARENT-CHILD        embed small precise chunks, return their larger parent for the model to read.
                    Precise matching plus sufficient context, at the cost of a second lookup.
METADATA FILTERING  store tenant, document type, date, version and access level as filterable
                    metadata, and filter BEFORE the vector search. Post-filtering returns fewer than k
                    and biases recall.
```

## Hybrid retrieval

```text
LEXICAL (BM25 / full-text)  exact terms, identifiers, rare tokens, code symbols, product names. Zero
                            training, interpretable, and what users mean when they type a specific
                            string.
VECTOR                      paraphrase, synonymy, conceptual similarity.
COMBINE                     run both, merge with Reciprocal Rank Fusion or a weighted normalised-score
                            blend. RRF needs no score calibration between two systems with different
                            score distributions, which is why it is the common default.
RERANK                      pass the top 50-100 merged candidates through a cross-encoder. A
                            cross-encoder reads query and document together and is far more accurate
                            than a bi-encoder similarity — and far too slow to run over the corpus.
                            The largest quality-per-latency improvement available after fixing chunking.
FILTER                      metadata predicates applied before retrieval, as above.
```

## Evaluation

Without this, every change is a guess and every improvement is unproven.

```text
BUILD A QUERY SET.    100-500 real queries, ideally from logs, with the documents that should be
                      retrieved. Real queries — not queries written while looking at the corpus, which
                      produces a set the system trivially passes.
MEASURE RETRIEVAL.    Recall@k (was the right document in the top k), MRR and nDCG@k (was it ranked
                      well). Report both.
MEASURE END-TO-END.   Faithfulness (is the answer supported by the retrieved context), answer
                      relevance, groundedness. A retrieval improvement that does not move the end
                      answer is not an improvement.
ABLATE.               flat vs HNSW, chunk sizes, with and without reranking, lexical-only vs
                      vector-only vs hybrid. Every number reported with the query set and the date.
WATCH DRIFT.          New documents change the distribution; a quantised or IVF index trained on old
                      data degrades. Re-measure on a schedule, not only at launch.
```

## Anti-patterns

```text
✗ Vectors only.                       Identifiers, negation and exact terms fail silently.
✗ Fixed-character chunking.           Ignores every structural boundary the content has.
✗ Post-filtering after the ANN search. Returns fewer than k and biases recall; filter first.
✗ Changing the embedding model without re-embedding.  The index becomes noise.
✗ Cosine distance on unnormalised vectors from a model trained for cosine.
✗ k = 3 by default.                   Too small when chunking is fine-grained. The right k follows
  from measured recall, not a template.
✗ No evaluation set.                  Every tuning decision is then aesthetic.
✗ Trusting the vendor's recall number. Recall is data-dependent; measure on your corpus against a flat
  index.
✗ Recording the embedding model version nowhere.  Six months later nobody knows whether the index
  matches the model in the code.
```

## References

- [`../agent-engineering/framework-comparison.md`](../agent-engineering/framework-comparison.md) — where retrieval sits in an agent stack
- [`../databases/indexing-strategy.md`](../databases/indexing-strategy.md) — pgvector is a Postgres extension and inherits its vacuum, memory and concurrency behaviour
- [`../evaluation/llm-judge-validation.md`](../evaluation/llm-judge-validation.md) — judging faithfulness and answer relevance
- [`skills/rag-pipeline/SKILL.md`](../../skills/rag-pipeline/SKILL.md) · [`skills/data-pipeline/SKILL.md`](../../skills/data-pipeline/SKILL.md) · [`skills/database-optimization/SKILL.md`](../../skills/database-optimization/SKILL.md)
- [`patterns/data/`](../../patterns/data/) · [`anti-patterns/data/`](../../anti-patterns/data/) · [`gotchas/`](../../gotchas/)
- Malkov & Yashunin, HNSW — arXiv:1603.09320 · pgvector — <https://github.com/pgvector/pgvector> · Johnson, Douze & Jégou, IVF-PQ — arXiv:1702.08734
