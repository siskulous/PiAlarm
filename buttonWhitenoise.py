#!/usr/bin/python
from RPi import GPIO
from time import sleep
from time import time
from pygame import mixer
import thread
from pygame import midi
from random import randint

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_UP)
playing=False

def music():
	global playing
	midi.init()
	midOut=midi.Output(2)
	midOut.set_instrument(122)
	start=time()
	now=time()
	while now-start<14400 and playing:
		print now-start
		note=randint(10,30)
		midOut.note_on(note,100)
		now=time()
		sleep(1)
		midOut.note_off(note,100)

	mixer.quit()
	thread.exit()

def buttonPushed():
	global playing
	if playing:
		playing=False
	else:
		playing=True
		thread.start_new_thread(music,())

def buttonListen():
	while True:
		GPIO.wait_for_edge(31, GPIO.FALLING)
		sleep(0.1)
		if not GPIO.input(31):
			buttonPushed()
		sleep(0.2)

thread.start_new_thread(buttonListen,())

while True:
	sleep(60)
