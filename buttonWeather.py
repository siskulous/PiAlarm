#!/usr/bin/python
from RPi import GPIO
from time import sleep
from os import system
from os import path

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
try:
	while True:
		if not GPIO.input(13):
			print('push')
			if not path.isfile('/tmp/weather.wav'):
				system('python /opt/pialarm/fetchWeather.py')
			system('aplay /tmp/weather.wav')
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

