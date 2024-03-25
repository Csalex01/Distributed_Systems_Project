from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path

# Initialize app with the current package name
app = Flask(__name__)

# Create database

db = SQLAlchemy()
DB_NAME = "votes.db"

# Secret key for encryption
app.config["SECRET_KEY"] = "985230d0ce098c081e5b5b70f9797064"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Register blueprints

from DS_Vote.base import base
from DS_Vote.auth import auth

app.register_blueprint(base, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")

# Initialize database

from .models import *

db.init_app(app)

if not path.exists(f"instance/{DB_NAME}"):
    with app.app_context():
        db.create_all()

    print("Database created")

# Initialize login manager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))