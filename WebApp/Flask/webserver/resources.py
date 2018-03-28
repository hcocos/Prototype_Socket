#!/usr/bin/env python
#coding: utf8 

from webserver import webserver
from flask import render_template

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Global werden die Ports und dazugehoerige Werte gesetzt
dosen = {
	2 : {'name' : 'Steckdose Nr. 1', 'status' : GPIO.HIGH},
	3 : {'name' : 'Steckdose Nr. 2', 'status' : GPIO.HIGH},
 	4 : {'name' : 'Steckdose Nr. 3', 'status' : GPIO.HIGH},
	5 : {'name' : 'Steckdose Nr. 4', 'status' : GPIO.HIGH},
	6 : {'name' : 'Steckdose Nr. 5', 'status' : GPIO.HIGH},
 	7 : {'name' : 'Steckdose Nr. 6', 'status' : GPIO.HIGH},
	8 : {'name' : 'Steckdose Nr. 7', 'status' : GPIO.HIGH},
	9 : {'name' : 'Steckdose Nr. 8', 'status' : GPIO.HIGH}}

# In Schleife werden jetzt die Dosen gesetzt
for dose in dosen:
	GPIO.setup(dose, GPIO.OUT)
	GPIO.output(dose, GPIO.HIGH)

# index Datei
@webserver.route('/')
@webserver.route('/index')
def index():
	
	isOn = False
	
	# liest den Status aller Ports aus 	
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)
	
	# Der Status der Dosen wird in Dictionary gespeichert und 
	# an HTML weitergereicht
	dynamicData = {
	'buttonState' : isOn,
	'dosen' : dosen
	}
	
	return render_template("index.html", **dynamicData)	


@webserver.route('/<button>')
@webserver.route('/index/<button>')
def switchCluster(button):
	
	# Wenn der Button im HTML Dokument 
	# gedrueckt wurde wird sein state auf
	# True gesetzt und die Steckdosen 
	# werden mit einem Delay von 1 Sekunde
	# angeschaltet
	# else werden sie abgeschaltet
	if button == "on":
		
		isOn = True
		response = "Cluster angeschaltet"
		for dose in dosen:
			GPIO.output(dose, GPIO.LOW)
			time.sleep(1)
	else:
		
		isOn = False
		response = "Cluster ausgeschaltet"
		for dose in dosen:
			GPIO.output(dose, GPIO.HIGH)
			time.sleep(1)
		
	# Der Status der Steckdosen wird im Dictionary gespeichert
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)

	dynamicData = {
	'dosen' : dosen,
	'buttonState' : isOn,
	'response':response
	}

	
	return render_template('index.html', **dynamicData)
