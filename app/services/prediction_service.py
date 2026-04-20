import joblib
from app.utils.feature_extractor import extract_features
from app.utils.url_checker import url_exists


class PredictionService:
    def __init__(self):
        self.model = joblib.load("models/url_model.pkl")

    def predict(self, url: str):

        # -------------------------
        # Normalize input
        # -------------------------
        url = str(url)

        # -------------------------
        # OPTIONAL: existence check (non-blocking)
        # -------------------------
        exists = url_exists(url)

        # -------------------------
        # Feature extraction
        # -------------------------
        features = extract_features(url)

        # -------------------------
        # Prediction
        # -------------------------
        result = self.model.predict([features])[0]
        probability = self.model.predict_proba([features])[0][result]

        return {
            "prediction": "phishing" if result == 1 else "legitimate",
            "confidence": round(float(probability), 4),
            "domain_resolves": exists
        }