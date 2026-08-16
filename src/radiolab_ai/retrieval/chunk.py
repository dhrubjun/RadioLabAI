from dataclasses import dataclass


@dataclass
class KnowledgeChunk:
    content: str
    metadata: dict[str, str]