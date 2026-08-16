from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.index_store import load_index, save_index
from radiolab_ai.retrieval.indexed_chunk import IndexedChunk


def test_save_and_load_index(tmp_path):
    index_path = tmp_path / "knowledge_index.json"

    indexed_chunks = [
        IndexedChunk(
            chunk=KnowledgeChunk(
                content="Test chunk content.",
                metadata={
                    "chunk_id": "test:1",
                    "source_id": "test_source",
                    "section": "Test Section",
                },
            ),
            embedding=[0.1, 0.2, 0.3],
        )
    ]

    save_index(indexed_chunks, index_path)
    loaded_chunks = load_index(index_path)

    assert len(loaded_chunks) == 1
    assert loaded_chunks[0].chunk.content == "Test chunk content."
    assert loaded_chunks[0].chunk.metadata["chunk_id"] == "test:1"
    assert loaded_chunks[0].chunk.metadata["source_id"] == "test_source"
    assert loaded_chunks[0].embedding == [0.1, 0.2, 0.3]