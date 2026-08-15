# Phase 0.5 - Knowledge Base and Retrieval Design

## Status

Complete

## 1. Goal

Define how RadioLab AI V1 will organize, retrieve, verify, and cite local knowledge before implementation begins.

The knowledge system should support technically grounded answers while remaining practical for a completely local application.

---

## 2. Scope

Phase 0.5 defines:

* Knowledge source categories and organization
* Supported document formats
* Document chunking
* Metadata requirements
* Retrieval behavior
* Source authority and prioritization
* Retrieval quality handling
* Conflicting-source behavior
* Citation and provenance requirements
* Knowledge updates
* The role of the local LLM
* V1 limitations

This phase defines the expected behavior only. It does not implement the knowledge base.

### Out of Scope

The following are deferred to implementation phases:

* Installing or configuring a vector database
* Generating embeddings
* Building the ingestion pipeline
* Writing retrieval or RAG code
* Connecting retrieval to the local LLM
* GUI implementation
* Retrieval benchmarking and parameter tuning

---

## 3. Knowledge Sources

RadioLab AI V1 will distinguish between five information-source categories.

### Official Documentation

Primary documentation from projects, libraries, hardware vendors, or other authoritative technical sources.

Examples include official GNU Radio documentation and official manuals.

### Trusted Technical References

Established technical material such as textbooks, papers, standards, and reliable SDR, DSP, or communications references.

### Curated Project Knowledge

Material intentionally prepared or selected for use by RadioLab AI, including project-specific technical explanations and reference notes.

### User Notes

Locally provided notes and documents.

User notes remain identifiable as user-provided material and are not automatically treated as verified technical facts.

### Tool-Generated Results

Results produced by verified RadioLab AI tools, including deterministic SDR or GNU Radio calculations.

Tool results are not stored as ordinary knowledge-base documents. They enter the answer pipeline separately when required.

---

## 4. Source Authority

Knowledge sources do not have equal authority.

The default authority order is:

1. Verified tool-generated results, within the task the tool is designed to perform
2. Official documentation
3. Trusted technical references
4. Curated project knowledge
5. User notes

This ordering is not applied blindly.

Source relevance, software or hardware version, technical context, and user intent must also be considered.

For example, when a user explicitly asks what their own notes say, those notes become the primary source for that request.

---

## 5. Knowledge Organization

Stored knowledge will be logically separated by source category while using standardized metadata.

Conceptually:

```text
RadioLab AI Knowledge
│
├── Official Documentation
│   ├── GNU Radio
│   └── Other official documentation
│
├── Trusted Technical References
│   ├── SDR
│   ├── DSP
│   └── Communications
│
├── Curated Project Knowledge
│
└── User Notes
```

Logical separation does not require separate physical databases.

The physical storage and indexing architecture will be selected during implementation.

---

## 6. Supported Document Formats

V1 will initially support:

* `.pdf`
* `.md`
* `.txt`

PDF support will target documents containing reliably extractable text.

Scanned or image-only PDFs requiring OCR are not guaranteed to work in V1.

Additional formats such as DOCX, PPTX, HTML, images, spreadsheets, and LaTeX source are deferred.

If text cannot be extracted reliably, the system should report the problem rather than silently ingest incomplete content.

---

## 7. Document Chunking

RadioLab AI will use a structure-aware hybrid chunking approach.

Natural boundaries such as headings, sections, and paragraphs should be preserved where practical. Sections that are too large will be divided into smaller chunks with limited overlap.

Technical elements such as equations, definitions, tables, code snippets, and parameter explanations should remain connected to the surrounding context where possible.

Exact chunk size and overlap values will be determined experimentally during implementation.

---

## 8. Metadata

Each stored chunk will retain enough metadata to identify and trace its origin.

Metadata may include:

* Source ID
* Source category
* Document title
* Section or heading
* Page number, when reliably available
* Chunk ID
* Topic or tags
* Source or document version
* Ingestion or update information

Artificial numerical trust scores will not be assigned to sources.

Metadata will support retrieval, filtering, citations, debugging, and provenance tracking.

---

## 9. Retrieval Design

RadioLab AI V1 will use hybrid retrieval.

The retrieval system will combine:

* Semantic/vector retrieval
* Keyword-based retrieval

Semantic retrieval is useful for conceptual similarity, while keyword retrieval is important for exact technical terms such as GNU Radio block names, parameters, APIs, acronyms, and error messages.

Results from both approaches will be merged and ranked before being provided to the local LLM.

The exact embedding model, search implementation, ranking algorithm, and weighting will be selected and tested during implementation.

---

## 10. Context Selection

Retrieval may initially produce a broader set of candidate chunks.

Before context is sent to the local LLM, the system should:

