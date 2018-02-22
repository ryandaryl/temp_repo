import os

# General

class Config(object):
    DEFAULT_ENVIRONMENT = 'Production'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_xxx'
    GOOGLE_URL = 'https://www.googleapis.com/oauth2/v3/'
    GOOGLE_CLIENT_ID = '478298850154-13hei7id3n8et1o722j9rdnrb2r3u3v9.apps.googleusercontent.com'

# Environments

class Development(Config):
    DEBUG = True

class Testing(Config):
    GOOGLE_URL = 'http://0.0.0.0:8001'

class Staging(Config):
    pass

class Production(Config):
    pass
