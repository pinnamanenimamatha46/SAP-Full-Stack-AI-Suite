from pydantic import BaseModel, Field


class RiskAssessment(BaseModel):
    risk_score: int = Field(ge=0, le=100)
    risk_level: str
    fraud_probability: float = Field(ge=0.0, le=1.0)
    explanation: str
    recommended_actions: list[str]
