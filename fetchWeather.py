# This script fetches weather from NOAA. 
#
# Scheduling info:
# The data is updated at 45 minutes past the hour every hour and
# should not be pulled more than once/hour.

#imports
import json, requests, commands
url='http://forecast.weather.gov/MapClick.php' #The URL to get the data
params = dict( #Adjust lat and lon for your area
    lat = 37.9752,
    lon = -100.8642,
    FcstType = 'json' #XML is also available
)
 
resp = requests.get(url=url, params=params) #Get the data
data = json.loads(resp.text) #Read the data into a Python object
 
weather=data['location']['areaDescription']+' Weather...' #Begin creating the string to feed into pico2wave
for i in range(0,3): #We pull the first 3 forecast periods, typically today, tonight, and tomorrow
    weather+=data['time']['startPeriodName'][i] + ': '
    weather+=data['data']['text'][i]

#Feed the string into pico2wave to create a wav file that the alarm script can read.
commands.getstatusoutput('pico2wave -w /tmp/weather.wav "' + weather + '"')
