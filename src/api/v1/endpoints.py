from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv 
import json
import os
import src.api.imdb as imdb
from ..constants import *

load_dotenv()
API_key=os.getenv("API_key")


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/usage", tags=["API Usage"])
async def usage():
    return (await imdb.call_usage(API_USAGE, API_key))

@router.get("/search/{title}", tags=["Search films by name"])
async def searchByTitle(title: str):
    request = await imdb.call_searchByTitle(API_SEARCH_TITLE, API_key, title)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])

@router.get("/get_trailer/{id}", tags=["Get trailer of a film"])
async def get_trailer(id: str):
    request = await imdb.call_get_trailer(API_GET_TRAILER, API_key, id)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["videoUrl"])

@router.get("/get_100", tags=["Get a set of TOP 100 films"])
async def getTOP100IMDBfilms():
    request = await imdb.call_TOP100IMDB(API_ADVANCED,API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])
