from unittest.mock import patch

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.indexed_chunk import IndexedChunk
from radiolab_ai.retrieval.retriever import retrieve


@patch("radiolab_ai.retrieval.retriever.hybrid_search")
@patch("radiolab_ai.retrieval.retriever.load_index")
def test_retrieve_loads_index_and_runs_hybrid_search(
    mock_load_index,
    mock_hybrid_search,
):
    chunk = KnowledgeChunk(
        content="Test content",
        metadata={"chunk_id": "test:1"},
    )

    mock_load_index.return_value = [
        IndexedChunk(
            chunk=chunk,
            embedding=[0.1, 0.2],
        )
    ]

    mock_hybrid_search.return_value = [chunk]

    results = retrieve(
        "test query",
        index_path="test_index.json",
        top_k=1,
    )

    mock_load_index.assert_called_once_with("test_index.json")

    mock_hybrid_search.assert_called_once_with(
        "test query",
        [chunk],
        [[0.1, 0.2]],
        top_k=1,
    )

    assert results == [chunk]