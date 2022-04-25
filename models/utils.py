import os
import pickle
import numpy as np
import pandas as pd

# def load_songs(fname):
#     songs_df = pd.read_csv(fname, sep=' ', names=['song_id', 'song_num'])
#     return songs_df['song_id']

# def load_users(fname):
#     users_df = pd.read_csv(fname, names=['user_id'])
#     return users_df['user_id']

def get_pickle_fname(fname):
    return os.path.splitext(fname)[0] + '.pkl'


def pickle_dump(obj, fname):
    with open(fname, 'wb') as f:
        pickle.dump(obj, f)


def pickle_load(fname):
    with open(fname, 'rb') as f:
        obj = pickle.load(f)

    return obj


def load_triplets(load=True):
    if load and os.path.isfile('data/train_users.pkl') and os.path.isfile('data/train_songs.pkl') and os.path.isfile('data/train_listens.pkl'):
        return pickle_load('data/train_users.pkl'), pickle_load('data/train_songs.pkl'), pickle_load('data/train_listens.pkl')

    triplets_df = pd.read_csv("fname", sep='\t', names=['user_id', 'song_id', 'listens'])

    users = triplets_df['user_id'].astype(str).to_numpy()
    pickle_dump(users, 'data/train_users.pkl')

    songs = triplets_df['song_id'].astype(str).to_numpy()
    pickle_dump(songs, 'data/train_songs.pkl')

    listens = triplets_df['listens'].astype(int).to_numpy()
    pickle_dump(listens, 'data/train_listens.pkl')

    return users, songs, listens


def load_song_titles(fname, load=True):
    pickle_fname = get_pickle_fname(fname)
    
    if load and os.path.isfile(pickle_fname):
        return pickle_load(pickle_fname)

    song_titles_df = pd.read_csv(fname, sep='<SEP>', names=['track_id', 'song_id', 'artist', 'song_title'], engine='python')[['song_id', 'song_title']]
    pickle_dump(song_titles_df, pickle_fname)
    return song_titles_df


# construct sparse matrix of users and songs 
def create_listen_matrix(load=True):
    if load and os.path.isfile('data/listen_matrix.pkl'):
        return pickle_load('data/listen_matrix.pkl')

    users, songs, listens = load_triplets('data/train_triplets.txt')

    # find unique users
    users_uniq = np.unique(users)
    # construct {user_id: index} dict for unique users
    users_map = {k: v for v, k in enumerate(users_uniq)}
    # map user_id to user_idx for every triplet user
    users_inds = list(map(lambda x: users_map[x], users))
    
    # find unique songs
    songs_uniq = np.unique(songs)
    # construct {song_id: index} dict for unique songs
    songs_map = {k: v for v, k in enumerate(songs_uniq)}
    # map song_id to song_idx for every triplet song
    songs_inds = list(map(lambda x: songs_map[x], songs))

    mat = sparse.coo_array((listens, (songs_inds, users_inds)), dtype=np.int32)

    pickle_dump(mat, 'listen_matrix.pkl')

    return mat
