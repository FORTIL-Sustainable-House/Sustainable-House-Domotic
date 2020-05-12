from flask import Blueprint

# Blueprint loaded by main app to get the routes
bp = Blueprint('errors', __name__, template_folder='templates')

# Import routes
from app.errors import handlers
