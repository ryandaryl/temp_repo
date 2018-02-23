import requests
from flask import jsonify
import flask_restful
from project import app
from project.restfulapi import blueprints
from project.restfulapi.session.simple.flask_session import Login

api = flask_restful.Api(blueprints[__name__], prefix="/session/oauth/google")

@api.route('/login')
class OAuth_Google_Login(Login):

    def check_values(self, request_values):
        if 'id_token' in request_values:
            return True, ''
        else:
            message = 'You need to add an id_token as a parameter. For example, ?id_token=XYZ123'
            return False, message
            

    def validate(self, request_values):
        id_token = request_values.get('id_token')
        google_url = app.config.get('GOOGLE_URL')
        path = 'tokeninfo'
        url = '/'.join(s.strip('/') for s in [google_url, path])
        params = { 'id_token': id_token }
        r = requests.get(url=url, params=params).json()
        if 'error_description' in r:
            # Token not valid
            return False
        elif r['aud'] == app.config.get('GOOGLE_CLIENT_ID'):
            self.google_client_id = r['sub']
            return True