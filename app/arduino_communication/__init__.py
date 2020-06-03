from flask import Blueprint

# Blueprint loaded by main app to get the routes
bp = Blueprint('arduino_communication', __name__, template_folder='templates')

# Import routes
from app.arduino_communication import listener
from app.arduino_communication import temperature_listener

