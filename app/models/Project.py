from pydantic import BaseModel

class Project(BaseModel):
    id: str
    mentorid: str
    title: str
    tag:str
    technology: str
    description: str
    mentor:str

