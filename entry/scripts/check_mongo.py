from pymongo import MongoClient

POST_COLL = MongoClient().ftmBackendDB.post
MATCH_USER_COLL = MongoClient().ftmBackendDB.match_user


def hash(s):
    import hashlib
    return int(hashlib.sha256(s.encode('UTF-8')).hexdigest(), base=16) % (10**18)


SOURCE_FB = "[FB]"
SOURCE_TW = "[TW]"

POST_COLL = MongoClient().ftmBackendDB.post
MATCH_USER_COLL = MongoClient().ftmBackendDB.match_user
BEST_COLL = MongoClient().ftmBackendDB.best
CLUSTER_COLL = MongoClient().ftmBackendDB.cluster


def get(tw_id):
    tw_id_h = hash(SOURCE_TW + tw_id)
    jo = POST_COLL.find({"_id": tw_id_h})[0]
    username = jo['username']
    post = jo['post']
    match_user = MATCH_USER_COLL.find({"_id": tw_id_h})[0]['user_id']


# print(len([d for d in CLUSTER_COLL.find()]))
# CLUSTER_COLL.delete_many({})
# print(len([d for d in CLUSTER_COLL.find()]))

# for x in POST_COLL.find({'_id': 416448155431553226}):
#     print(x)
#     break

# for x in MATCH_USER_COLL.find():
#     print(x)
#     break