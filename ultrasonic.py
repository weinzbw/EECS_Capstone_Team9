"""
Program Name: lidar_reading.py
Description: Sets up the lidar sensor to get readings. Will be used for detecting when the MPR is about to hit a wall or if it reached its goal.
Programmer(s): Ben Weinzirl
Date Made: 3/02/2025
Date(s) Revised: 3/30/2025 - Corrected from lidar sensor to ultrasonic sensor setup and reading
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""

from pynq.overlays.base import BaseOverlay
from pynq.lib.pmod import Pmod_ID
import time

base = BaseOverlay("base.bit")

sonar = Pmod_IO(base.PMODB, 0, "out")
# Only one wire needs to connect to a Pmod set, as the other two are for 5V and ground
# Change the PMOD and correct number to whatever the sensor ends up being plugged in to

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
