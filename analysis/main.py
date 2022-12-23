import json
from collections import defaultdict
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import multiprocessing
from joblib import Parallel, delayed
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

PREP_DIR = "./analysis/data/preped"
EXTRACT_DIR = "./analysis/data/extracted"
EXTRACT_DIR_2 = "./analysis/data/extracted_2"


def jaccard_set(list1, list2):
    """Define Jaccard Similarity function for two sets"""
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def mean_reciprocal_rank(l1, l2):
    rank_map = {}
    for i, v in enumerate(l2):
        if v not in rank_map:
            rank_map[v] = 1. / (i + 1)
    rr = 0
    for v in l1:
        rr += rank_map.get(v, 0)
    return rr / len(l1)


def extract_keyword(path):
    if os.path.exists(os.path.join(EXTRACT_DIR, path)):
        print(f'Exists {path}')
        return
    with open(os.path.join(PREP_DIR, path), 'rb') as handle:
        d = pickle.load(handle)
        user_id = d['user_id']
        print(f'Processing {user_id}')
        similarities = []

        for method in ['mpr', 'tpr', 'rake', 'gsdmm', 'lda', 'tfidf']:
            cosine_similarity = -1
            for n_best in [5, 10, 15, 20, 25, 30, 35, 40]:
                train_kw = requests.post("http://localhost:9002/v1/keyword", json={'method': method, 'n_best': n_best, 'data': d['train']}).json()['data']
                valid_kw = requests.post("http://localhost:9002/v1/keyword", json={'method': method, 'n_best': n_best, 'data': d['valid']}).json()['data']
                similarity = requests.post("http://localhost:9003/v1/similarity", json={'text': train_kw, 'text_compare': valid_kw}).json()['data']
                try:
                    cosine_similarity = similarity['similarity']
                except Exception as e:
                    print(repr(e))
                    cosine_similarity = -1
                jaccard_similarity = jaccard_set(" ".join(train_kw).split(), " ".join(valid_kw).split())
                similarities.append({
                    'method': method,
                    'n_best': n_best,
                    'train_kw': train_kw,
                    'valid_kw': valid_kw,
                    'cosine_similarity': cosine_similarity,
                    'jaccard_similarity': jaccard_similarity
                })
        temp = {'user_id': user_id, 'cosine_similarities': similarities}
        with open(os.path.join(EXTRACT_DIR, f'{user_id}.pickle'), 'wb') as handle:
            pickle.dump(temp, handle, protocol=pickle.HIGHEST_PROTOCOL)


def extract_keyword_2(path):
    if os.path.exists(os.path.join(EXTRACT_DIR_2, path)):
        print(f'Exists {path}')
        return
    with open(os.path.join(PREP_DIR, path), 'rb') as handle:
        d = pickle.load(handle)
        user_id = d['user_id']
        print(f'Processing {user_id}')
        similarities = []

        for method in ['mpr', 'tpr', 'rake', 'gsdmm', 'lda', 'tfidf']:
            cosine_similarity = -1
            for n_best in [5, 10, 15, 20, 25, 30, 35, 40]:
                start = time.time()
                train_kw = requests.post("http://localhost:9002/v1/keyword", json={'method': method, 'n_best': n_best, 'data': d['train']}).json()['data']
                valid_kw = requests.post("http://localhost:9002/v1/keyword", json={'method': method, 'n_best': n_best, 'data': d['valid']}).json()['data']
                run_time = time.time() - start
                similarity = requests.post("http://localhost:9003/v1/similarity", json={'text': train_kw, 'text_compare': valid_kw}).json()['data']
                try:
                    cosine_similarity = similarity['similarity']
                except Exception as e:
                    print(repr(e))
                    cosine_similarity = -1
                jaccard_similarity = jaccard_set(" ".join(train_kw).split(), " ".join(valid_kw).split())
                mrr = mean_reciprocal_rank(" ".join(train_kw).split(), " ".join(valid_kw).split())
                similarities.append({
                    'method': method,
                    'n_best': n_best,
                    'train_kw': train_kw,
                    'valid_kw': valid_kw,
                    'cosine_similarity': cosine_similarity,
                    'jaccard_similarity': jaccard_similarity,
                    'mean_reciprocal_rank': mrr,
                    'run_time': run_time
                })
        temp = {'user_id': user_id, 'cosine_similarities': similarities}
        with open(os.path.join(EXTRACT_DIR_2, f'{user_id}.pickle'), 'wb') as handle:
            pickle.dump(temp, handle, protocol=pickle.HIGHEST_PROTOCOL)


