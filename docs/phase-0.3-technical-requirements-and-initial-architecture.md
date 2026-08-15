# Phase 0.3 - Technical Requirements and Initial Architecture

**Project:** RadioLab AI
**Phase:** 0.3
**Status:** In Progress

## 1. Purpose

The purpose of Phase 0.3 is to define the technical requirements and initial architecture for RadioLab AI V1.

This phase describes what the first version of the system should technically support, how the major components should interact, and where the boundaries of V1 should remain.

The purpose is not to select every implementation technology. Decisions such as the exact local language model, model runtime, GUI framework, retrieval technology, embedding model, storage format, and prompt format will be made in later phases after appropriate investigation and testing.

---

## 2. V1 Technical Direction

RadioLab AI V1 will be a local Windows-based assistant focused on SDR and GNU Radio.

The system will:

* Run locally on a Windows computer.
* Support offline core operation after initial setup.
* Use a locally running language model.
* Use an approved local SDR and GNU Radio knowledge base.
* Support a limited set of deterministic local SDR calculation tools.
* Maintain enough conversation context to support follow-up questions.
* Support local conversation storage.
* Preserve source and calculation provenance where practical.
* Avoid requiring a cloud-based AI service during normal operation.

V1 is intended to establish a simple but extensible foundation. Advanced functionality will be added incrementally rather than attempting to build the complete future system in the first version.

---

# 3. Technical Requirements

## TR-01: Local Execution

RadioLab AI V1 will run locally on a Windows computer.

After the initial installation and setup, the core question-answering functionality should work without requiring an internet connection.

User questions and project-related information should not need to be sent to an external cloud-based AI service.

---

## TR-02: Hardware Compatibility

V1 should be designed to run on a reasonably capable Windows computer without requiring specialized server hardware.

CPU-only operation should be possible.

A compatible GPU may be used to improve inference speed but should not be mandatory for the basic functionality of V1.

Exact minimum and recommended RAM, storage, CPU, and GPU requirements will be determined after candidate local language models have been selected and benchmarked.

---

## TR-03: Local Language Model

V1 will use a language model that can run completely locally on the user's Windows computer.

The model should be capable of answering general SDR and GNU Radio questions and explaining technical concepts in beginner-friendly language.

The exact model will not be fixed during Phase 0.3.

Candidate models will later be evaluated based on factors including:

* Technical accuracy
* Response quality
* Inference speed
* Hardware requirements
* Licensing
* Suitability for offline operation

RadioLab AI should remain conceptually separate from the underlying language model. The language model is one component of the overall system.

---

## TR-04: Local Technical Knowledge

RadioLab AI should support a local knowledge base containing trusted SDR and GNU Radio information.

The knowledge base should work without an internet connection during normal operation.

Relevant information from the knowledge base should be retrievable and usable during response generation.

Only material that the project owns, creates, or is legally permitted to use should be included.

Preference should be given to:

* Project-created material
* Public-domain material
* Appropriately licensed open material
* Other material for which suitable permission has been established

Copyrighted material should not be copied into the knowledge base unless its license or permission allows the intended use.

The exact knowledge sources, formats, retrieval methods, and implementation technology will be determined later.

---

## TR-05: Local Data Processing and Privacy

RadioLab AI V1 should process user questions and generate responses locally.

During normal offline operation, user questions, generated responses, local knowledge, and conversation information should not be transmitted to external AI services or cloud servers.

The core question-answering functionality should not depend on external telemetry, analytics, or a cloud account.

Any future feature requiring network access should be clearly identified and should not silently transmit user or project information.

Internet access may still be required during installation or setup for purposes such as downloading dependencies or approved local models.

---

## TR-06: User Interface Separation

The user-interface layer should remain separate from the core RadioLab AI functionality.

A simple CLI may be used during early development and testing.

V1 may also provide a basic Windows GUI for entering questions and viewing responses.

The interface should not contain the core model, retrieval, tool, or conversation-management logic.

This separation should allow additional interfaces to be introduced later without requiring a major redesign of the underlying system.

---

## TR-07: Response Performance

RadioLab AI should provide responses within a practical amount of time on supported hardware.

Performance should be measured using defined test hardware and representative SDR and GNU Radio questions.

Useful measurements may include:

* Time until response generation begins
* Total response-generation time
* Knowledge-retrieval time
* Tool-execution time

