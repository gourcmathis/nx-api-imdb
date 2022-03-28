import http3

client = http3.AsyncClient()

async def call_usage(api_key: str):
    res = await client.get("https://imdb-api.com/API/Usage/"+api_key)
    return res.json()

async def call_TOP100(url: str, api_key: str):
    res = await client.get(url+"/"+api_key)
    return res.json()
