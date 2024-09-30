from pydantic import BaseModel

class Timeline(BaseModel):
    id: str
    date: str
    events: list[str]
    completed:bool = False
