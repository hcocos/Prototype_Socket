#!/usr/bin/env python
#coding: utf8 
 
import RPi.GPIO as GPIO
import time


# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BCM)

#Schaltet Warnungen auf der Kommandozeile aus
GPIO.setwarnings(False)

# Definiert alle Ports als Ausgang und 
# Setzt sie auf HIGH
for port in range(2, 11):
	GPIO.setup(port, GPIO.OUT)
	GPIO.output(port, GPIO.HIGH)


# Port 26 wird als Input mit Pull Down Widerstand gesetzt
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
 

# Interrupt Routine zum Schalten der Relais
def isr26(channel):
	
	button_Push_Flag = 0
	
	if GPIO.input(9) == 0:

		button_Push_Flag = 1
                
		print("\nPower OFF!\n")
		for port in range(2, 11):
                        #print("GPIO State Loop: %s" %GPIO.input(26))
                        GPIO.output(port, GPIO.HIGH)
                        #print ('Port ', port, ' gestoppt')
                        time.sleep(1)


		
	if GPIO.input(9) == 1 and button_Push_Flag == 0:
		
		print("\nPower ON!\n")
		for port in range(2, 11):
			#print("GPIO State Loop: %s" %GPIO.input(26))
			GPIO.output(port, GPIO.LOW)
			#print ('Port ', port, ' gestartet')
			time.sleep(1)
	
	# Der Interrupt wird geloescht und naschließend wieder angemeldet
	# Muss gemacht werden weil der Interrupt sonst doppelt ausgefuehrt wird
	GPIO.remove_event_detect(26)
	GPIO.add_event_detect(26, GPIO.RISING, callback=isr26, bouncetime=500)


# Definiert den Interrupt
GPIO.add_event_detect(26, GPIO.RISING, callback=isr26, bouncetime=500)


try:
	print("Started!\n")
	while True:
		pass		


except KeyboardInterrupt:
	GPIO.cleanup()
	print("Bye Bye")
