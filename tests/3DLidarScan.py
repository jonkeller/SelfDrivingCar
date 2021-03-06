#!/usr/bin/python

from RPIO import PWM
import time
import sys
sys.path.append('..')
from lidarLite import Lidar_Lite

PAN_SERVO_PIN = 14
TILT_SERVO_PIN = 8
RIGHT = 560
LEFT = 2500
CENTER = (LEFT + RIGHT) / 2
GRANULARITY_MICROSECONDS = 10
TILT_MIN_ANGLE = -45
TILT_MAX_ANGLE = 90
PAN_MIN_ANGLE = -90
PAN_MAX_ANGLE = 90
SLEEP_TIME = 0.02

def pan(angle):
    us = angleToMicroseconds(angle)
    servo.set_servo(PAN_SERVO_PIN, us)

def tilt(angle):
    us = angleToMicroseconds(angle)
    servo.set_servo(TILT_SERVO_PIN, us)

def angleToMicroseconds(angle):
    us = int(((angle + 90) * ((LEFT-RIGHT)/(180.0))) + RIGHT)
    us -= (us % GRANULARITY_MICROSECONDS)
    return us

def cleanup():
    servo.stop_servo(PAN_SERVO_PIN)
    servo.stop_servo(TILT_SERVO_PIN)

PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)
servo = PWM.Servo()
lidar = Lidar_Lite()
connected = lidar.connect(1)

if connected <= -1:
    print "Not Connected"
    exit(1)

print "Pan_Angle, Tilt_Angle, Distance (cm), Error"
INCREMENT = 2
for t in range(TILT_MIN_ANGLE, TILT_MAX_ANGLE+1, INCREMENT):
    tilt(t)
    for p in range(PAN_MIN_ANGLE, PAN_MAX_ANGLE+1, INCREMENT):
        pan(p)
        try:
            time.sleep(SLEEP_TIME)
            distance = lidar.getDistance()
            print p, ",", t, ",", distance, ","
        except:
            print p, ",", t, ",", -1, sys.exc_info()[0]
            pass

cleanup()

