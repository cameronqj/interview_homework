#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
#project: Cisco Interview Homework
#name: 5.py
#desc: Add two mutually exclusive arguments options, so the user can print what was done on steps 3 and 4, respectively, by passing each one to the script: a) -s which will take a number to use as session "id" b) -d  which will take a number to use as "device_id"
#date: 20200227
#author: cameron jones 

#load modules

import requests
import json
import argparse

#collect CLI input
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--session_id')
parser.add_argument('-d', '--device_id')
args = parser.parse_args()


#getjson defintion
def getjson(url,type,args):
	print (args)
	print (type)

	r = requests.get(url)
	data = r.json()

	for item in data:
			#if item['device_id'] == '3':
			if item[type] == args:
				if item['status'] == '0':
					print(item['description'], " -- OK")
				if item['status'] == '1':
					print(item['description'], " -- Critical")



#process cli and call function passing id/device_id based on flags
if args.session_id:
	getjson('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json', 'id', int(args.session_id))
if args.device_id:
	getjson('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json', 'device_id', args.device_id)

