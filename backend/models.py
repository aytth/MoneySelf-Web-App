from . import db 
from flask_login import UserMixin # flaskLogin helps in logging in the user
from sqlalchemy.sql import func

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     # func takes the current time and adds it as the default
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     # Default name of databases in sql is lowercase so dont need to specify that it is User
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(1500))
    # When getting relationship we reference the name of the class and not the sql database hence upercase
    # notes = db.relationship('Note')
