from app import db
from app.features import bp
from flask import render_template
from flask_login import login_required
from app.dummy_feature.models import Sensor, SensorType, TemperatureData, Feature, Room
import random
import json
import datetime


# Dummy example page
@bp.route('/temperature')
@login_required
def temperature():
    # Do stuff maybe...

    # Render the page
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    # [12, 19, 3, 5, 2, 3]['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']'# of Votes'

    room_one = Room.query.get(1)
    sensor_one = Sensor.query.get(1)
    if sensor_one is None:
        sensor_one_type = SensorType.query.get(1)
        if sensor_one_type is None:
            sensor_one_type = SensorType(label="DummyLebal")
            db.session.add(sensor_one_type)
            db.session.commit()
        sensor_one = Sensor(name="SensorToilette", sensor_type_id=sensor_one_type.id, room_id=room_one.id)
        db.session.add(sensor_one)
        db.session.commit()
    feature_one = Feature.query.get(1)
    #temperature_plus = TemperatureData(value=random.randint(42,69), sensor_id=sensor_one.id)
    #db.session.add(temperature_plus)
    #db.session.commit()
    temperature_plus = TemperatureData.query.filter_by(sensor_id=sensor_one.id).all()
    temp = []
    time = []
    for a in temperature_plus:
        #a_temp = {'value': a.value, 'snapshot_date': a.snapshot_date}
        temp.append(a.value)
        time.append(a.snapshot_date.strftime("%Y-%m-%dT%H:%M:%S"))
    #temperature_plus = json.dumps(list(temperature_plus))
    return render_template('features/temperature.html', title='Temperature', values=values, labels=labels,
                           legend=legend, data=0, sensor=sensor_one, feature=feature_one, temperature=temp, timestamps=time)
