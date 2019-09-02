from .schema import SyncStatus

class Service(object):
 def __init__(self, username):
   self.username = username

   if not username:
     raise Exception("username not provided")

 def find_user(self):
   pass

 def get_numlogins(self):
     pass

 def get_lastlogin(self):
     pass
