#!/usr/bin/env python
#coding: utf8 
 
import RPi.GPIO as GPIO
import time


# Sets the Numbering of the GPIO-Ports
GPIO.setmode(GPIO.BCM)

# Disables warnings on Command Line
GPIO.setwarnings(False)

# Defines all Ports as Output
# Then sets them to HIGH
for port in range(2, 11):
	GPIO.setup(port, GPIO.OUT)
	GPIO.output(port, GPIO.HIGH)


# Port 26 defined as Input and Pull-Down defined 
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
 

# Interrupt Routine to switch on Relays
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
	
	# The Interrupt has to be removed and afterwards needs to be reenabled
	# This is done to prevent the Interrupt of double execution
	GPIO.remove_event_detect(26)
	GPIO.add_event_detect(26, GPIO.RISING, callback=isr26, bouncetime=500)


# Adds the Interrupt
GPIO.add_event_detect(26, GPIO.RISING, callback=isr26, bouncetime=500)


try:
	print("Started!\n")
	while True:
		pass		


except KeyboardInterrupt:
	GPIO.cleanup()
	print("Bye Bye")
