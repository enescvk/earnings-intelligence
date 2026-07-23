from pydantic import BaseModel


class ExecutiveSummary(BaseModel):
    summary: str
    confidence: int