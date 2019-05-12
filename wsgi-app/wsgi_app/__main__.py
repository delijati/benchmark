import wsgi_app.app


def main():
    app = wsgi_app.app.create_app()
    app.run()
