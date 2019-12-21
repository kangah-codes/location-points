__author__ = "Joshua Akangah"
import json
import datetime

def convert_E7(value):
	return value/10000000

def convertTime(dt):
	return datetime.datetime.fromtimestamp(dt/1000.0)

def search(data):
	latitudes = []
	longitudes = []
	timestamp = []
	for k in data:
		for v in data[k]:
			for j in v:
				if j == 'latitudeE7':
					latitudes.append({"lat":convert_E7(v[j])})
				elif j == 'longitudeE7':
					longitudes.append({"lon":convert_E7(v[j])})
				# elif j == 'timestampMs':
				# 	timestamp.append({"time":convertTime(int(v[j])).strftime('%d/%m/%Y : %I:%M %p')})

	return zip(latitudes, longitudes)
