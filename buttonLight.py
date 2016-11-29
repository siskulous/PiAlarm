#!/usr/bin/python
from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(36,GPIO.OUT)
GPIO.output(36,False)

try:
	while True:
		if not GPIO.input(37):

			if GPIO.input(36):
				GPIO.output(36,False)
			else:
				GPIO.output(36,True)
			while not GPIO.input(37):
				sleep(0.1)
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

