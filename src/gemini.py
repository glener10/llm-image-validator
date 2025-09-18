import google.generativeai as genai
from google.generativeai import types
import json

from src.dtos.llm_response import LLMResponse
from src.prompt import get_prompt


async def exec_gemini_async(model_name: str, filepath, mime_type: str) -> LLMResponse:
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=types.GenerationConfig(
            response_mime_type="application/json",
            response_schema=LLMResponse,
        ),
    )
    print(f"🧠 firing model: {model_name}")
    response = await model.generate_content_async(
        contents=[
            {"mime_type": mime_type, "data": filepath.read_bytes()},
            get_prompt(),
        ]
    )

    print(f"✅ model finished: {model_name}")
    return LLMResponse(**json.loads(response.text))
