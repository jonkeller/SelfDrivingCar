#!/usr/bin/python

from RPIO import PWM
import time
import sys

PAN_SERVO_PIN = 14
TILT_SERVO_PIN = 8
RIGHT = 560
LEFT = 2500
CENTER = (LEFT + RIGHT) / 2
GRANULARITY_MICROSECONDS = 10

servo = PWM.Servo()

def pan(angle):
    us = angleToMicroseconds(angle)
    print angle, us, RIGHT, LEFT
    servo.set_servo(PAN_SERVO_PIN, us)

def tilt(angle):
    us = angleToMicroseconds(angle)
    print angle, us, RIGHT, LEFT
    servo.set_servo(TILT_SERVO_PIN, us)

def angleToMicroseconds(angle):
    us = int(((angle + 90) * ((LEFT-RIGHT)/(180.0))) + RIGHT)
    us -= (us % GRANULARITY_MICROSECONDS)
    return us

print "At any time, type something that isn't an integer to quit."
while True:
    try:
        angle = int(raw_input('Enter angle to pan in degrees (-90...90)? '))
        pan(angle)
        angle = int(raw_input('Enter angle to tilt in degrees (-90...90)? '))
        tilt(angle)
    except ValueError:
        print "Okay, stopping."
        break
    except (RuntimeError, TypeError, NameError, AttributeError) as detail:
        print "Unexpected error:", detail
    except:
        print "Unexpected error:", sys.exc_info()[0]
        break

servo.stop_servo(PAN_SERVO_PIN)
servo.stop_servo(TILT_SERVO_PIN)

