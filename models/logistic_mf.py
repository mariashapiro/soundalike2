import os
import pickle
import numpy as np
import implicit

import utils

class Recommender:
    def __init__(self, data_path='data/train_triplets.txt', load=True):
        self.load = load
        self.users, self.songs, self.listens = utils.load_triplets(data_path)
        print(self.songs[0])
        self.song_titles = utils.load_song_titles('data/unique_tracks.txt')

        self.model = implicit.lmf.LogisticMatrixFactorization()


    def recommend(self, song_id, k=10):
        print('Start recommendations...')
        listen_mat = utils.create_listen_matrix(load=self.load)

        print('Find unique songs...')
        if self.load and os.path.isfile('data/unique_songs.pkl'):
            songs_uniq = utils.pickle_load('data/unique_songs.pkl')
        else:
            songs_uniq = np.unique(self.songs)
            utils.pickle_dump(songs_uniq, 'data/unique_songs.pkl')

        print('Map songs to index...')
        if self.load and os.path.isfile('data/song_map.pkl'):
            song_map = utils.pickle_load('data/song_map.pkl')
        else:
            song_map = {k: v for v, k in enumerate(songs_uniq)}
            utils.pickle_dump(song_map, 'data/song_map.pkl')

        if self.load and os.path.isfile('data/lfm_model.pkl'):
            self.model = utils.pickle_load('data/lfm_model.pkl')
        else:
            self.model.fit(listen_mat)
            utils.pickle_dump(self.model, 'data/lfm_model.pkl')

        song_idx = song_map[song_id]
        print(song_idx)
        sim_songs = self.model.similar_items(song_idx, N=(k+1), item_users=listen_mat)
        rec_inds = sim_songs[0][1:k+1]
        print(rec_inds)
        rec_scores = sim_songs[1][1:k+1]
        
        rec_titles = []
        for rec_idx in rec_inds:
            song_id = self.songs[rec_idx]
            print(song_id)
            song_title = self.song_titles[self.song_titles['song_id'] == song_id]['song_title'].iloc[0]
            rec_titles.append(song_title)

        return rec_titles


def main():
    rec = Recommender(data_path='data/train_triplets.txt')
    print(rec.song_titles[rec.song_titles['song_id'] == 'SOBNXNE12AB0187B37']['song_title'].iloc[0])
    print(rec.recommend('SOBNXNE12AB0187B37', k=5))


if __name__ == "__main__":
    main()
