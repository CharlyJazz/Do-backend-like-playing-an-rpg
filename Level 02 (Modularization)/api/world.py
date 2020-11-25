from flask import Blueprint


bp = Blueprint("world", __name__, url_prefix="/world")


@bp.route("")
def world():
    return "World!"
