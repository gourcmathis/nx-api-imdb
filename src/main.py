from fastapi import FastAPI, Depends
from src.api.v1 import endpoints

app = FastAPI()
app.include_router(endpoints.router)

@app.get("/")
async def main_root(): 
    return {"Visit /docs to try the API"}