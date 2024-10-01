from pydantic import BaseModel
class Proposal(BaseModel):
    title: str
    name: str
    drive: str
    mentor: str