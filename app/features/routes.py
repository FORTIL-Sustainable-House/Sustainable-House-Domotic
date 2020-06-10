import datetime
import json
import random

from flask import render_template, request
from flask_login import login_required

from app.dummy_feature.models import Sensor, sensorFeature, SensorType, TemperatureData, Feature, Room
from app.features import bp
from app import db


# Feature selection page
@bp.route('/feature_select')
@login_required
def feature_selector():
    features = Feature.query.all()
    if len(features) <= 0:
        sensor = Sensor.query.get(1)
        feature = Feature(name='Temperature Pot de fleur', enum_type='temperature')
        feature.sensors.append(sensor)
        db.session.add(feature)
        db.session.commit()
        features = Feature.query.all()
    return render_template('features/feature_select.html', features=features)


# Temperature feature page
@bp.route('/temperature')
@login_required
def temperature():
    feature_one = Feature.query.get(1)
    sensor_number = request.args.get('sensor', default=None, type=int)
    sensor = None
    temp = None
    time = None
    sensors = Sensor.query.all()
    if sensor_number is not None:
        sensor = Sensor.query.get(sensor_number)
    if sensor is not None:
        temperature_plus = TemperatureData.query.filter_by(sensor_id=sensor.id).all()
        temp = []
        time = []
        date_format = '%Y-%m-%d %H:%M:%S'
        for a in temperature_plus:
            # a_temp = {'value': a.value, 'snapshot_date': a.snapshot_date}
            temp.append(a.value)
            time.append(a.snapshot_date.strftime(date_format))
    else:
        sensor_number = None



    # Render the page
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    # [12, 19, 3, 5, 2, 3]['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']'# of Votes'

    #room_one = Room.query.get(1)
    #sensor_one = Sensor.query.get(1)
    #if sensor_one is None:
        #sensor_one_type = SensorType.query.get(1)
        #if sensor_one_type is None:
            #sensor_one_type = SensorType(label="DummyLebal")
            #db.session.add(sensor_one_type)
            #db.session.commit()
        #sensor_one = Sensor(name="SensorToilette", sensor_type_id=sensor_one_type.id, room_id=room_one.id)
        #db.session.add(sensor_one)
        #db.session.commit()
    #temperature_plus = TemperatureData(value=random.randint(42,69), sensor_id=sensor_one.id)
    #db.session.add(temperature_plus)
    #db.session.commit()
    #temperature_plus = json.dumps(list(temperature_plus))
    return render_template('features/temperature.html', title='Temperature', values=values, labels=labels,
                           legend=legend, sensors=sensors, sensor=sensor, feature=feature_one, temperature=temp,
                           timestamps=time, sensor_number=sensor_number)
