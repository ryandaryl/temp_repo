import os
import requests
from flask import jsonify, request
import flask_restful
from project import blueprints, app

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
        params = { 'id_token': id_token }
        url = '/'.join([google_url, path])
        r = requests.get(url=url, params=params).json()
        if 'error_description' in r:
            # Token not valid
            response = jsonify(r)
            response.status_code = 400
            return response
        else:
            return jsonify({'status': 'logged_in'})

