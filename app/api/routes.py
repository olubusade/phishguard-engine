from fastapi import APIRouter
import time
import os
from app.schemas.request import URLRequest
from app.schemas.response import PredictionResponse
from app.services.prediction_service import PredictionService

router = APIRouter()


start_time = time.time()
service = PredictionService()

service = PredictionService()

@router.get("/health")
def health():
    uptime = time.time() - start_time

    # Check model availability
    model_loaded = os.path.exists("models/url_model.pkl")

    return {
        "status": "ok",
        "service": "PhishGuard Engine",
        "version": "2.0.0",
        "uptime_seconds": round(uptime, 2),
        "model_loaded": model_loaded
    }

@router.post("/predict", response_model=PredictionResponse)
def predict(request: URLRequest):

    return service.predict(request.url)