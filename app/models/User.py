from pydantic import BaseModel

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