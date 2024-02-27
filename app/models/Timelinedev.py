from pydantic import BaseModel
from typing import Optional

class Timeline1(BaseModel):
    index: int
    colorClass: str
    date: Optional[int] = None
    title: str
    info: str
    firstButtonText: str = ""
    firstButtonLink: str = ""
    secondButtonText: str = ""
    secondButtonLink: str = ""
