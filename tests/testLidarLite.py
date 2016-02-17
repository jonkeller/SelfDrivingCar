#!/usr/bin/python

import sys
sys.path.append('..')
from lidarLite import Lidar_Lite
import time

NUM_TESTS = 100
SLEEP_TIME = 1

lidar = Lidar_Lite()
connected = lidar.connect(1)

if connected <= -1:
    print "Not Connected"
    exit(1)

print "Connected"
print "Going to test", NUM_TESTS, "times: once every", SLEEP_TIME, "second(s)."

for i in range(NUM_TESTS):
    try:
        time.sleep(SLEEP_TIME)
        distance = lidar.getDistance()
        print "Distance:", distance, "cm"
    except:
        print "Exception"
        pass
#print "Velocity:", lidar.getVelocity()
