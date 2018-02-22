import os, sys
from gunicorn.app.base import BaseApplication
from importlib import import_module

#https://programtalk.com/python-examples/gunicorn.app.base.BaseApplication/
def run_server(app, host, port):
    import gunicorn.app.base
 
    class FlaskGUnicornApp(gunicorn.app.base.BaseApplication):
        options = {
            'bind': '{}:{}'.format(host, port),
            'workers': 1
        }
 
        def load_config(self):
            for k, v in self.options.items():
                self.cfg.set(k.lower(), v)
 
        def load(self):
            return app
 
    FlaskGUnicornApp().run()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0',
                    help='Run the server on this host address.')
    parser.add_argument('--port', default=8000,
                    help='Run the server on this port.', type=int)
    parser.add_argument('--package',
                    help='A path to a Python package or module (myproject.mypackage).')
    parser.add_argument('--app', default='app',
                    help='A WSGI callable defined in the module (such as app = Flask(__name__)).')
    args = parser.parse_args()
    app = getattr(
        import_module(args.package),
        args.app)
    run_server(app, args.host, args.port)
