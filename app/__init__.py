from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Setup Database and login view
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'


# Create app Function. Initiate all routes and configs
def create_app(config_class=Config):
    # Create empty flask app and link with config
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Link database and login to the app
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Import errors module
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Import authentication module
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Import Dummy_Feature module
    from app.dummy_feature import bp as dummy_bp
    app.register_blueprint(dummy_bp, url_prefix='/dummy_feature')

    # Push application context and return
    app.app_context().push()
    return app
