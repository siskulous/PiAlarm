#!/usr/bin/python
import sqlite3
from os import system
from datetime import datetime

db=sqlite3.connect('/data/alarms.db')
days=['mon','tue','wed','thu','fri','sat','sun']
today=days[datetime.today().weekday()]
print today

with db:

	cur=db.cursor()
	cur.execute("SELECT sid FROM schedule WHERE "+
		"(strftime('%Y-%m-%d %H:%M',first) = strftime('%Y-%m-%d %H:%M','now','localtime')" +
		" OR (strftime('%Y-%m-%d',first) < strftime('%Y-%m-%d','now','localtime') AND "+
		"strftime('%H:%M',first) = strftime('%H:%M','now','localtime') AND " + today + "=1))" +
		" AND enabled=1")

	row= cur.fetchall()
	if len(row) > 0:
		system("python /opt/pialarm/alarm.py")
db.close()


