from flask_restful import Api, Resource, reqparse
from flask import jsonify, make_response
import time
import pickle
import numpy as np
import pandas as pd
import os
from scipy.sparse import csr_matrix
import json

class SearchSongHandler(Resource):
  def get(self):
    data = {
      'resultStatus': 'SUCCESS',
      'message': "Search Song Handler"
      }
    print('here')
    return jsonify(data)

  def post(self):
    SONG_TITLE_KEY = 'song_title'
    parser = reqparse.RequestParser()
    parser.add_argument(SONG_TITLE_KEY, type=str)
    args = parser.parse_args()

    song_input = args['song_title']
    status = "Success"

    if not song_input:
      status = "Unsuccessful"
    
    rec_start = time.time()
    rec_songs, rec_song_metrics = get_recommended_songs(song_input)
    rec_end = time.time()
    print('time to recommend: {rec_time} s'.format(rec_time=(rec_end - rec_start)))
    return jsonify({"status": status, "rec_songs": rec_songs, "rec_song_metrics": rec_song_metrics})
  
  def options(self):
    return build_cors_preflight_response()
  
def build_cors_preflight_response():
  response = make_response()
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add('Access-Control-Allow-Headers', "*")
  response.headers.add('Access-Control-Allow-Methods', "*")
  return response

def get_recommended_songs(song_title):
  PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'models/data'))
  unique_songs = pickle.load(open(PATH + "/unique_tracks.pkl", 'rb'))
  matches = unique_songs[unique_songs['song_title'] == song_title]['song_id'].tolist()
  
  rec_song_ids = []
  song_id = None
  if matches:
    song_id = matches[0]
  else:
    print("no song found. please try again")
    return rec_song_ids

  model = pickle.load(open(PATH + "/als_model.pkl", 'rb'))
  song_map = pickle.load(open(PATH + "/song_map.pkl", 'rb'))
  train_songs = pickle.load(open(PATH + "/train_songs.pkl", 'rb'))

  print("song id: ", song_id)
  rec_song_inds, rec_song_metrics = model.similar_items(song_map[song_id], N=6)

  rec_titles = []
  for rec_idx in rec_song_inds:
    song_id = train_songs[rec_idx]
    song_title = unique_songs[unique_songs['song_id'] == song_id]['song_title'].iloc[0]
    rec_titles.append(song_title)

  print('rec_songs: ', rec_titles)
  return rec_titles, rec_song_metrics.tolist()
