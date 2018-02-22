import os
from flask import Flask, Blueprint
from whitenoise import WhiteNoise

app = Flask(__name__)

# Use this app to serve static files.
wnapp = WhiteNoise(app, root='./project/ui/')

def load_config():
    app.config.from_object('config.Config')
    environment = os.environ.get('FLASK_ENV', app.config.get('DEFAULT_ENVIRONMENT'))
    app.config.from_object('config.' + environment)

load_config()
import project.restfulapi
