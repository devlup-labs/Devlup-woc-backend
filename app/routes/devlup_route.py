from fastapi import APIRouter
from app.config.database import collection_projects
from app.schema.ProjectSchema import list_schema
from app.models.Project import Project

route = APIRouter()

@route.get('/projects')
async def get_projects():
    projects = list_schema(collection_projects.find())
    print(projects)
    return projects

@route.post('/project')
async def create_project(project: Project):
    collection_projects.insert_one(project.dict())
    return project