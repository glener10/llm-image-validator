import base64
import json
from pathlib import Path
from openai import AsyncOpenAI

from src.prompt import get_prompt
from src.env import get_openai_api_key
from src.dtos.llm_response import LLMResponse


async def exec_openai_async(
    model_name: str, filepath: Path, mime_type: str
) -> LLMResponse:
    try:
        async with AsyncOpenAI(api_key=get_openai_api_key()) as client:
            image_data = filepath.read_bytes()
            base64_image = base64.b64encode(image_data).decode("utf-8")
            image_url = f"data:{mime_type};base64,{base64_image}"

            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": get_prompt()},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url},
                        },
                    ],
                }
            ]

            print(f"🧠 firing model: {model_name}")
            response = await client.chat.completions.create(
                model=model_name,
                messages=messages,
                response_format={"type": "json_object"},
                max_tokens=300,
            )

            response_text = response.choices[0].message.content
            print(f"✅ model finished: {model_name}")
            return LLMResponse(**json.loads(response_text))
    except Exception as e:
        print(f"⚠️  error call openai model {model_name}: {e}")
        return LLMResponse(is_valid=False, issues="")
