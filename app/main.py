from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes_ticket import router as ticket_router
from pathlib import Path

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
    allow_origins=["*"],  # you can restrict to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
frontend_path = Path(__file__).parent / "frontend"

if not frontend_path.exists():
    raise RuntimeError(f"❌ Frontend folder not found at {frontend_path}")

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve index.html
@app.get("/", response_class=FileResponse)
def serve_index():
    return FileResponse(frontend_path / "index.html")
