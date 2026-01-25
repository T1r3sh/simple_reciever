"""
FastAPI Data Receiver - Entry Point

This is the main entry point for the FastAPI application.
Run with: uvicorn main:app --reload
"""

from api.main import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
