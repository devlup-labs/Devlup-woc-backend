
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Get the MongoDB connection URIs from environment variables
MONGO_URL_DEVLUP = os.environ.get("MONGO_URL_DEVLUP")
MONGO_URL_WOC = os.environ.get("MONGO_URL_WOC")

# Connecting to the MongoDB servers for Devlup and Woc
client_devlup = MongoClient(MONGO_URL_DEVLUP)
client_woc = MongoClient(MONGO_URL_WOC)

try:
    # Checking if thedatabase connection is successful
    client_devlup.admin.command('ping')
    print('Devlup database connected')

    # Access the databases
    db_devlup= client_devlup["Devlup-woc-backend"]
    collection_timeline1 = db_devlup["TimelinePage"]
    collection_team1 = db_devlup["TeamAll"]


    # Checkingif Woc database connection is successful
    client_woc.admin.command('ping')
    print('Woc database connected')

    # Access the Woc database
    db_woc = client_woc["Woc"]

    # Define collections for the Woc database 
    collection_projects = db_woc["projects"]
    collection_timeline = db_woc["timeline"]
    collection_users = db_woc["users"]
    collection_mentors = db_woc["mentors"]
    collection_ideas = db_woc["ideas"]
    collection_programs = db_woc["programs"]

except Exception as e:
    print('Database connection error:', e)