Exact performance targets will be established after candidate local models and hardware configurations have been benchmarked.

---

## TR-08: Technical Accuracy and Uncertainty

RadioLab AI should prioritize technically correct answers over producing an answer at all costs.

When sufficient information is unavailable, or when the system cannot determine an answer with reasonable confidence, it should communicate the limitation rather than intentionally presenting unsupported information as fact.

Relevant approved knowledge should be used when available.

Use of trusted knowledge does not guarantee that every LLM-generated response will be correct.

Technical accuracy should later be evaluated using representative SDR and GNU Radio questions.

RadioLab AI will not claim that LLM hallucinations can be completely eliminated.

---

## TR-09: Knowledge Source Licensing and Provenance

Every external source added to the RadioLab AI knowledge base should have its origin and usage rights documented.

The project should maintain sufficient provenance information to determine:

* Where the material came from
* Who created it, where applicable
* Its license or usage permission
* Relevant version or date information
* Other restrictions relevant to its use

Material with unclear or incompatible usage rights should not be added until those rights have been verified.

Public availability of material does not automatically mean that the material is public domain or freely reusable.

---

## TR-10: Modular System Design

RadioLab AI should use a modular architecture.

Major responsibilities should be logically separated, including:

* User interaction
* Core application coordination
* Knowledge retrieval
* Knowledge storage
* Local SDR tools
* Local language-model interaction
* Conversation management
* Configuration
* Diagnostics

Components should communicate through clear boundaries so individual technologies can later be replaced or improved without requiring a complete redesign.

The initial implementation should remain as simple as practical and should avoid unnecessary abstraction or complexity.

---

## TR-11: Configuration Management

Important configurable values should remain separate from the main application logic.

Settings that may vary between installations, models, or experiments should not be unnecessarily hard-coded throughout the source code.

V1 may use a simple local configuration mechanism.

The exact configuration format will be selected during implementation.

Sensitive configuration values, if introduced in the future, should not be committed directly to the Git repository.

---

## TR-12: Local Logging and Diagnostics

RadioLab AI should provide local diagnostic information sufficient to investigate errors and performance problems.

Logs should remain on the local computer and should not automatically be transmitted to an external service.

Normal diagnostic logs should avoid unnecessarily storing:

* Full user questions
* Full generated responses
* Complete retrieved documents
* Other potentially sensitive user information

More detailed logging may be intentionally enabled during controlled development or evaluation.

Diagnostic logging must remain separate from conversation history.

---

## TR-13: Conversation Context and History

RadioLab AI should maintain sufficient conversation context to understand follow-up questions referring to earlier parts of a conversation.

Conversation context should be handled locally.

Conversation history used for contextual understanding should remain logically separate from diagnostic logs.

The amount of history supplied to the local language model should account for:

* Model context-window limitations
* Memory usage
* Performance
* Relevance

The exact context-management strategy will be determined later.

---

## TR-14: Local Conversation Persistence

RadioLab AI should support storing conversation history locally so users can return to earlier conversations.

Users should be able to:

* Start a new conversation
* Reopen a stored conversation
* Continue an earlier conversation
* Delete stored conversations

Stored conversation history should remain local.

The complete stored conversation does not need to be supplied to the language model for every request.

The exact storage format and retention behavior will be determined later.

---

## TR-15: Error and Failure Handling

RadioLab AI should handle expected technical failures gracefully.

Where possible, the user should receive a clear and understandable error message rather than an unprocessed technical traceback.

Failures in one component should not unnecessarily cause the entire application to fail when meaningful recovery is possible.

Detailed technical information may be recorded in local diagnostic logs.

The system should not hide important component failures by presenting an apparently normal AI response when a required component has failed.

---

## TR-16: Repeatable Evaluation

RadioLab AI should have a repeatable evaluation process for assessing system quality and performance.

The evaluation set should contain representative SDR and GNU Radio questions, including:

* Basic technical questions
* Conceptual explanations
* Follow-up questions
* Questions requiring deterministic calculations
* Cases involving insufficient information
* Cases requiring uncertainty handling

Evaluation should consider factors such as:

* Technical correctness
* Relevance
* Clarity
* Handling of uncertainty
* Response performance
* Appropriate knowledge retrieval
* Appropriate tool use

