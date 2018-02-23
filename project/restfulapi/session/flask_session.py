from flask import jsonify, request
import flask_restful
from flask_login import login_required, logout_user, User
from project.restfulapi import blueprints

api = flask_restful.Api(blueprints[__package__], prefix="/session")


@api.route('/')
class SimpleLogout(flask_restful.Resource):

    @login_required
    def delete(self):
        logout_user()
        return jsonify({'status': 'log_out_ok', 'message': 'Log out from backend services was successful.'})


#Do not add a route for this class.
#Subclass it, and override the "validate" method.
class Login(flask_restful.Resource):

    def post(self):
        if not self.validate(request.values):
            response = jsonify({'status': 'log_in_failed'})
            response.status_code = 400
            return response
        # And create new user if ID is not found.
        # It uses id=0 for all users.
        user = User(0)
        login_user(user)
        return jsonify({'status': 'log_in_ok',
                        'message': 'Log in to backend services was successful.'})
    
    def validate(self):
        return False