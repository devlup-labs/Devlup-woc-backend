from pydantic import BaseModel
from Project import Project
class User(BaseModel):
    id:str
    first_name: str
    last_name: str
    year: str
    branch:str
    gender:str
    githublink:str
    role:str
    phonenumber:int
    projects : list[Project]=[]