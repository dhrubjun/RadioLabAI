from radiolab_ai.retrieval.chunker import chunk_markdown_by_section
from radiolab_ai.retrieval.document import KnowledgeDocument


def test_chunk_markdown_by_section():
    document = KnowledgeDocument(
        content="""# Test Chapter

## 1.1 First Section

First section content.

## 1.2 Second Section

Second section content.
""",
        metadata={
            "source_id": "test_source",
            "title": "Test Chapter",
        },
    )

    chunks = chunk_markdown_by_section(document)

    assert len(chunks) == 2

    assert chunks[0].metadata["source_id"] == "test_source"
    assert chunks[0].metadata["section"] == "1.1 First Section"
    assert "First section content." in chunks[0].content

    assert chunks[1].metadata["source_id"] == "test_source"
    assert chunks[1].metadata["section"] == "1.2 Second Section"
    assert "Second section content." in chunks[1].content