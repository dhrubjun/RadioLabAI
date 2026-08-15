# Phase 0.7 - V1 Implementation Plan and Project Structure

## Status

Complete

## Goal

Define a practical implementation plan for RadioLab AI V1 that translates the approved architecture, knowledge/retrieval design, and GUI design into a clear development structure and sequence.

Phase 0.7 does not implement production functionality. It defines how V1 will be built and tested.

## Implementation Strategy

RadioLab AI V1 will be implemented incrementally in small, testable stages. Major components will be integrated progressively rather than built independently and combined only at the end.

Temporary mocks may be used to validate end-to-end flows before real subsystems are available. Mocks must be clearly identified and removed from the production path once the real component is integrated.

## V1 Implementation Stages

1. Application skeleton and environment setup
2. Basic GUI shell
3. End-to-end message flow using mock responses
4. Local LLM integration
5. Knowledge Base and retrieval integration
6. Answer validation, source handling, and fallback behavior
7. V1 engineering-tool integration
8. Full system integration and stabilization

Each stage must reach a working, tested checkpoint before the next major stage begins.

## Initial V1 Knowledge Scope

V1 will initially target the material represented by Chapters 1-6 of the `sdr-with-gnu-radio` learning project:

1. What is Software Defined Radio
2. Understanding Signals
3. Sampling and Aliasing
4. Complex Numbers for SDR
5. I and Q Signals
6. From Time Domain to Frequency Domain

This material will be treated as a curated knowledge source, but RadioLab AI will maintain its own ingestion and indexing process rather than depending on the external repository at runtime.

Knowledge will be integrated incrementally, beginning with a small subset and expanding only after retrieval quality is validated.

## Project Structure

V1 will use a simple modular, `src`-based Python structure organized by responsibility.

```text
RadioLabAI/
├── docs/
├── src/
│   └── radiolab_ai/
│       ├── gui/
│       ├── app/
│       ├── llm/
│       ├── retrieval/
│       ├── tools/
│       ├── config/
│       └── utils/
├── knowledge_base/
│   ├── sdr_book/
│   ├── notes/
│   └── other_approved_sources/
├── tests/
│   ├── unit/
│   └── integration/
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
└── README.md
```

Additional directories for configuration or generated runtime data will be introduced only when required.

## Module Responsibilities

### `app/`

Acts as the orchestration layer. It coordinates request validation, routing, retrieval, engineering-tool calls, LLM interaction, fallback behavior, and response assembly.

### `llm/`

Provides a small isolated interface to the selected local language model. It handles model/runtime interaction, prompt-related inputs, generation settings, responses, and model-specific failures.

### `retrieval/`

Handles ingestion, chunking, indexing, similarity search, relevance handling, and source metadata for approved knowledge sources. It returns context and retrieval status but does not generate final answers.

### `tools/`

Contains deterministic and independently testable engineering calculations. Tools validate required inputs and return structured results or clear failure states. The LLM may explain tool results but does not replace deterministic calculations when an approved tool is available.

### `gui/`

Implements the approved V1 interface and interaction flow. It collects user input and presents responses, sources, errors, and status information without containing model, retrieval, or engineering-processing logic.

### `config/` and `utils/`

Configuration handling will be centralized and validated. Secrets will not be stored in committed configuration files. `utils/` will contain only genuinely shared helpers and will not become a general-purpose dumping ground.

## Error Handling and Logging

Errors will be handled within the module where they occur and passed to the orchestration layer using consistent failure states. The orchestration layer will convert them into clear user-facing messages.

Standard Python logging will be sufficient for V1. Important events, warnings, and failures will be logged without exposing secrets or unnecessarily recording user content. Internal tracebacks will not be shown directly to users.

## Testing Strategy

V1 will use:

- unit tests for deterministic components;
- integration tests for interactions between major modules; and
- a concise acceptance-test set for complete user-facing workflows.

Retrieval quality will also be tested independently from LLM answer generation.

Relevant tests must pass before an implementation stage is considered complete. V1 will prioritize meaningful behavioral tests rather than an arbitrary code-coverage target.

## Environment and Dependencies

RadioLab AI V1 will use a dedicated Python virtual environment.

Runtime and development dependencies will be separated into `requirements.txt` and `requirements-dev.txt`. Dependencies will be introduced incrementally and pinned once a stable working environment is established.

Additional environment-management or containerization tools will not be introduced unless technically necessary. One supported Python version will be documented after compatibility is verified.

## Runtime and Generated Data

Approved knowledge sources will remain separate from generated artifacts such as vector indexes, embeddings, caches, temporary files, and logs.

Re-creatable runtime artifacts will not be committed to Git by default and will be excluded through `.gitignore`. Log storage will remain simple and bounded.

## Development Checkpoints and Git Workflow

A major implementation stage is complete only when:

- its intended behavior works;
- relevant tests pass;
- known limitations are recorded; and
- the work reaches a stable committed and pushed checkpoint.

Commits will be small and focused around meaningful units of working progress. Large mixed-purpose commits and unclear commit messages will be avoided.

Implementation work after Phase 0.7 will be tracked using focused GitHub issues aligned primarily with the major implementation stages.

## Completion Criteria

Phase 0.7 is complete when the V1 implementation plan is sufficiently defined to begin coding without reopening major architecture questions.

The implementation sequence, module boundaries, initial knowledge scope, project structure, testing strategy, environment approach, runtime-data handling, error/logging approach, and development workflow are defined.

Minor implementation details may still be decided during development where they do not change the approved V1 architecture or scope.
