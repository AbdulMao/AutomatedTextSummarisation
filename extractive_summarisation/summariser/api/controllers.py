from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api
from extractive_summarisation.summariser.src import summariser
from extractive_summarisation.summariser.validation import language_detect
from extractive_summarisation.summariser.validation import length_detect

app = Flask(__name__)
api = Api(app)
CORS(app)


class Summariser(Resource):
    def get(self):
        return {'about': 'Text Summariser'}

    def post(self):

        data_json = request.get_json(force=True)
        text = data_json['text']

        if language_detect.detect_lang(text) == 'en':
            return {'status': 'Wrong language, English only'}, 400

        elif not length_detect.length(text):
            return {'status': 'Too short to summarise'}, 400

        else:
            summary = summariser.runitAll(text)
            return summary, 200


class HealthCheck(Resource):
    def get(self):
        return {'status': 'Successful'}, 200


api.add_resource(Summariser, '/summary')
api.add_resource(HealthCheck, '/health')

if __name__ == '__main__':
    app.run(debug=True,
            host=app.config.get("HOST", "localhost"),
            port=app.config.get("PORT", 5000)
            )

