from pydantic import BaseModel

class ContactUS(BaseModel):
    email: str
    name: str
    contactno: str
    comments: str
