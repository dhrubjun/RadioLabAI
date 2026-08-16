from radiolab_ai.retrieval.markdown_loader import load_markdown_document


def test_load_markdown_document(tmp_path):
    document_path = tmp_path / "test_document.md"
    document_path.write_text(
        """---
source_id: test_source
title: Test Document
---
# Test Heading

This is test content.
""",
        encoding="utf-8",
    )

    document = load_markdown_document(document_path)

    assert document.metadata["source_id"] == "test_source"
    assert document.metadata["title"] == "Test Document"
    assert document.content == "# Test Heading\n\nThis is test content."

import pytest

from radiolab_ai.retrieval.markdown_loader import load_markdown_document


def test_load_markdown_document_rejects_missing_front_matter(tmp_path):
    document_path = tmp_path / "test_document.md"
    document_path.write_text(
        "# Test Heading\n\nThis is test content.",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing front matter"):
        load_markdown_document(document_path)


def test_load_markdown_document_rejects_unclosed_front_matter(tmp_path):
    document_path = tmp_path / "test_document.md"
    document_path.write_text(
        """---
source_id: test_source
title: Test Document
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="not closed"):
        load_markdown_document(document_path)