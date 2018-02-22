import os
from flask import Flask, Blueprint
from whitenoise import WhiteNoise
from flask_login import LoginManager, UserMixin
import flask_restful
from setuptools import find_packages
import project.restfulapi.route_decorator

app = Flask(__name__)

# Use this app to serve static files.
wnapp = WhiteNoise(app, root='./project/ui/')

blueprints = {}

class User(UserMixin):

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return str(self.id)

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    return User(userid)

def get_config():
    app.config.from_object('config.Config')
    environment = os.environ.get('FLASK_ENV', app.config.get('DEFAULT_ENVIRONMENT'))
    app.config.from_object('config.' + environment)

def get_blueprints(filter_path=''):
    for path in find_packages():
        if filter_path in path:
            blueprints[path] = Blueprint(path, path)
            __import__(path)
            app.register_blueprint(blueprints[path])

get_config()
get_blueprints('project.restfulapi.')
