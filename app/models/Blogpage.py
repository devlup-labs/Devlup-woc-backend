from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    author: str
    date: str
    avatarid: str
    readTime: str
    image: str
    link: str
