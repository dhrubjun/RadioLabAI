from unittest.mock import patch

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.semantic_search import (
    _cosine_similarity,
    semantic_search,
)


def test_cosine_similarity_identical_vectors():
    score = _cosine_similarity(
        [1.0, 0.0],
        [1.0, 0.0],
    )

    assert score == 1.0


@patch("radiolab_ai.retrieval.semantic_search.generate_embedding")
def test_semantic_search_ranks_most_similar_chunk_first(
    mock_generate_embedding,
):
    mock_generate_embedding.return_value = [1.0, 0.0]

    chunks = [
        KnowledgeChunk(
            content="First chunk",
            metadata={"chunk_id": "test:1"},
        ),
        KnowledgeChunk(
            content="Second chunk",
            metadata={"chunk_id": "test:2"},
        ),
    ]

    chunk_embeddings = [
        [0.0, 1.0],
        [1.0, 0.0],
    ]

    results = semantic_search(
        "test query",
        chunks,
        chunk_embeddings,
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].metadata["chunk_id"] == "test:2"