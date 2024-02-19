from pydantic import BaseModel

class Idea(BaseModel):
    title: str
    description: str
    name:str
