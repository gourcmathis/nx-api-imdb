from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv 
from src.imdb import *
import json
import os
import src.requestsimdb as requestsimdb

load_dotenv()
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
async def usage():
    return (await requestsimdb.call_usage(API_USAGE, API_key))

@router.get("/search/{title}")
async def searchByTitle(title: str):
    request = await requestsimdb.call_searchByTitle(API_SEARCH_TITLE, API_key, title)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])

@router.get("/get_films")
async def get100MostPopularFilms():
    request = await requestsimdb.call_TOP100(API_TOP100, API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["items"])

@router.get("/get_250")
async def getTOP250IMDBfilms():
    request = await requestsimdb.call_TOP250IMDB(API_ADVANCED,API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])
