from flask import Flask, send_from_directory
from api.SearchSongHandler import SearchSongHandler
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
cors = CORS(app) #comment this on deployment
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


@app.route("/", defaults={'path':''})
@cross_origin()
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(SearchSongHandler, '/flask/search')