from quart import Quart
from asgi_app.view import view


def create_app(debug=False):
    app = Quart(__name__)
    app.register_blueprint(view)
    app.debug = debug
    return app
