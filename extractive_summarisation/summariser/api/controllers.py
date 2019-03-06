from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from extractive_summarisation.summariser.src import summariser

app = Flask(__name__)
api = Api(app)


class Summariser(Resource):
    def get(self):
        return {'about': 'Text Summariser'}

    def post(self):
        data_json = request.get_json(force=True)
        summary = summariser.runitAll(data_json['text'])
        return {'summary': summary}


class HealthCheck(Resource):
    def get(self):
        return {'status': 'Successful'}


api.add_resource(Summariser, '/summary')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True)

