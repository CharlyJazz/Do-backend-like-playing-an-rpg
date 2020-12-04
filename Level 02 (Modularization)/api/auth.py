from flask import Blueprint


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST"])
def login():
    """
    Endpoint to manage users' login
    """
    return "login!"


@bp.route("/register", methods=["POST"])
def register():
    """
    Endpoint to manage users' registration
    """
    return "register!"
