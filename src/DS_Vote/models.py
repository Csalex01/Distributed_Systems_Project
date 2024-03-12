from . import db
from flask_login import UserMixin

# Model for Users
class Users(db.Model, UserMixin):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)

    # This is required for getting the ID to log the user in
    def get_id(self):
        return self.UserID

# Model for Votes
class Votes(db.Model):
    VoteID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    WhiteGold = db.Column(db.Boolean, nullable=False, default=False)
    BlueBlack = db.Column(db.Boolean, nullable=False, default=False)
    Other = db.Column(db.String, nullable=False, default="")
