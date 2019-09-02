from .schema import User
from app import db

class Service(object):

 def __init__(self, user_id):
   self.dbconn = db
   self.user_id = user_id

 def add_user_log(self, timestamp):
     user = User.query.filter_by(id=self.user_id).first()
     user.lastlogin = timestamp
     user.numlogins = user.numlogins + 1
     #self.dbconn.session.flush()
     self.dbconn.session.commit()

 def get_numlogins(self):
     pass

 def get_lastlogin(self):
     pass


