from pydantic import BaseModel

class Project(BaseModel):
    id: int
    title: str
    description: str
    mentor:str
