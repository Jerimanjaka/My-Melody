from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AudioJob:
    id: int
    file_path: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    result_path: Optional[str] = None
    error_message: Optional[str] = None