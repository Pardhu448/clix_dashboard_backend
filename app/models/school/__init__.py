from .schema import Metric1, Metric2, Metric3
# All the service requests related to school and state level metrics are provided from
# here.

class Service(object):
 def __init__(self, user_id):
   self.school_server_code = user_id

   if not school_server_code:
     raise Exception("user-id not provided")

 def find_user(self):
   pass

 def get_numlogins(self):
     pass

 def get_lastlogin(self):
     pass
