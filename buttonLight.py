#!/usr/bin/python
from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(36,GPIO.OUT)
GPIO.output(36,False)

'''
What? No try/except loop?

Nope. Two reasons. First and foremost, this script should be running in the background and thus
is problematic to interrupt. It can be done via kill, but really if you do that you're probably
going to want to reboot to get the clock working again anyway. Second, and more importantly, we DO
NOT want to clean up the GPIO. Other scripts are using it too and cleaning it up will break them.
'''
while True:
	GPIO.wait_for_edge(37, GPIO.FALLING)
	sleep(0.1)
	if not GPIO.input(37):
		if GPIO.input(36):
			GPIO.output(36,False)
		else:
			GPIO.output(36,True)
	sleep(0.2)
