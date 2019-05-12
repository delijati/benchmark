from quart import Blueprint

view = Blueprint("view", __name__, url_prefix="")


@view.route("/")
async def root_view():
    return "[ASGI] Dobro dosli!"
