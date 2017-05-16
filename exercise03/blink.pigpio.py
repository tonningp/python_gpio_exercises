#!/usr/bin/env python3
import pigpio
import time

class Led:
    pi = pigpio.pi()       # pi accesses the local Pi's GPIO
    pi.set_mode(18, pigpio.OUTPUT) # GPIO 18 as output

pi.write(18,1)
time.sleep(2)
pi.write(18,0)
