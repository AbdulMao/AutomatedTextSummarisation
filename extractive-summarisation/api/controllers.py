from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Summariser(Resource):
    def get(self):
        return {'about': 'Hello World2'}

    def post(self):
        data_json = request.get_json(force=True)
        return {'you sent': data_json}


api.add_resource(Summariser, '/')

if __name__ == '__main__':
    app.run(debug=True)
