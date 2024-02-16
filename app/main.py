from fastapi import FastAPI
from app.routes import woc_route, devlup_route
app = FastAPI()

app.include_router(woc_route.route)
app.include_router(devlup_route.route)

