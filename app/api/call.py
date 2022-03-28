from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv 
import json
import os
import app.requestsimdb as requestsimdb

load_dotenv()
External_API=os.getenv("External_API")
API_key=os.getenv("API_key")

class baseFilms(BaseModel):
    id = str
    title: str
    year: str
    image: str
    imDbRating: str
    # genre: str


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/get_films")
async def getFilmsJSON():
    request = await requestsimdb.call_api(External_API, API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["items"])
