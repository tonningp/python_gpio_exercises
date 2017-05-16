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

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(led01,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led01,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
