from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.config import settings
from api.routers import data


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""

    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        debug=settings.DEBUG,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(data.router, prefix=settings.API_V1_PREFIX, tags=["data"])

    @app.get("/")
    async def root():
        """Root endpoint."""
        return {
            "message": "FastAPI Data Receiver",
            "version": settings.VERSION,
            "docs": "/docs",
        }

    return app


# Create app instance
app = create_app()
