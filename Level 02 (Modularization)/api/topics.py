from flask import Blueprint, request


bp = Blueprint("topics", __name__, url_prefix="/topics")


@bp.route("")
def topics():
    """
    Endpoint to get topics
    """
    return "topics!"
