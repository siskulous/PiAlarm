#!/usr/bin/python
import thread, time, glob, ConfigParser
from random import choice
from time import sleep
from os import system
from RPi import GPIO

#Since we're using external commands we need to handle the volume increase externally
#In the pygame version of this script pygame handles the volume, but unfortunately
#pygame seems to not handle media files correctly with the raspi
def vol(mins):
	#Calculate the sleep time
	secs=mins*60
	sleepTime=secs//50
	volume=50 #Volume starts at 50%, which is dang near inaudible on my Pi
	while volume<=100: #Run until full volume
                command="amixer sset PCM " + str(volume) + '%' #Build the command
		print(command)
                system(command)#Run the command
                volume=volume+1 #Increase the volume for the next iteration
                sleep(sleepTime) #Wait sleepTime seconds before raising volume again

#The function that plays the music and weather
def music(mins, lightPin):
	secs=mins*60 #Calculate how many seconds to run
	start=time.time()#Get starting time
	now=time.time()#Initialize the now var for the loop
	songs=glob.glob("/home/pi/music/*.mp3") #Get the list of songs
	while now-start<secs: #Loop for specified time
		song=choice(songs) #Pick a song
		system('mpg123 "' + song + '"') #Play it with mplayer for maximum compatibility
		system('aplay /tmp/weather.wav') #Play the weather
		#The weather is grabbed hourly from NOAA by the fetchWeather.py script
		now=time.time() #Get the current time so we know how long we've been running
	GPIO.output(lightPin,False)
#Turn on light
def light(mins, lightPin):
	#Since I'm testing this code on a PC ATM I need to comment out the GPIO stuff
	#
	#GPIO.setmode(GPIO.BOARD)
	secs=mins*60 #Get the time to run
	start=time.time() #Get the starting time
	now=time.time() #Initialize the var for the loop
	while now - start < secs: #Wait till it's time
		now=time.time()
		sleep(10)
	GPIO.output(lightPin, True) #turn on the light


config=ConfigParser.ConfigParser()
config.read("/opt/piawake/alarmConfig")
lightTime=config.getint("alarm","lightTime")
lightPin=config.getint("alarm","lightPin")
volTime=config.getint('alarm','volTime')
musicTime=config.getint('alarm','musicTime')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightPin, GPIO.OUT)

thread.start_new_thread(vol,(volTime,))
thread.start_new_thread(light,(lightTime, lightPin))
music(musicTime, lightPin)

