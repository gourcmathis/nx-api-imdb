import http3

client = http3.AsyncClient()

async def call_usage(url:str, api_key: str):
    res = await client.get(url+api_key)
    return res.json()

async def call_searchByTitle(url:str, api_key: str, title: str):
    res= await client.get(url+api_key+"/"+title)
    return res.json()

async def call_TOP100IMDB(url:str, api_key: str):
    res= await client.get(url+api_key+"?groups=top_250&count=100")
    return res.json()

async def call_get_trailer(url:str, api_key: str, id: str):
    res = await client.get(url+api_key+"/"+id)
    return res.json()