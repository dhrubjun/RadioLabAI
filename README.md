# RadioLabAI

RadioLabAI is a local AI assistant designed to help students, engineers, researchers, and hobbyists working with Software Defined Radio (SDR) and GNU Radio.

The project focuses on providing a simple assistant that can run locally after the initial setup. This is useful in situations where users cannot or do not want to send their technical work, project details, or questions to an external AI service.

## Project Goal

The goal of RadioLabAI is to build a local AI assistant that can:

* Answer basic questions about Software Defined Radio.
* Answer basic questions about GNU Radio.
* Explain technical concepts in beginner-friendly language.
* Provide responses that are clear and natural.
* Run locally after the required initial setup.
* Respond within a reasonable amount of time on the target hardware.
* Clearly indicate when it does not know an answer instead of inventing information.

The first version will be intentionally simple. More advanced capabilities can be added gradually after the basic system is working and understood.

## Target Users

RadioLabAI is intended for:

* Students learning SDR or GNU Radio.
* Engineers working with SDR systems.
* Researchers experimenting with radio communication systems.
* Hobbyists learning or building SDR projects.

## Version 1 Scope

The first version of RadioLabAI will focus on text-based questions and answers related to basic SDR and GNU Radio concepts.

The initial development platform is Windows.

## Version 1 Limitations

Version 1 will not:

* Analyse GNU Radio flowgraphs or diagrams provided by users.
* Detect mistakes or flaws in a user's GNU Radio model.
* Automatically understand an existing SDR project.
* Replace detailed engineering analysis or validation.
* Guarantee that every generated answer is correct.

These limitations may be reconsidered in later phases of the project.

## Success Criteria

The initial version will be evaluated based on:

1. Technical correctness of its answers.
2. Response time.
3. Ability to acknowledge when it does not know something rather than providing an unreliable answer.

## Project Status

RadioLabAI is currently in V1 implementation.

The project is being developed in small phases. Each phase will be documented so that important decisions, limitations, experiments, and changes can be tracked over time.


## Development Setup

RadioLab AI V1 currently uses Python 3.10.

Create and activate a virtual environment on Windows PowerShell:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1

```

Install the development dependencies and the project in editable mode:

```powershell
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

Run the application:

```powershell
python -m radiolab_ai
```

Run the tests:

```powershell
pytest
```