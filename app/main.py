from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.api.v1.url_shortener_api import router
from sqlalchemy.orm import Session
from app.api.v1.models import Url  
from app.db import engine, Base, get_db
from app.api.v1.crud import get_url_by_short_url, increment_clicks
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My api for url shortener",
    description="",
    version="0.1"
)
app.include_router(router, prefix="/urls", tags=["Url"])

@app.get("/")
async def root():
    return {"status": "running"}

@app.get("/{short_url}")
def redirect_by_short_url(short_url: str, db: Session = Depends(get_db)):
    new_url_data = get_url_by_short_url(db, short_url)
    if new_url_data is None:
        raise HTTPException(status_code=404, detail="URL not found")
    increment_clicks(db, new_url_data)
    return RedirectResponse(url=new_url_data.url, status_code=303)
