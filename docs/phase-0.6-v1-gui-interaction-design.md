# Phase 0.6 - V1 GUI and Interaction Design

## 1. Goal

The goal of Phase 0.6 is to define a simple and practical V1 GUI and end-to-end interaction flow for RadioLab AI.

The interface should allow users to:

* Ask SDR and GNU Radio questions.
* Receive clear technical answers.
* View relevant calculations, tool results, figures, and sources.
* Inspect supporting source material.
* Provide additional information when clarification is required.
* Understand when RadioLab AI cannot reliably complete a request.
* Continue a technical discussion through follow-up questions.

Phase 0.6 defines the user experience only. GUI implementation and framework selection are outside this phase.

## 2. V1 Scope

The V1 GUI will cover:

* Main application window.
* Question input.
* Conversation display.
* Answer presentation.
* Source presentation and inspection.
* Technical tool results.
* Figures and visualizations.
* Clarification requests.
* Processing states.
* Failures and limitations.
* Basic local conversation history.
* New Chat behavior.
* Minimal Settings and About access.

V1 will not include:

* User accounts or cloud synchronization.
* File, image, audio, or GNU Radio flowgraph uploads.
* Collaboration or conversation sharing.
* Advanced conversation organization or search.
* Advanced plot interaction.
* Extensive appearance customization.
* Separate interfaces for internal tools or retrieval components.
* Developer-oriented controls or diagnostics.

## 3. Overall Interface

RadioLab AI V1 will use a single-window, conversation-centered desktop interface.

The application will contain:

* A minimal sidebar.
* A scrollable main conversation area.
* A multiline question input anchored at the bottom.

The sidebar will provide:

* New Chat.
* Recent conversations.
* Settings.
* About.

Internal components such as the knowledge base, SDR tools, GNU Radio tools, retrieval system, models, and developer logs will not appear as primary navigation destinations.

## 4. Question Input

The question input will:

* Accept multiline plain text.
* Provide a visible Send control.
* Support keyboard submission.
* Prevent empty requests from being submitted.

V1 will not support attachments, images, audio, or flowgraph uploads.

If required information is missing or ambiguous, RadioLab AI will request clarification within the conversation instead of guessing.

## 5. Answer Presentation

Each response will be presented as one integrated technical answer.

Depending on the question, a response may contain:

1. Main explanation.
2. Equations or calculations.
3. Code or technical examples.
4. Tool-generated results.
5. Figures.
6. Warnings or limitations.
7. Supporting sources.

Only relevant elements will be shown. Every answer does not need every section.

Raw retrieval output, internal prompts, model reasoning, function calls, and other developer-oriented information will not be shown to normal users.

## 6. Sources

Supporting sources will appear in a compact **Sources** section below the relevant answer.

Each source should identify available information such as:

* Source category.
* Document or source name.
* Relevant section or location.

Source categories may include official documentation, personal notes, and other approved knowledge-base material.

Sources will be inspectable directly within the conversation.

Expanding a source will show the actual relevant retrieved excerpt together with its identifying metadata. An LLM-generated summary will not be presented as if it were the original retrieved evidence.

RadioLab AI will not invent or imply supporting sources when none were retrieved.

## 7. Tool Results

When a supported technical tool is used:

* The result will be integrated into the answer.
* RadioLab AI will explain the result in understandable technical language.
* The interface will identify that the relevant result was produced or calculated using a tool when appropriate.

Raw function calls, arguments, execution metadata, and internal logs will remain hidden.

If a required tool fails or cannot perform the requested operation, RadioLab AI will communicate the limitation instead of silently replacing the result with an unsupported answer.

## 8. Figures and Visualizations

Figures will be generated only when they improve the technical explanation.

Figures will:

* Appear inline with the relevant response.
* Be accompanied by an explanation or interpretation.
* Identify the supporting tool or process when appropriate.

V1 does not require advanced plot interaction, editing, or figure-management features.

## 9. Processing State

After the user submits a question, the interface will immediately indicate that processing has started.

Simple user-facing states may include:

* Processing...
* Searching knowledge base...
* Running calculation...

Internal reasoning, retrieval chunk counts, routing decisions, model prompts, and other implementation details will remain hidden.

The GUI should remain responsive while processing.

A simple **Stop** control should allow the user to stop an active request.

## 10. Clarification Flow

Missing, ambiguous, or unusable input will be handled through normal conversation.

Example:

```text
User:
Calculate the wavelength.

RadioLab AI:
What frequency should I use? Please include the unit.

User:
915 MHz
```

RadioLab AI will retain the relevant context and continue the original request without requiring the user to repeat the complete question.

Clarification should only be requested when the missing information materially affects the reliability or correctness of the answer.

## 11. Failures and Limitations

RadioLab AI will clearly communicate situations such as:

* Insufficient supporting knowledge.
* Unsupported requests.
* Required tool failures.
* Operations not supported by available tools.
* Unsupported V1 input types.

When possible, the response should explain what the user can do next.

The system will not hide retrieval or required-tool failures by presenting unsupported LLM-generated results.

Stack traces, internal exceptions, and developer diagnostics will be handled through application logging rather than displayed in the normal conversation.

## 12. Conversation Behavior

Follow-up questions within the same conversation will retain relevant conversational context.

Selecting **New Chat** will start a fresh conversation context.

Basic conversation history will be stored locally so recent conversations can be reopened after restarting RadioLab AI.

V1 will not require:

