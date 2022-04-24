from flask_restful import Api, Resource, reqparse
from flask import jsonify, make_response

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
    
    return jsonify({"status": status, "song_title": song_title_value})
  
  def options(self):
    return build_cors_preflight_response()
  
def build_cors_preflight_response():
  response = make_response()
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add('Access-Control-Allow-Headers', "*")
  response.headers.add('Access-Control-Allow-Methods', "*")
  return response