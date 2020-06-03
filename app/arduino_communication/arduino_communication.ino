#include <Wire.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2       // DS18B20 data wire is connected to input 2

typedef uint8_t DeviceAdress[8];

DeviceAdress thermometerAdress;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);

void setup() {
  Serial.begin(9600);
  tempSensor.begin();                              // intialize the temp sensor
  tempSensor.setResolution(thermometerAdress, 12);  // set temperature resoluton (choose between 9 and 12)
}

void loop() {
  tempSensor.requestTemperatures();               // request the temperature to the sensor
  Serial.println(tempSensor.getTempCByIndex(0));  // print value into serial output
  delay(500);                                    // delay each print by X milliseconds
}



