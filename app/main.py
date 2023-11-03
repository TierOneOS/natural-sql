from fastapi import FastAPI
from app.routers import queryRouter

app = FastAPI()

@app.get("/")
async def ping():
    return {"Hello": "World"}

app.include_router(queryRouter.router)
