from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class SyncStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schoolname = db.Column(db.String(120), unique=False, nullable=True)
    schoolcode = db.Column(db.String(60), unique=False, nullable=True)
    district = db.Column(db.String(60), unique=False, nullable=True)
    lastupdated = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(60), unique=False, nullable=False)
    previous_update_date = db.Column(db.DateTime, nullable=False)
    currentfilesize = db.Column(db.String(60), unique=False, nullable=True)
    previousfilesize = db.Column(db.String(60), unique=False, nullable=True)

    def __repr__(self):
       return '<School {}>'.format(self.schoolcode)
