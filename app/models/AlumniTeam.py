from pydantic import BaseModel

class AlumniTeam(BaseModel):
    name: str
    role: str
    avatar: str
    linkedin: str
    mail: str
    github: str
