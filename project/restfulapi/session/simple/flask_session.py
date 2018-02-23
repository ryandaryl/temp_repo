from flask import jsonify, request
import flask_restful
from flask_login import login_required, login_user, logout_user
from project.restfulapi import blueprints
from project.restfulapi.session import User

api = flask_restful.Api(blueprints[__package__], prefix="/session")

@api.route('/')
class Logout(flask_restful.Resource):

    @login_required
    def delete(self):
        logout_user()
        return jsonify({'status': 'logout_ok',
                       'message': 'Log out from backend services was successful.'})


class Login(flask_restful.Resource):

    def post(self):
        values_ok, message = self.check_values(request.values)
        if not values_ok:
            response = jsonify({'message': message, 'status': 'login_failed'})
            response.status_code = 400
            return response
        if self.validate(request.values):
            user = User(0)
            login_user(user)
            return jsonify({'status': 'login_ok',
                            'message': 'Log in to backend services was successful.'})
        else:
            response = jsonify({'status': 'login_failed'})
            response.status_code = 400
            return response
    
    def validate(self):
        return False

    def check_values(self, request_values):
        return True, ''
 


# Do not add a route for the "Login" class.
# Subclass it, and override the "validate" method.

# "User(0)" should use a unique id.
# It should get database user id from self.[properties]
# And create new user if ID is not found.
# Currently, it uses id=0 for all users.
