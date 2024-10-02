from pydantic import BaseModel
class Proposal(BaseModel):
    id: str
    title: str
    name: str
    drive: str
    status:bool=False
    mentor: str
    email: str