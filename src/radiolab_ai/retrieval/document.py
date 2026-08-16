from dataclasses import dataclass


@dataclass
class KnowledgeDocument:
    content: str
    metadata: dict[str, str]