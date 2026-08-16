from unittest.mock import patch

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.document import KnowledgeDocument
from radiolab_ai.retrieval.index_builder import build_markdown_index


@patch("radiolab_ai.retrieval.index_builder.save_index")
@patch("radiolab_ai.retrieval.index_builder.generate_embedding")
@patch("radiolab_ai.retrieval.index_builder.chunk_markdown_by_section")
@patch("radiolab_ai.retrieval.index_builder.load_markdown_document")
def test_build_markdown_index(
    mock_load_document,
    mock_chunk_document,
    mock_generate_embedding,
    mock_save_index,
):
    document = KnowledgeDocument(
        content="Test content",
        metadata={"source_id": "test_source"},
    )

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

    mock_load_document.return_value = document
    mock_chunk_document.return_value = chunks
    mock_generate_embedding.side_effect = [
        [0.1, 0.2],
        [0.3, 0.4],
    ]

    build_markdown_index(
        "test_document.md",
        "test_index.json",
    )

    mock_load_document.assert_called_once_with("test_document.md")
    mock_chunk_document.assert_called_once_with(document)

    assert mock_generate_embedding.call_count == 2
    mock_generate_embedding.assert_any_call("First chunk")
    mock_generate_embedding.assert_any_call("Second chunk")

    saved_chunks = mock_save_index.call_args.args[0]

    assert len(saved_chunks) == 2
    assert saved_chunks[0].chunk.metadata["chunk_id"] == "test:1"
    assert saved_chunks[0].embedding == [0.1, 0.2]
    assert saved_chunks[1].chunk.metadata["chunk_id"] == "test:2"
    assert saved_chunks[1].embedding == [0.3, 0.4]

    assert mock_save_index.call_args.args[1] == "test_index.json"