from fastapi import FastAPI

from contextlib import asynccontextmanager



from app.api.routes import router

from app.core.config import settings

from app.core.logger import logger



# --------------------------------------------------

# LIFESPAN MANAGER

# --------------------------------------------------

@asynccontextmanager

async def lifespan(app: FastAPI):

    """

    Handles startup and shutdown events.

    Ideal for loading ML models into memory to avoid latency on first request.

    """

    logger.info(f"🚀 {settings.app_name} v2.1.0 starting...")

    

    # Example: Initialize ML model here if needed

    # app.state.model = load_my_model()

    

    yield  # Application is now handling requests



    logger.info(f"🛑 {settings.app_name} shutting down...")





# --------------------------------------------------

# APP FACTORY

# --------------------------------------------------

def create_app() -> FastAPI:

    app = FastAPI(

        title=f"🛡️ {settings.app_name}",

        description=(

            "### Overview\n"

            "Busade PhishGuard Engine is a specialized AI-driven microservice designed to "

            "identify and classify URL-based threats in real-time. It leverages "

            "lightweight machine learning to provide high-confidence security scores.\n\n"

            

            "### Core Capabilities\n"

            "* **Real-time Inference:** Low-latency URL analysis.\n"

            "* **Heuristic Engine:** Analyzes URL structure and patterns.\n"

            "* **Zero-Trust Ready:** Easily integrates into existing security pipelines.\n"

            "* **Docker-First:** Optimized for containerized environments like Render/Kubernetes.\n\n"

            

            "### Contact & Support\n"

            "- **Organization:** Crovix Global Technologies\n"

            "- **Environment:** Production-Ready"

        ),

        version="2.1.0",

        lifespan=lifespan,

        docs_url="/docs",

        redoc_url="/redoc"

    )



    # --------------------------------------------------

    # GLOBAL HEALTH CHECK (Crucial for Docker/Render)

    # --------------------------------------------------

    @app.get("/", tags=["System"], summary="Service Health Check")

    async def health_check():

        """

        Confirms the service is live and reachable.

        Used by Render/Docker health probes.

        """

        return {

            "status": "online",

            "service": settings.app_name,

            "version": "2.1.0"

        }



    # Register modular routes

    app.include_router(router, prefix="/api/v1")



    return app





# --------------------------------------------------

# APP INSTANCE

# --------------------------------------------------

app = create_app()