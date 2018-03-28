#!/usr/bin/env python
#coding: utf8 


from flask import Flask, jsonify


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


app = Flask(__name__)


# gibt den Status aller Steckdosen als JSON Objekt zurueck
@app.route('/webservice/stem/status', methods=['GET'])
def status():

	# liest den Status aller Ports aus      
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)

	return jsonify({'Dose':dosen})


# schaltet alle Steckdosen der Reihe nach an
@app.route('/webservice/stem/on/all', methods=['GET'])
def allOn():

	for dose in dosen:
		GPIO.output(dose, GPIO.LOW)
		time.sleep(1)

	return "Alle Steckdosen angeschaltet!\n"


# schaltet alle Steckdosen der Reihe nach aus
@app.route('/webservice/stem/off/all', methods=['GET'])
def allOff():

	for dose in dosen:
		GPIO.output(dose, GPIO.HIGH)
		time.sleep(1)

	return "Alle Steckdosen ausgeschaltet!\n"

if __name__ == '__main__':
    app.run(debug=True, host='192.168.178.220',port=2789)


