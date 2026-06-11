from fastapi import FastAPI
from app.api.v1.url_shortener_api import router
from app.api.v1.models import Url  
from app.db import engine, Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My api for url shortener",
    description="",
    version="0.1"
)
app.include_router(router, prefix="/url", tags=["Url"])

@app.get("/")
async def root():
    return {"status": "running"}



