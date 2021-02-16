from flask import Blueprint, request


bp = Blueprint("articles", __name__, url_prefix="/articles")


@bp.route("", methods=["GET", "POST"])
def articles():
    """
    Endpoints to create and retrieve articles
    """
    if request.method == "POST":
        return "create article!"
    else:
        return "articles!"


@bp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def article():
    """
    Endpoints to manage a single article
    """
    if request.method == "PUT":
        return "edit article!"
    elif request.method == "DELETE":
        return "delete article!"
    else:
        return "article!"


@bp.route("/<int:id>/claps", methods=["POST"])
def clap():
    """
    Endpoint to clap an article
    """
    return "clap!"
