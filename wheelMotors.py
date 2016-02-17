import io
import time
import RPi.GPIO as GPIO
from pins import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_wheel_enable_pin, GPIO.OUT)
GPIO.setup(left_wheel_in1_pin, GPIO.OUT)
GPIO.setup(left_wheel_in2_pin, GPIO.OUT)
GPIO.setup(right_wheel_enable_pin, GPIO.OUT)
GPIO.setup(right_wheel_in3_pin, GPIO.OUT)
GPIO.setup(right_wheel_in4_pin, GPIO.OUT)

wheel_motor_unit_distance_time = .500 # seconds for the motor to go a distance of "1"
wheel_motor_speed = 99 # 0...99

left_wheel_motor = GPIO.PWM(left_wheel_enable_pin, 100)
right_wheel_motor = GPIO.PWM(right_wheel_enable_pin, 100)

# Sets the direction of the left wheels to "forward" (though they may not actually be moving).
def left_wheel_wheels_forward():
    GPIO.output(left_wheel_in1_pin, True)
    GPIO.output(left_wheel_in2_pin, False)

# Sets the direction of the left wheels to "backward" (though they may not actually be moving).
def left_wheel_wheels_backward():
    GPIO.output(left_wheel_in1_pin, False)
    GPIO.output(left_wheel_in2_pin, True)

# Sets the direction of the right wheels to "forward" (though they may not actually be moving).
def right_wheel_wheels_forward():
    GPIO.output(right_wheel_in3_pin, True)
    GPIO.output(right_wheel_in4_pin, False)

# Sets the direction of the right wheels to "backward" (though they may not actually be moving).
def right_wheel_wheels_backward():
    GPIO.output(right_wheel_in3_pin, False)
    GPIO.output(right_wheel_in4_pin, True)

# Make the left motor start going, in whichever direction was set via the above methods
def startLeftMotor():
    #set("duty", wheel_motor_speed)
    left_wheel_motor.start(wheel_motor_speed)

# Make the left motor stop going, in whichever direction was set via the above methods
def stopLeftMotor():
    #set("duty", "0")
    left_wheel_motor.stop()

# Make the right motor start going, in whichever direction was set via the above methods
def startRightMotor():
    #set("duty", wheel_motor_speed)
    right_wheel_motor.start(wheel_motor_speed)

# Make the right motor stop going, in whichever direction was set via the above methods
def stopRightMotor():
    #set("duty", "0")
    right_wheel_motor.stop()

def driveForward(count):
    left_wheel_wheels_forward()
    right_wheel_wheels_forward()
    startLeftMotor()
    startRightMotor()
    for i in range(count):
        time.sleep(wheel_motor_unit_distance_time)
    stopLeftMotor()
    stopRightMotor()

def driveBackward(count):
    left_wheel_wheels_backward()
    right_wheel_wheels_backward()
    startLeftMotor()
    startRightMotor()
    for i in range(count):
        time.sleep(wheel_motor_unit_distance_time)
    stopLeftMotor()
    stopRightMotor()

def turnLeft(count):
    right_wheel_wheels_forward()
    left_wheel_wheels_backward()
    startLeftMotor()
    startRightMotor()
    for i in range(count):
        time.sleep(wheel_motor_unit_distance_time)
    stopLeftMotor()
    stopRightMotor()

def turnRight(count):
    left_wheel_wheels_forward()
    right_wheel_wheels_backward()
    startLeftMotor()
    startRightMotor()
    for i in range(count):
        time.sleep(wheel_motor_unit_distance_time)
    stopLeftMotor()
    stopRightMotor()

