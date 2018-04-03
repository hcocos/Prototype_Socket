#!/usr/bin/env python
#coding: utf8 


from flask import Flask, jsonify


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


app = Flask(__name__)


# Returns the status of the Sockets as a JSON Object
@app.route('/webservice/stem/status', methods=['GET'])
def status():

	# reads the status of the sockets     
	for dose in dosen:
		dosen[dose]['status'] = GPIO.input(dose)

	return jsonify({'Dose':dosen})


# switches on the sockets sequentially
@app.route('/webservice/stem/on/all', methods=['GET'])
def allOn():

	for dose in dosen:
		GPIO.output(dose, GPIO.LOW)
		time.sleep(1)

	return "All Sockets switched on!\n"


# switches off the sockets sequentially
@app.route('/webservice/stem/off/all', methods=['GET'])
def allOff():

	for dose in dosen:
		GPIO.output(dose, GPIO.HIGH)
		time.sleep(1)

	return "All Sockets switched off!\n"

if __name__ == '__main__':
    app.run(debug=True, host='192.168.178.220',port=2789)


