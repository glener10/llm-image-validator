import asyncio
import datetime
import pathlib
import google.generativeai as genai

from src.env import get_api_key
from src.dtos.response import Response
from src.gemini import exec_gemini_async
from src.args import get_args
from src.utils.image import get_image_mime_type

# TODO: Exec gpt
# TODO: Exec NanoBanana with recommended issues


async def main():
    args = get_args()

    mime_type = get_image_mime_type(args.input)
    filepath = pathlib.Path(args.input)
    genai.configure(api_key=get_api_key())

    gemini_models_to_execute = [
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-pro",
        "gemini-2.5-flash-lite",
    ]
    tasks = [
        exec_gemini_async(model, filepath, mime_type)
        for model in gemini_models_to_execute
    ]
    results_from_models = await asyncio.gather(*tasks)
    responses = [
        Response(llm_response=result, model=model)
        for model, result in zip(gemini_models_to_execute, results_from_models)
    ]

    has_issues = any(not response.llm_response.is_valid for response in responses)

    if not has_issues:
        print("🤖 no problem was identified in the image by any model")
        return

    print("⚠️  issues were identified in the image by at least one model")
    issues = []
    for response in responses:
        if not response.llm_response.is_valid:
            issues.append(response.llm_response.issues)
            print(
                f"⚙️  model {response.model} identifyed the following: {response.llm_response.issues}"
            )


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"🚀 starting process at {start_time}")

    asyncio.run(main())

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"⏱️  execution finished at {end_time}. Total time: {total_time}")
