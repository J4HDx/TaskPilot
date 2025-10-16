from fastapi import FastAPI
from typing import Dict

from .routes import flows
from .core.config import settings
from .database import init_db
from .utils.scheduler import setup_flow_scheduler

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An open-source automation platform.",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    init_db()
    setup_flow_scheduler()

@app.get("/api/health", tags=["Health"])
def health_check() -> Dict[str, str]:
    """
    Checks if the API is running.
    """
    return {"status": "ok"}

# Include API routers
app.include_router(flows.router, prefix="/api", tags=["Flows"])