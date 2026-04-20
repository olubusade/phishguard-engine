from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes import router
from app.core.config import settings
from app.core.logger import logger


# --------------------------------------------------
# LIFESPAN MANAGER (NEW STANDARD)
# --------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("🚀 PhishGuard Engine starting...")

    yield  # App runs here

    # Shutdown logic
    logger.info("🛑 PhishGuard Engine shutting down...")


# --------------------------------------------------
# APP FACTORY
# --------------------------------------------------
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description=(
            "PhishGuard Engine\n\n"
            "A lightweight, production-ready URL threat detection service.\n\n"
            "### Features\n"
            "- Fast ML-based URL classification\n"
            "- Lightweight architecture (no external dependencies)\n"
            "- Real-time inference\n"
            "- Modular microservice design\n"
        ),
        version="2.0.0",
        lifespan=lifespan
    )

    # Register routes
    app.include_router(router, prefix="/api/v1")

    return app


# --------------------------------------------------
# APP INSTANCE
# --------------------------------------------------
app = create_app()