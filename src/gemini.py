from io import BytesIO
import google.generativeai as genai
from google.generativeai import types
from PIL import Image
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


def generate_new_image(input_path: str, issues: list[str]):
    try:
        prompt_issues = ", ".join(issues)
        prompt = (
            "Generate a new version of this image correcting the following issues: "
            f"{prompt_issues}"
        )
        image_input = Image.open(input_path)

        NANO_BANANA_MODEL = "gemini-2.5-flash-image-preview"
        model = genai.GenerativeModel(model_name=NANO_BANANA_MODEL)
        response = model.generate_content([prompt, image_input])

        image_parts = [
            part.inline_data.data
            for part in response.candidates[0].content.parts
            if part.inline_data
        ]

        if image_parts:
            image = Image.open(BytesIO(image_parts[0]))
            image.save("output.png")
            print(f"✅ image saved to output.png")
    except Exception as e:
        print(f"⚠️  could not generate the corrected image: {e}")
