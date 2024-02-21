from pydantic import BaseModel

class CurrentTeam(BaseModel):
    name: str
    role: str
    avatar: str
    linkedin: str
    mail: str
    github: str
