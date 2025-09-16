import datetime
import pathlib
from py_compile import main

from src.dtos.response import Response
from src.gemini import exec_gemini
from src.args import get_args
from src.utils.image import get_image_mime_type

#TODO: Exec async https://gemini.google.com/app/e71302c05abbd445?_gl=1*7g3lkp*_ga*MTMxNDcyMDcwLjE3NDkxNjg2ODQ.*_ga_WC57KJ50ZZ*czE3NDkxNjg2ODMkbzEkZzEkdDE3NDkxNjg3NTckajU0JGwwJGgw
#TODO: Exec gpt
#TODO: Exec NanoBanana with recommended issues

def main():
    args = get_args()

    mime_type = get_image_mime_type(args.input)
    filepath = pathlib.Path(args.input)

    gemini_models_to_execute = [
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-pro",
        "gemini-2.5-flash-lite",
    ]

    responses = []
    for model in gemini_models_to_execute:
        print(f"🧠 executing model: {model}")
        response = exec_gemini(model, filepath, mime_type)
        response_dto = Response(llm_response=response, model=model)
        responses.append(response_dto)

    has_issues = False
    for response in responses:
        if not response.llm_response.is_valid:
            has_issues = True

    if not has_issues:
        print("🤖 no problem was identified in the image")
        return

    print("⚠️  issues were identified in the image by at least one model")
    issues = []
    for response in responses:
        if not response.llm_response.is_valid:
            issues.append(response.llm_response.issues)
            print(
                f"⚙️ model {response.model} identifyed the following: {response.llm_response.issues}"
            )


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"🚀 starting process at {start_time}")

    main()

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"⏱️  execution finished. Total time: {total_time}")
