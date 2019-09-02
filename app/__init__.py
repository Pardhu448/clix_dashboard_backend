from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_bcrypt import Bcrypt

#from celery import Celery
#import celeryconfig

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config.from_object(Config)

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)

#app.config['CELERY_BROKER_URL'] = 'redis://localhost:6390/0'
#app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6390/0'

#celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)
#celery.config_from_object(celeryconfig)

from app import routes, models, endpoints
