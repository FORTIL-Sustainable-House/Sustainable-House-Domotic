import serial
import datetime

from app import db
from app.dummy_feature.models import TemperatureData, Sensor

ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0]

def arduino_com(loop_time, sensor_id):
        
    if loop_time <=0 or loop_time > 30:   # security: loop_time cannot be negative and longer than 30 seconds
        print("usage: between 0-30")
        return 0
    loop_time = datetime.timedelta(seconds=loop_time)   # convert loop_time from int to timedelta to be able to compare it with datetime
    
    timestart = datetime.datetime.now()                 # get current date time
    TemperatureData(value=0, snapshot_date=timestart)   # create a TemperatureData object with value 0 and the current date and time
    
    total_value = 0    # value that count the number of values send by the arduino during the looptime requested
    
    while True:
        read_serial = ser.readline().decode('ascii')[:-2]    #reading the serial output of the arduino and deleting \n\b at the end of the string
        total_value += 1                       # increment total_value by one
        value_time = datetime.datetime.now()   # get the current datetime (some milliseconds elapsed since last check)
        
        str_value_time = value_time.strftime("%H:%M:%S")   # convert value_time into string value
        print("temperature value [ " + read_serial + " ] at: " + str_value_time)    # debug print
        
        new_temperature = TemperatureData(value=read_serial, snapshot_date=value_time, sensor_id=sensor_id)   # creating a new TemperatureData object
        db.session.add(new_temperature)            # add and ...
        db.session.commit()                        # commit this TemperatureData to the database
        
        if (value_time - timestart) > loop_time:   # when loop_time has elapsed, return the number of input value received
            return total_value
        
        