from flask import Flask, request
from flask_restful import Resource, Api
from extractive_summarisation.topic_model.src import topic_recognition
from extractive_summarisation.topic_model.validation import language_detect

app = Flask(__name__)
api = Api(app)


class TopicModeller(Resource):
    def get(self):
        return {'about': 'Topic Modeller'}

    def post(self):
        data_json = request.get_json(force=True)
        text = data_json['text']
        if language_detect.detect_lang(text) == 'en':
            topics = topic_recognition.topic_recognition(text)
            return {'topics': topics}, 200
        else:
            return {'status': 'Wrong language, English only'}, 400


class HealthCheck(Resource):
    def get(self):
        return {'status': 'Successful'}


api.add_resource(TopicModeller, '/topic')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True,
            host=app.config.get("HOST", "localhost"),
            port=app.config.get("PORT", 9000)
            )
