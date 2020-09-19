#!/usr/bin/env python3
import os
import requests

#Path of text files
path = ''
keys = ['title','name','date','feedback']
folder = os.listdir(path)

for file in folder:
  keycount = 0
  feedback = {}
  with open(path+file) as fl:
    for line in fl :
      value = line.strip()
      feedback[keys[keycount]] = value
      keycount += 1
      print(feedback)
      response = requests.post("<ip-address>/feedback/",json=feedback)

print(response.request.body)
print(response.status_code)
