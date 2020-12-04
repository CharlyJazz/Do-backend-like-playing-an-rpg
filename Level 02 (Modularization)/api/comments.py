from flask import Blueprint


bp = Blueprint("comments", __name__, url_prefix="/comments")


@bp.route("", methods=["POST"])
def comments():
    """
    Endpoint to create comments
    """
    return "create comment!"


@bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def comment():
    """
    Endpoints to manage a single comment
    """
    if request.method == "PUT":
        return "edit comment!"
    elif request.method == "DELETE":
        return "delete comment!"
    else:
        return "comment!"
