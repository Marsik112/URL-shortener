from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from app.db import Base

class Url(Base):
    __tablename__= "Url"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(100), nullable=False)
    short_url: Mapped[Optional[str | None]] = mapped_column(String(10), nullable=True, default="")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now())
 