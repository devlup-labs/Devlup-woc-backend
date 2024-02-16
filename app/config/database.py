from pymongo import MongoClient
from app.variables import MONGO_URI
client = MongoClient(MONGO_URI)

try:
    client.admin.command('ping')
    print('database connected')
    db = client['DevlupWoc']
    collection_projects = db['projects']

except:
    print('database not connected')