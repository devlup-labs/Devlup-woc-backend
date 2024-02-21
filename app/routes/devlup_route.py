from fastapi import APIRouter
from config.database import (
    collection_timeline1,
    collection_current1,
    collection_alumni1,
)
from schema.TimelineSchema1 import list_schema3
from schema.AlumniTeamSchema import list_schema2
from schema.CurrentTeamSchema import list_schema1

route = APIRouter()

@route.get('/current-team')
async def get_current_team():
    current_team = list_schema1(collection_current1.find())
    return current_team

@route.get('/alumni-team')
async def get_alumni_team():
    alumni_team = list_schema2(collection_alumni1.find())
    return alumni_team

@route.get('/timeline')
async def get_timeline():
    timeline = list_schema3(collection_timeline1.find())
    return timeline
