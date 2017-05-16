#!/usr/bin/env python3
# https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-example

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
led01 = 18

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(led01, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(led01, GPIO.LOW)
GPIO.output(led01,GPIO.HIGH)
time.sleep(2)
GPIO.output(led01,GPIO.LOW)
GPIO.cleanup() # cleanup all GPIO

# so now, using this code as and example, add another led pin and light
# 1 light for 2 seconds, then light the other light for 2 seconds then end the
# program.


