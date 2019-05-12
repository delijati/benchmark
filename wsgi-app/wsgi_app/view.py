from flask import Blueprint

view = Blueprint("view", __name__, url_prefix="")


@view.route("/")
def root_view():
    return "[WSGI] Dobro dosli!"
