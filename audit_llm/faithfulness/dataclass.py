from typing import Any

from pydantic import BaseModel, Field, validator


class LLMJudgeInput(BaseModel):
    sources: str = Field(default="")
    previous_sentences: str = Field(default="")
    phrase: str

    @validator("sources", "previous_sentences", pre=True, always=True)
    def force_default_if_invalid(cls, v: Any) -> str:
        if not isinstance(v, str):
            return ""
        return v
