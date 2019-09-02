from datetime import datetime
from app import db

class Metric1(db.Model):
    '''
    This model corresponds to Metric1 of school.
    It is time variation of attendance in terms of unique
    user logins in a day.
    User logins are captured from tools and modules data of the school
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. attendance
    5. state
    6. district
    '''
    __tablename__ = 'metric1'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    attendance_tools = db.Column(db.Integer, unique=False, nullable=True)
    attendance_modules = db.Column(db.Integer, unique=False, nullable=True)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32), unique=False, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric1 of : {}>'.format(self.school_server_code)

class Metric2(db.Model):
    '''
    This model corresponds to Metric2 of a school.
    It is time variation of number of modules (subject wise) attempted
    by all students in a school together on a particular day.
    Number of modules attempted in a day are captured from modules data of the school.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. numofmodules
    5. domain
    6. state
    7. district
    '''
    __tablename__ = 'metric2'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    numofmodules = db.Column(db.Integer, unique=False, nullable=False)
    domain = db.Column(db.String(32), unique=False, nullable=False)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32), unique=False, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric2 of : {}>'.format(self.school_server_code)

class Metric3(db.Model):
    '''
    This model corresponds to Metric3 of a school.
    It is time variation of amount of time spent (in minutes) on tools(tool wise)
    by all students in a school together on a particular day.
    Time spent on different tools in a day is from tools data of the school.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. time_spent
    5. tool
    6. state
    '''
    __tablename__ = 'metric3'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    time_spent = db.Column(db.Integer, unique=False, nullable=False)
    tool = db.Column(db.String(64), unique=False, nullable=False)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32),unique=False, nullable=False )
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric3 of : {}>'.format(self.school_server_code)
