from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.url import URL_create, URL
from app.api.v1.models import Url
from app.api.v1.generator_url import decode_url, generate_short_url

def create_url(db: Session, url_data: URL) -> URL_create:
    
    db_url = Url(
        url=url_data.url
    )
    db.add(db_url)
    db.flush()
    short_url = generate_short_url(db_url.id)
    db_url.short_url = short_url
    db.commit()
    db.refresh(db_url)
    return db_url
