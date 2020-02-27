#project: Cisco Interview Homework
#name: 1.py
#desc: Create a script that loads the JSON data from https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json and print the full JSON
#date: 20200226
#author: cameron jones 

#load modules
import requests

#request page
r = requests.get('https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json')

#print r.json
print(r.json())


