from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URL= os.environ.get("MONGO_URL")
client = MongoClient({MONGO_URL})

try:
    client.admin.command('ping')
    print('database connected')
    db = client["DevlupWoc"]
    collection_projects = db["projects"]
    collection_timeline = db["timeline"]
    collection_users = db["users"]
    collection_users.create_index(
        [("first_name", 1), ("last_name", 1)],
        unique=True,
        name="firstname_lastname_unique"
    )
    collection_mentors = db["mentors"]
    collection_ideas = db["ideas"]   
    collection_programs = db["programs"]  
    collection_proposals = db["proposals"]  
    collection_progress = db["progress"]

except:
    print('database not connected')