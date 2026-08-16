import pytest

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.keyword_search import search_chunks


def test_search_chunks_ranks_matching_chunks():
    chunks = [
        KnowledgeChunk(
            content="A traditional radio uses dedicated hardware circuits.",
            metadata={"chunk_id": "test:1"},
        ),
        KnowledgeChunk(
            content=(
                "Software Defined Radio performs many signal-processing "
                "operations digitally in software."
            ),
            metadata={"chunk_id": "test:2"},
        ),
    ]

    results = search_chunks("software defined radio", chunks)

    assert len(results) == 2
    assert results[0].metadata["chunk_id"] == "test:2"

def test_search_chunks_boosts_section_heading_matches():
    chunks = [
        KnowledgeChunk(
            content="Software Defined Radio is discussed in this section.",
            metadata={
                "chunk_id": "test:1",
                "section": "General Radio Background",
            },
        ),
        KnowledgeChunk(
            content="Software Defined Radio is discussed in this section.",
            metadata={
                "chunk_id": "test:2",
                "section": "What Is Software Defined Radio?",
            },
        ),
    ]

    results = search_chunks("What is Software Defined Radio?", chunks)

    assert results[0].metadata["chunk_id"] == "test:2"

def test_search_chunks_respects_top_k():
    chunks = [
        KnowledgeChunk(
            content="Software Defined Radio basics.",
            metadata={"chunk_id": "test:1"},
        ),
        KnowledgeChunk(
            content="Software radio processing.",
            metadata={"chunk_id": "test:2"},
        ),
        KnowledgeChunk(
            content="Radio hardware and software.",
            metadata={"chunk_id": "test:3"},
        ),
    ]

    results = search_chunks(
        "software radio",
        chunks,
        top_k=2,
    )

    assert len(results) == 2


def test_search_chunks_rejects_invalid_top_k():
    with pytest.raises(ValueError, match="top_k must be at least 1"):
        search_chunks(
            "software radio",
            [],
            top_k=0,
        )