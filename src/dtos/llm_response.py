from pydantic import BaseModel


class LLMResponse(BaseModel):
    is_valid: bool
    issues: str
