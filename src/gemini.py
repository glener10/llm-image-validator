from google import genai
from google.genai import types

from src.dtos.llm_response import LLMResponse
from src.env import get_api_key
from src.prompt import get_prompt


def exec_gemini(model: str, filepath, mime_type: str) -> LLMResponse:
    prompt = get_prompt()
    api_key = get_api_key()

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=[
            types.Part.from_bytes(
                data=filepath.read_bytes(),
                mime_type=mime_type,
            ),
            prompt,
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LLMResponse,
        ),
    )
    return response
