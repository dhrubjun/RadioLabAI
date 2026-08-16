from radiolab_ai.llm.ollama_client import generate_response


def get_response(message: str) -> str:
    return generate_response(message)