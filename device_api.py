#!/usr/bin/python3
"""
Query device api and return status code with number of devices 
"""

import json
import yaml
import requests
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Reading configuration
file = 'config.yml'
data = yaml.safe_load(open(file))
data_api = data['api']

IP = data_api['IP']
url = 'https://'+ IP +':50001/rest/nodes/'
userid= data_api['userid']
password= data_api['password']

def dev_api():
    #resp= requests.get(url, auth =HTTPBasicAuth('device_api','Charter123'),verify=False)
    resp= requests.get(url, auth =HTTPBasicAuth(userid, password),verify=False)
    #Convert response to the list of dictionary
    info = resp.json()
    #length of output = Number of devices
    devices = (len(info))
    #print(type(info),info)
    return(resp.status_code, devices)

if __name__=='__main__':
  out = dev_api()
  print(out)
