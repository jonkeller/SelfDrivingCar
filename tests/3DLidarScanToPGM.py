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
TILT_MAX_ANGLE = 85
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

INCREMENT = 2
W = 1 + (PAN_MAX_ANGLE - PAN_MIN_ANGLE) / INCREMENT
H = 1 + (TILT_MAX_ANGLE - TILT_MIN_ANGLE) / INCREMENT
MaxDepth = 0
depths = [[0 for x in range(W+1)] for y in range(H+1)]

i=0;
for t in range(TILT_MIN_ANGLE, TILT_MAX_ANGLE+1, INCREMENT):
    tilt(t)
    j=0
    for p in range(PAN_MIN_ANGLE, PAN_MAX_ANGLE+1, INCREMENT):
        pan(p)
        try:
            time.sleep(SLEEP_TIME)
            depth = lidar.getDistance()
            if depth > MaxDepth:
                MaxDepth = depth
            depths[i][j] = depth
        except:
            pass
        j+=1
    i+=1

print "P2"
print W, H   #"91 57"
print MaxDepth
for y in range(i):
    for x in range(j):
        print depths[y][x],
    print ""

cleanup()

