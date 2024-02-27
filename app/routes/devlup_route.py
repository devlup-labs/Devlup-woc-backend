from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from config.database import (
    collection_timeline1,
    collection_team1,
    collection_blog1,
    collection_project1,
    collection_videos1,
    collection_contact1
)
from schema.TimelineSchema1 import list_schema3, timeline1_dict
from schema.AlumniTeamSchema import list_schema2, alumniteam_dict
from schema.CurrentTeamSchema import list_schema1, currteam_dict
from schema.BlogPageSchema import list_blogs_schema
from schema.ProjectSchema1 import list_projectpage_schema
from schema.VideosSchema import videos_list
from schema.ContactUSSchema import list_contact
from models.CurrentTeam import CurrentTeam
from models.AlumniTeam import AlumniTeam
from models.Timelinedev import Timeline1
from models.Projects import Projects
from models.Blogpage import Blog
from models.Videos import Videos
from models.ContactUS import ContactUS
route = APIRouter()
# email posting
@route.post('/contactus')
async def post_cont(con: ContactUS):
    conn = con.dict()
    collection_contact1.insert_one(conn)
    return {'status': 'success'}
# email fetching
@route.get('/contactus')
async def get_mails():
    emails=list_contact(collection_contact1.find({}))
    return JSONResponse(content=emails)

# Videos fetching
@route.get('/videos')
async def get_videos():
    vidp=videos_list(collection_videos1.find({}))
    return JSONResponse(content=vidp)

# Videos posting
@route.post('/videos')
async def post_videos(videos: Videos):
    vidd = videos.dict()
    collection_videos1.insert_one(vidd)
    return {'status': 'success'}

# ProjectPage fetching
@route.get('/projectpage')
async def get_projectspage():
    projp=list_projectpage_schema(collection_project1.find({}))
    return JSONResponse(content=projp)
# ProjectPage post

@route.post('/projectpage')
async def post_projects(projects : Projects):
    prod = projects.dict()
    collection_project1.insert_one(prod)
    return {'status': 'success'}


# Blog Page fetching
@route.get('/blogpage')
async def get_blogpage():
    blogp=list_blogs_schema(collection_blog1.find({}))
    return JSONResponse(content=blogp)

# Blog Page Post
@route.post('/blogpage')
async def post_blog(blog : Blog):
    blogd = blog.dict()
    collection_blog1.insert_one(blogd)
    return {'status': 'success'}


# Fetch from current
@route.get('/current-team')
async def get_current_team():
    current_team = list_schema1(collection_team1.find({"AlumniStatus": 0}))
    return JSONResponse(content=current_team)
# Post to Current
@route.post('/current-team')
async def post_current_team(current_team: CurrentTeam):
    current_teamd = current_team.dict()
    collection_team1.insert_one(current_teamd)

    return {'status': 'success'}
# Fetch from alumni
@route.get('/alumni-team')
async def get_alumni_team():
    alumni_team = list_schema2(collection_team1.find({"AlumniStatus": 1}))
    return JSONResponse(content=alumni_team)

# Post to alumni
@route.post('/alumni-team')
async def post_alumni_team(alumni_team: AlumniTeam):
    alumni_teamd = alumni_team.dict()
    collection_team1.insert_one(alumni_teamd)
    return {'status': 'success'}



@route.get('/timeline')
async def get_timeline():
    timeline = list_schema3(collection_timeline1.find({}))
    return JSONResponse(content=timeline)

# Post to timeline
@route.post('/timeline')
async def post_timeline(timeline1: Timeline1):
    timelined = timeline1.dict()
    collection_timeline1.insert_one(timelined)

    return {'status': 'success'}
