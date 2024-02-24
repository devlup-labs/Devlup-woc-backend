from fastapi import APIRouter,HTTPException,Query
from fastapi import  Request
from config.database import collection_projects
from config.database import collection_timeline,collection_mentors,collection_ideas,collection_programs,collection_proposals
from config.database import collection_users
from schema.TimelineSchema import timeline_dict,timeline_list
from schema.IdeaSchema import idea_dict,idea_list
from schema.UserSchema import user_dict,user_list
from schema.MentorSchema import mentor_dist,mentor_list
from schema.ProjectSchema import dict_schema,list_schema
from schema.ProgramSchema import program_dist,program_list
from schema.ProposalSchema import proposal_dist,proposal_list
from starlette.requests import Request  
from google.auth.transport import requests
from fastapi.responses import JSONResponse
from bson import ObjectId
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET =os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI")
import requests
route = APIRouter()

#projects 
@route.post('/project')
async def get_projects(request:Request):
    data = await request.json()
    project = dict_schema(data)
    collection_projects.insert_one(project)
    return{"success":"true"}

@route.get('/projects')
async def get_projects():
    projects = list_schema(collection_projects.find())
    return projects

#timeline
@route.get('/timeline')
async def get_timeline():
    timeline =collection_timeline.find({})
    timelines=[]
    for x in timeline:
        timeline_data = timeline_dict(x)
        timelines.append(timeline_data)
    return{'status':'ok','data':timelines}

@route.post('/timeline')
async def post_timeline(request:Request):
    data = await request.json()
    timeline = timeline_dict(data)
    collection_timeline.insert_one(timeline)
    return{'status':'success'}
 
@route.put('/updatetimeline/{id}/{done}')
async def update_timeline(id:str,done:bool):
 collection_timeline.update_one(
    {"_id": ObjectId(id)},
    {"$set": {"completed": done}}  
 )
 return{'status':'success'}
 
    
#google authentication
@route.post("/auth/google")
async def auth_google(request:Request):
    data = await request.json()
    code = data['code']
    token_url = "https://accounts.google.com/o/oauth2/token"
    
    data = {
        "code": code,
        "client_id": {GOOGLE_CLIENT_ID},
        "client_secret":{GOOGLE_CLIENT_SECRET},
        "redirect_uri": {GOOGLE_REDIRECT_URI},
        "grant_type": "authorization_code",
        "expires_in": 86400
    }
    response = requests.post(token_url, data=data)
    resp=  response.json()
    access_token=resp.get("access_token")
    refresh_token = resp.get("refresh_token")
    if(access_token):
        user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
        return {"success":True, "user":user_info.json(),"token":access_token,"refresh":refresh_token}
    else:      return {"success":False}
   
#token verification
@route.post("/token")
async def get_user(request:Request):
    data = await request.json()
    token = data['access_token']
    refresh_token = data['refresh_token']
   
    data = {
        "client_id": {GOOGLE_CLIENT_ID},
        "client_secret": {GOOGLE_CLIENT_SECRET},
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }

    try:
     user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {token}"})
     response = requests.post("https://oauth2.googleapis.com/token", data=data)
     response_data = response.json()
     if response.ok:
        access_token = response_data["access_token"]
     else:
        return {"success":False}
     getuser=user_info.json()
     if getuser is None or 'id' not in getuser:
      user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
      getuser = user_info.json()
     user=collection_users.find_one({'id':getuser["id"]})
     return {"success":True, "image":getuser["picture"],'user':user,"access_token":access_token}
    
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

#edit_timeline
@route.post("/")
async def edit_timeline(request:Request):
    data = await request.josn()
    status = data.status
    Id = data.id
    id = ObjectId(Id)
    item = collection_timeline.find_one({"_id": id})
    new_values = {"$set": {"date": item.date, "events": item.events,"completed":status}}
    collection_timeline.update_one({"_id": id}, new_values)

#user
@route.post("/user")
async def create_user(request:Request):
    data = await request.json()
    user = user_dict(data)
    collection_users.insert_one(user)
    return{"success":"true"}

@route.post("/userinfo")
async def get_user(request:Request):
    data = await request.json()
    id= data['id']
    
    user =collection_users.find_one({'id':id})
    if(user):
     user_format = user_dict(user)
     return {"success":"true",'user':user_format}
    else :
     return{"success":'false'}

