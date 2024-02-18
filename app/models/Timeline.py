from pydantic import BaseModel

class Timeline(BaseModel):
    Date: str
    events: list[str]
    completed:bool = False
