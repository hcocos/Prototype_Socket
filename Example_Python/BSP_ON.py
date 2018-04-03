#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO

import time

# Sets the GPIO Numbering to the Port Numbering 
GPIO.setmode(GPIO.BCM)

# Disables warnings on Command Line
GPIO.setwarnings(False)

# Defines all GPIO-Ports as Output 
# Then sets the State to HIGH
for port in range(2, 10):
	GPIO.setup(port, GPIO.OUT)
	GPIO.output(port, GPIO.HIGH)

print("Ports wurden gesetzt")

# Toggles all Ports with a delay of 500ms
for port in range(2, 10):
	GPIO.output(port, GPIO.LOW)
	print ('Port ', port, ' gestartet')
	time.sleep(0.5)

