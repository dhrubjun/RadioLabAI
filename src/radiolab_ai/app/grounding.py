from radiolab_ai.retrieval.chunk import KnowledgeChunk


def build_grounded_prompt(
    question: str,
    chunks: list[KnowledgeChunk],
) -> str:
    context_parts = []

    for chunk in chunks:
        section = chunk.metadata.get("section", "Unknown section")
        context_parts.append(
            f"[{section}]\n{chunk.content}"
        )

    context = "\n\n".join(context_parts)

    return (
        "Use the following local knowledge to answer the user's question. "
        "Base the answer on this context and do not invent unsupported details.\n\n"
        f"{context}\n\n"
        f"Question:\n{question}"
    )