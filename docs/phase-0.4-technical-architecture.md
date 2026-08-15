# Phase 0.4 - Technical Architecture and Local Stack

**Status:** Complete

## 1. Goal

Define the technical architecture and local-first technology stack for
RadioLab AI V1 before implementation begins.

This phase converts the product and system decisions from earlier phases
into concrete architectural boundaries for the local LLM, RAG pipeline,
tools, visualization, routing, orchestration, testing, configuration,
and repository structure.

Phase 0.4 is a design phase. Technology parameters that require real
implementation testing are intentionally deferred rather than guessed.

## 2. Core Architecture Principles

RadioLab AI V1 will:

-   Run locally after initial setup.
-   Be designed around the realistic capability of locally runnable
    models rather than assuming cloud-model-level reasoning.
-   Use the LLM primarily for understanding requests, constrained
    reasoning, routing support, and explanation.
-   Use RAG for traceable, source-grounded knowledge.
-   Use deterministic tools for calculations, analysis, measurement,
    inspection, and controlled operations when appropriate.
-   Keep knowledge-base evidence, tool results, and general LLM
    knowledge logically distinguishable.
-   Prefer bounded, application-controlled workflows over unrestricted
    autonomous agent loops.
-   Preserve clear dependency boundaries around major replaceable
    components.
-   Treat implemented, verified, and supported capabilities as different
    states.

A useful responsibility model is:

``` text
LLM           -> understand, reason, route, explain
RAG           -> retrieve sourced knowledge
Tools         -> calculate, analyse, measure, inspect, execute
Visualization -> present validated tool/data results
Application   -> validate and orchestrate the complete workflow
```

## 3. Development Environment

RadioLab AI V1 will be developed with a Windows-first local development
workflow.

The development environment should remain simple enough for V1 while
leaving room for later Linux support if required.

The architecture should avoid unnecessary operating-system-specific
coupling in application logic.

## 4. Local AI Stack

### 4.1 Local Runtime

RadioLab AI V1 will use **Ollama** as the initial local LLM runtime.

The application will not directly depend on Ollama throughout the
codebase. RadioLab AI will define its own internal LLM interface, with
an Ollama-specific adapter behind it.

``` text
RadioLab AI
     |
     v
Internal LLM Interface
     |
     v
Ollama Adapter
     |
     v
Ollama
     |
     v
Local Model
```

The official Ollama Python library will be used inside the Ollama
adapter for the initial implementation.

### 4.2 Local Model Strategy

The initial target is approximately an 8B-14B class model, preferably
quantized where appropriate for local execution.

Initial candidate model families may include:

-   Qwen
-   Gemma
-   Llama

The final model will not be selected during architecture design.
Candidate models will be benchmarked on representative RadioLab AI
tasks.

Model evaluation must consider more than general conversational quality.
It should include:

-   request classification;
-   tool-family selection;
-   parameter extraction;
-   instruction following;
-   RAG-grounded answering;
-   explanation of deterministic tool results;
-   handling of missing information;
-   latency and local resource requirements.

### 4.3 Local-Model Capability Principle

Features must be designed around the realistic capability of the
selected local model.

Where possible, reliability should be improved by moving work into:

-   deterministic application logic;
-   structured routing;
-   constrained tool exposure;
-   validation;
-   RAG;
-   specialized tools;
-   structured inputs and outputs.

Features that cannot be made sufficiently reliable on the target local
model will be simplified, deferred, or excluded from V1.

## 5. Knowledge Base and RAG Stack

### 5.1 Knowledge Sources

The V1 knowledge base will organize content by source category.

Initial categories:

-   official documentation;
-   curated technical references;
-   personal notes.

Adding content to the knowledge base does not automatically make the
content verified.

Source identity, source authority, retrieval relevance, and verification
status are separate concepts.

### 5.2 Supported V1 Formats

Initial ingestion formats:

-   text-based PDF;
-   Markdown;
-   plain text.

Initially out of scope:

-   scanned PDFs requiring OCR;
-   automatic web crawling;
-   Word documents;
-   PowerPoint documents;
-   spreadsheets;
-   other complex formats.

