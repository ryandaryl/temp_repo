import flask_restful
from project.restfulapi import blueprints

api = flask_restful.Api(blueprints[__name__], prefix="/blueprint")

@api.route('/helloworld')
class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}
