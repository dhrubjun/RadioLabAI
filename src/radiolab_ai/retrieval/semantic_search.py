import math

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.embeddings import generate_embedding


def semantic_search(
    query: str,
    chunks: list[KnowledgeChunk],
    chunk_embeddings: list[list[float]],
    top_k: int = 3,
) -> list[KnowledgeChunk]:
    if top_k < 1:
        raise ValueError("top_k must be at least 1.")

    if len(chunks) != len(chunk_embeddings):
        raise ValueError(
            "chunks and chunk_embeddings must have the same length."
        )

    query_embedding = generate_embedding(query)

    scored_chunks: list[tuple[float, KnowledgeChunk]] = []

    for chunk, chunk_embedding in zip(chunks, chunk_embeddings):
        score = _cosine_similarity(
            query_embedding,
            chunk_embedding,
        )
        scored_chunks.append((score, chunk))

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [chunk for _, chunk in scored_chunks[:top_k]]


def _cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    if len(vector_a) != len(vector_b):
        raise ValueError("Embedding vectors must have the same length.")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )
    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)