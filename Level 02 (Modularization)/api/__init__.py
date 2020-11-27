from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from . import articles

    app.register_blueprint(articles.bp)

    from . import users

    app.register_blueprint(users.bp)

    from . import topics

    app.register_blueprint(topics.bp)

    from . import auth

    app.register_blueprint(auth.bp)

    from . import comments

    app.register_blueprint(comments.bp)

    return app
