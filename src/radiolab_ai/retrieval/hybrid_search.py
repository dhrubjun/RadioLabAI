from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.keyword_search import search_chunks
from radiolab_ai.retrieval.semantic_search import semantic_search


def hybrid_search(
    query: str,
    chunks: list[KnowledgeChunk],
    chunk_embeddings: list[list[float]],
    top_k: int = 3,
) -> list[KnowledgeChunk]:
    if top_k < 1:
        raise ValueError("top_k must be at least 1.")

    keyword_results = search_chunks(
        query,
        chunks,
        top_k=len(chunks),
    )

    semantic_results = semantic_search(
        query,
        chunks,
        chunk_embeddings,
        top_k=len(chunks),
    )

    scores: dict[str, int] = {}
    chunk_lookup: dict[str, KnowledgeChunk] = {}

    for results in (keyword_results, semantic_results):
        result_count = len(results)

        for index, chunk in enumerate(results):
            chunk_id = chunk.metadata["chunk_id"]
            rank_points = result_count - index

            scores[chunk_id] = scores.get(chunk_id, 0) + rank_points
            chunk_lookup[chunk_id] = chunk

    ranked_ids = sorted(
        scores,
        key=scores.get,
        reverse=True,
    )

    return [
        chunk_lookup[chunk_id]
        for chunk_id in ranked_ids[:top_k]
    ]