"""
Program Name: hiding.py
Description: This is the hiding algorithm that the MPR follows when hiding
Programmer(s): Ben Weinzirl
Date Made: 3/16/2025
Date(s) Revised: 3/30/2025 - Updated to include work on sensor-reading files
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""


from pynq.overlays.base import BaseOverlay
import irsensor.py
import ultrasonic.py
import time

# For now, this is psuedocode until readings from Lidar sensors are achieved and the wheels can move.
def hiding(self, difficulty, time):
# two minutes for hiding to not waste time.

  while time is not 0:
    lidar_reading = Lidar.reading

    if lidar_reading < 20: # The robot is in front of a wall
      walls = MPR.countWalls() # Returns number of walls around MPR
      if walls >= difficulty # difficulty represents # of walls that must be around the MPR
        MPR.done() # Shutdown command tbd
      else:
        # Functions to be created in the movement file
        MPR.backup()
        MPR.turn_right()
    else:
      MPR.move() # Robot moves around randomly to find a spot

    MPR.hiding(difficulty - 1, time/2) # If the MPR cannot find a spot, the difficulty is decreased
  


