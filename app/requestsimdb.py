import http3

client = http3.AsyncClient()

async def call_api(url: str, api_key: str):
    r = await client.get(url+"/"+api_key)
    return r.json()