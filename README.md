# PiAwake
A Raspberry Pi based alarm clock

<i>PiAwake Features:</i><br>
  <u>When the alarm goes off</u>
  Play random songs from a selection of music in /home/pi/Music. <br>
  Slowly increase the volume over a specified number of minutes.<br>
  Turn on a light after a specified number of minutes.<br>
  Read the day's weather forecast between songs<br>
  NO SNOOZE OR OFF! The music will play for as long as it's been configured to play (an hour by default). There's 
    no way to turn it off and go back to sleep without SSHing into the PiAwake<br>
  <br>
  <u>Other features</u><br>
  Web-based alarm scheduler.<br>
  Play music on demand<br>
  Read weather on demand<br>
  Turn light on/off on demand<br>
  Play user-provided white noise<br>
  Display time and date<br>
  Read the previous day's Pittsburg Penguins hockey scores (see hockey.py to change, comment out line 39 of alarm.py to disable)<br>
  
  <i>A note on the displays:</i><br>
  Initially I used a 16x2 LCD display so I could show both the time and date. However, I found that with my glasses off - as they generally are when I'm trying to read the time from an alarm clock, usually at night - I couldn't read it. For this reason I switched to a larger 7 segment display. It only shows the time, not the date, but I can read it when I wake up in the middle of the night. I'm including the code for both, but the code for my 7 segment display - mostly not my own code (see the comments in code7.c for the attribution)- is in C. As such I'm also including the binary of it. To compile this yourself you'll need both the Wiring Pi library and the TM1637 header in the TM1637.zip file.<br>
  <br>
<i>Hardware:</i><br>
  SBC with network - preferably wifi - Raspberry Pi compatible GPIO and audio output<br>
  Necessary accessories for said SBC (power supply, etc)<br>
  A 16x2 I2C LCD display OR a TM1637 4x7 Segment LED display<br>
  A 5v class D amplifier and compatible speaker or speakers<br>
  An Arduino compatible single relay controller<br>
  <br>
  <u>Optional hardware<u><br>
  Momentary switches for extra functionality<br>
  <br>
  <u>Hardware setup</u><br>
  NOTE: With the exception of the SDA and SCL pins the pin numbers I'm giving here are defaults and can be changed. If you change them you will need to edit the scripts to reflect your changes.<br><br>
  
  If using the 16x2 display:<br>
    Connect the I2C backpack to the GPIO (pin 3=SDA, pin 4=5v+, pin 5=SCL, pin 6=Ground)<br>
  <br>
  If using the 7 segment display:<br>
    Connect the 7 segment display to GPIO (pin 3=DIO, pin 4=5v+, pin 5=Clk, pin 6=Ground)<br><br>
  
  Connect the relay controller to the GPIO (pin 2=5v+, pin 34=Ground, pin 36=signal)<br>
  Connect all the buttons to a common ground on pin 39<br>
  Connect the button for the light to pin 37<br>
  Connect the button for music to pin 29<br>
  Connect the button for the weather to pin 13<br>
  Connect the button for white noise to pin 31<br>
  Wire a lamp or light bulb socket to the relay<br>
  Plug your amp into the Pi's audio output (plug or PWM via GPIO) and wire your speaker(s) to it.<br>
  Put everything together in an enclosure of some sort (for reference on size, mine's in the case of an old external hard drive enclosure)<br>
  Plug in your wifi card<br>
  <br>
  OPTIONAL<br>
  Solder a power cord onto the prongs of a 5v 3amp phone charger with 2 USB ports. Alternatively you could pull power for the amp from the USB on the Pi. DO NOT try to power the amp from the GPIO. You'll only burn up your Pi.
  
 Solder a second pair of wires to the same prongs and use them to provide power to the light through the relay. Protect the connections with heat shrink tubes. Use one USB port to power the Pi and the other to power your amp. End result: one power cord coming out of you alarm clock powering all 3 devices inside it.<br>
  
  
<br>
<i>Software:</i><br>
  Raspian<br>
  The RPi-GPIO library (preinstalled on the current version of Raspian)<br>
  apt-get install python-smbus i2c-tools mpg123 libttspico-utils apache2 php5 sqlite3 python-sqlite3 php5-sqlite timidity
  <br><br>
  
<i>Installation</i><br>
  First, boot Raspian with a monitor and keyboard connected to your Pi. Use raspi-config to enable I2C.<br>
  Set up your wifi. For convenience, a static IP address is recommended. (Google for tutorials on setting up wifi with static IPs on the Raspberry Pi. The process is more drawn out than I want to document here.)<br>
  Install PiAwake. Eventually I'll get a script written to automate this. Run the following commands:
  <ol>
  <li>sudo mkdir /data && sudo chown www-data /data && cp alarms.db /data</li>
  <li>sudo mkdir /opt/piawake && sudo cp *.py /opt/piawake</li>
  <ol>
    <li>If using the 7 segment display: sudo cp clock7 /opt/piawake</li>
  </ol>
  <li>tar -xf html.tar.gz && sudo cp -r html /var/www</li>
  <li>sudo crontab -e</li>
  </ol>
  <p>
  Scroll to the bottom of your crontab file and paste in the following lines:<br><br>
  55 * * * * python /opt/piawake/fetchWeather.py<br>
  * * * * * python /opt/piawake/readAlarms.py<br>
  @reboot python /opt/piawake/buttonWeather.py<br>
  @reboot python /opt/piawake/buttonWhitenoise.py<br>
  @reboot python /opt/piawake/buttonMusic.py<br>
  @reboot python /opt/piawake/buttonLight.py<br>
  
  </p>
  <p>
  If you're using the 16x2 display, paste in the following line:<br>
  @reboot python /opt/piawake/clock.py
  </p>
  <p>
  If you're using the 7 segment display, paste in the following line:<br>
  @reboot /opt/piawake/clock7 9 8 27
  
  
  </p>
  
  If you're planning to use the white noise feature you'll need to copy your white noise file to /opt/piawake/whiteNoise.mp3. My white noise file may or may not subject to copyright (I can't remember where I got it several years ago). Since I don't know for sure I can't in good conscience distribute it with this package. There are plenty of white noise files in the public domain (NASA has some "space sounds" that make good ones). By default the white noise file will play for 4 hours or until the end of your mp3 file, whichever comes first. I put this limitation in because my white noise file is 10 hours long and I didn't want it to still be playing when the alarm went off.
