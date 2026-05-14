from fastapi import FastAPI
from app.api.dashboard import router as dashboard_router

app = FastAPI(title="Sales Performance Dashboard", version="1.0.0")
app.include_router(dashboard_router, prefix="/api/v1/dashboard", tags=["Dashboard"])

@app.get("/")
def health():
    return {"status": "healthy"}
