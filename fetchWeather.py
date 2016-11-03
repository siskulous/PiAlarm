import json, requests, commands
url='http://forecast.weather.gov/MapClick.php'
params = dict(
    lat = 37.9752,
    lon = -100.8642,
    FcstType = 'json'
)
 
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
 
#weather=data['location']['areaDescription']+' Weather...'
weather="Garden City Kansas Weather... "
for i in range(0,3):
    weather+=data['time']['startPeriodName'][i] + ': '
    weather+=data['data']['text'][i]

commands.getstatusoutput('pico2wave -w /tmp/weather.wav "' + weather + '"')
