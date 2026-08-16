from pathlib import Path

from radiolab_ai.retrieval.document import KnowledgeDocument


def load_markdown_document(path: str | Path) -> KnowledgeDocument:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")

    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError("Knowledge document is missing front matter.")

    metadata: dict[str, str] = {}
    closing_index = None

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

        if ":" not in line:
            raise ValueError(f"Invalid metadata line: {line}")

        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    if closing_index is None:
        raise ValueError("Knowledge document front matter is not closed.")

    content = "\n".join(lines[closing_index + 1 :]).strip()

    return KnowledgeDocument(
        content=content,
        metadata=metadata,
    )