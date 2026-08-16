from unittest.mock import patch

from radiolab_ai.app.conversation import get_response
from radiolab_ai.retrieval.chunk import KnowledgeChunk


def test_get_response_uses_retrieved_knowledge():
    chunk = KnowledgeChunk(
        content="Software Defined Radio moves radio processing into software.",
        metadata={
            "chunk_id": "test:1",
            "section": "What Is Software Defined Radio?",
        },
    )

    with (
        patch(
            "radiolab_ai.app.conversation.retrieve",
            return_value=[chunk],
        ) as mock_retrieve,
        patch(
            "radiolab_ai.app.conversation.build_grounded_prompt",
            return_value="grounded prompt",
        ) as mock_build_prompt,
        patch(
            "radiolab_ai.app.conversation.generate_response",
            return_value="Software Defined Radio response",
        ) as mock_generate_response,
    ):
        response = get_response("What is SDR?")

    mock_retrieve.assert_called_once_with("What is SDR?")
    mock_build_prompt.assert_called_once_with(
        "What is SDR?",
        [chunk],
    )
    mock_generate_response.assert_called_once_with(
        "grounded prompt"
    )

    assert response == "Software Defined Radio response"