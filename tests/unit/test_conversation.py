from unittest.mock import patch

from radiolab_ai.app.conversation import get_response


def test_get_response_uses_llm_response():
    with patch(
        "radiolab_ai.app.conversation.generate_response",
        return_value="Software Defined Radio response",
    ):
        response = get_response("What is SDR?")

    assert response == "Software Defined Radio response"