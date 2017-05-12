#!/usr/bin/python
from RPi import GPIO
from time import sleep
from pygame import mixer
from random import choice
from glob import glob
import thread


GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.IN,pull_up_down=GPIO.PUD_UP)
songs=glob('/home/pi/music/*.mp3')

'''

def gpio_callback():
	if(musicMode):
		mixer.music.stop()
		mixer.quit()
		musicMode=False
	else:
		musicMode=True
		mixer.init(44100)
		songs=glob('/home/pi/music/*.mp3')
		while true:
			song=choice(songs)
			print(song)
			mixer.music.load(song)
			mixer.music.play()
			while mixer.music.get_busy():
				sleep(2)
	sleep(0.2)

'''
def music():
	mixer.init(44100)
	songs=glob('/home/pi/music/*.mp3')
	while mixer.get_init():
		mixer.music.load(choice(songs))
		mixer.music.play()
		try:
			while mixer.music.get_busy():
				sleep(1)
		except Exception:
			thread.exit()

def buttonPushed():
	if mixer.get_init():
		mixer.music.stop()
		mixer.quit()
	else:
		thread.start_new_thread(music,())

def buttonListen():
	while True:
		GPIO.wait_for_edge(33, GPIO.FALLING)
		sleep(0.05)
		if(not GPIO.input(33)):
			buttonPushed()
		sleep(0.2)

thread.start_new_thread(buttonListen,())

while True:
	sleep(60)
	
