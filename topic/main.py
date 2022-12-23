from fastapi import FastAPI
from typing import List
import pandas as pd
import numpy as np
import os
from fastapi.responses import JSONResponse
from helpers.logger import get_logger
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity
import fasttext
import traceback

os.chdir(os.path.dirname(__file__))


class ModelInit():

    @staticmethod
    def load():
        MODEL_PATH = "./data/fasttext_twitter_25.bin"
        model = fasttext.load_model(MODEL_PATH)
        return model


class TopicIdentifier():

    def __init__(self, model):
        TOPIC_DATA_PATH = "./data/topic.csv"
        df = pd.read_csv(TOPIC_DATA_PATH)
        df = df.groupby(df['topic'])['word'].apply(list).reset_index(name='word')
        topic = {}
        for _, row in df.iterrows():
            topic[row['topic']] = np.array([model.get_word_vector(w) for w in set(row['word'])])
        get_logger().info(f'TopicIdentifierInit done')
        self.MODEL = model
        self.TOPIC = topic

    def identify(self, keywords):
        try:
            kw_flat = [w for kw in keywords for w in kw.split()]
            kw_emb = np.array([self.MODEL.get_word_vector(w) for w in kw_flat])
            result = {}
            for topic, emb in self.TOPIC.items():
                d = cosine_similarity(kw_emb, emb)
                d = d.sum().tolist()
                d_nrm = d / (len(emb) * len(kw_flat))
                result[topic] = round(d_nrm, 4)
            return result
        except:
            return {}


class SimilarityCaculator():

    def __init__(self, model):
        self.MODEL = model

    def calculate(self, text, text_compare):
        try:
            kw_flat = [w for kw in text for w in kw.split()]
            kw_emb = np.array([self.MODEL.get_word_vector(w) for w in kw_flat])
            lb_flat = [w for kw in text_compare for w in kw.split()]
            lb_emb = np.array([self.MODEL.get_word_vector(w) for w in lb_flat])
            d = cosine_similarity(kw_emb, lb_emb)
            d = d.sum().tolist()
            d_nrm = d / (len(lb_flat) * len(kw_flat))
            d_nrm = round(d_nrm, 4)
            return {'similarity': d_nrm}
        except:
            return {}


# class Clusterer():

#     def __init__(self, model):
#         self.MODEL = model

#     def cluster(self, texts):
#         try:
#             texts = [text if text else ["a"] for text in texts]
#             text_flats = [[w for kw in text for w in kw.split()] for text in texts]
#             text_emb = np.array([np.array([self.MODEL.get_word_vector(w) for w in text_flat]).mean(axis=0) for text_flat in text_flats])
#             # cluster = OPTICS(n_clusters=12, assign_labels='discretize', random_state=0).fit(text_emb).labels_.tolist()
#             cluster = OPTICS(metric='cosine', min_cluster_size=8).fit(text_emb).labels_.tolist()
#             return {'cluster': cluster}
#         except Exception as e:
#             print(f"Failed to cluster {str(e)}")
#             return []


class Clusterer():

    def __init__(self, model):
        self.MODEL = model

    def cluster(self, text, text_compare):
        try:
            cluster = [similar_calculator.calculate(text, tc).get('similarity', -1) for tc in text_compare]
            return {'cluster': cluster}
        except Exception as e:
            print(f"Failed to cluster {traceback.format_exc()}")
            return []


class TopicRequest(BaseModel):
    data: List[str]


class SimilarityRequest(BaseModel):
    text: List[str]
    text_compare: List[str]


class ClusterRequest(BaseModel):
    text: List[str]
    text_compare: List[List[str]]


app = FastAPI()

model = None
topic_identifier = None
similar_calculator = None
clusterer = None


@app.on_event("startup")
async def startup_event():
    global model
    global topic_identifier
    global similar_calculator
    global clusterer
    model = ModelInit.load()
    topic_identifier = TopicIdentifier(model)
    similar_calculator = SimilarityCaculator(model)
    clusterer = Clusterer(model)


@app.post("/v1/topic")
def topic(q: TopicRequest):
    data = topic_identifier.identify(q.data)
    return JSONResponse(content={'data': data}, status_code=200)


@app.post("/v1/similarity")
def similarity(q: SimilarityRequest):
    data = similar_calculator.calculate(q.text, q.text_compare)
    return JSONResponse(content={'data': data}, status_code=200)


@app.post("/v1/cluster")
def similarity(q: ClusterRequest):
    data = clusterer.cluster(q.text, q.text_compare)
    return JSONResponse(content={'data': data}, status_code=200)
