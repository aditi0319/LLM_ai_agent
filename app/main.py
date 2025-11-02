from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.api.routes_ticket import router as ticket_router
import os
import pathlib

app = FastAPI(
    title="AI Customer Support Agent",
    description="An intelligent API to classify and assist customer support queries.",
    version="1.0.0"
)

# Include API routes
app.include_router(ticket_router)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the frontend files
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
if not os.path.exists(frontend_path):
    raise RuntimeError(f"❌ Frontend folder not found at {frontend_path}")

@app.get("/", response_class=HTMLResponse)
def root():
    with open(frontend_path / "index.html", "r", encoding="utf-8") as f:
        return f.read()
