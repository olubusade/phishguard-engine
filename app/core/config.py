from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PhishGuard Engine"
    model_path: str = "models/url_model.pkl"

settings = Settings()