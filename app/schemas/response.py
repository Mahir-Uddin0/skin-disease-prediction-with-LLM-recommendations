from pydantic import BaseModel


class SkinAnalysisResponse(BaseModel):
    disease: str
    confidence: float
    recommendations: str
    next_steps: str
    tips: str