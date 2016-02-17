#!/usr/bin/python

import io
import time
import sys
sys.path.append('..')
from wheelMotors import *

def testLeftMotor(count):
    left_wheels_forward()
    startLeftMotor()
    for i in range(count):
        time.sleep(motor_unit_distance_time)
    stopLeftMotor()

def testRightMotor(count):
    right_wheels_forward()
    startRightMotor()
    for i in range(count):
        time.sleep(motor_unit_distance_time)
    stopRightMotor()

def test():
    driveForward(2)
    driveBackward(2)
    turnLeft(2)
    turnRight(2)

test()
GPIO.cleanup()
