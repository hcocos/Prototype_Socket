#!/usr/bin/env python
#coding: utf8 

from webserver import webserver
from flask import render_template

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# The Sockets are defined globally in this dictionary
dosen = {
	2 : {'name' : 'Socket No. 1', 'status' : GPIO.HIGH},
	3 : {'name' : 'Socket No. 2', 'status' : GPIO.HIGH},
 	4 : {'name' : 'Socket No. 3', 'status' : GPIO.HIGH},
	5 : {'name' : 'Socket No. 4', 'status' : GPIO.HIGH},
	6 : {'name' : 'Socket No. 5', 'status' : GPIO.HIGH},
 	7 : {'name' : 'Socket No. 6', 'status' : GPIO.HIGH},
	8 : {'name' : 'Socket No. 7', 'status' : GPIO.HIGH},
	9 : {'name' : 'Socket No. 8', 'status' : GPIO.HIGH}}

# This Loop defines the Sockets as Output and sets them to HIGH (Off)
for dose in dosen:
	GPIO.setup(dose, GPIO.OUT)
	GPIO.output(dose, GPIO.HIGH)

# index File
@webserver.route('/')
@webserver.route('/index')
def index():
	
	isOn = False
	
	# Reads status of the sockets	
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)
	
	# The status of the sockets is saved in dictionary and then
	# returned to the index file
	dynamicData = {
	'buttonState' : isOn,
	'dosen' : dosen
	}
	
	return render_template("index.html", **dynamicData)	


@webserver.route('/<button>')
@webserver.route('/index/<button>')
def switchCluster(button):
	
	# If the Button on the HTML page is clicked
	# the state of the Button is changed
	# True the Sockets switched on
	# with a delay of 1 second
	# else the Sockets switche off
	if button == "on":
		
		isOn = True
		response = "Cluster on"
		for dose in dosen:
			GPIO.output(dose, GPIO.LOW)
			time.sleep(1)
	else:
		
		isOn = False
		response = "Cluster off"
		for dose in dosen:
			GPIO.output(dose, GPIO.HIGH)
			time.sleep(1)
		
	# The status of the sockets is saved in dictionary
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)

	dynamicData = {
	'dosen' : dosen,
	'buttonState' : isOn,
	'response':response
	}

	
	return render_template('index.html', **dynamicData)
