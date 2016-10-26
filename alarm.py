###########################################################
# This paste contains two files because the alarm clock
# system it impliments requires both of them. The first 
# file is the actual alarm script. It will grab all MP3s
# from a given location and play them, one at a time, while
# reading the weather forecast (obtained from NOAA via the
# second script) in between each song.
#
# As of the time of this post I am manually setting crontab
# entries to trigger the alarm each day. This is, therefore
# a work in progress. At some point over the next week I'll
# be adding a web-based configuration for the whole thing
# with a database to hold the schedule.
############################################################


#imports
import commands, thread, time, glob
from random import choice
from time import sleep
from pygame import mixer

#This function is the actual alarm clock
def music(mins):
	#The timing functions use seconds, I want the input in minutes. Make the adjustment.
	secs=mins*60
	start=time.time()
	now=time.time()
	songs=glob.glob("~/Music/*.mp3")	#Read the directory with the MP3s
	mixer.init()	#Initiate the mixer
	volume=0.1      #set the initial volume
	#Play music until the specified time is up
	while now-start<secs:
		song=choice(songs) #Choose a song at random
		mixer.music.load(song) #Load the song into Pygame's music interface
		mixer.music.play() #start playing
		mixer.music.queue("/tmp/weather.wav") #Queue up the weather after each song
		while mixer.music.get_busy(): #Wait for the music to stop before loading another one.
			if volume < 1.0: #Slowly fade the volume up over the course of 10 minutes.
				volume=volume+0.01
				mixer.music.set_volume(volume)
			sleep(6)
		now=time.time()

#Unfinished and unimplemented function to turn on the light
def light(mins):
	secs=mins*60
	start=time.time()
	now=time.time()
	while now - start < secs:
		sleep(10)
	#Turn on the GPIO pin controlling the light

music(60)
#thread.start_new_thread(light,(5,))
