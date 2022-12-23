import aiohttp
import asyncio
import json

async def post(session, url, data):
    resp = await session.request('POST', url=url, json=data)
    jo = await resp.json()
    return jo['data']

async def concurrent_post(url, data_many):
    async with aiohttp.ClientSession() as session:
        tasks = []        
        for data in data_many:
            tasks.append(post(session, url, data))
        results = await asyncio.gather(*tasks)
        return results