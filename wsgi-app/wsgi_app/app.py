from flask import Flask
from wsgi_app.view import view


def create_app(debug=False):
    app = Flask(__name__)
    app.register_blueprint(view)
    app.debug = debug
    return app
