from flask import Blueprint


bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/<username>", methods=["GET", "PUT"])
def user():
    """
    Endpoints to manage single users
    """
    if request.method == "PUT":
        return "edit user!"
    else:
        return "user!"
