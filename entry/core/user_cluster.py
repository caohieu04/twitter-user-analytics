from pymongo import MongoClient
from helpers.logger import get_logger
from helpers.aiorequest import concurrent_post
from core.normalized_data import NormalizedDataByTime
from itertools import chain

class UserCluster():

    SOURCE_TW = "[TW]"
    POST_COLL = MongoClient().ftmBackendDB.post
    URL_SIMILARITY = "http://localhost:9003/v1/similarity"
    URL_CLUSTER = "http://localhost:9003/v1/cluster"
    BEST_COLL = MongoClient().ftmBackendDB.best
    POST_COLL = MongoClient().ftmBackendDB.post
    CLUSTER_COLL = MongoClient().ftmBackendDB.cluster

    def __init__(self):
        pass

    async def process_one(self, d, cache):
        d = NormalizedDataByTime(d['_id'], d['username'], d['post'], d['user_id'], d['source'])
        await d.extract_keyword(["tpr"], cache)
        await d.evaluate_keyword()
        await d.identify_topic(["tpr"], cache)
        await d.display(cache)
        d = d.__dict__
        print(d['_id'], d['source'], d['username'], d['user_id'])
        return d

    async def process(self, cache):
        for d in self.POST_COLL.find({'source': '[TW]'}):
            await self.process_one(d, cache)

    async def get(self, tw, cache):
        N_MOST_SIMILAR = 12
        _id = tw['_id']
        record = self.CLUSTER_COLL.find_one({'_id': _id})
        if record and cache:
            return record['cluster']
        else:
            self.CLUSTER_COLL.delete_one({'_id': _id})
            users = []
            text = None
            for d in self.BEST_COLL.find():
                p = self.POST_COLL.find_one({'_id': d['_id']})
                if p and p['_id'] == _id:
                    text = list(chain(*d['keyword_best']))
                    continue
                if not p or p['source'] != '[TW]':
                    continue
                user = {'username': p['username'], 'user_id': p['user_id'], '_id': p['_id'], 'source': p['source']}
                kw = list(chain(*d['keyword_best']))
                user['len_keyword_best'] = len(kw)
                user['keyword_best_flat'] = kw
                users.append(user)
            users = sorted(users, key=lambda x: x['len_keyword_best'], reverse=True)[:int(len(users) * 0.3)]
            text_compare = [u['keyword_best_flat'] for u in users]
            body = [{'text': text,'text_compare': text_compare}]
            response = await concurrent_post(self.URL_CLUSTER, body)
            response = response[0]['cluster']
            for r, u in zip(response, users):
                u['similarity'] = r
                u.pop('len_keyword_best')
                u.pop('keyword_best_flat')
            cluster = sorted(users, key=lambda x: x['similarity'], reverse=True)[:N_MOST_SIMILAR]
            self.CLUSTER_COLL.insert_one({'_id': _id, 'cluster': cluster})
            get_logger().info(f"[{_id}] User cluster get {cluster}")
            return cluster
