#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO

# Sets the GPIO Numbering to the Port Numbering 
GPIO.setmode(GPIO.BCM)

# Disables warnings on Command Line
GPIO.setwarnings(False)

for port in range(2, 10):
	GPIO.setup(port, GPIO.HIGH)

print("Ports wurden geschlossen")
GPIO.cleanup()
