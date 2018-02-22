# General

class Config(object):
    DEFAULT_ENVIRONMENT = 'Production'
    GOOGLE_URL = 'https://www.googleapis.com/oauth2/v3/'

# Environments

class Development(Config):
    DEBUG = True

class Testing(Config):
    GOOGLE_URL = 'http://0.0.0.0:8001'

class Staging(Config):
    pass

class Production(Config):
    pass
