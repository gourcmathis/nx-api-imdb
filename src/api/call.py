from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv 
import http3
import json
import os


client = http3.AsyncClient()

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


async def call_api(url: str, api_key: str):
    r = await client.get(url+"/"+api_key)
    return r.json()


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/get_films")
async def getFilmsJSON():
    request = await call_api(External_API, API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["items"])
