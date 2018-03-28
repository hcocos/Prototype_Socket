#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO


# Setzt das Schema auf GPIO Nummern
GPIO.setmode(GPIO.BCM)

# Schaltet Warnungen auf der Kommandozeile aus
GPIO.setwarnings(False)

GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.HIGH)

