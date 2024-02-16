from fastapi import APIRouter
from app.config.database import collection_projects

route = APIRouter()

@route.get('/projects2')
async def get_projects():
    pass
