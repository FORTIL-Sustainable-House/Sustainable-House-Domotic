from flask import Blueprint

# Blueprint loaded by main app to get the routes
bp = Blueprint('auth', __name__, template_folder='templates')

# Import routes
from app.auth import routes
