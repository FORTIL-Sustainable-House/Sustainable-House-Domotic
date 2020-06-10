import datetime
import json
import random

from flask import render_template, request
from flask_login import login_required

from app.dummy_feature.models import Sensor, sensorFeature, SensorType, TemperatureData, Feature, Room
from app.features import bp
from app import db


# Temperature feature page
@bp.route('/temperature')
@login_required
def temperature():
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
            temp.append(a.value)
            time.append(a.snapshot_date.strftime(date_format))
    else:
        sensor_number = None

    return render_template('features/temperature.html', title='Temperature', sensors=sensors,
                           sensor=sensor, feature=feature_one, temperature=temp,
                           timestamps=time, sensor_number=sensor_number)
