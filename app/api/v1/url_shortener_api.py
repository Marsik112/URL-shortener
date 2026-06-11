from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.url import URL_create, URL
from app.api.v1 import crud
from app.db import get_db
router = APIRouter()

@router.get("/")
async def root():
    return{"status": "ok"}

@router.post("/shorten")
def create_shorten(url: URL, db: Session = Depends(get_db)):
    new_url = crud.create_url(db,url)
    return new_url