These may be added in later versions when required.

### 5.3 Parsing

RadioLab AI will use a modular parsing layer.

PDF, Markdown, and TXT may use format-specific parsers, but all parsers
will produce a common internal document representation.

Parsing should preserve useful source/location information when
available, such as:

-   filename;
-   source category;
-   page;
-   section or heading;
-   verification-related metadata.

### 5.4 Chunking

RadioLab AI V1 will use structure-aware chunking.

Chunking should prefer natural boundaries such as:

-   headings;
-   sections;
-   paragraphs.

Limited overlap between adjacent chunks may be used to preserve context
around boundaries.

Exact chunk size and overlap will be tuned during implementation and
retrieval evaluation rather than fixed in Phase 0.4.

### 5.5 Embeddings

Embeddings will be generated locally.

The same embedding model will be used for knowledge-base chunks and
user-query embeddings.

The embedding model should be:

-   lightweight enough for local use;
-   suitable for technical English;
-   effective with SDR and GNU Radio terminology;
-   compatible with the selected vector-store approach.

The exact embedding model will be selected through testing.

### 5.6 Vector Storage

RadioLab AI V1 will initially use **Chroma** as the local persistent
vector store.

It will store/search:

-   embeddings;
-   document chunks;
-   associated metadata.

Access to Chroma will be isolated behind an application-owned
vector-store/retrieval abstraction so another backend can be adopted
later if requirements change.

### 5.7 Retrieval

V1 will use semantic vector retrieval with metadata-based filtering.

The exact number of retrieved chunks and similarity thresholds will be
determined through evaluation.

Reranking is not required initially. It may be introduced later if
retrieval evaluation shows a clear need.

Retrieved chunks must preserve their source metadata.

### 5.8 Source Metadata and Citations

A common minimum metadata model should include fields such as:

``` text
document_id
source_type
source_name
file_name
page_number
section
verification_status
```

Fields may be empty when they do not apply.

Source references shown in answers must be derived from stored/retrieved
metadata rather than invented by the LLM.

RadioLab AI will distinguish:

-   **Traceable:** the source is known.
-   **Authoritative:** the source is classified as authoritative.
-   **Verified:** the information has passed whatever verification
    process RadioLab AI defines.

Retrieval relevance does not automatically imply source authority or
verification.

### 5.9 Knowledge Gaps and General Model Knowledge

When sufficient knowledge-base evidence exists, RadioLab AI may provide
a source-grounded answer.

If sufficient knowledge-base evidence is unavailable, RadioLab AI may
use an appropriate deterministic tool or the local LLM's general
knowledge where suitable.

General LLM knowledge must not be presented as:

-   knowledge-base-grounded;
-   cited from a source that was not retrieved;
-   verified merely because the model produced it.

When the user explicitly asks what a particular source or set of notes
says, RadioLab AI will not silently substitute general model knowledge
if the requested source does not contain the answer.

If neither the available knowledge, tools, nor model can provide a
sufficiently reliable answer, RadioLab AI will clearly state the
limitation.

## 6. Tool and Application Stack

### 6.1 Common Tool Architecture

RadioLab AI will use a modular tool layer with a common internal tool
interface and central tool registry.

Conceptually, a tool exposes:

``` text
name
description
input schema
validation
execution
structured result
```

Initial/future tool domains include:

``` text
Tools
├── DSP / calculation
├── SDR
└── GNU Radio
```

Deterministic calculations and operations should use tools when an
appropriate tool exists rather than relying on the LLM to perform the
operation itself.

The LLM may help identify or select the required capability and explain
results, but application/tool code controls actual execution.

### 6.2 Reuse of Previous DSP Project

Existing deterministic DSP tools from the previous `dsp-ai-agent`
project may be reused after:

1.  technical/mathematical review;
2.  adaptation to the RadioLab AI tool interface;
3.  adequate tests;
4.  integration verification;
5.  local-model routing verification where applicable.

OpenAI-specific agent, routing, and function-calling dependencies from
the previous project will not be carried over directly because RadioLab
AI V1 uses a local Ollama-based architecture.

