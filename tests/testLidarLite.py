#!/usr/bin/python

import sys
sys.path.append('..')
from lidarLite import Lidar_Lite
import time

lidar = Lidar_Lite()
connected = lidar.connect(1)

if connected <= -1:
    print "Not Connected"
    exit(1)

print "Connected"
for i in range(100):
    try:
        time.sleep(1)
        distance = lidar.getDistance()
        print "Distance:", distance, "cm"
    except:
        print "Exception"
        pass
#print "Velocity:", lidar.getVelocity()
