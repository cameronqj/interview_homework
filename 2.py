#project: Cisco Interview Homework
#name: 2.py
#desc: Build on script (1) to only print fields of session with "id" 107
#date: 20200226
#author: cameron jones 

#load modules
import requests
import json

#request page 
r = requests.get('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json')

#set data to json format
data = r.json()

#print where id = 107
for item in data:
	if item['id'] == 107:
		print(item)