Existing concepts such as a DSP tool interface, structured tool results,
tool registry, validation, artifacts, and tool families may provide
useful starting points.

Reuse does not automatically mean a capability is supported.

### 6.3 Structured Tool Results

All tools will return a common structured result.

The result model must distinguish at least:

-   success;
-   warnings;
-   unsupported operations;
-   execution errors.

Successful results may contain:

-   structured numerical/data results;
-   metadata;
-   warnings;
-   generated artifacts such as technical figures.

A tool failure must not be transformed by the LLM into an apparently
successful result.

### 6.4 Request Classification and Routing

RadioLab AI will include a request-classification and routing layer.

Routing may select:

-   knowledge-base retrieval;
-   DSP tools;
-   SDR tools;
-   GNU Radio tools;
-   visualization;
-   general LLM knowledge;
-   combinations of the above.

Requests are not required to belong to only one category.

The router will only select registered and available capabilities.

A hybrid approach may combine deterministic application rules with
constrained local-LLM semantic classification.

The router should detect missing required inputs before execution and
request clarification rather than inventing missing parameters.

### 6.5 Bounded Execution Orchestration

Application code will control execution order.

Example:

``` text
User request
   |
   v
Classification / routing
   |
   v
Validate required inputs
   |
   v
Retrieve relevant knowledge (if needed)
   |
   v
Run deterministic tool (if needed)
   |
   v
Generate validated figure (if needed)
   |
   v
Collect structured context/results
   |
   v
Local LLM explanation
```

The local LLM will not control unrestricted multi-step autonomous agent
loops in V1.

Execution should stop or safely fall back when:

-   required information is missing;
-   validation fails;
-   a tool fails;
-   a requested capability is unsupported.

The orchestration design should minimize unnecessary LLM calls to
improve local reliability and performance.

### 6.6 Hierarchical Tool Exposure

The local model should not be exposed to the complete tool catalogue for
every request.

RadioLab AI will use hierarchical tool exposure:

``` text
User request
   |
   v
High-level classification
   |
   v
Relevant capability/tool family
   |
   v
Small registered tool subset
   |
   v
Final selection when needed
```

Unrelated, disabled, or unavailable tools will not be exposed.

If a tool family cannot be identified reliably, RadioLab AI should
prefer clarification or a safe fallback rather than exposing every
available tool.

### 6.7 Tool Safety and Validation

All tool inputs will be validated by deterministic application/tool code
before execution.

LLM-generated parameters never bypass validation.

Validation may include:

-   required inputs;
-   data types;
-   numerical constraints;
-   valid ranges;
-   domain-specific constraints;
-   device capabilities;
-   runtime/software availability.

SDR tools will additionally validate relevant hardware/device
capabilities.

GNU Radio tools will additionally validate relevant flowgraph, block,
dependency, and runtime requirements.

Invalid input should result in a structured failure rather than silent
correction or uncontrolled execution.

### 6.8 Technical Figures and Visualization

RadioLab AI V1 will support technical figures generated from
deterministic tool outputs and validated numerical data.

The LLM will not directly fabricate technical plots.

Possible technical visualizations include:

-   time-domain signals;
-   FFT/spectrum plots;
-   PSD plots;
-   filter magnitude/phase responses;
-   sampling/reconstruction plots;
-   other data-driven DSP visualizations.

Future SDR capabilities may produce spectrum or waterfall visualizations
based on actual measurements.

Plotting components should validate relevant properties such as:

-   source data;
-   x/y dimensions;
-   finite values;
-   units;
-   axes;
-   labels;
-   scales.

Figures should be deterministic and testable.

The LLM may explain a figure after the underlying deterministic
component has produced it.

### 6.9 Selective Visualization

RadioLab AI will not generate a figure for every question.

A figure should be generated when:

-   the user explicitly requests a plot/graph/visualization; or
-   visualization provides clear technical value to the analysis.

Conceptual questions, simple calculations, and other responses that do
not materially benefit from visualization should not automatically
generate figures.

Visualization intent will be part of request classification/routing.

