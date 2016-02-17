#!/usr/bin/python

import sys
sys.path.append('..')
from mastMotor import *

def test(): 
    steps = 100
    while int(steps) > 0:
        delay = raw_input("Delay between steps (milliseconds)?")
        steps = raw_input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("How many steps backward? ")
        backward(int(delay) / 1000.0, int(steps))

test()

cleanup()
