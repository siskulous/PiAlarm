# PiAlarm
A Raspberry Pi based alarm clock

This project is very much a work in progress. Currently I have the files here running on my desktop and being set up to run
daily via crontab.

<i>PiAlarm Features:</i><br>
  Play random songs from a selection of music. Current plans are to load the music by copying them into a shared folder.<br>
  Slowly increase the volume over a specified number of minutes.<br>
  Turn on a light after a specified number of minutes.<br>
  Read the day's weather forecast between songs<br>
  NO SNOOZE OR OFF! The music will play for as long as it's been configured to play (an hour by default). There's 
    no way to turn it off and go back to sleep without SSHing into the PiAlarm<br>
  Web-based configuration.<br>
  <br>
<i>Hardware:</i><br>
  Raspberry Pi 2 or later (Any would in theory work, but as I don't have one older than a 2 to test I'm saying 2 or later)<br>
  Necessary accessories for said RasPi (power supply, USB on-the-go adapter for the Zero, etc.)<br>
  An I2C LCD display.<br>
  A speaker or speakers (I'm using a USB powered portable speaker)<br>
  Momentary switches for extra functionality (I'm planning one to display the current IP address, one to read the
    weather on demand, and one to turn the lamp on and off.)<br>
  A USB wifi card (optional - you could plug your clock into ethernet instead)<br>
  A relay and some way to wire it up (I'm using a relay control board made for Arduinos. They're cheap and they work well.)<br>
    Alternatively you could have an LED array suitable to being powered by the Pi's GPIO, but I want to use regular light bulbs.<br>
<br>
<i>Software:</i><br>
  Raspian<br>
  The RPi-GPIO library (preinstalled on the current version of Raspian)<br>
  apt-get install python-smbus i2c-tools python-pygame libttspico-utils apache2 php5 mariadb-server python-sqlite php5-sqlite