The architecture distinguishes:

``` text
Can the system generate a figure? -> capability
Should it generate one here?      -> routing decision
```

### 6.10 Observability and Diagnostics

RadioLab AI V1 will include structured local diagnostics across:

-   routing;
-   retrieval;
-   tool execution;
-   visualization;
-   LLM generation.

Diagnostics should capture useful development information such as:

-   selected capability/route;
-   selected tool;
-   component status;
-   structured error category;
-   execution timing.

User-facing error messages should remain concise and understandable.

Detailed developer diagnostics remain separate.

Logging should minimize unnecessary storage of:

-   raw user queries;
-   complete conversations;
-   source-document contents;
-   other potentially sensitive information.

Performance timing will help identify bottlenecks in local execution.

### 6.11 Dependency Boundaries

Clear boundaries will be maintained around major replaceable/external
components:

-   LLM runtime;
-   vector store;
-   tool framework;
-   visualization/output handling;
-   SDR integration;
-   GNU Radio integration.

Technology-specific implementations will be isolated behind RadioLab
AI-owned interfaces/adapters where this provides meaningful
architectural value.

Internal numerical libraries such as NumPy and SciPy may be used
directly inside deterministic DSP implementations without unnecessary
abstraction.

### 6.12 Testing and Capability Verification

RadioLab AI will distinguish:

``` text
Implemented != Verified != Supported
```

A feature is not considered supported simply because code exists.

Deterministic DSP tools will be tested against known numerical or
analytical results.

Technical figures will be tested primarily through their underlying data
and plotting consistency rather than LLM visual judgment.

Testing should verify relevant properties such as:

-   expected numerical outputs;
-   frequencies;
-   filter characteristics;
-   data dimensions;
-   axes;
-   units;
-   labels;
-   scales.

RAG evaluation should separately test:

-   retrieval quality;
-   correct source/chunk retrieval;
-   grounding;
-   citation/source-metadata correctness.

End-to-end local-model tests should evaluate:

-   routing;
-   parameter extraction;
-   tool selection;
-   missing-input handling;
-   final explanation.

A capability should only be presented as supported after satisfying
defined verification criteria.

## 7. Project Structure

RadioLab AI V1 will use a Python `src` layout.

Target high-level structure:

``` text
RadioLabAI/
|
├── src/
│   └── radiolab_ai/
│       ├── app/
│       ├── llm/
│       ├── rag/
│       │   ├── parsers/
│       │   ├── chunking/
│       │   ├── embeddings/
│       │   ├── vector_store/
│       │   └── retrieval/
│       ├── tools/
│       │   ├── core/
│       │   ├── dsp/
│       │   ├── sdr/
│       │   └── gnuradio/
│       ├── routing/
│       ├── orchestration/
│       ├── visualization/
│       ├── config/
│       └── diagnostics/
|
├── knowledge/
│   ├── official/
│   ├── references/
│   └── personal/
|
├── data/
│   ├── vector_store/
│   ├── artifacts/
│   ├── logs/
│   └── temp/
|
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── capability/
│   └── fixtures/
|
├── docs/
│   ├── phases/
│   └── architecture/
|
├── scripts/
│   ├── setup/
│   ├── knowledge/
│   └── development/
|
├── config/
│   └── defaults.toml
|
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

This is an architectural target. Empty directories do not need to be
created before they have a real purpose.

### 7.1 Separation of Responsibilities

``` text
knowledge/ -> original knowledge-source material
data/      -> generated/local runtime state
src/       -> application code
tests/     -> verification
docs/      -> project/architecture documentation
scripts/   -> support utilities outside normal runtime
```

### 7.2 Runtime Data

Generated/local runtime data will be separated from original source
documents.

Dedicated locations may include:

-   persistent vector-store data;
-   generated artifacts;
-   diagnostic logs;
-   temporary processing files.

Runtime paths should be configurable.

Generated and user-specific runtime data should not be committed to Git
by default.

### 7.3 Configuration

RadioLab AI will use centralized configuration management.

Safe project defaults may be stored in a version-controlled
configuration file such as:

``` text
config/defaults.toml
```

A `.env.example` file may document supported local environment variables
without real private values.

Machine-specific/private values may be stored locally through `.env` or
environment variables and must be excluded from Git.

Application components should consume validated settings through a
central configuration layer rather than independently reading
environment variables or hard-coded paths.

### 7.4 Documentation and Scripts

Phase history and current architecture documentation will be kept under
`docs/`.

Project-support scripts may be organized by purpose under `scripts/`.

Scripts are intended for setup, development, maintenance, knowledge
management, and similar support tasks that are not part of the normal
application runtime.

Core application behavior belongs under `src/radiolab_ai/`.

## 8. High-Level V1 Architecture

``` text
                              USER
                                |
                                v
                    Request Classification
                                |
                                v
                            Router
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
            RAG               Tools          General LLM
             |                  |
             |        +---------+---------+
             |        |         |         |
             |       DSP       SDR    GNU Radio
             |        |
             |        +---- Visualization
             |              when useful
             |
             +------------------+------------------+
                                |
                                v
                    Bounded Orchestration
                                |
                                v
                 Structured / Validated Context
                                |
                                v
                         Local LLM
                                |
                                v
                  Final Answer + Provenance
