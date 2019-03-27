from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api
from extractive_summarisation.summariser.src import summariser
from extractive_summarisation.summariser.validation import language_detect

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
            summary = summariser.runitAll(text)
            # return {'summary': summary}, 200
            return summary, 200
        else:
            return {'status': 'Wrong language, English only'}, 400


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

