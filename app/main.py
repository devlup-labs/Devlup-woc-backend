from fastapi import FastAPI
from routes import devlup_route
from routes import woc_route
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
@app.get('/')
def read_root():
    return {"Hello": "World"}
app.include_router(woc_route.route)
app.include_router(devlup_route.route)

