from flask import Flask


def create_app(test_config=None):
    # create the app
    app = Flask(__name__)

    from . import hello

    app.register_blueprint(hello.bp)

    from . import world

    app.register_blueprint(world.bp)

    return app
