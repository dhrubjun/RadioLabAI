import re

from radiolab_ai.retrieval.chunk import KnowledgeChunk


STOP_WORDS = {
    "a",
    "an",
    "and",
    "in",
    "is",
    "of",
    "the",
    "to",
    "what",
}


def search_chunks(
    query: str,
    chunks: list[KnowledgeChunk],
    top_k: int = 3,
) -> list[KnowledgeChunk]:
    if top_k < 1:
        raise ValueError("top_k must be at least 1.")

    query_terms = _tokenize(query)

    scored_chunks: list[tuple[int, KnowledgeChunk]] = []

    for chunk in chunks:
        chunk_terms = _tokenize(chunk.content)
        section_terms = _tokenize(chunk.metadata.get("section", ""))

        body_score = len(query_terms & chunk_terms)
        heading_score = len(query_terms & section_terms) * 2

        score = body_score + heading_score

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [chunk for _, chunk in scored_chunks[:top_k]]


def _tokenize(text: str) -> set[str]:
    terms = set(re.findall(r"\b\w+\b", text.lower()))
    return terms - STOP_WORDS