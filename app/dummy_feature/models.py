from app import db
from sqlalchemy.sql import func

# Model for the environment table
class Environment(db.Model):
	# Set the table name
	__tablename__ = 'environment'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(50), unique=True)
	rooms = db.relationship('Room', backref='environment', lazy=True)

	def __repr__(self):
		return '<Environment {}>'.format(self.label)

# Model for the room table
class Room(db.Model):
	# Set the table name
	__tablename__ = 'room'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True)
	area = db.Column(db.Float, nullable=True)
	environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'), nullable=False)
	temperature_datas = db.relationship('TemperatureData', backref='room', lazy=True)

	def __repr__(self):
		return '<Room {}>'.format(self.name)

# Model for the sensor table
class Sensor(db.Model):
	# Set the table name
	__tablename__ = 'sensor'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	active = db.Column(db.Boolean, server_default="1")
	temperature_datas = db.relationship('TemperatureData', backref='sensor', lazy=True)

	def __repr__(self):
		return '<Sensor {}>'.format(self.name)

# Model for the association table between tables "sensor" and "room".
sensorRoom = db.Table(
	'sensor_room',
	db.Column('sensor_id', db.Integer, db.ForeignKey('sensor.id'), primary_key=True),
	db.Column('room_id', db.Integer, db.ForeignKey('room.id'), primary_key=True)
)

# Model for the temperature's data table
class TemperatureData(db.Model):
	# Set the table name
	__tablename__ = 'temperature_data'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Float, nullable=False)
	snapshot_date = db.Column(db.DateTime, server_default=func.now())
	sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)