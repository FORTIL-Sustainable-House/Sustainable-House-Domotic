from app import db
from sqlalchemy.sql import func

# Model for the room table
class Room(db.Model):
	# Set the table name
	__tablename__ = 'room'

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
	__tablename__ = 'sensor_type'

	# Set table columns.
	id = db.Column(db.Integer, primary_key=True)
	label = db.Column(db.String(100), unique=True, nullable=False)
	sensors = db.relationship('Sensor', backref='sensor_type', lazy=True)

	def __repr__(self):
		return '<Sensor Type {}>'.format(self.label)

# Model for the sensor table
class Sensor(db.Model):
	# Set the table name
	__tablename__ = 'sensor'

	# Set table columns
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	active = db.Column(db.Boolean, server_default="1")
	sensor_type_id = db.Column (db.Integer, db.ForeignKey('sensor_type.id'), nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
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
	sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

	def __repr__(self):
		return '<Temperature data {}>'.format(self.value)

# Model for the association table between tables "sensor" and "feature".
sensorFeature = db.Table(
	'sensor_feature',
	db.Column('sensor_id', db.Integer, db.ForeignKey('sensor.id'), primary_key=True),
	db.Column('feature_id', db.Integer, db.ForeignKey('feature.id'), primary_key=True)
)

# Model for feature table.
class Feature(db.Model):
	# Set the table name.
	__tablename__ = 'feature'

	# Set table columns.
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	enum_type = db.Column(db.Enum('type','other'), nullable=False)

	def __repr__(self):
		return '<Feature {}>'.format(self.name)
