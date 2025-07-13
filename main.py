from google.adk.cli.fast_api import get_fast_api_app
import os

AGENTS_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:8080", "*"]
SERVE_WEB_INTERFACE = True

app = get_fast_api_app(agents_dir=AGENTS_DIR,
                      allow_origins=ALLOWED_ORIGINS,
                      web=SERVE_WEB_INTERFACE
                      )

@app.get("/health", tags=["Health Check"])
async def health_check():
    """Health check endpoint to verify the service is running."""
    return {"status": "ok", "message": "Service is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))