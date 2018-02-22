from flask import jsonify
import flask_restful
from flask_login import LoginManager, UserMixin, \
                        login_required, login_user, logout_user
from project import blueprints, User

api = flask_restful.Api(blueprints[__name__], prefix="/simple")

@api.route('/login')
class SimpleLogin(flask_restful.Resource):
    def get(self):
        login_user(User(0))
        return jsonify({'message': 'Logged in to Flask.'})

@api.route('/logout')
class SimpleLogout(flask_restful.Resource):
    @login_required
    def get(self):
        logout_user()
        return jsonify({'message': 'Logged out of Flask.'})

@api.route('/')
class MyContent(flask_restful.Resource):
    @login_required
    def get(self):
        return jsonify({'message': 'You are viewing protected content.'})