from flask import jsonify
import flask_restful
from flask_login import login_required
from project import blueprints

api = flask_restful.Api(blueprints[__name__], prefix="/content")

@api.route('/')
class MyContent(flask_restful.Resource):
    @login_required
    def get(self):
        return jsonify({'message': 'You are viewing protected content.'})