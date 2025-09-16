import datetime
import pathlib
from py_compile import main

from src.gemini import exec_gemini
from src.args import get_args
from src.utils.image import get_image_mime_type


def main():
    args = get_args()

    mime_type = get_image_mime_type(args.input)
    filepath = pathlib.Path(args.input)

    gemini_models_to_execute = [
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-pro",
        "gemini-2.5-flash-lite",
    ]

    gemini_response = []
    for model in gemini_models_to_execute:
        print(f"🧠 executing model: {model}")
        response = exec_gemini(model, filepath, mime_type)
        gemini_response.append(response)

    print("🤖 all models executed")


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"🚀 starting process at {start_time}")

    main()

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"⏱️  execution finished. Total time: {total_time}")
