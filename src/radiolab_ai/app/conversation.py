from radiolab_ai.app.grounding import build_grounded_prompt
from radiolab_ai.llm.ollama_client import generate_response
from radiolab_ai.retrieval.retriever import retrieve


def get_response(message: str) -> str:
    chunks = retrieve(message)
    prompt = build_grounded_prompt(message, chunks)

    return generate_response(prompt)