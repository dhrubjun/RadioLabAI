from dataclasses import dataclass

from radiolab_ai.retrieval.chunk import KnowledgeChunk


@dataclass
class IndexedChunk:
    chunk: KnowledgeChunk
    embedding: list[float]