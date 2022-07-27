from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/")

@bp.route('/index')
def index():
    return "Hello, World!"
