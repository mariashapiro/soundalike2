from flask_restful import Api, Resource, reqparse
from flask import jsonify, make_response
import pickle
import numpy as np
import pandas as pd
import os

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
    print(args)

    song_title_value = args['song_title']
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight
    status = "Success"

    if not song_title_value:
      status = "Unsuccessful"
    
    rec_songs = get_recommended_songs_from_model(song_title_value)
    return jsonify({"status": status, "rec_songs": rec_songs})
  
  def options(self):
    return build_cors_preflight_response()
  
def build_cors_preflight_response():
  response = make_response()
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add('Access-Control-Allow-Headers', "*")
  response.headers.add('Access-Control-Allow-Methods', "*")
  return response

def get_recommended_songs_from_model(song_title):
  PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'models/data'))
  unique_songs_file = pickle.load(open(PATH + "/unique_tracks.pkl", 'rb'))
  song_id_matches = unique_songs_file[unique_songs_file['song_title'] == song_title]['song_id'].tolist()
  
  rec_songs = []
  song_id = None
  if song_id_matches:
    song_id = song_id_matches
  else:
    print("no song found. please try again")
    return rec_songs

  model = pickle.load(open(PATH + "/lfm_model.pkl", 'rb'))
  rec_songs = model.recommend(song_id)
  print(rec_songs)
  return rec_songs
  

  