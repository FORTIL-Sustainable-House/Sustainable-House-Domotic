from flask_login import UserMixin

from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login


# Model for the user table
class User(UserMixin, db.Model):
    # Set the table name
    __tablename__ = 'users'

    # Set tables columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    # Function used to print the model
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Set the password in the database
    def set_password(self, password):
        # Password is hashed and saved as a non-reversible hash value
        # Actual password is only known while handling account creation and connection request
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if a given password corresponds to the the non-reversible hash-value
        # Actual password is only known while handling account creation and connection request
        return check_password_hash(self.password_hash, password)


# Get a user from ID
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Model for the room table
class Room(db.Model):
	# Set the table name
	__tablename__ = 'rooms'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True)
	area = db.Column(db.Float, nullable=True)
	sensors = db.relationship('Sensor', backref='room', lazy=True)

	def __repr__(self):
		return '<Room {}>'.format(self.name)


# Model for the sensor type table
class SensorType(db.Model):
	# Set the table name.
	__tablename__ = 'sensor_types'

	# Set table columns.
	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(100), unique=True, nullable=False)
	sensors = db.relationship('Sensor', backref='sensor_type', lazy=True)

	def __repr__(self):
		return '<Sensor Type {}>'.format(self.label)


# Model for the sensor table
class Sensor(db.Model):
	# Set the table name
	__tablename__ = 'sensors'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	active = db.Column(db.Boolean, server_default="1")
	sensor_type_id = db.Column (db.Integer, db.ForeignKey('sensor_types.id'), nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
	temperature_datas = db.relationship('TemperatureData', backref='sensor', lazy=True)

	def __repr__(self):
		return '<Sensor {}>'.format(self.name)


# Model for the temperature's data table
class TemperatureData(db.Model):
	# Set the table name
	__tablename__ = 'temperature_data'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Float, nullable=False)
	snapshot_date = db.Column(db.DateTime, server_default=func.now())
	sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.id'), nullable=False)

	def __repr__(self):
		return '<Temperature data {}>'.format(self.value)


# Model for feature table.
class Feature(db.Model):
	# Set the table name.
	__tablename__ = 'features'

	# Set table columns.
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	enum_type = db.Column(db.Enum('temperature', 'type', 'other', name='feature_types'), nullable=False)

	def __repr__(self):
		return '<Feature {}>'.format(self.name)


# Model for the association table between tables "sensor" and "feature".
sensorFeature = db.Table(
	'sensor_features',
	db.Column('sensor_id', db.Integer, db.ForeignKey('sensors.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('features.id'), primary_key=True)
)