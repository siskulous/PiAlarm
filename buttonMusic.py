#!/usr/bin/python
from RPi import GPIO
from time import sleep
from pygame import mixer
from random import choice
from glob import glob

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.IN,pull_up_down=GPIO.PUD_UP)
songs=glob('/home/pi/music/*.mp3')
try:
	while True:
		if not GPIO.input(33):
			sleep(0.5)
			musicMode=True
			mixer.init(44100)
			while musicMode:
				song=choice(songs)
				mixer.music.load(song)
				mixer.music.play()
				while mixer.music.get_busy():
					if not GPIO.input(33):
						mixer.music.stop()
						musicMode=False
				sleep(0.5)
			mixer.quit()
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

