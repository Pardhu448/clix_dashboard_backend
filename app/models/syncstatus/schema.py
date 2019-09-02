from app import db

class SyncStatus(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(128), unique=False, nullable=False)
    school_server_code = db.Column(db.String(64), index=True, unique=False, nullable=False)
    district = db.Column(db.String(32), unique=False, nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(32), unique=False, nullable=False)
    filesize_update_date = db.Column(db.String(64), nullable=False)

    def __repr__(self):
       return '<SchoolSyncStatus of: {}>'.format(self.school_server_code)