1. Rank candidates by relevance.
2. Remove unnecessary duplication or highly overlapping results.
3. Select the strongest supporting chunks.
4. Preserve useful source diversity where appropriate.
5. Stay within the available context budget.

V1 will not permanently assume a fixed number of retrieved chunks.

Exact candidate limits, context budgets, and selection parameters will be determined through testing with the selected local model and hardware.

---

## 11. Retrieval Quality

The closest retrieval result is not automatically a good result.

RadioLab AI will therefore include a retrieval-quality gate.

Retrieved information must meet an experimentally determined relevance standard before being treated as supporting knowledge.

If sufficient supporting information cannot be found, RadioLab AI should clearly state that reliable information was not available in the current local knowledge sources.

The model's pretrained knowledge must not be presented as though it were verified by the local knowledge base.

Exact relevance thresholds will be calibrated during implementation.

---

## 12. Conflicting Information

Retrieved sources may occasionally disagree.

When a meaningful conflict is identified, RadioLab AI should consider:

* Source authority
* Relevance
* Software or hardware version
* Technical context and assumptions
* User intent

Higher-authority sources should normally be preferred for factual verification.

Meaningful disagreements should not be silently hidden. Where appropriate, the conflicting sources should both be identified.

If the available evidence cannot resolve the conflict, RadioLab AI should communicate the uncertainty instead of inventing a resolution.

---

## 13. Citations and Provenance

Knowledge-backed answers must retain provenance information for the sources used.

User-facing citations should identify, where available:

* Source category
* Document title
* Section or heading
* Page number

Citation information must come from metadata attached to retrieved knowledge rather than being invented by the local LLM.

Internal information such as vector IDs, embedding IDs, database keys, similarity scores, and chunk IDs should not appear as normal user-facing citations.

The visual presentation of citations will be decided during the V1 GUI design phase.

---

## 14. Knowledge Updates

V1 will use simple document-level lifecycle management.

When a document is added, it is processed and indexed.

When an existing document changes, its previously indexed content should be replaced by the updated content.

When a document is removed, its associated searchable chunks should also be removed.

Retrieval should normally operate on the currently active version of a document.

Maintaining a complete historical version system inside the knowledge base is outside the V1 scope.

---

## 15. Role of the Local LLM

The local LLM is primarily responsible for reasoning over, synthesizing, and explaining retrieved knowledge and verified tool outputs.

It is not the source of technical verification.

For knowledge-backed technical answers, the model should not present unsupported technical claims, fabricated citations, or invented tool results as verified information.

When sufficient evidence is unavailable, the response should communicate that limitation.

The model may use its language and reasoning capabilities to make retrieved technical information easier to understand, including beginner-friendly explanations.

---

## 16. High-Level Retrieval Flow

```text
Local Knowledge Sources
        │
        ▼
Document Processing
        │
        ▼
Structure-Aware Chunking
        │
        ▼
Metadata + Local Index
        │
        ▼
User Question
        │
        ▼
Hybrid Retrieval
(Semantic + Keyword)
        │
        ▼
Ranking and Filtering
        │
        ▼
Retrieval Quality Check
        │
   ┌────┴────┐
   │         │
Enough     Insufficient
Evidence    Evidence
   │         │
   ▼         ▼
Context    Report Limitation
   │
   ├── Verified Tool Results
   │    when required
   ▼
Local LLM
   │
   ▼
Grounded Answer
+
Citations
```

---

## 17. V1 Limitations

The V1 knowledge system deliberately remains limited and testable.

V1 does not guarantee:

* OCR for scanned or image-only documents
* Support for document formats beyond PDF, Markdown, and plain text
* Automatic internet retrieval
* Perfect retrieval for every question
* Automatic detection of every contradiction
* Correctness simply because information exists in the knowledge base
* Verification of unsupported pretrained LLM knowledge
* Full document-version history
* Advanced retrieval techniques unless testing demonstrates a need for them

Exact values for chunk size, overlap, retrieval thresholds, ranking weights, retrieved chunk counts, context budgets, and similar parameters are intentionally left for implementation and testing.

Retrieved information remains attributable to its source. Retrieval alone does not make a source correct.

---

## 18. Completion Criteria

Phase 0.5 is complete when:

* Knowledge source categories are defined.
* Knowledge organization is defined.
* V1 document support is defined.
* Chunking strategy is defined.
* Metadata requirements are defined.
* Retrieval behavior is defined.
* Source authority rules are defined.
* Citation and provenance behavior is defined.
* Weak retrieval behavior is defined.
* Conflicting-source behavior is defined.
* Knowledge update behavior is defined.
* Local LLM grounding rules are defined.
* V1 limitations and deferred features are documented.
* The Phase 0.5 design has been reviewed.
* This document has been committed and pushed to GitHub.


