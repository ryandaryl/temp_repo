import os
import requests
from flask import jsonify, request
import flask_restful
from flask_login import login_user
from project import blueprints, app, User

api = flask_restful.Api(blueprints[__name__], prefix="/oauth/google")

@api.route('/login')
class OAuth_Google_login(flask_restful.Resource):
    def post(self):
        if 'id_token' in request.values:
            id_token = request.values.get('id_token')
        else:
            response = jsonify({ 'error_description':
                            'You need to add an id_token as a parameter. ' \
                            'For example, ?id_token=XYZ123' })
            response.status_code = 400
            return response
        google_url = app.config.get('GOOGLE_URL')
        path = 'tokeninfo'
        url = '/'.join(s.strip('/') for s in [google_url, path])
        params = { 'id_token': id_token }
        r = requests.get(url=url, params=params).json()
        if 'error_description' in r:
            # Token not valid
            response = jsonify(r)
            response.status_code = 400
            return response
        elif r['aud'] == app.config.get('GOOGLE_CLIENT_ID'):
            google_user_id = r['sub']
            # It should look up the user's database ID using the Google ID.
            # It uses id=0 for all users.
            user = User(0)
            login_user(user)
            return jsonify({'status': 'log_in_ok',
                            'message': 'Log in to backend services was successful.'})

