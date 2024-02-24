from pydantic import BaseModel
from typing import List, Optional

class Projects(BaseModel):
    id: str
    avatarSrc: str
    name: str
    bio: str
    socialIcons: Optional[List[dict]] = []
    buttons: Optional[List[str]] = []
    isPro: Optional[bool] = False
