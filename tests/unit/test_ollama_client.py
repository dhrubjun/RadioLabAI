from unittest.mock import patch

import pytest

from radiolab_ai.llm.ollama_client import LLMError, generate_response


def test_generate_response_returns_model_content():
    fake_response = {
        "message": {
            "content": "SDR means Software Defined Radio."
        }
    }

    with patch(
        "radiolab_ai.llm.ollama_client.ollama.chat",
        return_value=fake_response,
    ):
        response = generate_response("What is SDR?")

    assert response == "SDR means Software Defined Radio."


def test_generate_response_raises_llm_error_when_ollama_fails():
    with patch(
        "radiolab_ai.llm.ollama_client.ollama.chat",
        side_effect=RuntimeError("Ollama unavailable"),
    ):
        with pytest.raises(LLMError):
            generate_response("What is SDR?")