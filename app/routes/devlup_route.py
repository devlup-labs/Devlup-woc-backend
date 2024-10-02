from fastapi import APIRouter
from config.database import collection_projects
from models.Project import Project

route = APIRouter()



@route.post('/project')
async def create_project(project: Project):
    collection_projects.insert_one(project.dict())
    return project