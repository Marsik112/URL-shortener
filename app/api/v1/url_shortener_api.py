from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.url import URLCreate, URLResponse
from app.api.v1 import crud
from app.db import get_db
router = APIRouter()

@router.get("/health")
async def root():
    return{"status": "ok"}

@router.post("/shorten", response_model=URLResponse)
def create_shorten(url: URLCreate, db: Session = Depends(get_db)):
    new_url = crud.create_url(db,url)
    return new_url

@router.get("/{short_url}", response_model=URLResponse)
def get_json_from_short_url(short_url: str, db: Session = Depends(get_db)):
    url_data = crud.get_url_by_short_url(db, short_url)
    if url_data == None:
        raise HTTPException(status_code=404, detail="URL not found")
    return url_data
