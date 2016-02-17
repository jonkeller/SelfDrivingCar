import io
import time
import RPi.GPIO as GPIO
from pins import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(mast_enable_pin, GPIO.OUT)
GPIO.setup(mast_in1_pin, GPIO.OUT)
GPIO.setup(mast_in2_pin, GPIO.OUT)
GPIO.setup(mast_in3_pin, GPIO.OUT)
GPIO.setup(mast_in4_pin, GPIO.OUT)
 
GPIO.output(mast_enable_pin, True)

def cleanup():
    GPIO.output(mast_enable_pin, False)
    GPIO.output(mast_in1_pin, False)
    GPIO.output(mast_in2_pin, False)
    GPIO.output(mast_in3_pin, False)
    GPIO.output(mast_in4_pin, False)
    GPIO.cleanup()
 
def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)
 
def forwardWithCallback(delay, steps, callback):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    callback()
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    callback()
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    callback()
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    callback()
 
def backward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)
 
  
def setStep(w1, w2, w3, w4):
    GPIO.output(mast_in1_pin, w1)
    GPIO.output(mast_in2_pin, w2)
    GPIO.output(mast_in3_pin, w3)
    GPIO.output(mast_in4_pin, w4)

