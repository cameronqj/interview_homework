#project: Cisco Interview Homework
#name: 3.py
#desc: Modify script (2) to check the status field of session with "id" 107 and print its description and whether the session is OK or CRITICAL
#date: 20200226
#author: cameron jones 

#load modules
import requests
import json

#request page
r = requests.get('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json')
#set data to json
data = r.json()

#print  0=ok, 1=critical for ID == 107
for item in data:

	if item['id'] == 107:
		if item['status'] == '0':
			print(item['description'], " --OK")
		if item['status'] == '1':
			print(item['description'], " -- Critical")
