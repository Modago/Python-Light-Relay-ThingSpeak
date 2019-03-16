#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial
serial.__version__
import time
import requests

user_input = input('Type 1 to turn light on, Type 0 to turn light off')
url = f'https://api.thingspeak.com/update?api_key=PYZU7IZ814A3PGGE&field1={user_input}'
print(url)
r = requests.get(url)
print(r)

url = 'https://api.thingspeak.com/channels/712547/fields/1.json?results=1'

#use the requests library to pull down the data from thingspeak into a variable

r = requests.get(url)
print(r)
json_data = r.json()
print(json_data['feeds'][0]['field1'])

ser = serial.Serial('/dev/cu.usbserial-DN02SRDI',9600)   # check which port was really used
time.sleep(2)
print(ser.name)

                                    
     
if json_data['feeds'][0]['field1'] == '1':
    ser.write(b'H')
        # turn light on
    print('Light is now on')
        
elif json_data['feeds'][0]['field1'] == '0':
    ser.write(B'L')
        # Turn light off
    print('Light is now off')


ser.close()  # close port


# In[ ]:




