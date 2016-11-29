#!/usr/bin/python
import smbus
import time

# Define the display parameters
ADDR = 0x27 # The I2C address of the display
WIDTH = 16 # How many characters per line on the display
bus=smbus.SMBus(1) # Open I2C interface, 0 for RPi 1, 1 for RPi 2+

# BE CAREFUL EDITTING BELOW THIS LINE

#Some constants
CHR = 1 # Mode for sending data
CMD = 0 # Mode for sending commands
LINE_1 = 0x80 # Memory buffer for 1st line
LINE_2 = 0xC0 # Memory address for 2nd line
EN = 0b00000100 # Enable bit
BACKLIGHT = 0x08 # 0x08 to turn backlight on, 0x00 to turn backlight off
DELAY=0.0005 # Time to pause for a delay
PULSE=0.0005 # Time to pause for a pulse


def sendByte(bits,mode):

	#Initialize the display
	high = mode | (bits & 0xF0) | BACKLIGHT
	low = mode | ((bits<<4) & 0xF0) | BACKLIGHT
	bus.write_byte(ADDR,high)
	time.sleep(DELAY)
	bus.write_byte(ADDR,(high|EN))
	time.sleep(PULSE)
	bus.write_byte(ADDR,high& -EN)
	time.sleep(DELAY)
	bus.write_byte(ADDR,low)
	time.sleep(DELAY)
	bus.write_byte(ADDR,(low|EN))
	time.sleep(PULSE)
	bus.write_byte(ADDR,low& -EN)

def sendTime():
	curTime=time.strftime('%H:%M') # Current time, HH:MM
	curDate=time.strftime('%a %b %d, %Y') # Current date WWWW MMM D, YYYY
	
	# Adjust the lengths of the strings to match the display
	curTime=curTime.center(WIDTH," ")
	curDate=curDate.center(WIDTH," ")

	# Send the strings to the display
	sendByte(LINE_1, CMD)
	for i in range(WIDTH):
		sendByte(ord(curTime[i]),CHR)
	sendByte(LINE_2, CMD)
	for i in range(WIDTH):
		sendByte(ord(curDate[i]),CHR)

#Initialize the display
sendByte(0x33,CMD)
sendByte(0x32,CMD)
sendByte(0x06,CMD)
sendByte(0x0C,CMD)
sendByte(0x28,CMD)
sendByte(0x01,CMD)
time.sleep(DELAY)

sendTime()

# Get the clock synced up to change exactly on the minute
while(time.strftime("%S") != "00"):
	time.sleep(1)
while True:
	sendTime()
	time.sleep(60) 
