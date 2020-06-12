from flask import Blueprint

# Blueprint loaded by main app to get the routes
bp = Blueprint('management', __name__, template_folder='templates')

# Import routes
from app.management import routes
