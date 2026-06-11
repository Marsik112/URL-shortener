from typing import Optional
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from app.schemas.setting import settings

engine =create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


