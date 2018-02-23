from flask_login import LoginManager
from project import app

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    return User(userid)

from . import flask_session