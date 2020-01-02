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
    school_name = db.Column(db.String(64), unique=False, nullable=True)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric1 of : {}>'.format(self.school_server_code)

class Metric2(db.Model):
    '''
    This model corresponds to Metric2 of a school.
    It is time variation of number of modules attempted (by domain)
    by all students in a school together on a particular day.
    Number of modules attempted in a day are captured from modules data of the school.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. e_num_modules
    5. m_num_modules
    6. s_num_modules
    7. state
    8. district
    9. school_name
    '''
    __tablename__ = 'metric2'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    e_num_modules = db.Column(db.Integer, unique=False, nullable=True)
    m_num_modules = db.Column(db.Integer, unique=False, nullable=True)
    s_num_modules = db.Column(db.Integer, unique=False, nullable=True)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32), unique=False, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric2 of : {}>'.format(self.school_server_code)

class Metric3(db.Model):
    '''
    This model corresponds to Metric3 of a school.
    It is time variation of number of tools attempted (by domain)
    by all students in a school together on a particular day.
    Number of modules attempted in a day are captured from modules data of the school.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. e_num_tools
    5. m_num_tools
    6. s_num_tools
    7. state
    8. district
    9. school_name
    '''
    __tablename__ = 'metric3'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    e_num_tools = db.Column(db.Integer, unique=False, nullable=True)
    m_num_tools = db.Column(db.Integer, unique=False, nullable=True)
    s_num_tools = db.Column(db.Integer, unique=False, nullable=True)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32), unique=False, nullable=False)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric3 of : {}>'.format(self.school_server_code)


class Metric4(db.Model):
    '''
    This model corresponds to Metric4 of a school.
    It is the distribution of days server was idle to
    the days with some activity.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. days_server_idle
    5. days_server_tools
    6. days_server_modules
    7. days_server_tools_modules
    6. state
    7. district
    '''
    __tablename__ = 'metric4'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    days_server_idle = db.Column(db.Integer, unique=False, nullable=True)
    days_server_tools = db.Column(db.Integer, unique=False, nullable=True)
    days_server_modules = db.Column(db.Integer, unique=False, nullable=True)
    days_server_tools_modules = db.Column(db.Integer, unique=False, nullable=True)
    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32),unique=False, nullable=False )
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric4 of : {}>'.format(self.school_server_code)


class Metric5(db.Model):
    '''
    This model corresponds to Metric5 of a school.
    It gives the number of students engaged with different tools in a day.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. <All tool names>
    6. state
    7. district
    '''
    __tablename__ = 'metric5'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)

    tool_ice = db.Column(db.Integer, unique=False, nullable=True)
    tool_factorisation = db.Column(db.Integer, unique=False, nullable=True)
    tool_coins_puzzle = db.Column(db.Integer, unique=False, nullable=True)
    tool_rationpatterns = db.Column(db.Integer, unique=False, nullable=True)
    tool_food_sharing_tool = db.Column(db.Integer, unique=False, nullable=True)
    tool_ages_puzzle = db.Column(db.Integer, unique=False, nullable=True)
    tool_policesquad = db.Column(db.Integer, unique=False, nullable=True)
    tool_astroamer_element_hunt_activity = db.Column(db.Integer, unique=False, nullable=True)
    tool_astroamer_moon_track = db.Column(db.Integer, unique=False, nullable=True)
    tool_astroamer_planet_trek_activity = db.Column(db.Integer, unique=False, nullable=True)

    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32),unique=False, nullable=False )
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric5 of : {}>'.format(self.school_server_code)

class Metric6(db.Model):
    '''
    This model corresponds to Metric5 of a school.
    It gives the number of students engaged with different modules in a day.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. date
    4. <All tool names>
    6. state
    7. district
    '''
    __tablename__ = 'metric6'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)

    module_English_Beginner = db.Column(db.Integer, unique=False, nullable=True)
    module_English_Elementary = db.Column(db.Integer, unique=False, nullable=True)
    module_i2C = db.Column(db.Integer, unique=False, nullable=True)
    module_Geometric_Reasoning_Part_I = db.Column(db.Integer, unique=False, nullable=True)
    module_Geometric_Reasoning_Part_II = db.Column(db.Integer, unique=False, nullable=True)
    module_Linear_Equations = db.Column(db.Integer, unique=False, nullable=True)
    module_Proportional_Reasoning = db.Column(db.Integer, unique=False, nullable=True)
    module_Atomic_Structure = db.Column(db.Integer, unique=False, nullable=True)
    module_Sound = db.Column(db.Integer, unique=False, nullable=True)
    module_Understanding_Motion = db.Column(db.Integer, unique=False, nullable=True)
    module_Basic_Astronomy = db.Column(db.Integer, unique=False, nullable=True)
    module_Health_and_Disease = db.Column(db.Integer, unique=False, nullable=True)
    module_Ecosystem = db.Column(db.Integer, unique=False, nullable=True)
    module_Reflecting_on_Values = db.Column(db.Integer, unique=False, nullable=True)
    module_Post_CLIx_Survey = db.Column(db.Integer, unique=False, nullable=True)
    module_Pre_CLIx_Survey = db.Column(db.Integer, unique=False, nullable=True)


    state = db.Column(db.String(32), unique=False, nullable=False)
    district = db.Column(db.String(32),unique=False, nullable=False )
    #posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Metric6 of : {}>'.format(self.school_server_code)

class SchoolInfo(db.Model):
    '''
    This model corresponds to Metric5 of a school.
    It gives the number of students engaged with different modules in a day.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. schoolDescription
    5. dateUpdated
    '''
    __tablename__ = 'schoolinfo'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    dateUpdated = db.Column(db.DateTime, unique=False, nullable=True)
    schoolDescription = db.Column(db.Text, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<SchoolInfo of : {}>'.format(self.school_server_code)


class SchoolImage(db.Model):
    '''
    This model corresponds to Metric5 of a school.
    It gives the number of students engaged with different modules in a day.
    following are the attributes of this table:
    1. id
    2. school_server_code
    3. schoolImageName
    5. dateUpdated
    '''

    __tablename__ = 'schoolimage'
    id = db.Column(db.Integer, primary_key=True)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    dateUpdated = db.Column(db.DateTime, unique=False, nullable=True)
    schoolImageName = db.Column(db.Text, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<SchoolImage of : {}>'.format(self.school_server_code)



