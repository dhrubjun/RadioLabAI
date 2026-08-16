import logging
import time

import ollama

logger = logging.getLogger(__name__)

MODEL_NAME = "llama3.1:8b"


class LLMError(Exception):
    """Raised when the local language model cannot generate a response."""


def generate_response(message: str) -> str:
    start_time = time.perf_counter()

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are RadioLab AI, a local assistant focused on "
                        "Software Defined Radio, GNU Radio, DSP, and related topics. "
                        "Interpret SDR as Software Defined Radio unless the user "
                        "clearly indicates another meaning."
                    ),
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
    except Exception as exc:
        raise LLMError("The local language model could not generate a response.") from exc

    elapsed_time = time.perf_counter() - start_time
    logger.info("LLM response generated in %.2f seconds", elapsed_time)

    return response["message"]["content"]