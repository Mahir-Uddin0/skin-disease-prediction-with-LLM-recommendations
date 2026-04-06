from pydantic import BaseModel


class SkinAnalysisResponse(BaseModel):
    disease: str
    confidence: float
    
    
# This needs to be updated to include LLM recommendations in the future.