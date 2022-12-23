from typing import List
import pke
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from rake_nltk import Rake
from gsdmm import MovieGroupProcess
# from helpers.logger import get_logger
import numpy as np


class ExtractorBase:

    def rake_extractor(data, n_best):
        N_GRAM = 2
        r = Rake(min_length=N_GRAM, max_length=N_GRAM, include_repeated_phrases=False)
        r.extract_keywords_from_text(data)
        return r.get_ranked_phrases()[:n_best]

    def multipartite_rank_extractor(data, n_best):
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(data, language='en')
        pos = {'NOUN', 'PROPN', 'ADJ'}
        extractor.candidate_selection(pos=pos)
        # Build the Multipartite graph and rank candidates using random walk,
        #    alpha controls the weight adjustment mechanism, see TopicRank for
        #    threshold/method parameters.
        extractor.candidate_weighting(alpha=1.1, threshold=0.74, method='average')
        keyphrases = extractor.get_n_best(n=n_best)
        results = []
        for scored_keywords in keyphrases:
            for keyword in scored_keywords:
                if isinstance(keyword, str):
                    results.append(keyword)
        return results

    def topic_rank_extractor(data, n_best):
        extractor = pke.unsupervised.TopicRank()
        extractor.load_document(data, language='en')
        pos = {'NOUN', 'PROPN', 'ADJ'}
        extractor.candidate_selection(pos=pos)
        extractor.candidate_weighting()
        keyphrases = extractor.get_n_best(n=n_best)
        results = []
        for scored_keywords in keyphrases:
            for keyword in scored_keywords:
                if isinstance(keyword, str):
                    results.append(keyword)
        return results

    def lda_extractor(data, n_best):
        LDA_THRESH = 2
        cv = CountVectorizer(max_df=1, min_df=1, stop_words='english')
        dtm = cv.fit_transform(data.split("."))
        lda = LatentDirichletAllocation(n_components=n_best, random_state=42)
        lda_fit = lda.fit(dtm)
        # for id_value, value in enumerate(lda_fit.components_):
        #     print(f"The topic would be {id_value}")
        #     print([cv.get_feature_names()[index] for index in value.argsort()[-10:]])
        top_keywords = [[cv.get_feature_names()[index] for index in topics.argsort()[-LDA_THRESH:]] for topics in lda_fit.components_]
        top_keywords = [" ".join(topic) for topic in top_keywords]
        return top_keywords[:n_best]

    def tfidf_extractor(data, n_best):
        tfidf_vectorizer = TfidfVectorizer(max_df=1, min_df=1, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(data.split("."))
        importance = np.argsort(np.asarray(tfidf.sum(axis=0)).ravel())[::-1]
        tfidf_feature_names = np.array(tfidf_vectorizer.get_feature_names())
        return tfidf_feature_names[importance[:n_best]].tolist()

    def gsdmm_extractor(data, n_best):
        GSDMM_WORD_PER_TOPIC = 2

        def top_words(cluster_word_distribution, top_cluster, values):
            result = []
            for cluster in top_cluster:
                sort_dicts = sorted(cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:values]
                keyword = " ".join([p[0] for p in sort_dicts])
                if keyword:
                    result.append(keyword)
            return result[:n_best]

        data = [sent.split() for sent in data.split(".")]
        mgp = MovieGroupProcess(K=int(n_best * 1.2), alpha=0.4, beta=0.4, n_iters=40)
        mgp.fit(data, 1000)
        doc_count = np.array(mgp.cluster_doc_count)
        top_index = doc_count.argsort()[-n_best:][::-1]

        return top_words(mgp.cluster_word_distribution, top_index, GSDMM_WORD_PER_TOPIC)


class Extractor(ExtractorBase):

    METHOD_MAP = {
        "mpr": ExtractorBase.multipartite_rank_extractor,
        "tpr": ExtractorBase.topic_rank_extractor,
        "gsdmm": ExtractorBase.gsdmm_extractor,
        "lda": ExtractorBase.lda_extractor,
        "rake": ExtractorBase.rake_extractor,
        "tfidf": ExtractorBase.tfidf_extractor
    }

    def __init__(self):
        pass

    @classmethod
    def extract(cls, method: str, data: str, n_best: int) -> List[str]:
        try:
            if not data:
                return []
            return cls.METHOD_MAP[method](data, n_best)
        except Exception as e:
            # get_logger().error(f"Error in extractor: {e}")
            return []

    @classmethod
    def extract_all(cls, data: str, n_best: int) -> List[str]:
        result = {}
        # import time
        # start = time.time()
        for m, method in cls.METHOD_MAP.items():
            # print(f"Extracting {m} in {time.time() - start} seconds")
            # start = time.time()
            result[m] = method(data, n_best)
        return result