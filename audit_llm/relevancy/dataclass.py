from pydantic import BaseModel


class llmJudgeInput(BaseModel):
    question_fr: str
    answer: str
