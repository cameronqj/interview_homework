#project: Cisco Interview Homework
#name: 4.py
#desc: Create a new function on top of script (3) to now print the same output, but for all sessions of "device_id" 3
#date: 20200226
#author: cameron jones 

#load modules

import requests
import json

#define getjson function to print ok/critical for device_id=3

def getjson(url):
	r = requests.get(url)

	data = r.json()
	for item in data:
		if item['device_id'] == '3':
			if item['status'] == '0':
				print(item['description'], " -- OK")
			if item['status'] == '1':
				print(item['description'], " -- Critical")



#execute getjson and pass in url
getjson('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json')
