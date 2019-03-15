# Python-Light-Relay
Using Python script and Thinkspeak values to turn a AC light on or off
Python-light-relay
Problem Statement
The objective was to find a way to turn a light on and off using the SparkFun RedBoard and interfacing the Arduino software with Python. We set out to have a user input “H” or “L” inputs into Python which would be read by the Arduino software and subsequently run a current through the relay to operate the light. 
 
Hardware Setup
Bill of Materials
component
vendor
Arduino
SparkFun RedBoard - Programmed with Arduino
Relay
SparkFun Beefcake Relay Control Kit (Ver. 2.0)
Jumper wires
Jumper Wires Premium 6" M/M Pack of 10
Mini-B USB cable
SparkFun USB Mini-B Cable - 6 Foot
Enclosure
Big Red Box - Enclosure
extension cord male end
Recieved from PCC Engineering Lab
extension cord female end
Recieved from PCC Engineering Lab
Hardware Schematic.

Hookup Guide:
Step 1:
	Cut holes into Big Red Box enclosure. Make sure that the Arduino MiniB connector line up.












Step 2: 
		Thread the power cables through the side holes and separate the wire colors.  Now using the black wires, connect the Male prong to the High voltage side of the relay marked COM. Next, do the same with the female, but connect to the spot in the middle marked NO. In this step, you will also connect three jumper wires to the low voltage side of the relay.








Step 3:
		Next, using the twist-on wire connectors, twist both white wires together and both green wires together. Tuck them down in the Big Red Box somewhere out of the way. In this step, you will also want to screw down the Beefcake relay into one of the risers that are provided. 





https://github.com/nganvan/Python-Light-Relay/blob/master/thinkspeak%20value.ipynb
















Step 4:
		In this final step place your Arduino on one of the ¾ inch risers and secure it to one of the spaces in the bottom of the box. The next thing you will need to do is connect the wires from the relay. Take the black jumper wire secured to the ground port and connect it to the Arduino’s GND port. Now, take the Yellow wire secured to the CTRL port on the relay and connect it to port #13 on the Arduino. Finally, Take the red wire secured tot he 5v port on the relay and connect it to the 5v port on your Arduino. 





















Code:
We have two python code:
Write data for thingspeak. 
This code will send the data ( 1 or 0 ) to thingspeak 
import requests 
user_input = input('Type 1 to turn light on, Type 0 to turn light off')
url = f'https://api.thingspeak.com/update?api_key=PYZU7IZ814A3PGGE&field1={user_input}'
print(url)
r = requests.get(url)
print(r)


	2: Read data from thingspeak and Python communication with an Arduino.
This code will pull the data from thingspeak. If the data equal 1 the light will turn on and if the data equal 0 the light will turn off.
The script was run in Python. The serial Port had to be the correct one in order for the Python script to run. Our port was '/dev/cu.usbserial-DN02SRDI' and must be checked in the Windows Device Manager.



thinkspeak value.ipynb



import serial
serial.__version__
import serial
import time
import requests

#use the requests library to pull down the data from thingspeak into a variable

r = requests.get(url)
print(r)
json_data = r.json()
print(json_data['feeds'][0]['field1'])

ser = serial.Serial('/dev/cu.usbserial-DN02SRDI',9600)   #This is our port /dev/cu.usbserial-DN02SRDI

time.sleep(2)
# print(ser.name)
 # Turn light on     
if json_data['feeds'][0]['field1'] == '1':
    ser.write(b'H') 
    print('Light is now on')

 # Turn light off        
elif json_data['feeds'][0]['field1'] == '0':
    ser.write(B'L')
    print('Light is now off')
ser.close()  # close port









Arduino code:

/*
  Physical Pixel

  An example of using the Arduino board to receive data from the computer. In
  this case, the Arduino boards turns on an LED when it receives the character
  'H', and turns off the LED when it receives the character 'L'.

  The data can be sent from the Arduino Serial Monitor, or another program like
  Processing (see code below), Flash (via a serial-net proxy), PD, or Max/MSP.

  The circuit:
  - LED connected from digital pin 13 to ground

  created 2006
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe and Scott Fitzgerald

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/PhysicalPixel
*/

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}













Result: 

 
 
Future Work
Future endeavors are to automate the lighting, so the lights turn on and off relative to the falling and rising of the sun. The times for this could be collected using data online providing when sunrise and sunset occur each day.
 
 
 
License
The MIT License
Copyright <2019> <Evan,Hoang,Ngan>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





