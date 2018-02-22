import os
from flask import Flask, jsonify, request

google_app = Flask(__name__)

@google_app.route("/tokeninfo")
def validate():
    if request.args['id_token'] == 'XYZmyvalidtoken123':
        return jsonify({'aud': '456testgoogleclientid789'})
    else:
        return jsonify({'error_description': 'Invalid Value'})
