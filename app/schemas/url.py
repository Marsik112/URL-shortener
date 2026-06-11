from pydantic import BaseModel
from datetime import datetime

class URL(BaseModel):
    url: str

class URL_create(BaseModel):
    id : int
    url: str
    short_url: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}