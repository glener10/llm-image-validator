from src.dtos.llm_response import LLMResponse
from pydantic import BaseModel


class Response(BaseModel):
    llm_response: LLMResponse
    model: str
