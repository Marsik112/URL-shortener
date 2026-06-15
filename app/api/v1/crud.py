from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.url import URLCreate
from app.api.v1.models import Url
from app.api.v1.generator_url import generate_short_url

def create_url(db: Session, url_data: URLCreate) -> Url:
    
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

def get_url_by_short_url(db: Session, short_url: str) -> Url | None:
    stmt = select(Url).where(Url.short_url == short_url)
    url_data = db.execute(stmt).scalar_one_or_none()
    return url_data

def increment_clicks(db: Session, url_data: Url) -> Url:
    url_data.clicks += 1
    db.commit()
    db.refresh(url_data)
    return url_data

