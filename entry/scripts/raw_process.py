import json
import os
from collections import defaultdict
from pymongo import MongoClient
import traceback


def hash(s):
    import hashlib
    return int(hashlib.sha256(s.encode('UTF-8')).hexdigest(), base=16) % (10**18)


POST_COLL = MongoClient().ftmBackendDB.post
MATCH_USER_COLL = MongoClient().ftmBackendDB.match_user

SOURCE_FB = "[FB]"
SOURCE_TW = "[TW]"

tw_id_set = set()


def facebook_raw_to_mongo():
    POST_COLL.delete_many({})
    MATCH_USER_COLL.delete_many({})
    DIR_PATH = "./data/facebook-raw/"
    post_dict = defaultdict(lambda: {'username': "", 'post': [], 'source': '', 'user_id': ""})
    match_user_dict = defaultdict(list)
    for json_path in os.listdir(DIR_PATH):
        if not json_path.endswith(".json"):
            continue
        try:
            with open(os.path.join(DIR_PATH, json_path)) as file:
                tw_id = json_path.split("_")[0].lower()
                tw_id_h = hash(SOURCE_TW + tw_id)
                tw_id_set.add(tw_id)
                print(tw_id, tw_id_h)
                jos = list(json.load(file))
                first_jo = jos[0]
                h = hash(SOURCE_FB + first_jo["user_id"])
                if h not in match_user_dict[tw_id_h]:
                    match_user_dict[tw_id_h].append(h)
                post_dict[h]['user_id'] = first_jo["user_id"]
                post_dict[h]['source'] = SOURCE_FB
                post_dict[h]['username'] = first_jo["username"]
                for jo in jos:
                    try:
                        post_dict[h]['post'].append({
                            'post_id': jo["post_id"],
                            'timestamp': jo["timestamp"],
                            'text': jo["text"],
                        })
                    except:
                        pass
        except Exception as e:
            print("Error in file: ", json_path, traceback.format_exc())
    post = [{'_id': k} | dict(v) for k, v in post_dict.items()]
    match_user = [{'_id': k, 'user_id': v} for k, v in match_user_dict.items()]
    for v in post:
        s = f"{v['_id']}-{len(v['post'])}-{v['username']}-{v['user_id']}-{v['source']}"
        print(s)
    print(match_user)
    print(tw_id_set)
    POST_COLL.insert_many(post)
    MATCH_USER_COLL.insert_many(match_user)


# print(matched)
# print(tw_id_set)


def twitter_raw_to_mongo():
    DATA_PATH = "./data/twitter-raw/raw.json"
    with open(DATA_PATH) as file:
        data = json.load(file)
    post_dict = defaultdict(lambda: {'username': "", 'post': [], 'source': '', 'user_id': ""})
    for jo in data:
        try:
            h = hash(SOURCE_TW + jo["user_id"])
            post_dict[h]['user_id'] = jo["user_id"]
            post_dict[h]['source'] = SOURCE_TW
            post_dict[h]['username'] = jo["username"]
            post_dict[h]['post'].append({
                'post_id': jo["post_id"],
                'timestamp': jo["timestamp"],
                'text': jo["text"],
            })
        except:
            pass
    post = [{'_id': k} | dict(v) for k, v in post_dict.items()]
    for v in post:
        s = f"{v['_id']}-{len(v['post'])}-{v['username']}-{v['user_id']}-{v['source']}"
        print(s)
    POST_COLL.insert_many(post)


if __name__ == "__main__":
    POST_COLL.delete_many({})
    MATCH_USER_COLL.delete_many({})
    facebook_raw_to_mongo()
    print("[Facebook done]")
    twitter_raw_to_mongo()
    print("[Twitter done]")
