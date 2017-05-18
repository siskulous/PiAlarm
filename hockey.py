#!/usr/bin/python
import json, requests, command
from time import strftime
url='https://statsapi.web.nhl.com/api/v1/schedule'
curDate=strftime('%Y-%m-%d')
curDate='2017-05-03'
humanDate=strftime('%B %d')
params=dict(
	teamId=5, #Pittsburg Pengiuns
	expand='schedule.teams,schedule.game.seriesSummary,seriesSummary.series',
	site='en_nhl',
	gameType='',
	timecode='',
	startDate=curDate,
	endDate=curDate
)
resp=requests.get(url=url,params=params)
data=json.loads(resp.text)

if(data['totalGames'] > 0):
	summary="Pittsburg Penguins scores from " + humanDate +": "
	series=data['dates'][0]['games'][0]['seriesSummary']
	teams=data['dates'][0]['games'][0]['teams']
	summary=summary + ' final score is '
	summary=summary + teams['home']['team']['name'] + ': ' + str(teams['home']['score']) +'. '
	summary=summary + teams['away']['team']['name'] + ': ' + str(teams['away']['score']) +'. '
	summary=summary + 'Series ' + series['gameLabel'] + ', ' + series['seriesStatus']
else:
	summary=''


commands.getstatusoutput('pico2wave -w /tmp/hockey.wav "' + summary + '"')
#print(summary)