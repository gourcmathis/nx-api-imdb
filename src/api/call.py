from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv 
import json
import os
import src.requestsimdb as requestsimdb

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

@router.get("/usage")
async def usage(api_key: str = API_key):
    return (await requestsimdb.call_usage(api_key))

@router.get("/get_films")
async def getFilmsJSON():
    request = await requestsimdb.call_TOP100(External_API, API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["items"])

