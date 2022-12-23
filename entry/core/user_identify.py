from pymongo import MongoClient
from helpers.logger import get_logger
from helpers.aiorequest import concurrent_post
from itertools import chain


class UserIdentifier():

    URL_SIMILARITY = "http://localhost:9003/v1/similarity"
    USER_IDENFITY_COLL = MongoClient().ftmBackendDB.user_identify

    def __init__(self):
        pass

    async def identify(self, tw_data, fb_data_many, cache):
        _id = tw_data['_id']
        try:
            record = self.USER_IDENFITY_COLL.find_one({'_id': _id})
            if cache and record:
                return record['user_identify']
            else:
                self.USER_IDENFITY_COLL.delete_one({'_id': _id})

                tw_kw = list(chain(*tw_data['keyword_best']))
                body = [{'text': tw_kw, 'text_compare': list(chain(*fb_data['keyword_best']))} for fb_data in fb_data_many]
                response = await concurrent_post(self.URL_SIMILARITY, body)
                result = [{
                    'similarity': res.get('similarity', -1),
                    'username': d['username'],
                    'user_id': d['user_id'],
                    '_id': d['_id'],
                    'source': d['source']
                } for d, res in zip(fb_data_many, response)]
                result.sort(key=lambda x: x['similarity'], reverse=True)
                self.USER_IDENFITY_COLL.insert_one({'_id': _id, 'user_identify': result})
                return result
        except Exception as e:
            get_logger().warning(f"Failed to identify user {str(e)}")
            return {}