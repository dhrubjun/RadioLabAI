from pathlib import Path

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.hybrid_search import hybrid_search
from radiolab_ai.retrieval.index_store import load_index


DEFAULT_INDEX_PATH = Path("data/indexes/knowledge_index.json")


def retrieve(
    query: str,
    index_path: str | Path = DEFAULT_INDEX_PATH,
    top_k: int = 3,
) -> list[KnowledgeChunk]:
    indexed_chunks = load_index(index_path)

    chunks = [
        indexed_chunk.chunk
        for indexed_chunk in indexed_chunks
    ]

    embeddings = [
        indexed_chunk.embedding
        for indexed_chunk in indexed_chunks
    ]

    return hybrid_search(
        query,
        chunks,
        embeddings,
        top_k=top_k,
    )