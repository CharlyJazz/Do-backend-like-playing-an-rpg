from flask import Blueprint


bp = Blueprint("articles", __name__, url_prefix="/articles")


@bp.route("")
def articles():
    return "articles!"
