from flask import Blueprint

# Blueprint loaded by main app to get the routes
bp = Blueprint('dummy_feature', __name__, template_folder='templates')

# Import routes
from app.dummy_feature import routes
