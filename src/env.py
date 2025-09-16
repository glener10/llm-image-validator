from dotenv import load_dotenv
import os


def get_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("❌ missing API_KEY in .env")
    return api_key
