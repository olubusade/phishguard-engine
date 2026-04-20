from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    domain_resolves: bool