from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.url import URLCreate, URLResponse, URLUpdate, URLListItem
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
    if url_data is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return url_data

@router.patch("/{short_url}", response_model=URLResponse)
def update_url(short_url: str, url_update: URLUpdate, db: Session = Depends(get_db)):
    url_data = crud.get_url_by_short_url(db, short_url)
    if url_data is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    new_url_data = crud.update_url(db, url_data, url_update.url)
    return new_url_data

@router.delete("/{short_url}")
def delete_short_url(short_url: str, db: Session = Depends(get_db)):
    url_data = crud.get_url_by_short_url(db, short_url)
    if url_data is None:
        raise HTTPException(status_code=404, detail="URL not found")       
    crud.delete_url(db, url_data)
    return {"status": "Url deleted successful"}

@router.get("/", response_model=list[URLListItem])
def get_all_url(db:Session = Depends(get_db)):
    url_list = crud.get_all_url(db)
    return url_list