```

The system should preserve the origin of important information:

-   knowledge base -\> source-backed retrieved information;
-   tools -\> computed/measured/inspected results;
-   LLM knowledge -\> general model knowledge.

These origins must not be silently confused.

## 9. Deferred to Implementation and Evaluation

The following decisions are intentionally deferred because they require
real implementation testing:

-   final local LLM model;
-   final embedding model;
-   exact RAG chunk size;
-   exact chunk overlap;
-   retrieval top-K;
-   similarity thresholds;
-   whether reranking becomes necessary;
-   exact plotting validation rules for individual tools;
-   exact DSP tools migrated from `dsp-ai-agent`;
-   SDR hardware implementation details;
-   GNU Radio implementation details;
-   local performance benchmarks;
-   exact capability-verification thresholds;
-   detailed user-interface implementation.

Deferring these items is intentional and does not mean the architecture
is undefined.

## 10. Phase 0.4 Completion Criteria

Phase 0.4 can be marked complete when:

-   [x] Development environment assumptions are defined.
-   [x] Local LLM runtime and integration approach are defined.
-   [x] Local-model selection strategy is defined.
-   [x] Local-model capability limitations are explicitly considered.
-   [x] Knowledge source categories and initial V1 formats are defined.
-   [x] Parsing architecture is defined.
-   [x] Chunking strategy is defined.
-   [x] Local embedding strategy is defined.
-   [x] Local vector-storage approach is defined.
-   [x] Retrieval and metadata-filtering approach is defined.
-   [x] Source metadata and citation principles are defined.
-   [x] Knowledge-gap and general-model fallback behavior is defined.
-   [x] Common tool architecture and registry are defined.
-   [x] Previous DSP-project reuse strategy is defined.
-   [x] Structured tool results and failure behavior are defined.
-   [x] Request classification and routing are defined.
-   [x] Bounded execution orchestration is defined.
-   [x] Hierarchical tool exposure is defined.
-   [x] Deterministic tool validation is required.
-   [x] Technical visualization requirements are defined.
-   [x] Selective visualization behavior is defined.
-   [x] Observability and diagnostics are defined.
-   [x] Major dependency boundaries are defined.
-   [x] Testing and capability-verification principles are defined.
-   [x] Repository/project structure is defined.
-   [x] Runtime-data separation is defined.
-   [x] Configuration and secrets handling are defined.
-   [x] Documentation and scripts organization are defined.
-   [x] Implementation-dependent decisions are explicitly deferred.
-   [x] Phase 0.4 decisions are documented.

## 11. Phase Outcome

Phase 0.4 establishes the technical architecture for RadioLab AI V1
without prematurely implementing or tuning components that require
empirical testing.

The architecture is local-first, modular, testable, and intentionally
constrained around realistic local-model capabilities.

The next phase should begin implementation incrementally, with each
component understood, tested, and verified before the project moves to
the next major capability.
