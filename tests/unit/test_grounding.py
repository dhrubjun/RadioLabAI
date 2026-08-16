from radiolab_ai.app.grounding import build_grounded_prompt
from radiolab_ai.retrieval.chunk import KnowledgeChunk


def test_build_grounded_prompt_includes_context_and_question():
    chunks = [
        KnowledgeChunk(
            content="An ADC converts an analog signal into digital samples.",
            metadata={
                "section": "1.3 So What Is Software Defined Radio?",
            },
        )
    ]

    prompt = build_grounded_prompt(
        "What does an ADC do?",
        chunks,
    )

    assert "1.3 So What Is Software Defined Radio?" in prompt
    assert "An ADC converts an analog signal into digital samples." in prompt
    assert "What does an ADC do?" in prompt