The same or equivalent evaluation set should be usable when comparing different models, retrieval approaches, configurations, and later RadioLab AI versions.

Evaluation results should be documented so improvements and regressions can be measured.

---

## TR-17: Replaceable AI Components

The local language model and knowledge-retrieval implementation should be replaceable without requiring major changes to unrelated parts of RadioLab AI.

The architecture should support experimentation with different compatible:

* Local models
* Model configurations
* Model runtimes
* Retrieval approaches

V1 does not need to provide end users with a sophisticated multi-model management system.

This requirement primarily exists to prevent unnecessary architectural lock-in.

---

## TR-18: Basic Local SDR Calculation Tools

RadioLab AI V1 should support a limited set of deterministic local tools for common SDR-related calculations.

Where an appropriate tool exists, deterministic calculations should not depend solely on LLM-generated arithmetic or reasoning.

Potential V1 calculation areas may include:

* Sample-rate calculations
* Decimation and interpolation
* Frequency and wavelength conversion
* Linear and dB conversion
* Sampling and Nyquist-related calculations
* Basic FFT and frequency-bin calculations

The exact V1 tool set will be defined later.

Tool execution should remain local.

Advanced functionality such as GNU Radio flowgraph execution, flowgraph analysis, SDR hardware control, and arbitrary user-code execution is outside V1 scope.

---

## TR-19: Answer Provenance and Source Visibility

RadioLab AI should preserve and expose provenance information for technical answers where practical.

Information retrieved from the local knowledge base should retain references to its approved source.

Deterministic calculations should be identifiable as outputs from local SDR tools.

The system should not falsely identify LLM-generated statements as independently verified information.

Project-created notes are valid knowledge sources and should have appropriate provenance information.

A project-created source may contain metadata such as:

* Source ID
* Title
* Author
* Source type
* Topic
* Original file
* Usage rights
* Creation or revision date

For example:

`NOTE-001 - Project-created note`

The user-facing interface may show a simpler source description while more complete provenance metadata is retained internally.

---

## TR-20: Input Validation and Clarification

RadioLab AI should validate user input when required before retrieval, tool execution, or final response generation.

If required information is:

* Missing
* Incomplete
* Ambiguous
* Invalid for a selected tool
* In an unsupported format

the system should request clarification rather than silently guessing.

If a user communicates in an unsupported language, RadioLab AI should clearly request input in a supported language rather than silently misinterpreting the message.

Supported languages will be determined through later model selection and testing.

---

# 4. Initial V1 Architecture

The initial logical architecture is:

```text
                         USER
                           |
                           v
                  +------------------+
                  |  User Interface  |
                  |    CLI / GUI     |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Core Application |
                  +--------+---------+
                           |
                    Input Validation
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
 +----------------+ +----------------+ +----------------+
 | Conversation   | |   Knowledge    | | Local SDR      |
 | Management     | |   Retrieval    | | Calculation    |
 +-------+--------+ +-------+--------+ | Tools          |
         |                  |          +-------+--------+
         v                  v                  |
 +---------------+   +---------------+         v
 | Local         |   | Local         |    Deterministic
 | Conversation  |   | Knowledge     |       Result
 | Storage       |   | Base          |
 +---------------+   +---------------+
                            |
          +-----------------+-----------------+
                            |
                            v
                Response Context Construction
                            |
                            v
                  +--------------------+
                  | Local LLM Interface|
                  +---------+----------+
                            |
                            v
                  +--------------------+
                  | Local LLM / Runtime|
                  +---------+----------+
                            |
                            v
                     Generated Answer
                            |
                            v
                    Core Application
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          Conversation            Diagnostics
            Storage                 / Logs
                 |
                 v
            User Interface
                 |
                 v
                USER
```

Local configuration supports the application components but is not itself part of the normal question-answering flow.

---

# 5. Architecture Decisions

## A-01: Overall Local Modular Architecture

RadioLab AI V1 will use a modular, fully local architecture consisting of:

* User-interface layer
* Core application logic
* Local knowledge-retrieval system
* Local knowledge base
* Local SDR calculation tools
* Local LLM interface
* Local language model/runtime
* Conversation management and storage
* Local configuration
* Local diagnostics

Normal core operation should not require a cloud AI service.

---

## A-02: User Interface Responsibility

The user-interface layer will handle user interaction and presentation.

