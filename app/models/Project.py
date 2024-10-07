from pydantic import BaseModel

class Project(BaseModel):
    id: str
    mentorid: str
    title: str
    tag:str
    technology: str
    description: str
    mentor:str
    completed:bool=False
    mentee:list[str]=[]
    codelink: str = ""
    year:str
    progress:str=""

