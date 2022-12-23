from pymongo import MongoClient
from helpers.logger import get_logger
from core.normalized_data import NormalizedDataByTime
import traceback

POST_COLL = MongoClient().ftmBackendDB.post
MATCH_USER_COLL = MongoClient().ftmBackendDB.match_user
SOURCE_FB = "[FB]"
SOURCE_TW = "[TW]"


def hash(s):
    import hashlib
    return int(hashlib.sha256(s.encode('UTF-8')).hexdigest(), base=16) % (10**18)


async def run_core(d, cache):
    await d.extract_keyword(["tpr"], cache)
    await d.evaluate_keyword()
    await d.identify_topic(["tpr"], cache)
    await d.display(cache)
    print(d._id, d.username, d.source)


async def run(tw_id: str, cache: bool = False, fetch_data_only: bool = False):
    try:
        tw_id_h = hash(SOURCE_TW + tw_id)
        get_logger().info(f"Get {tw_id} {tw_id_h}")
        match_user = MATCH_USER_COLL.find_one({"_id": tw_id_h})['user_id']
        data = [POST_COLL.find_one({"_id": tw_id_h})] + [POST_COLL.find_one({"_id": int(u)}) for u in match_user]
        data = [NormalizedDataByTime(d['_id'], d['username'], d['post'], d['user_id'], d['source']) for d in data]
        if fetch_data_only:
            return [d.__dict__ for d in data]
        # await asyncio.gather(*[wrap(d, cache) for d in data])
        for d in data:
            await run_core(d, cache)
        return [d.__dict__ for d in data]
    except Exception as e:
        print(f"Failed to get data {str(e)}: {traceback.format_exc()}")
        return []