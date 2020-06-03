from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.arduino_communication import bp, temperature_listener
from app.arduino_communication.temperature_listener import arduino_com
from app.dummy_feature.models import TemperatureData, Sensor, SensorType, Room

# Main page.
@bp.route('/temperature_listener')
@login_required
def temperature_listener():
    room_one = Room.query.get(1)
    if room_one is None:
        room_one = Room(name="chambre", area=42)
        db.session.add(room_one)
        db.session.commit()
        
    sensor_one = Sensor.query.get(1)
    if sensor_one is None:
        sensor_one_type = SensorType.query.get(1)
        if sensor_one_type is None:
            sensor_one_type = SensorType(label="Temperature")
            db.session.add(sensor_one_type)
            db.session.commit()
        sensor_one = Sensor(name="TemperatureSensor", sensor_type_id=sensor_one_type.id, room_id=room_one.id)
        db.session.add(sensor_one)
        db.session.commit()
    
    duration = 15;
    temp_value = arduino_com(duration, sensor_one.id)
    
    # Render the page
    return render_template('arduino_communication/temperature_listener.html', title='Temperature Listener', sensor=sensor_one, values=temp_value, time=duration)

