#!/usr/bin/python
from RPi import GPIO
from pygame import mixer
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_UP)
mixer.init(44100)
start=time.time()
mixer.music.set_volume(70)
try:
	while True:
		if not GPIO.input(31):
			sleep(0.5)
			musicMode=True
			while musicMode:
				mixer.music.load("/opt/pialarm/whiteNoise.mp3")
				mixer.music.play()
				now=time.time()
				while mixer.music.get_busy():
					if not GPIO.input(31) or now-start>14400:
						mixer.music.stop()
						musicMode=False
					now=time.time()
				sleep(0.5)
		sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