Core AI behavior, retrieval, model interaction, tool execution, and conversation-management logic should remain outside the UI.

This should allow CLI and GUI interfaces to use the same underlying RadioLab AI functionality.

---

## A-03: Core Application Responsibility

The Core Application will coordinate the main question-answering workflow.

Its responsibilities include:

* Receiving user input
* Coordinating input validation
* Obtaining relevant conversation context
* Requesting knowledge retrieval
* Requesting SDR tool execution where appropriate
* Constructing response context
* Requesting model inference
* Handling component failures
* Returning the result to the user interface

The Core Application should coordinate these components without becoming tightly coupled to a particular model, retrieval technology, or interface.

---

## A-04: Knowledge Retrieval Responsibility

The Knowledge Retrieval component will search the approved local knowledge base and return relevant information to the Core Application.

It should not generate the final natural-language response.

The retrieval implementation should remain replaceable so different approaches can later be evaluated.

---

## A-05: Local Knowledge Base Responsibility

The Local Knowledge Base will contain or represent approved SDR and GNU Radio information available for retrieval.

All included material must comply with licensing and provenance requirements.

The knowledge base should remain local and preserve sufficient source metadata.

The knowledge base may be logically divided into areas such as:

```text
knowledge/
├── notes/
│   ├── sdr/
│   └── gnuradio/
├── public-domain/
├── open-licensed/
└── metadata/
```

The final structure may change during implementation.

Knowledge may also be categorized by topic, for example:

* SDR fundamentals
* GNU Radio
* DSP
* Sampling
* Modulation
* Filtering

Source type and technical topic are separate concepts.

Original source material and its searchable representation may be processed or stored differently as long as provenance remains traceable.

The storage and search technology will be selected later.

---

## A-06: Local SDR Calculation Tools Responsibility

The Local SDR Calculation Tools component will perform a limited set of well-defined deterministic SDR calculations.

The Core Application will invoke an appropriate tool when a supported calculation is required.

Tool-generated numerical results should be treated as authoritative calculation outputs.

The LLM may:

* Explain the result
* Contextualize the result
* Present the result clearly

The LLM should not independently replace or alter a successful deterministic tool result.

If:

* No suitable tool exists
* Required inputs are missing
* Input is invalid
* Tool execution fails

the Core Application should communicate that status to the response-generation process.

RadioLab AI must not present an unverified LLM-generated calculation as though it were a tool-verified result.

Where appropriate, the system may instead request missing information or provide a conceptual explanation.

---

## A-07: Local LLM Interface Responsibility

The Local LLM Interface will provide a boundary between RadioLab AI and the selected local model/runtime.

The Core Application should communicate with the language model through this interface rather than depending directly on model-specific implementation details.

The interface may receive:

* User question
* Relevant conversation context
* Retrieved approved knowledge
* Provenance information
* Verified SDR tool results
* Applicable system instructions
* Relevant failure or limitation information

It should return the generated output or an appropriate failure status.

Compatible models and runtimes should be replaceable with limited impact on unrelated components.

---

## A-08: Conversation Management and Storage

The Conversation Management component will maintain conversation state required for follow-up interactions and manage locally persisted conversations.

Conversation information will remain separate from diagnostic logging.

The system should support creating, reopening, continuing, and deleting conversations.

The complete stored conversation does not need to be provided to the LLM for every request.

Context selection should eventually consider relevance, model limitations, memory use, and performance.

---

## A-09: Configuration Responsibility

RadioLab AI will use a local configuration mechanism for settings that may vary between installations, models, experiments, or runtime environments.

Application components should obtain configurable values through the defined configuration mechanism rather than unnecessarily hard-coding them.

The exact configuration format will be selected during implementation.

---

## A-10: Diagnostics and Logging Responsibility

RadioLab AI will use local diagnostics and logging for:

* Debugging
* Error investigation
* Performance measurement
* Component-status information

Diagnostic logs should avoid unnecessary storage of user content.

Logs may record identifiers such as source IDs or tool names without storing entire documents or conversations.

Detailed logging may be intentionally enabled during controlled development or evaluation.

Diagnostic logging will remain separate from conversation storage.

---

## A-11: Response Context and Prompt Construction

The Core Application will construct the response context supplied to the Local LLM Interface.

The context may include:

