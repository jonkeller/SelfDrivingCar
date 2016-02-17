import time
from lidarLite import Lidar_Lite
from mastMotor import *

lidar = Lidar_Lite()

def test(): 
    connected = lidar.connect(1)

    if connected <= -1:
        print "Not Connected"
        return -1
    print "Connected"

    moveDelaySeconds = 0.05
    revolutions = 5
    forwardWithCallback(moveDelaySeconds, revolutions*mast_steps_per_revolution, measure) # Will call measure 4x that many times

def measure():
    readDelaySeconds = 0.0
    GPIO.output(mast_enable_pin, False)
    GPIO.output(mast_in1_pin, False)
    GPIO.output(mast_in2_pin, False)
    GPIO.output(mast_in3_pin, False)
    GPIO.output(mast_in4_pin, False)
    if readDelaySeconds > 0.0:
        time.sleep(readDelaySeconds)
    try:
        distance = lidar.getDistance()
        #print "Distance:", distance, "cm"
        print distance
    except Exception as e:
        print "Exception:", e
        #print "Exception"
    GPIO.output(mast_enable_pin, True)

test()

GPIO.cleanup()