* Conversation folders.
* Tags.
* Favorites.
* Conversation search.
* Sharing.
* Cloud synchronization.

## 13. Initial State

When RadioLab AI opens without an active conversation, or when New Chat is selected, the application will display a simple empty state focused on asking a question.

A small number of representative examples may be shown, such as:

* Explain what a Costas loop does.
* Calculate the wavelength at 915 MHz.
* What does a low-pass filter block do in GNU Radio?

The initial screen will not contain dashboards, tool launchers, knowledge-base statistics, or unsupported capabilities.

## 14. Settings

V1 will expose only settings required for normal local operation.

Low-level model, retrieval, generation, and tool parameters will not be exposed to normal users.

The exact operational settings will be determined during implementation when the runtime requirements are known.

Non-essential appearance customization is outside the V1 scope.

## 15. Response Actions

V1 response actions will remain minimal.

Users should be able to copy answers and relevant technical content where practical.

V1 will not require:

* Regenerate.
* Like/dislike feedback.
* Sharing.
* Editing previously submitted messages.

Users can refine a request through normal follow-up conversation.

## 16. Visual Direction

The interface will use a clean and restrained technical design focused on readability.

Technical elements such as:

* Code.
* Equations.
* Calculations.
* Figures.
* Warnings.
* Sources.

should have clear visual hierarchy.

Large messaging-style chat bubbles are not required. Technical responses should have enough horizontal space for engineering content.

V1 will initially use one sensible visual theme. Extensive theming, animation, branding, and decorative customization are outside scope.

## 17. V1 Interaction Flow

The primary interaction flow is:

```text
Application opens
        |
        v
Empty state / existing conversation
        |
        v
User submits question
        |
        v
Processing
        |
        +----------------------+
        |                      |
        v                      v
Clarification needed      Request can proceed
        |                      |
        v                      v
User provides input     Retrieval / tools if required
        |                      |
        +----------->----------+
                               |
                               v
                      Supported result?
                         /           \
                       Yes            No
                        |              |
                        v              v
                Integrated answer   Clear limitation
                        |
                        v
             Calculation/code if relevant
                        |
                        v
                 Figure if relevant
                        |
                        v
                      Sources
                        |
                        v
               Source inspection
                        |
                        v
                  Follow-up question
                        |
                +-------+-------+
                |               |
                v               v
        Continue context     New Chat
                                |
                                v
                         Fresh context
```

## 18. V1 Wireframe

```text
+--------------------------------------------------------------------------------+
| RadioLab AI                                                                    |
+----------------------+---------------------------------------------------------+
|                      |                                                         |
| + New Chat           |  You                                                    |
|                      |  Calculate the wavelength of a 915 MHz signal.           |
| Recent Conversations |                                                         |
|                      |  -----------------------------------------------------  |
| Costas Loop          |                                                         |
| FM Demodulation      |  RadioLab AI                                            |
| Sample Rate          |                                                         |
|                      |  The wavelength of a 915 MHz signal is approximately     |
|                      |  0.328 m, or 32.8 cm.                                   |
|                      |                                                         |
|                      |  Calculation                                            |
|                      |  ----------------------------------------------------   |
|                      |                                                         |
|                      |      lambda = c / f                                      |
|                      |                                                         |
|                      |      Frequency       915 MHz                             |
|                      |      Wavelength      ~0.328 m                            |
|                      |                                                         |
|                      |      Calculated using: SDR Calculation Tool              |
|                      |                                                         |
|                      |  [Figure, when relevant]                                 |
|                      |                                                         |
|                      |  Sources                                                |
|                      |  ----------------------------------------------------   |
|                      |                                                         |
|                      |  [1] Official Documentation                    [View]    |
|                      |      Relevant reference                                 |
|                      |                                                         |
|                      |  [2] Personal Notes                            [View]    |
|                      |      DSP Notes -> Relevant Section                      |
|                      |                                                         |
|                      |                                              [Copy]     |
|                      |                                                         |
| Settings             |  -----------------------------------------------------  |
| About                |                                                         |
|                      |  +---------------------------------------------------+  |
|                      |  | Ask about SDR or GNU Radio...                   |  |
|                      |  |                                                   |  |
|                      |  +-------------------------------------------[Send]--+  |
+----------------------+---------------------------------------------------------+
```

The conversation area will scroll independently while the question input remains accessible at the bottom.

## 19. Design Principles

The V1 GUI will follow these principles:

1. Keep the technical conversation as the primary focus.
2. Let users interact with their engineering problem rather than internal system components.
3. Show important provenance without exposing unnecessary implementation details.
4. Never imply that unsupported information has been verified.
5. Ask for clarification rather than making technically important assumptions.
6. Keep failures and limitations visible and understandable.
7. Add GUI features only when they provide clear value to the V1 user.
8. Prefer simplicity over unnecessary flexibility or customization.

## 20. Completion Criteria

Phase 0.6 is complete when:

* The V1 layout is defined.
* The primary interaction flow is defined.
* Question input behavior is defined.
* Answer presentation is defined.
* Source presentation and inspection are defined.
* Tool and figure presentation are defined.
* Clarification behavior is defined.
* Processing, failure, and limitation states are defined.
* Basic conversation behavior is defined.
* A wireframe-level representation is documented.

Technology-specific startup failures, infrastructure errors, GUI framework selection, runtime configuration details, and implementation-specific edge cases will be addressed during later implementation phases.
