from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv 
from src.imdb import *
import json
import os
import src.requestsimdb as requestsimdb

load_dotenv()
API_key=os.getenv("API_key")


router = APIRouter(
    prefix="/api/v1",
)

@router.get("/usage", tags=["API Usage"])
async def usage():
    return (await requestsimdb.call_usage(API_USAGE, API_key))

@router.get("/search/{title}", tags=["Search films by name"])
async def searchByTitle(title: str):
    request = await requestsimdb.call_searchByTitle(API_SEARCH_TITLE, API_key, title)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])

@router.get("/get_trailer/{id}", tags=["Get trailer of a film"])
async def get_trailer(id: str):
    request = await requestsimdb.call_get_trailer(API_GET_TRAILER, API_key, id)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["videoUrl"])

@router.get("/get_films", tags=["Get a set of 100 films"])
async def get100MostPopularFilms():
    request = await requestsimdb.call_TOP100(API_TOP100, API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["items"])

@router.get("/get_250", tags=["Get a set of TOP 250 films"])
async def getTOP250IMDBfilms():
    request = await requestsimdb.call_TOP250IMDB(API_ADVANCED,API_key)
    dictionary = json.dumps(request)
    films = json.loads(dictionary)
    return(films["results"])
