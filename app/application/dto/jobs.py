from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobDTO(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    posted_at: Optional[datetime] = None
    is_active: Optional[bool] = True