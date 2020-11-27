from flask import Blueprint


bp = Blueprint("comments", __name__, url_prefix="/comments")


@bp.route("")
def comments():
    return "comments!"
