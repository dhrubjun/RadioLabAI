from unittest.mock import patch

from radiolab_ai.retrieval.embeddings import generate_embedding


@patch("radiolab_ai.retrieval.embeddings.ollama.embed")
def test_generate_embedding(mock_embed):
    mock_embed.return_value = {
        "embeddings": [
            [0.1, 0.2, 0.3]
        ]
    }

    embedding = generate_embedding("test text")

    mock_embed.assert_called_once_with(
        model="nomic-embed-text",
        input="test text",
    )

    assert embedding == [0.1, 0.2, 0.3]