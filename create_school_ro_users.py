from app import app
from config import Config

# TO get all the relevant credentials for postgresql backend

DB_TYPE = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_USER = Config.POSTGRES_USER
DB_PASS = Config.POSTGRES_PASSWORD
DB_HOST = '172.17.0.1'
DB_PORT = Config.POSTGRES_PORT
DB_NAME = 'clix_dashboard_db'
POOL_SIZE = 50
SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s' % (DB_TYPE, DB_DRIVER, DB_USER,
                                                  DB_PASS, DB_HOST, DB_PORT, DB_NAME)

from sqlalchemy import create_engine, MetaData
#from config.clix_config import SQLALCHEMY_DATABASE_URI, POOL_SIZE

from app.models.user.schema import User
from app import db
import time

Engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=POOL_SIZE, max_overflow=0)
connec = Engine.connect()

# Code to delete rows specific to a state 
#'''
#select * from metric1 where substring(split_part(school_server_code, '-', 2) from 1 for 2) = 'tg';
#'''

def get_all_schools():
    '''
    fetch all unique schools in db
    :return: list of schools
    '''
    all_schools = connec.execute('SELECT DISTINCT school_server_code FROM metric1;').fetchall()
    return [''.join(each[0].split('-')[::-1]) for each in all_schools]

def create_ro_school_admins(school_admins):
    '''
    Takes a list of school admin, which has same username and password.
    And assigns them ro access to clix_dashboard_db tables.
    :param school_admins:
    :return: Success or Error
    '''

    try:
        create_role = """ CREATE ROLE readaccess; 
        GRANT USAGE ON SCHEMA public TO readaccess; 
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO readaccess; 
        ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readaccess;
        """
        check_for_role = connec.execute(""" SELECT 1 FROM pg_roles WHERE rolname='readaccess'
        """).fetchone()


        if (not check_for_role) or (check_for_role[0] != 1):
            connec.execute(create_role)

        for each in school_admins:
            user = each
            assign_users = """ CREATE USER {0} WITH PASSWORD 'clixdata'; 
            GRANT readaccess TO {0}; 
            """.format(user)

            list_users = """SELECT u.usename AS "User Name" FROM pg_catalog.pg_user u;
            """

            users = [each[0] for each in connec.execute(list_users).fetchall()]
            if user not in users:
                connec.execute(assign_users)
                create_school_user(user) 
            else:
                print("School {} already exists in backend DB.".format(user))
    except Exception as e:
        print(e)
        raise(Exception)

def create_school_user(school):
    '''
    To create user roles for schools to access school related visuals
    :param schools:
    :return:
    '''
    #for each in schools:
    passwd = 'clixdata'
    email = 'clixdashboard@tiss.edu'
    adminuser = User(username=school, password=passwd)
    # adminuser.set_password(password=passwd)
    try:
      db.session.add(adminuser)
      db.session.commit()
      print('Added user {0} to db.'.format(school))
    except Exception as e:
      print(e)
      time.sleep(2)
    return None

if __name__ == '__main__':
    create_ro_school_admins(get_all_schools())
    #create_school_users(get_all_schools())