@route.put("/updateuser")
async def update_user(request:Request):
   resp = await request.json()
   data= resp['updateduser']
   user = collection_users.find_one({"id": data['id']})
   if user is None:
      return{"success":"false","error":"user is not found"}
   else :
      update_user = user_dict(data)
      collection_users.update_one(
        {"_id": user["_id"]}, 
        {"$set": update_user}  
    )
   return {"success":'true',"update_user":update_user}

#mentor
@route.post("/tobementor")
async def request_mentor(request:Request):
   resp = await request.json()
   user = collection_mentors.find_one({"id":resp["id"]})
   if(user):
      return{"success":False,'msg':"You have already sent your request."}
   else:
    mentor = mentor_dist(resp)
    collection_mentors.insert_one(mentor)
    return{"success":True,'msg':"Successfully sent request"}

@route.post("/acceptmentor")
async def acceptmentor(request:Request):
    resp = await request.json()
    user = collection_users.find_one({"id": resp['id']})
    user['role']='2'
    collection_users.update_one(
        {"_id": user["_id"]}, 
        {"$set": user}  )
    collection_mentors.delete_one({"id":  resp["id"]})
    return{"success":"true"}
   
@route.get("/getrequests")
async def getmentor_requests():
    mentors = mentor_list(collection_mentors.find())
    return mentors

@route.get("/allmentors")
async def getmentors():
   mentors = collection_users.find({'role':'2'})
   mentors = user_list(mentors)
   return mentors
#ideas
@route.post("/idea")
async def create_idea(request:Request):
   try:
    resp = await request.json()
    idea = idea_dict(resp)
    collection_ideas.insert_one(idea)
    return {'success':'true'}
   except requests.exceptions.RequestException as e:
    return {"success": False, "error": str(e)}
@route.get("/idea")
async def getallideas():
    ideas = idea_list(collection_ideas.find())
    return ideas

#programs
@route.post("/program")
async def add_program(request:Request):
   try:
    resp = await request.json()
    program = program_dist(resp)
    collection_programs.insert_one(program)
    return {'success':'true'}
   except requests.exceptions.RequestException as e:
    return {"success": False, "error": str(e)}

@route.get("/pastprograms")
async def getpastprograms():
    programs = program_list(collection_programs.find())
    return programs

#addsprojects
@route.post("/users/project")
async def append_project_to_user(request: Request):
    resp = await request.json()
    user_id = resp["user"]
    project_id = resp["_id"]
    user = collection_users.find_one({"id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found", success=False)
        
    user = user_dict(user)  # Assuming user_dict is defined elsewhere and returns a dict
    
    if len(user["projects"]) >= 2:
        return {"success": False, 'msg': "Already applied for two projects"}
    
    project = collection_projects.find_one({"_id": ObjectId(project_id)})
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_user = collection_users.update_one(
        {"id": user_id},
        {"$addToSet": {"projects": project}}
    )
    user = collection_users.find_one({"id":user_id})
    user = user_dict(user)
    proposal = resp["proposal"]
    collection_proposals.insert_one(proposal)
    proposal=proposal_dist(proposal)
    return {"msg": "Project appended to user successfully","proposal":proposal,"user":user}
@route.get("/{user_id}/projects")
async def user_projects(user_id:str):
   user = collection_users.find_one({"id":user_id})  
   projects = list_schema(user["projects"])
   return projects

#proposal
route.post("/addproposal")
async def addproposal(request:Request):
   data = await request.json()
   proposal = collection_proposals.insert_one(data)
   proposal = proposal_dist(proposal)
   return{"success":"true","proposal":proposal}

@route.delete("/deleteproposal")
async def deleteproposal(user_id: str = Query(...), title: str = Query(...)):
   user_id = (user_id)
   collection_users.update_one(
        {'id':user_id},  
        {'$pull': {'projects': {'title':title}}}, 
    )
   user = collection_users.find_one({"id":user_id})
   user = user_dict(user)
   return{"success":"true","msg":"Deleted proposal","user":user}

@route.get("/proposals/{mentor}")
async def getproposals(mentor:str): 
   proposals = collection_proposals.find({"mentor":mentor})
   proposals = proposal_list(proposals)
   return proposals