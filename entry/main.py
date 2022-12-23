from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from core.pipeline import run
from core.user_identify import UserIdentifier
from core.user_cluster import UserCluster
from helpers.logger import get_logger

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/v1/twitter/{tw_id}")
async def root(tw_id: str = '', cache: bool = True):
    get_logger().info(f"Request received tw_id={tw_id} cache={cache}")
    tw_id = tw_id.lower()
    data = await run(tw_id, cache, fetch_data_only=False)
    result = {}
    result['twitter'] = [d for d in data if d['source'] == "[TW]"]
    result['facebook'] = [d for d in data if d['source'] == "[FB]"]
    result['user_identify'] = await UserIdentifier().identify(result['twitter'][0], result['facebook'], cache)
    result['user_cluster'] = await UserCluster().get(result['twitter'][0], cache)
    return {'data': result}

@app.get("/v1/twitter/fetch_data/{tw_id}")
async def root(tw_id: str = '', cache: bool = True):
    get_logger().info(f"Request received tw_id={tw_id} cache={cache}")
    tw_id = tw_id.lower()
    data = await run(tw_id, cache, fetch_data_only=True)
    results = {'twitter': [d for d in data if d['source'] == "[TW]"], 'facebook': [d for d in data if d['source'] == "[FB]"]}
    return {'data': results}

@app.get("/v1/cluster")
async def root(cache: bool = True):
    get_logger().info(f"/v1/cluster cache={cache}")
    await UserCluster().process(cache)
    return {'data': 'success'}