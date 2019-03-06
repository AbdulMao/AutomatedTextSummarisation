from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from extractive_summarisation.topic_model.src import topic_recognition

app = Flask(__name__)
api = Api(app)


class TopicModeller(Resource):
    def get(self):
        return {'about': 'Topic Modeller'}

    def post(self):
        data_json = request.get_json(force=True)
        topics = topic_recognition.topic_recognition(data_json['text'])
        return {'topics': topics}


class HealthCheck(Resource):
    def get(self):
        return {'status': 'Successful'}


api.add_resource(TopicModeller, '/topic')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True)

