from unittest.mock import patch

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.hybrid_search import hybrid_search


@patch("radiolab_ai.retrieval.hybrid_search.semantic_search")
@patch("radiolab_ai.retrieval.hybrid_search.search_chunks")
def test_hybrid_search_combines_keyword_and_semantic_rankings(
    mock_keyword_search,
    mock_semantic_search,
):
    chunk_a = KnowledgeChunk(
        content="Chunk A",
        metadata={"chunk_id": "test:a"},
    )
    chunk_b = KnowledgeChunk(
        content="Chunk B",
        metadata={"chunk_id": "test:b"},
    )
    chunk_c = KnowledgeChunk(
        content="Chunk C",
        metadata={"chunk_id": "test:c"},
    )

    chunks = [chunk_a, chunk_b, chunk_c]

    mock_keyword_search.return_value = [
        chunk_a,
        chunk_b,
        chunk_c,
    ]

    mock_semantic_search.return_value = [
        chunk_c,
        chunk_a,
        chunk_b,
    ]

    results = hybrid_search(
        "test query",
        chunks,
        chunk_embeddings=[
            [1.0, 0.0],
            [0.0, 1.0],
            [0.5, 0.5],
        ],
        top_k=3,
    )

    assert [chunk.metadata["chunk_id"] for chunk in results] == [
        "test:a",
        "test:c",
        "test:b",
    ]