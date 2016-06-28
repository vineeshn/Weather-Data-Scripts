#!/usr/bin/python

import json, urllib2
from datetime import datetime
from pytz import timezone  

#For Sydney
url = 'http://api.openweathermap.org/data/2.5/weather?q=sydney,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Sydney')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [ data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Melbourne
url = 'http://api.openweathermap.org/data/2.5/weather?q=melbourne,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Melbourne')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Adelaide
url = 'http://api.openweathermap.org/data/2.5/weather?q=adelaide,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Adelaide')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Canberra
url = 'http://api.openweathermap.org/data/2.5/weather?q=canberra,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Canberra')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Wollongong
url = 'http://api.openweathermap.org/data/2.5/weather?q=wollongong,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/NSW')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Perth
url = 'http://api.openweathermap.org/data/2.5/weather?q=perth,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Perth')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'], time,data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Brisbane
url = 'http://api.openweathermap.org/data/2.5/weather?q=brisbane,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Brisbane')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Albury
url = 'http://api.openweathermap.org/data/2.5/weather?q=albury,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/NSW')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Darwin
url = 'http://api.openweathermap.org/data/2.5/weather?q=darwin,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Darwin')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])

#For Eucla
url = 'http://api.openweathermap.org/data/2.5/weather?q=Eucla,au&appid=572eb5a028c89cd2941592d9e07e7f4f'
response=urllib2.urlopen(url)
data=json.load(response)
time = timezone('Australia/Eucla')
time = datetime.now(time)
time = time.strftime('%Y-%m-%d %H:%M:%S')
print '|'.join([str(i) for i in [data['name'],time, data['coord']['lon'], data['coord']['lat'], data['weather'][0]['main'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'] ]])