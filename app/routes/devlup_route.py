from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from config.database import (
    collection_timeline1,
    collection_team1,
    collection_blog1,
    collection_project1
)
from schema.TimelineSchema1 import list_schema3, timeline1_dict
from schema.AlumniTeamSchema import list_schema2, alumniteam_dict
from schema.CurrentTeamSchema import list_schema1, currteam_dict
from schema.BlogPageSchema import list_blogs_schema
from schema.ProjectSchema1 import list_projectpage_schema
route = APIRouter()

# ProjectPage fetching
@route.get('/projectpage')
async def get_projectspage():
    projp=list_projectpage_schema(collection_project1.find({}))
    return JSONResponse(content=projp)
# Blog Page fetching
@route.get('/blogpage')
async def get_blogpage():
    blogp=list_blogs_schema(collection_blog1.find({}))
    return JSONResponse(content=blogp)


@route.get('/current-team')
async def get_current_team():
    current_team = list_schema1(collection_team1.find({"AlumniStatus": 0}))
    return JSONResponse(content=current_team)

# post request
@route.post('/current-team')
async def post_current_team(request: Request):
    data = await request.json()
    current_team = currteam_dict(data)
    collection_team1.insert_one(current_team)
    return {'status': 'success'}

@route.get('/alumni-team')
async def get_alumni_team():
    alumni_team = list_schema2(collection_team1.find({"AlumniStatus": 1}))
    return JSONResponse(content=alumni_team)

# Post to alumni
@route.post('/alumni-team')
async def post_alumni_team(request: Request):
    data = await request.json()
    alumni_team = alumniteam_dict(data)
    collection_team1.insert_one(alumni_team)
    return {'status': 'success'}


@route.get('/timeline')
async def get_timeline():
    timeline = list_schema3(collection_timeline1.find({}))
    return JSONResponse(content=timeline)

# Post to timeline
@route.post('/timeline')
async def post_timeline(request: Request):
    data = await request.json()
    timeline = timeline1_dict(data)
    collection_timeline1.insert_one(timeline)
    return {'status': 'success'}

