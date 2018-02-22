from flask import jsonify
import flask_restful
from flask_login import login_required, logout_user
from project.restfulapi import blueprints

api = flask_restful.Api(blueprints[__name__], prefix="/logout")

@api.route('/')
class SimpleLogout(flask_restful.Resource):
    @login_required
    def delete(self):
        logout_user()
        return jsonify({'status': 'log_out_ok', 'message': 'Log out from backend services was successful.'})