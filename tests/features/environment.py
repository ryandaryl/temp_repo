import os
import coveralls
from yaml import load

def before_all(context):
    context.settings = load(open('features/conf.yaml').read())
    port = os.environ.get('PORT') or context.settings['port']
    context.base_url = '{}:{}'.format(context.settings['host'], port)
    context.headers = {}
    context.verify_ssl = True