* System instructions
* Current user question
* Relevant conversation history
* Retrieved approved knowledge
* Source/provenance information
* Verified SDR tool results
* Component failure or limitation information

The response context should distinguish between:

* User-provided information
* Retrieved knowledge
* Deterministic tool outputs
* System instructions

The exact prompt format and context-construction strategy will be determined through implementation and evaluation rather than fixed during Phase 0.3.

---

# 6. Example V1 Question Flow

Consider the following question:

> I have a 4 MHz sample rate and decimate by 8. What will my new sample rate be, and why might I need a low-pass filter?

A possible V1 processing flow is:

```text
User Question
     |
     v
Input Validation
     |
     +--> Conversation context
     |
     +--> Knowledge Retrieval
     |       |
     |       +--> Approved information about
     |            decimation and filtering
     |
     +--> SDR Calculation Tool
             |
             +--> 4 MHz / 8
             |
             +--> 500 kHz
     |
     v
Response Context
     |
     +--> User question
     +--> Relevant conversation context
     +--> Retrieved knowledge + source IDs
     +--> Tool-verified result
     |
     v
Local LLM
     |
     v
Generated explanation
     |
     v
User
```

A future interface could present provenance in a form similar to:

```text
Output sample rate: 500 kHz
Calculated by: Sample Rate Tool

Explanation:
...

Sources:
- NOTE-005: Decimation Notes
- DOC-003: Approved SDR Reference
```

The exact user-interface presentation will be determined later.

---

# 7. V1 Knowledge Organization

The knowledge system should remain organized rather than becoming a single uncontrolled collection of documents.

Knowledge may be separated by source type and categorized by technical topic.

Examples of source types include:

* Project-created notes
* Public-domain material
* Appropriately open-licensed material

Examples of technical topics include:

* SDR fundamentals
* GNU Radio
* DSP
* Sampling
* Modulation
* Filters

Every approved source should remain traceable through appropriate metadata.

A project-created note may, for example, be identified as:

```text
Source ID: NOTE-001
Title: Notes on IQ Sampling
Source Type: Project-created note
Topic: Sampling
Original File: notes/sdr/iq-sampling.md
Usage Rights: Project-owned
```

The exact metadata schema will be defined in a later phase.

---

# 8. V1 Boundaries

RadioLab AI V1 will not attempt to provide every possible future capability.

The following are outside the current V1 scope:

* Analysis of uploaded GNU Radio flowgraphs or diagrams
* Automatic detection of errors in GNU Radio designs
* GNU Radio flowgraph execution
* SDR hardware control
* Arbitrary user-code execution
* A comprehensive set of all possible SDR calculation tools
* Unlimited conversation context
* Dependence on cloud AI services for normal operation
* Inclusion of material with unclear or incompatible usage rights
* A guarantee that every LLM-generated statement is correct

These limitations may be reconsidered in later phases or future versions.

---

# 9. Decisions Intentionally Deferred

Phase 0.3 does not select the following implementation details:

* Exact local language model
* Model size or quantization
* Local model runtime
* Exact minimum hardware requirements
* GUI framework
* Knowledge-storage technology
* Retrieval algorithm
* Vector database, if any
* Embedding model, if any
* Document chunking strategy
* Conversation-storage format
* Configuration-file format
* Prompt format
* Context-selection algorithm
* Exact V1 SDR tool list
* Supported languages
* Final source metadata schema

These decisions should be made through focused investigation, implementation, and testing in later phases.

---

# 10. Phase 0.3 Completion Criteria

Phase 0.3 can be considered complete when:

* The V1 technical requirements have been documented.
* The initial logical architecture has been documented.
* Responsibilities of the major system components are clearly defined.
* Local execution and privacy expectations are documented.
* Knowledge licensing and provenance expectations are documented.
* SDR calculation tool behavior and limitations are documented.
* Conversation context and storage requirements are documented.
* Input validation and failure-handling expectations are documented.
* V1 scope boundaries are documented.
* Implementation decisions intentionally deferred to later phases are clearly identified.
* The document has been reviewed for consistency with the Phase 0.1 project definition.
* The Phase 0.3 GitHub issue has been updated or closed after the phase is completed.

---

## 11. Current Status

**Phase 0.3 Status: Complete**

The technical requirements and initial architecture for Phase 0.3 have been defined and reviewed.
