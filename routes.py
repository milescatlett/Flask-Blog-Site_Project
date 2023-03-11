from flask import Blueprint

site = Blueprint('site', __name__)


@site.route("/")
def index():
    return "this is the home page"
