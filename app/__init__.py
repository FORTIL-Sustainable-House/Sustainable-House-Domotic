import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
login = LoginManager()
login.init_app(app)
login.login_view = 'auth.login'


from app.models import *


# Import authentication module
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')


# Import authentication module
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)


# Import authentication module
from app.features import bp as features_bp
app.register_blueprint(features_bp, url_prefix='/features')


# Import authentication module
from app.management import bp as management_bp
app.register_blueprint(management_bp, url_prefix='/management')