def do_prep_data():
    d = defaultdict(lambda: {'data': [], 'train': [], 'valid': []})
    with open("./entry/data/twitter-raw/raw.json") as file:
        data = json.load(file)
        data = data
        for jo in data:
            d[jo['user_id']]['data'].append(jo['text'])

    RATIO = 0.95
    for user_id, v in d.items():
        print(f'Preprocessing {user_id}')
        data_len = len(v['data'])
        temp = {'user_id': user_id, 'data': v['data'], 'train': v['data'][:int(data_len * RATIO)], 'valid': v['data'][int(data_len * RATIO):]}
        with open(os.path.join(PREP_DIR, f'{user_id}.pickle'), 'wb') as handle:
            pickle.dump(temp, handle, protocol=pickle.HIGHEST_PROTOCOL)


def do_analysis():
    sns.set_theme()
    df = pd.DataFrame(columns=['method', 'n_best', 'cosine_similarity', 'jaccard_similarity'])
    for path in os.listdir(EXTRACT_DIR):
        with open(os.path.join(EXTRACT_DIR, path), 'rb') as handle:
            d = pickle.load(handle)
            for r in d['cosine_similarities']:
                method, n_best, cosine_similarity, jaccard_similarity = r['method'], r['n_best'], r['cosine_similarity'], r['jaccard_similarity']
                new_row = pd.Series({'method': method, 'n_best': n_best, 'cosine_similarity': cosine_similarity, 'jaccard_similarity': jaccard_similarity})
                df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
    df = df.groupby(by=['method', 'n_best']).mean().reset_index()
    df.to_csv("evaluate.csv", index=False)
    fig_jaccard = sns.lineplot(data=df, x="n_best", y="jaccard_similarity", hue="method")
    fig_jaccard.get_figure().savefig("./analysis/data/graph/jaccard_similarity.svg", format='svg')
    fig_jaccard.get_figure().savefig("./analysis/data/graph/jaccard_similarity.png", dpi=1200)
    plt.clf()
    fig_cosine = sns.lineplot(data=df, x="n_best", y="cosine_similarity", hue="method")
    fig_cosine.get_figure().savefig("./analysis/data/graph/consine_similarity.svg", format='svg')
    fig_cosine.get_figure().savefig("./analysis/data/graph/consine_similarity.png", dpi=1200)


def do_analysis_2():
    sns.set_theme()
    df = pd.DataFrame(columns=['method', 'n_best', 'cosine_similarity', 'jaccard_similarity'])
    for path in os.listdir(EXTRACT_DIR_2):
        with open(os.path.join(EXTRACT_DIR_2, path), 'rb') as handle:
            d = pickle.load(handle)
            for r in d['cosine_similarities']:
                method, n_best, cosine_similarity, jaccard_similarity, run_time, mrr = r['method'], r['n_best'], r['cosine_similarity'], r[
                    'jaccard_similarity'], r['run_time'], r['mean_reciprocal_rank']
                new_row = pd.Series({
                    'method': method,
                    'n_best': n_best,
                    'cosine_similarity': cosine_similarity,
                    'jaccard_similarity': jaccard_similarity,
                    'run_time': run_time,
                    'mean_reciprocal_rank': mrr
                })
                df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
    df = df.groupby(by=['method', 'n_best']).mean().reset_index()
    df.to_csv("evaluate.csv", index=False)

    def gen_fig(name):
        fig = sns.lineplot(data=df, x="n_best", y=name, hue="method")
        fig.get_figure().savefig(f"./analysis/data/graph_2/{name}.svg", format='svg')
        fig.get_figure().savefig(f"./analysis/data/graph_2/{name}.png", dpi=1200)
        plt.clf()

    gen_fig('jaccard_similarity')
    gen_fig('cosine_similarity')
    gen_fig('run_time')
    gen_fig('mean_reciprocal_rank')


if __name__ == '__main__':
    do_prep_data()
    # Parallel(n_jobs=2)(delayed(extract_keyword)(path) for path in os.listdir(PREP_DIR))
    Parallel(n_jobs=2)(delayed(extract_keyword_2)(path) for path in os.listdir(PREP_DIR))
    # do_analysis()
    do_analysis_2()