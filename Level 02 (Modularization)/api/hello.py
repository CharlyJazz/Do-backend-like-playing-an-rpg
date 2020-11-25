from flask import Blueprint


bp = Blueprint("hello", __name__, url_prefix="/hello")


@bp.route("")
def hello():
    return "Hello!"
