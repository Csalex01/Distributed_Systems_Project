from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

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

class EnrolledStudents(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Vote = db.Column(db.Boolean, default=False) # The idea is that if the vote is White/Gold then the Vote is True and for Blue/Black False