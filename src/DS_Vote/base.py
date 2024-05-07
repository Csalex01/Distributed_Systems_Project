
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

from DS_Vote.models import *

base = Blueprint("base", __name__)

@base.route("/")
def index():
    """
    Renders the home page of the application.

    Returns:
        The rendered home page HTML template.
    """
    return render_template("index/home.html")
