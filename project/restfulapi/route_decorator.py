#http://flask.pocoo.org/snippets/129/

import flask_restful

def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

flask_restful.Api.route = api_route