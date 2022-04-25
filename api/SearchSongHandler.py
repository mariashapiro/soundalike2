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
    
    get_recommended_songs_from_model(song_title_value)
    return jsonify({"status": status, "song_title": song_title_value})
  
  def options(self):
    return build_cors_preflight_response()
  
def build_cors_preflight_response():
  response = make_response()
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add('Access-Control-Allow-Headers', "*")
  response.headers.add('Access-Control-Allow-Methods', "*")
  return response

def get_recommended_songs_from_model(song_title):
  pathh = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'models/data/unique_tracks.pkl'))
  unique_songs_file = pickle.load(open(pathh, 'rb'))
  # song_titles_df = pd.read_csv(
  #   fname, sep='<SEP>',
  #   names=['track_id', 'song_id', 'artist', 'song_title'],
  #   engine='python'
  #   )[['song_id', 'song_title']]
  # song_match = song_titles_df[song_titles_df['song_title'] == song_title]['song_id'].tolist()[0]
  # print('song_match', song_match)

  