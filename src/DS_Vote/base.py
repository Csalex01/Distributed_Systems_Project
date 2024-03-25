
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

from DS_Vote.models import *

base = Blueprint("base", __name__)

@base.route("/")
def index():
    return render_template("index/home.html")

@base.route("/vote")
def vote():
    return render_template("index/vote.html")