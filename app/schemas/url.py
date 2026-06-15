from pydantic import BaseModel
from datetime import datetime

class URLCreate(BaseModel):
    url: str

class URLResponse(BaseModel):
    id : int
    url: str
    short_url: str
    created_at: datetime
    updated_at: datetime
    clicks: int

    model_config = {"from_attributes": True}