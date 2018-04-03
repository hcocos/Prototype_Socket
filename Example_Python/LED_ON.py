#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO


# Sets the GPIO Numbering to the Port Numbering 
GPIO.setmode(GPIO.BCM)

# Disables warnings on Command Line
GPIO.setwarnings(False)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)

