from fastapi import FastAPI, Depends
from app.api import call


app = FastAPI()
app.include_router(call.router)

@app.get("/")
async def main_root(): 
    return {"Visit /docs to try the API"}