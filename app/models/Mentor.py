from pydantic import BaseModel

class Mentor(BaseModel):
    id: int
    name:str
