#!/usr/bin/python
from RPi import GPIO
from time import sleep
from time import time
from pygame import mixer
import thread

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def music():
	mixer.init(44100)
	start=time()
	now=time()
	while now-start<14400:
		mixer.music.load('/opt/pialarm/whiteNoise.mp3')
		mixer.music.play()
		mixer.music.set_volume(0.3)
		try:
			#In case the file's not big enough. This is why I don't just have it sleep for 4 hours.
			while mixer.music.get_busy():
				now=time()
				if now-start>14400:
					mixer.quit()
				sleep(6)
		except Exception:
			thread.exit()
	mixer.quit()

def buttonPushed():
	sleep(0.1)
	if not GPIO.input(31):
		if mixer.get_init():
			mixer.music.stop()
			mixer.quit()
		else:
			thread.start_new_thread(music,())

def buttonListen():
	while True:
		GPIO.wait_for_edge(31, GPIO.FALLING)
		buttonPushed()
		sleep(1)

thread.start_new_thread(buttonListen,())

while True:
	sleep(600)
