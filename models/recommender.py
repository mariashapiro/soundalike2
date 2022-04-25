import implicit

import utils

class Recommender:
    def __init__(self, type='cos', params={}, load=True):
        self.type = type
        self.load = load
        self.users, self.songs, self.listens = utils.load_triplets()
        self.song_titles = utils.load_song_titles('data/unique_tracks.txt')

        if type == 'cos':
            K = params.get('K', 10)
            self.model = implicit.nearest_neighbours.CosineRecommender(K=K)
        elif type == 'lmf':
            factors = params.get('factors', 30)
            lr = params.get('learning_rate', 1.00)
            reg = params.get('regularization', 0.6)
            iter = params.get('iterations', 30)
            neg_prop = params.get('neg_prop', 30)
            self.model = implicit.lmf.LogisticMatrixFactorization(
                    factors=factors,
                    learning_rate=lr, 
                    regularization=reg, 
                    iterations=iter, 
                    neg_prop = neg_prop
                )
        elif type == 'als':
            factors = params.get('factors', 100)
            reg = params.get('regularization', 0.01)
            iter = params.get('iterations', 15)
            self.model = implicit.als.AlternatingLeastSquares(
                    factors=factors,
                    regularization=reg, 
                    iterations=iter
                )

    def recommend(self, song_id, k=5):
        print('Start recommendations...')
        listen_mat = utils.create_listen_matrix()

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

        model_fname = 'data/{type}_model.pkl'.format(type=self.type)
        if self.load and os.path.isfile(model_fname):
            self.model = utils.pickle_load(model_fname)
        else:
            self.model.fit(listen_mat)
            utils.pickle_dump(self.model, model_fname)

        song_idx = song_map[song_id]
        sim_songs = self.model.similar_items(song_idx, N=(k+1))
        rec_inds = sim_songs[0][1:k+1]
        rec_scores = sim_songs[1][1:k+1]
        
        rec_titles = []
        for rec_idx in rec_inds:
            song_id = self.songs[rec_idx]
            song_title = self.song_titles[self.song_titles['song_id'] == song_id]['song_title'].iloc[0]
            rec_titles.append(song_title)

        return rec_titles


def main():
    rec = Recommender(type='lfm', load=True)
    print(rec.song_titles[rec.song_titles['song_id'] == 'SOBNXNE12AB0187B37']['song_title'].iloc[0])
    print(rec.recommend('SOBNXNE12AB0187B37', k=5))

if __name__ == "__main__":
    main()