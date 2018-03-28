#!/usr/bin/env python
#coding: utf8 

import RPi.GPIO as GPIO

import time

# Setzt das Schema auf GPIO Nummern
GPIO.setmode(GPIO.BCM)

# Schaltet Warnungen auf der Kommandozeile aus
GPIO.setwarnings(False)

# Definiert alle Ports als Ausgang und 
# Setzt sie auf HIGH
for port in range(2, 10):
	GPIO.setup(port, GPIO.OUT)
	GPIO.output(port, GPIO.HIGH)

print("Ports wurden gesetzt")

# Schaltet die Ports an mit 5 Sekunden Unterbrechung zwischen jedem Port
for port in range(2, 10):
	GPIO.output(port, GPIO.LOW)
	print ('Port ', port, ' gestartet')
	time.sleep(0.5)

