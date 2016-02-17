#!/usr/bin/python

import RPi.GPIO as GPIO
import time

PAN_SERVO_PIN = 23
TILT_SERVO_PIN = 24

RIGHT = 23 # 23% of 100Hz, which is 2.3ms
LEFT = 1
CENTER = (RIGHT+LEFT)/2.0
HALF_RANGE = CENTER-LEFT

RIGHT_ANGLE = 65.0 # My servo goes from about +65 degrees to about -65 degrees
LEFT_ANGLE = -RIGHT_ANGLE
CENTER_ANGLE = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PAN_SERVO_PIN, GPIO.OUT)
GPIO.setup(TILT_SERVO_PIN, GPIO.OUT)

frequency = 100 # In Hz
pan_pwm = GPIO.PWM(PAN_SERVO_PIN, frequency)
tilt_pwm = GPIO.PWM(TILT_SERVO_PIN, frequency)
pan_pwm.start(CENTER)
tilt_pwm.start(CENTER)

def pan(angle):
    move_servo(pan_pwm, angle)

def tilt(angle):
    move_servo(tilt_pwm, angle)

def move_servo(servo_pwm, angle):
    # For my particular servo, the angle is -65...65
    # Experimentation indicates that we want to set pulse width to 1ms for -65, 1.2ms for 0, and 2.3ms for 65
    # We want duty to be expressed as a percentage of frequency.
    # So that is 1% of the 100Mhz frequency for -65, 12% for 0, and 23% for 65 degrees
    duty = (HALF_RANGE*float(angle)/RIGHT_ANGLE) + CENTER
    servo_pwm.ChangeDutyCycle(duty)

for i in [LEFT_ANGLE, LEFT_ANGLE/2, CENTER_ANGLE, RIGHT_ANGLE/2, RIGHT_ANGLE]:
    print "Moving to pan", i, "degrees"
    pan(i)
    time.sleep(3)

for i in [LEFT_ANGLE, LEFT_ANGLE/2, CENTER_ANGLE, RIGHT_ANGLE/2, RIGHT_ANGLE]:
    print "Moving to tilt", i, "degrees"
    tilt(i)
    time.sleep(3)

print "Now to move interactively:"
print "At any time, type something that isn't an integer to quit."

while True:
    try:
        degrees = int(raw_input('How many degrees to pan? '))
        pan(degrees)
        degrees = int(raw_input('How many degrees to tilt? '))
        tilt(degrees)
    except ValueError:
        break

GPIO.cleanup()
