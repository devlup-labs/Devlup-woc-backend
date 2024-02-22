# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
# 
# # Load environment variables from .env file
# load_dotenv()
# 
# # Get the MongoDB connection URIs from environment variables
# MONGO_URL_DEVLUP = os.environ.get("MONGO_URL_DEVLUP")
# MONGO_URL_WOC = os.environ.get("MONGO_URL_WOC")
# 
# # Connect to the MongoDB servers for Devlup and Woc
# client_devlup = MongoClient(MONGO_URL_DEVLUP)
# client_woc = MongoClient(MONGO_URL_WOC)
# 
# try:
#     # Check if the Devlup database connection is successful
#     client_devlup.admin.command('ping')
#     print('Devlup database connected')
# 
#     # Accessing the Devlup database
#     db_devlup = client_devlup["Devlup-woc-backend"]
# 
#     # Define collections for the Devlup database
#     collection_team1 = db_devlup["TeamAll"]
#     collection_timeline1 = db_devlup["TimelinePage"]
# 
#     # Filter team members into current and alumni based on alumni status
#     collection_current1 = collection_team1.find({"AlumniStatus": 0})
#     collection_alumni1 = collection_team1.find({"AlumniStatus": 1})
# 
#     # Check if the Woc database connection is successful
#     client_woc.admin.command('ping')
#     print('Woc database connected')
# 
#     # Access the Woc database
#     db_woc = client_woc["Woc"]
# 
#     # Define collections for the Woc database (commented-out)
#     collection_projects = db_woc["projects"]
#     collection_timeline = db_woc["timeline"]
#     collection_users = db_woc["users"]
#     collection_mentors = db_woc["mentors"]
#     collection_ideas = db_woc["ideas"]
#     collection_programs = db_woc["programs"]
# 
# except Exception as e:
#     print('Database connection error:', e)
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection URIs from environment variables
MONGO_URL_DEVLUP = os.environ.get("MONGO_URL_DEVLUP")
MONGO_URL_WOC = os.environ.get("MONGO_URL_WOC")

# Connect to the MongoDB servers for Devlup and Woc
client_devlup = MongoClient(MONGO_URL_DEVLUP)
client_woc = MongoClient(MONGO_URL_WOC)

try:
    # Check if the Devlup database connection is successful
    client_devlup.admin.command('ping')
    print('Devlup database connected')

    # Access the databases
    db_devlup= client_devlup["Devlup-woc-backend"]

    # db_team1 = client_devlup["Team"]

    # db_timeline1 = client_devlup["Timeline"]

    # Define collections for the databases, More to add as we go
    # collection_current1 = db_team1["Current"]
    # collection_alumni1 = db_team1["Alumni"]
    collection_timeline1 = db_devlup["TimelinePage"]

    collection_team1 = db_devlup["TeamAll"]


    # Check if the Woc database connection is successful
    client_woc.admin.command('ping')
    print('Woc database connected')

    # Access the Woc database
    db_woc = client_woc["Woc"]

    # Define collections for the Woc database (commented-out)
    collection_projects = db_woc["projects"]
    collection_timeline = db_woc["timeline"]
    collection_users = db_woc["users"]
    collection_mentors = db_woc["mentors"]
    collection_ideas = db_woc["ideas"]
    collection_programs = db_woc["programs"]

except Exception as e:
    print('Database connection error:', e)