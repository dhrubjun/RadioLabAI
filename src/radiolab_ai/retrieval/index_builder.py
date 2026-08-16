from pathlib import Path

from radiolab_ai.retrieval.chunker import chunk_markdown_by_section
from radiolab_ai.retrieval.embeddings import generate_embedding
from radiolab_ai.retrieval.index_store import save_index
from radiolab_ai.retrieval.indexed_chunk import IndexedChunk
from radiolab_ai.retrieval.markdown_loader import load_markdown_document


def build_markdown_index(
    document_path: str | Path,
    index_path: str | Path,
) -> None:
    document = load_markdown_document(document_path)
    chunks = chunk_markdown_by_section(document)

    indexed_chunks = [
        IndexedChunk(
            chunk=chunk,
            embedding=generate_embedding(chunk.content),
        )
        for chunk in chunks
    ]

    save_index(indexed_chunks, index_path)