"""
Program Name: hiding.py
Description: This is the hiding algorithm that the MPR follows when hiding
Programmer(s): Ben Weinzirl
Date Made: 3/16/2025
Date(s) Revised:
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""


# Imports for time, PYNQ base, lidar sensor, and maybe np?

# For now, this is psuedocode until readings from Lidar sensors are achieved and the wheels can move.
def hiding(self, difficulty, time):
# two minutes for hiding to not waste time.

while time is not 0:
  lidar_reading = Lidar.reading

  if lidar_reading < 20: # The robot is in front of a wall
    walls = MPR.countWalls() # Returns number of walls around MPR
    if walls >= difficulty # difficulty represents # of walls that must be around the MPR
      MPR.done()
    else:
      MPR.backup()
      MPR.turn_right()
  else:
    MPR.move() # Robot moves around randomly to find a spot

MPR.hiding(difficulty - 1, time/2) # If the MPR cannot find a spot, the difficulty is decreased
  


