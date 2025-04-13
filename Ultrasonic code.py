#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
from pynq.overlays.base import BaseOverlay
from pynq.lib import Arduino_IO

# Load the base overlay for PYNQ-Z1
base = BaseOverlay("base.bit")

# Define the pins for the trigger and echo
# A0 = 14, A1 = 15 (pins on the Arduino header for trig and echo)
trigPin = 14  # Corresponds to A0 on the Arduino header
echoPin = 15  # Corresponds to A1 on the Arduino header

# Initialize the trigger and echo pins
trig = Arduino_IO(base.ARDUINO, trigPin, 'out')
echo = Arduino_IO(base.ARDUINO, echoPin, 'in')

# Function to measure the distance using the HC-SR04 sensor
def measure_distance():
    # Clear the trigPin
    trig.write(0)
    time.sleep(0.000002)  # Wait for 2 microseconds

    # Set the trigPin on HIGH for 10 microseconds
    trig.write(1)
    time.sleep(0.000010)  # Wait for 10 microseconds
    trig.write(0)

    # Measure the duration of the pulse on the echoPin
    while echo.read() == 0:  # Wait for the echo to start
        pass
    start_time = time.time()  # Record the start time

    while echo.read() == 1:  # Wait for the echo to end
        pass
    end_time = time.time()  # Record the end time

    # Calculate the duration of the pulse
    duration = end_time - start_time

    # Calculate the distance (speed of sound = 340 m/s)
    distance = (duration * 340) / 2  # Distance = (time * speed_of_sound) / 2

    return distance

# Main loop to continuously measure the distance
while True:
    dist = measure_distance()
    print(f"Distance: {dist:.2f} meters")
    time.sleep(1)  # Wait for 1 second before measuring again


# In[ ]:




