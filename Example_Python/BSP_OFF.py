#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO

# Setzt das Schema auf GPIO Nummern
GPIO.setmode(GPIO.BCM)

# Schaltet Warnungen auf der Kommandozeile aus
GPIO.setwarnings(False)

for port in range(2, 10):
	GPIO.setup(port, GPIO.HIGH)

print("Ports wurden geschlossen")
GPIO.cleanup()
