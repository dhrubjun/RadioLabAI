from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.document import KnowledgeDocument


def chunk_markdown_by_section(
    document: KnowledgeDocument,
) -> list[KnowledgeChunk]:
    chunks: list[KnowledgeChunk] = []

    current_heading = None
    current_lines: list[str] = []

    for line in document.content.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                chunks.append(
                    _build_chunk(
                        document,
                        current_heading,
                        current_lines,
                        len(chunks) + 1,
                    )
                )

            current_heading = line[3:].strip()
            current_lines = [line]
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        chunks.append(
            _build_chunk(
                document,
                current_heading,
                current_lines,
                len(chunks) + 1,
            )
        )

    return chunks


def _build_chunk(
    document: KnowledgeDocument,
    heading: str,
    lines: list[str],
    chunk_number: int,
) -> KnowledgeChunk:
    metadata = document.metadata.copy()
    metadata["section"] = heading
    metadata["chunk_id"] = (
        f"{document.metadata['source_id']}:{chunk_number}"
    )

    return KnowledgeChunk(
        content="\n".join(lines).strip(),
        metadata=metadata,
    )