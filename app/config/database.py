from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URL= os.environ.get("MONGO_URL")
client = MongoClient({MONGO_URL})

try:
    client.admin.command('ping')
    print('database connected')
    db = client["Devlup-woc-backend"]
    collection_projects = db["projects"]
    collection_timeline = db["timeline"]
    collection_users = db["users"]
    collection_mentors = db["mentors"]
    collection_ideas = db["ideas"]   
    collection_programs = db["programs"]  
    collection_proposals = db["proposals"]  

 # Accessing  the collections

    collection_timeline1 = db["TimelinePage"]
    collection_team1 = db["TeamAll"]
    collection_blog1 = db["BlogPage"]
    collection_project1 = db["Projects1"]
    collection_videos1=db["videosPage"]

except:
    print('database not connected')