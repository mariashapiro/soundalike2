import os
import pickle
import numpy as np
import pandas as pd
import scipy.sparse as sparse
from sklearn.metrics.pairwise import cosine_similarity

import utils

class Recommender:
    def __init__(self, data_path='data/train_triplets.txt', load=True):
        self.load = load
        self.users, self.songs, self.listens = utils.load_triplets(load=self.load)
        self.song_titles = utils.load_song_titles('data/unique_tracks.txt')


    # calculate similarities between songs (if axis=0) or users
    def create_sim_matrix(self, listen_mat, axis=0):
        if self.load and os.path.isfile('data/similarity_matrix.pkl'):
            return utils.pickle_load('data/similarity_matrix.pkl')

        mat = listen_mat
        # normalize song vectors using L2-norm
        norms = sparse.csr_matrix(1/np.sqrt(mat.multiply(mat).sum(1)), dtype=np.int32).transpose()
        norm_mat = mat.multiply(norms)
        if axis == 0:
            sim_mat = cosine_similarity(norm_mat.transpose(), dense_output=False)
        else:
            sim_mat = cosine_similarity(norm_mat, dense_output=False)

        utils.pickle_dump(sim_mat, 'data/similarity_matrix.pkl')

        return sim_mat


    def recommend(self, song_id, k=10):
        print('Start recommendations...')
        listen_mat = utils.create_listen_matrix(load=self.load)
        sim_mat = self.create_sim_matrix(listen_mat, axis=0)
        songs_uniq = np.unique(self.songs)
        song_map = {k: v for v, k in enumerate(songs_uniq)}
        
        song_idx = song_map[song_id]
        sim_vec = sim_mat.getrow(song_idx).toarray()
        rec_inds = sim_vec.argsort()[::-1][0][:k]
        
        rec_titles = []
        for rec_idx in rec_inds:
            song_id = songs_uniq[rec_idx]
            song_title = self.song_titles[self.song_titles['song_id'] == song_id]['song_title'].iloc[0]
            rec_titles.append(song_title)

        return rec_titles


def main():
    rec = Recommender(data_path='data/train_triplets.txt')
    print(rec.song_titles[rec.song_titles['song_id'] == 'SOBNXNE12AB0187B37']['song_title'].iloc[0])
    print(rec.recommend('SOBNXNE12AB0187B37'))


if __name__ == "__main__":
    main()
