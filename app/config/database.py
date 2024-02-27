
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Get the MongoDB connection URIs from environment variables
MONGO_URL = os.environ.get("MONGO_URL")

# Connecting to the MongoDB server
client = MongoClient(MONGO_URL)

try:
    # Checking if the database connection is successful
    client.admin.command('ping')
    print('Database connected')

    # Accessing the database
    db = client["Devlup-woc-backend"]

   # Accessing  the collections

    collection_timeline1 = db["TimelinePage"]
    collection_team1 = db["TeamAll"]
    collection_blog1 = db["BlogPage"]
    collection_project1 = db["Projects1"]
    collection_videos1=db["videosPage"]
    # for Woc
    collection_projects = db["projects"]
    collection_timeline = db["timeline"]
    collection_users = db["users"]
    collection_mentors = db["mentors"]
    collection_ideas = db["ideas"]
    collection_programs = db["programs"]

except Exception as e:
    print('Database connection error:', e)