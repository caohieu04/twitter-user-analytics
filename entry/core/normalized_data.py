import asyncio
import bisect
from typing import List, Dict
from pymongo import MongoClient
from helpers.logger import get_logger
from helpers.aiorequest import concurrent_post
from collections import defaultdict
import traceback

POST_COLL = MongoClient().ftmBackendDB.post
MATCH_USER_COLL = MongoClient().ftmBackendDB.match_user
SOURCE_FB = "[FB]"
SOURCE_TW = "[TW]"


class NormalizedData():

    URL_KEYWORD = "http://localhost:9002/v1/keyword"
    URL_TOPIC = "http://localhost:9003/v1/topic"
    N_BEST = 40
    KEYWORD_COLL = MongoClient().ftmBackendDB.keyword
    TOPIC_COLL = MongoClient().ftmBackendDB.topic

    def __init__(self, _id: str, data: List[str]):
        self._id = _id
        self.data = data
        self.keyword = {}
        self.topic = {}

    async def extract_keyword(self, kinds, cache):
        try:
            record = self.KEYWORD_COLL.find_one({'_id': self._id})
            if cache and record:
                self.keyword = record['keyword']
            else:
                self.KEYWORD_COLL.delete_one({'_id': self._id})
                post_data = [{'method': kind, 'n_best': self.N_BEST, 'data': self.data} for kind in kinds]
                result = await concurrent_post(self.URL_KEYWORD, post_data)
                self.keyword = {k: v for k, v in zip(kinds, result)}
                self.KEYWORD_COLL.insert_one({'_id': self._id, 'keyword': self.keyword})
        except Exception as e:
            get_logger().warning(f"Failed to extract keyword {str(e)}")
            self.keyword = {}
        return self.keyword

    async def identify_topic(self, kinds, cache):
        try:
            record = self.TOPIC_COLL.find_one({'_id': self._id})
            if cache and record:
                self.topic = record['topic']
            else:
                self.TOPIC_COLL.delete_one({'_id': self._id})
                bodydata = [{'data': self.keyword[kind]} for kind in kinds]
                result = await concurrent_post(self.URL_TOPIC, bodydata)
                self.topic = {k: v for k, v in zip(kinds, result)}
                self.TOPIC_COLL.insert_one({'_id': self._id, 'topic': self.topic})
        except Exception as e:
            get_logger().warning(f"Failed to identify topic {str(e)}")
            self.topic = {}
        return self.topic


class NormalizedDataByTime():

    URL_SIMILARITY = "http://localhost:9003/v1/similarity"
    BEST_COLL = MongoClient().ftmBackendDB.best
    LIMIT_PER_TIMESTAMP = 300
    CURRENT_TIME = 1667477356
    TIMESTAMP_STEP = 7776000  # 3 month
    TIMESTAMP_START = CURRENT_TIME - TIMESTAMP_STEP * 8  # 1597493356
    TIMESTAMP_MARK = [i for i in range(TIMESTAMP_START, CURRENT_TIME + 1, TIMESTAMP_STEP)]

    def __init__(self, _id: str, username: str, post: List[Dict[str, str]], user_id: str, source: str):
        self._id = _id
        self.username = username
        self.user_id = user_id
        self.source = source
        self.data_by_time = {t: [] for t in self.TIMESTAMP_MARK}
        for p in post:
            t_idx = min(len(self.TIMESTAMP_MARK) - 1, bisect.bisect(self.TIMESTAMP_MARK, p['timestamp']))
            t = self.TIMESTAMP_MARK[t_idx]
            if len(self.data_by_time[t]) < self.LIMIT_PER_TIMESTAMP:
                self.data_by_time[t].append(p)
        self.data_by_time = {t: NormalizedData(f"{_id}@{t}", [d['text'] for d in data]) for t, data in self.data_by_time.items() if t != self.TIMESTAMP_START}

    async def extract_keyword(self, kinds, cache):
        await asyncio.gather(*[data.extract_keyword(kinds, cache) for data in self.data_by_time.values()])
        get_logger().info(f"[{self._id}] Extracted keyword")

    async def identify_topic(self, kinds, cache):
        await asyncio.gather(*[data.identify_topic(kinds, cache) for data in self.data_by_time.values()])
        get_logger().info(f"[{self._id}] Identified topic")

    async def evaluate_keyword(self):
        request = defaultdict(lambda: defaultdict(list))
        for time, data in self.data_by_time.items():
            for kind, kw in data.keyword.items():
                if time != self.CURRENT_TIME:
                    request[kind]['text'] += kw
                else:
                    request[kind]['text_compare'] += kw
        body = [body for body in request.values()]
        response = await concurrent_post(self.URL_SIMILARITY, body)
        self.evaluate = {k: v.get('similarity', -1) for k, v in zip(request.keys(), response)}
        get_logger().info(f"[{self._id}] Evaluated keyword")

    async def display(self, cache):
        record = self.BEST_COLL.find_one({'_id': self._id})
        if cache and record:
            self.timeline, self.kind_best, self.keyword_best, self.topic_best = \
                record['timeline'], record['kind_best'], record['keyword_best'], record['topic_best']
            get_logger().info(f"[{self._id}] Displayed from cache")
        else:
            self.BEST_COLL.delete_one({'_id': self._id})
            maxi = -1
            kind_best = ""
            keyword_best = []
            timeline = list(self.data_by_time.keys())
            for k, v in self.evaluate.items():
                if v >= maxi:
                    maxi = v
                    kind_best = k

            for _, data in self.data_by_time.items():
                for kind, kw in data.keyword.items():
                    if kind == kind_best:
                        keyword_best.append(kw)

            topic_best = []
            for time, data in self.data_by_time.items():
                for kind, topic in data.topic.items():
                    if kind == kind_best:
                        topic_best.append(dict(topic.items()))

            self.timeline = timeline
            self.kind_best = kind_best
            self.keyword_best = keyword_best
            self.topic_best = topic_best
            get_logger().info(f"[{self._id}] Pushed to cache")
            self.BEST_COLL.insert_one({'_id': self._id, 'timeline': timeline, 'kind_best': kind_best, 'keyword_best': keyword_best, 'topic_best': topic_best})