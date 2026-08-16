import json
from pathlib import Path

from radiolab_ai.retrieval.chunk import KnowledgeChunk
from radiolab_ai.retrieval.indexed_chunk import IndexedChunk


def save_index(
    indexed_chunks: list[IndexedChunk],
    path: str | Path,
) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "chunks": [
            {
                "content": indexed_chunk.chunk.content,
                "metadata": indexed_chunk.chunk.metadata,
                "embedding": indexed_chunk.embedding,
            }
            for indexed_chunk in indexed_chunks
        ]
    }

    file_path.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def load_index(
    path: str | Path,
) -> list[IndexedChunk]:
    file_path = Path(path)
    data = json.loads(file_path.read_text(encoding="utf-8"))

    indexed_chunks: list[IndexedChunk] = []

    for item in data["chunks"]:
        chunk = KnowledgeChunk(
            content=item["content"],
            metadata=item["metadata"],
        )

        indexed_chunks.append(
            IndexedChunk(
                chunk=chunk,
                embedding=item["embedding"],
            )
        )

    return indexed_chunks