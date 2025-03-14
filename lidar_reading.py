"""
Program Name: lidar_reading.py
Description: Sets up the lidar sensor to get readings. Will be used for detecting when the MPR is about to hit a wall or if it reached its goal.
Programmer(s): Ben Weinzirl
Date Made: 3/02/2025
Date(s) Revised:
Preconditions: 
Postconditions: 
Errors/Exceptions:
Side Effects:
Invariants: 
Known Faults:
"""

import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar

def get_data():
    # May have to change COM5 to correct port (Use Windows Device Manager)
    lidar = RPLidar('COM5', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):    
        break    
        lidar.stop()    
    return scan

for i in range(1000000):    
    if(i%7==0):    
        x = np.radians([])   
        y = []    
    print(i)    
    current_data=get_data()    
    for point in current_data:    
        if point[0]==15:    
            x.append(point[2]*np.sin(point[1]))    
            y.append(point[2]*np.cos(point[1]))    
    plt.clf()    
    plt.scatter(x, y)    
    plt.pause(.1)    
plt.show()
